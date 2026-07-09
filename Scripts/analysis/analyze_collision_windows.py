#!/usr/bin/env python3
"""Analyze score/collision jumps from UGV score_timeseries.csv files."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


SCORE_COLUMNS = ("T", "cR", "cO", "P")
EVENT_COLUMNS = ("cR", "cO", "P")


def as_float(value: str | None) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def read_rows(path: Path) -> list[dict[str, float | None]]:
    rows: list[dict[str, float | None]] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for raw in reader:
            rows.append({key: as_float(raw.get(key)) for key in ("Time", *SCORE_COLUMNS)})
    return rows


def load_metrics(run_dir: Path) -> dict[str, Any]:
    metrics_path = run_dir / "metrics.json"
    if not metrics_path.exists():
        return {}
    return json.loads(metrics_path.read_text(encoding="utf-8-sig"))


def analyze_run(run_dir: Path, label: str) -> dict[str, Any]:
    score_path = run_dir / "score_timeseries.csv"
    if not score_path.exists():
        raise FileNotFoundError(f"missing score_timeseries.csv: {score_path}")

    rows = read_rows(score_path)
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
            if old is not None and new is not None and new != old:
                changes[column] = {"from": old, "to": new, "delta": new - old}
        if changes:
            events.append({"time": row.get("Time"), "changes": changes})
        previous = row

    metrics = load_metrics(run_dir)
    final_row = rows[-1] if rows else {}
    return {
        "label": label,
        "run_dir": str(run_dir),
        "score_path": str(score_path),
        "runtime_status": metrics.get("runtime_status"),
        "simulation_exit_state": metrics.get("simulation_exit_state"),
        "final": {key: metrics.get(name, final_row.get(name)) for key, name in {
            "time_s": "time_s",
            "road_collisions": "road_collisions",
            "obstacle_collisions": "obstacle_collisions",
            "avoidance_score": "avoidance_score",
        }.items()},
        "score_values_at_end": metrics.get("score_values_at_end", {}),
        "event_count": len(events),
        "events": events,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    lines: list[str] = [
        "# Collision Window Analysis",
        "",
        "## Runs",
        "",
        "| Label | Runtime | Exit | T/s | cR | cO | P | Events | Evidence |",
        "|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for run in result["runs"]:
        score = run.get("score_values_at_end") or {}
        final = run.get("final") or {}
        lines.append(
            "| {label} | `{runtime}` | {exit_state} | {time_s} | {cr} | {co} | {p} | {events} | `{evidence}` |".format(
                label=run["label"],
                runtime=run.get("runtime_status"),
                exit_state=run.get("simulation_exit_state"),
                time_s=score.get("T", final.get("time_s")),
                cr=score.get("cR", final.get("road_collisions")),
                co=score.get("cO", final.get("obstacle_collisions")),
                p=score.get("P", final.get("avoidance_score")),
                events=run["event_count"],
                evidence=run["run_dir"],
            )
        )

    lines.extend(["", "## Jump Events", ""])
    for run in result["runs"]:
        lines.extend([f"### {run['label']}", ""])
        if not run["events"]:
            lines.extend(["- no score/collision jumps detected", ""])
            continue
        lines.append("| Time/s | Changes |")
        lines.append("|---:|---|")
        for event in run["events"]:
            changes = []
            for column, payload in event["changes"].items():
                changes.append(f"{column}: {payload['from']} -> {payload['to']} ({payload['delta']:+g})")
            lines.append(f"| {event['time']} | {'; '.join(changes)} |")
        lines.append("")

    lines.extend(
        [
            "## Notes",
            "",
            "- This analysis uses saved `score_timeseries.csv` files only.",
            "- It does not rerun MWORKS and does not prove physical UGV behavior.",
            "- Use the event times to decide the next visual or state-signal inspection window.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="append", nargs=2, metavar=("LABEL", "RUN_DIR"), required=True)
    parser.add_argument("--json-out", required=True)
    parser.add_argument("--md-out", required=True)
    args = parser.parse_args()

    runs = [analyze_run(Path(run_dir), label) for label, run_dir in args.run]
    result = {"runs": runs}

    json_path = Path(args.json_out)
    md_path = Path(args.md_out)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result, md_path)
    print(json.dumps({"ok": True, "runs": len(runs), "md_out": str(md_path), "json_out": str(json_path)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
