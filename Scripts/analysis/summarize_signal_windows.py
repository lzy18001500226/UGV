#!/usr/bin/env python3
"""Summarize UGV controller signals around score/collision jump times."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from statistics import mean
from typing import Any


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
    extra_rows: list[dict[str, float | None]],
    event_time: float,
    radius: float,
    signals: list[str],
) -> dict[str, Any]:
    window_rows = [
        row for row in extra_rows
        if row.get("Time") is not None and abs(float(row["Time"]) - event_time) <= radius
    ]
    nearest = min(
        extra_rows,
        key=lambda row: abs(float(row.get("Time") or 0.0) - event_time),
    )
    summary: dict[str, Any] = {"nearest_time": nearest.get("Time"), "row_count": len(window_rows), "signals": {}}
    for signal in signals:
        values = [row.get(signal) for row in window_rows if row.get(signal) is not None]
        nearest_value = nearest.get(signal)
        if values:
            summary["signals"][signal] = {
                "nearest": nearest_value,
                "min": min(values),
                "max": max(values),
                "mean": mean(values),
            }
        else:
            summary["signals"][signal] = {"nearest": nearest_value, "min": None, "max": None, "mean": None}
    return summary


def analyze_run(run_dir: Path, label: str, radius: float, signals: list[str]) -> dict[str, Any]:
    score_rows = read_csv(run_dir / "score_timeseries.csv")
    extra_rows = read_csv(run_dir / "extra_timeseries.csv")
    events = detect_events(score_rows)
    return {
        "label": label,
        "run_dir": str(run_dir),
        "radius_s": radius,
        "events": [
            {
                **event,
                "window": summarize_window(extra_rows, float(event["time"]), radius, signals),
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
    lines = ["# Signal Window Summary", ""]
    for run in result["runs"]:
        lines.extend([f"## {run['label']}", "", f"Evidence: `{run['run_dir']}`", ""])
        if not run["events"]:
            lines.extend(["- no score/collision jump events detected", ""])
            continue
        lines.append("| Time/s | Changes | df | dl | dr | flag | ctrl speed | ctrl steer | sensor x | sensor y |")
        lines.append("|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|")
        for event in run["events"]:
            signals = event["window"]["signals"]
            changes = "; ".join(
                f"{column}: {payload['from']}->{payload['to']}"
                for column, payload in event["changes"].items()
            )
            lines.append(
                "| {time} | {changes} | {df} | {dl} | {dr} | {flag} | {speed} | {steer} | {x} | {y} |".format(
                    time=fmt(event["time"]),
                    changes=changes,
                    df=fmt(signals["obsAvoidController_Sysblock.chart.df"]["nearest"]),
                    dl=fmt(signals["obsAvoidController_Sysblock.chart.dl"]["nearest"]),
                    dr=fmt(signals["obsAvoidController_Sysblock.chart.dr"]["nearest"]),
                    flag=fmt(signals["obsAvoidController_Sysblock.chart.flag"]["nearest"]),
                    speed=fmt(signals["ctrlAlloc.speed"]["nearest"]),
                    steer=fmt(signals["ctrlAlloc.steer"]["nearest"]),
                    x=fmt(signals["distanceSensor1.vehicle_position[1]"]["nearest"]),
                    y=fmt(signals["distanceSensor1.vehicle_position[2]"]["nearest"]),
                )
            )
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
