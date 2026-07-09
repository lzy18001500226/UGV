#!/usr/bin/env python3
"""Summarize UGV controller signals around score/collision jump times."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from statistics import mean
from typing import Any, Iterable


EVENT_COLUMNS = ("cR", "cO", "P")
DEFAULT_SIGNALS = (
    "obsAvoidController_Sysblock.chart.df",
    "obsAvoidController_Sysblock.chart.dl",
    "obsAvoidController_Sysblock.chart.dr",
    "obsAvoidController_Sysblock.chart.flag",
    "obsAvoidController_Sysblock.speed",
    "obsAvoidController_Sysblock.steer",
    "ctrlAlloc.speed",
    "ctrlAlloc.steer",
    "body3DOF1_1.P_vehicle[1]",
    "body3DOF1_1.P_vehicle[2]",
    "distanceSensor1.vehicle_position[1]",
    "distanceSensor1.vehicle_position[2]",
)


def as_float(value: str | None) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def read_csv(path: Path) -> list[dict[str, float | None]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader)
        rows: list[dict[str, float | None]] = []
        for raw in reader:
            normalized: dict[str, float | None] = {}
            seen_time = False
            for key, value in zip(header, raw):
                # MWORKS extra exports may contain duplicate Time columns; keep the first.
                if key == "Time":
                    if seen_time:
                        continue
                    seen_time = True
                normalized[key] = as_float(value)
            rows.append(normalized)
        return rows


def read_signal_series(path: Path, signals: Iterable[str]) -> dict[str, list[tuple[float, float | None]]]:
    """Read MWORKS CSV exports while preserving each signal's nearest left Time column.

    MWORKS `extra_timeseries.csv` can be exported as several time/value groups:
    `Time, signal_a, ..., Time, signal_b, ...`.  A normal dict keyed by `Time`
    silently attaches every signal to the first time axis, which can shift
    diagnostics for later groups.  For each requested signal, bind values to the
    closest preceding `Time` column in the header.
    """

    wanted = set(signals)
    series: dict[str, list[tuple[float, float | None]]] = {signal: [] for signal in signals}
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader)
        time_for_column: list[int | None] = []
        current_time_index: int | None = None
        for index, key in enumerate(header):
            if key == "Time":
                current_time_index = index
            time_for_column.append(current_time_index)

        signal_columns = [
            (index, key, time_for_column[index])
            for index, key in enumerate(header)
            if key in wanted and time_for_column[index] is not None
        ]

        for raw in reader:
            for value_index, key, time_index in signal_columns:
                if time_index is None or time_index >= len(raw) or value_index >= len(raw):
                    continue
                timestamp = as_float(raw[time_index])
                if timestamp is None:
                    continue
                series[key].append((timestamp, as_float(raw[value_index])))
    return series


def detect_events(score_rows: list[dict[str, float | None]]) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    previous: dict[str, float | None] | None = None
    for row in score_rows:
        if previous is None:
            previous = row
            continue
        changes: dict[str, dict[str, float | None]] = {}
        for column in EVENT_COLUMNS:
            old = previous.get(column)
            new = row.get(column)
            if old is not None and new is not None and new != old:
                changes[column] = {"from": old, "to": new, "delta": new - old}
        if changes:
            events.append({"time": row.get("Time"), "changes": changes})
        previous = row
    return events


def summarize_window(
    extra_series: dict[str, list[tuple[float, float | None]]],
    event_time: float,
    radius: float,
    signals: list[str],
) -> dict[str, Any]:
    row_count = max(
        (
            sum(1 for timestamp, _ in extra_series.get(signal, []) if abs(timestamp - event_time) <= radius)
            for signal in signals
        ),
        default=0,
    )
    summary: dict[str, Any] = {"nearest_time": None, "row_count": row_count, "signals": {}}
    for signal in signals:
        samples = extra_series.get(signal, [])
        nearest_sample = min(samples, key=lambda item: abs(item[0] - event_time)) if samples else None
        if nearest_sample is not None and summary["nearest_time"] is None:
            summary["nearest_time"] = nearest_sample[0]
        nearest_time = nearest_sample[0] if nearest_sample is not None else None
        nearest_value = nearest_sample[1] if nearest_sample is not None else None
        values = [value for timestamp, value in samples if abs(timestamp - event_time) <= radius and value is not None]
        if values:
            summary["signals"][signal] = {
                "nearest_time": nearest_time,
                "nearest": nearest_value,
                "min": min(values),
                "max": max(values),
                "mean": mean(values),
            }
        else:
            summary["signals"][signal] = {
                "nearest_time": nearest_time,
                "nearest": nearest_value,
                "min": None,
                "max": None,
                "mean": None,
            }
    return summary


def analyze_run(run_dir: Path, label: str, radius: float, signals: list[str]) -> dict[str, Any]:
    score_rows = read_csv(run_dir / "score_timeseries.csv")
    extra_series = read_signal_series(run_dir / "extra_timeseries.csv", signals)
    events = detect_events(score_rows)
    return {
        "label": label,
        "run_dir": str(run_dir),
        "radius_s": radius,
        "events": [
            {
                **event,
                "window": summarize_window(extra_series, float(event["time"]), radius, signals),
            }
            for event in events
            if event.get("time") is not None
        ],
    }


def fmt(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.4g}"
    return str(value)


def write_markdown(result: dict[str, Any], path: Path) -> None:
    def nearest(signals: dict[str, Any], name: str) -> Any:
        payload = signals.get(name) or {}
        return payload.get("nearest")

    lines = ["# Signal Window Summary", ""]
    selected_signals = result.get("signals") or list(DEFAULT_SIGNALS)
    for run in result["runs"]:
        lines.extend([f"## {run['label']}", "", f"Evidence: `{run['run_dir']}`", ""])
        if not run["events"]:
            lines.extend(["- no score/collision jump events detected", ""])
            continue
        columns = ["Time/s", "Changes", *selected_signals]
        align = ["---:", "---", *(["---:"] * len(selected_signals))]
        lines.append("| " + " | ".join(columns) + " |")
        lines.append("|" + "|".join(align) + "|")
        for event in run["events"]:
            signals = event["window"]["signals"]
            changes = "; ".join(
                f"{column}: {payload['from']}->{payload['to']}"
                for column, payload in event["changes"].items()
            )
            row = [fmt(event["time"]), changes]
            row.extend(fmt(nearest(signals, signal)) for signal in selected_signals)
            lines.append("| " + " | ".join(row) + " |")
        lines.append("")
    lines.extend(
        [
            "## Notes",
            "",
            "- Values are nearest exported samples at the collision/score jump time.",
            "- Use the JSON output for min/max/mean over the configured window radius.",
            "- This is post-run evidence analysis only; it does not rerun MWORKS.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="append", nargs=2, metavar=("LABEL", "RUN_DIR"), required=True)
    parser.add_argument("--radius", type=float, default=0.5)
    parser.add_argument("--signal", action="append", default=[])
    parser.add_argument("--json-out", required=True)
    parser.add_argument("--md-out", required=True)
    args = parser.parse_args()

    signals = args.signal or list(DEFAULT_SIGNALS)
    result = {
        "radius_s": args.radius,
        "signals": signals,
        "runs": [analyze_run(Path(run_dir), label, args.radius, signals) for label, run_dir in args.run],
    }
    json_path = Path(args.json_out)
    md_path = Path(args.md_out)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, md_path)
    print(json.dumps({"ok": True, "runs": len(result["runs"]), "md_out": str(md_path), "json_out": str(json_path)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
