#!/usr/bin/env python3
"""Summarize path-planner and obstacle-avoidance contributions near score jumps."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from statistics import mean
from typing import Any, Iterable


EVENT_COLUMNS = ("cR", "cO", "P")
SIGNALS = (
    "ctrlAlloc.speed_pp",
    "ctrlAlloc.speed_oa",
    "ctrlAlloc.firstOrder1.y",
    "ctrlAlloc.speed",
    "ctrlAlloc.steer_pp",
    "ctrlAlloc.steer_oa",
    "ctrlAlloc.firstOrder.y",
    "ctrlAlloc.steer",
    "obsAvoidController_Sysblock.chart.df",
    "obsAvoidController_Sysblock.chart.dl",
    "obsAvoidController_Sysblock.chart.dr",
    "obsAvoidController_Sysblock.chart.flag",
    "obsAvoidController_Sysblock.speed",
    "obsAvoidController_Sysblock.steer",
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
            row: dict[str, float | None] = {}
            seen_time = False
            for key, value in zip(header, raw):
                if key == "Time":
                    if seen_time:
                        continue
                    seen_time = True
                row[key] = as_float(value)
            rows.append(row)
    return rows


def read_signal_series(path: Path, signals: Iterable[str]) -> dict[str, list[tuple[float, float | None]]]:
    """Read signal samples with each signal bound to its own MWORKS time axis."""

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


def detect_events(rows: list[dict[str, float | None]]) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    previous: dict[str, float | None] | None = None
    for row in rows:
        if previous is None:
            previous = row
            continue
        changes: dict[str, dict[str, float | None]] = {}
        for column in EVENT_COLUMNS:
            old = previous.get(column)
            new = row.get(column)
            if old is not None and new is not None and old != new:
                changes[column] = {"from": old, "to": new, "delta": new - old}
        if changes:
            events.append({"time": row.get("Time"), "changes": changes})
        previous = row
    return events


def signal_summary(series: dict[str, list[tuple[float, float | None]]], event_time: float, radius: float) -> dict[str, Any]:
    row_count = max(
        (
            sum(1 for timestamp, _ in series.get(signal, []) if abs(timestamp - event_time) <= radius)
            for signal in SIGNALS
        ),
        default=0,
    )
    summary: dict[str, Any] = {"nearest_time": None, "row_count": row_count, "signals": {}}
    for signal in SIGNALS:
        samples = series.get(signal, [])
        nearest_sample = min(samples, key=lambda item: abs(item[0] - event_time)) if samples else None
        if nearest_sample is not None and summary["nearest_time"] is None:
            summary["nearest_time"] = nearest_sample[0]
        nearest_time = nearest_sample[0] if nearest_sample is not None else None
        nearest_value = nearest_sample[1] if nearest_sample is not None else None
        values = [value for timestamp, value in samples if abs(timestamp - event_time) <= radius and value is not None]
        summary["signals"][signal] = {
            "nearest_time": nearest_time,
            "nearest": nearest_value,
            "min": min(values) if values else None,
            "max": max(values) if values else None,
            "mean": mean(values) if values else None,
        }
    return summary


def analyze_run(label: str, run_dir: Path, radius: float) -> dict[str, Any]:
    score_rows = read_csv(run_dir / "score_timeseries.csv")
    extra_series = read_signal_series(run_dir / "extra_timeseries.csv", SIGNALS)
    events = detect_events(score_rows)
    return {
        "label": label,
        "run_dir": str(run_dir),
        "radius_s": radius,
        "events": [
            {
                **event,
                "window": signal_summary(extra_series, float(event["time"]), radius),
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


def changes_text(changes: dict[str, Any]) -> str:
    return "; ".join(
        f"{name}: {payload['from']}->{payload['to']}"
        for name, payload in changes.items()
    )


def write_markdown(result: dict[str, Any], path: Path) -> None:
    lines = [
        "# CtrlAlloc Contribution Analysis",
        "",
        "This is offline analysis of saved MWORKS CSV exports. It does not rerun MWORKS.",
        "",
    ]
    for run in result["runs"]:
        lines.extend([f"## {run['label']}", "", f"Evidence: `{run['run_dir']}`", ""])
        if not run["events"]:
            lines.extend(["- no score/collision jump events detected", ""])
            continue
        lines.append("| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |")
        lines.append("|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
        for event in run["events"]:
            signals = event["window"]["signals"]
            row = [
                fmt(event["time"]),
                changes_text(event["changes"]),
                fmt(signals["ctrlAlloc.speed_pp"]["nearest"]),
                fmt(signals["ctrlAlloc.speed_oa"]["nearest"]),
                fmt(signals["ctrlAlloc.firstOrder1.y"]["nearest"]),
                fmt(signals["ctrlAlloc.speed"]["nearest"]),
                fmt(signals["ctrlAlloc.steer_pp"]["nearest"]),
                fmt(signals["ctrlAlloc.steer_oa"]["nearest"]),
                fmt(signals["ctrlAlloc.firstOrder.y"]["nearest"]),
                fmt(signals["ctrlAlloc.steer"]["nearest"]),
                fmt(signals["obsAvoidController_Sysblock.chart.df"]["nearest"]),
                fmt(signals["obsAvoidController_Sysblock.chart.dl"]["nearest"]),
                fmt(signals["obsAvoidController_Sysblock.chart.dr"]["nearest"]),
                fmt(signals["obsAvoidController_Sysblock.chart.flag"]["nearest"]),
            ]
            lines.append("| " + " | ".join(row) + " |")
        lines.append("")
    lines.extend(
        [
            "## Interpretation Rules",
            "",
            "- `speed_pp` / `steer_pp` are path-planner commands entering `CtrlAlloc`.",
            "- `speed_oa` / `steer_oa` are obstacle-avoidance commands entering `CtrlAlloc`.",
            "- `oa_*_filtered` are first-order filtered obstacle-avoidance contributions after `factor_oa`.",
            "- Large final-steer values with small obstacle steer indicate path-planner dominance.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="append", nargs=2, metavar=("LABEL", "RUN_DIR"), required=True)
    parser.add_argument("--radius", type=float, default=0.5)
    parser.add_argument("--json-out", required=True)
    parser.add_argument("--md-out", required=True)
    args = parser.parse_args()

    result = {
        "radius_s": args.radius,
        "signals": SIGNALS,
        "runs": [analyze_run(label, Path(run_dir), args.radius) for label, run_dir in args.run],
    }
    json_path = Path(args.json_out)
    md_path = Path(args.md_out)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, md_path)
    print(json.dumps({"ok": True, "md_out": str(md_path), "json_out": str(json_path)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
