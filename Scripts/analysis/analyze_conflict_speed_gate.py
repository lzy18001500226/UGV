#!/usr/bin/env python
"""Analyze v103-style conflict speed-gate windows in MWORKS extra timeseries."""

from __future__ import annotations

import argparse
import csv
import json
from bisect import bisect_left
from pathlib import Path
from statistics import mean


SIGNALS = [
    "ctrlAlloc.speed_oa",
    "ctrlAlloc.steer_oa",
    "ctrlAlloc.unitDelay1.y",
    "ctrlAlloc.unitDelay3.y",
    "ctrlAlloc.gain2.u",
    "ctrlAlloc.steer",
    "pathPlanner.steering_angle",
    "pathPlanner.target_v",
    "pathPlanner.closest_index",
    "obsAvoidController_Sysblock.chart.df",
    "obsAvoidController_Sysblock.chart.dl",
    "obsAvoidController_Sysblock.chart.dr",
    "obsAvoidController_Sysblock.chart.flag",
]


def _float_or_none(value: str | None) -> float | None:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def _nearest_time_index(headers: list[str], idx: int) -> int:
    for j in range(idx, -1, -1):
        if headers[j] == "Time":
            return j
    raise ValueError(f"no Time column before {headers[idx]!r} at index {idx}")


def _read_signal_series(csv_path: Path) -> dict[str, list[tuple[float, float]]]:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        headers = next(reader)
        signal_indices: dict[str, int] = {}
        time_indices: dict[str, int] = {}
        for signal in SIGNALS:
            if signal in headers:
                idx = headers.index(signal)
                signal_indices[signal] = idx
                time_indices[signal] = _nearest_time_index(headers, idx)

        series = {signal: [] for signal in signal_indices}
        for row in reader:
            for signal, idx in signal_indices.items():
                t = _float_or_none(row[time_indices[signal]] if time_indices[signal] < len(row) else None)
                v = _float_or_none(row[idx] if idx < len(row) else None)
                if t is not None and v is not None:
                    series[signal].append((t, v))
    return series


def _nearest_value(series: list[tuple[float, float]], t: float, max_dt: float) -> float | None:
    if not series:
        return None
    times = [x[0] for x in series]
    pos = bisect_left(times, t)
    candidates = []
    if pos < len(series):
        candidates.append(series[pos])
    if pos > 0:
        candidates.append(series[pos - 1])
    if not candidates:
        return None
    best_t, best_v = min(candidates, key=lambda tv: abs(tv[0] - t))
    if abs(best_t - t) > max_dt:
        return None
    return best_v


def _build_rows(series: dict[str, list[tuple[float, float]]], max_dt: float) -> list[dict[str, float]]:
    base_signal = "ctrlAlloc.speed_oa"
    rows = []
    for t, speed_oa in series.get(base_signal, []):
        row = {"Time": t, base_signal: speed_oa}
        complete = True
        for signal in SIGNALS:
            if signal == base_signal or signal not in series:
                continue
            v = _nearest_value(series[signal], t, max_dt)
            if v is None:
                complete = False
                break
            row[signal] = v
        if complete:
            rows.append(row)
    return rows


def _gate_active(row: dict[str, float]) -> bool:
    return (
        row["ctrlAlloc.speed_oa"] < 0
        and row["ctrlAlloc.steer_oa"] * row["ctrlAlloc.unitDelay1.y"] < 0
        and abs(row["ctrlAlloc.unitDelay1.y"]) > 0.15
        and row["ctrlAlloc.unitDelay3.y"] > 0.35
    )


def _intervals(times: list[float], gap: float) -> list[dict[str, float]]:
    if not times:
        return []
    intervals = []
    start = prev = times[0]
    for t in times[1:]:
        if t - prev > gap:
            intervals.append({"start": start, "end": prev, "duration": prev - start})
            start = t
        prev = t
    intervals.append({"start": start, "end": prev, "duration": prev - start})
    return intervals


def _summarize(label: str, csv_path: Path, max_dt: float, interval_gap: float) -> dict:
    series = _read_signal_series(csv_path)
    rows = _build_rows(series, max_dt=max_dt)
    active = [r for r in rows if _gate_active(r)]
    times = [r["Time"] for r in active]

    def stat(signal: str) -> dict[str, float | None]:
        vals = [r[signal] for r in active if signal in r]
        if not vals:
            return {"min": None, "max": None, "mean": None}
        return {"min": min(vals), "max": max(vals), "mean": mean(vals)}

    samples = []
    for r in active[:8]:
        samples.append(
            {
                "t": r["Time"],
                "gain2_u": r.get("ctrlAlloc.gain2.u"),
                "unitDelay3_y": r.get("ctrlAlloc.unitDelay3.y"),
                "steer_oa": r.get("ctrlAlloc.steer_oa"),
                "path_steer_delay": r.get("ctrlAlloc.unitDelay1.y"),
                "df": r.get("obsAvoidController_Sysblock.chart.df"),
                "dl": r.get("obsAvoidController_Sysblock.chart.dl"),
                "dr": r.get("obsAvoidController_Sysblock.chart.dr"),
                "target_v": r.get("pathPlanner.target_v"),
                "closest_index": r.get("pathPlanner.closest_index"),
            }
        )

    return {
        "label": label,
        "csv_path": str(csv_path),
        "aligned_rows": len(rows),
        "active_rows": len(active),
        "active_time_span": [min(times), max(times)] if times else None,
        "intervals": _intervals(times, gap=interval_gap),
        "stats": {
            "df": stat("obsAvoidController_Sysblock.chart.df"),
            "dl": stat("obsAvoidController_Sysblock.chart.dl"),
            "dr": stat("obsAvoidController_Sysblock.chart.dr"),
            "target_v": stat("pathPlanner.target_v"),
            "path_steer_delay": stat("ctrlAlloc.unitDelay1.y"),
            "steer_oa": stat("ctrlAlloc.steer_oa"),
            "unitDelay3_y": stat("ctrlAlloc.unitDelay3.y"),
            "gain2_u": stat("ctrlAlloc.gain2.u"),
            "closest_index": stat("pathPlanner.closest_index"),
        },
        "first_samples": samples,
    }


def _write_md(out: Path, summaries: list[dict]) -> None:
    lines = ["# Conflict Speed-Gate Window Analysis", ""]
    lines.append("Gate predicate:")
    lines.append("")
    lines.append("```text")
    lines.append("speed_oa < 0")
    lines.append("and steer_oa * delayed_path_steer < 0")
    lines.append("and abs(delayed_path_steer) > 0.15")
    lines.append("and delayed_path_speed > 0.35")
    lines.append("```")
    lines.append("")
    for summary in summaries:
        lines.append(f"## {summary['label']}")
        lines.append("")
        lines.append(f"- source: `{summary['csv_path']}`")
        lines.append(f"- aligned rows: `{summary['aligned_rows']}`")
        lines.append(f"- active rows: `{summary['active_rows']}`")
        lines.append(f"- active span: `{summary['active_time_span']}`")
        lines.append("")
        lines.append("| interval | start | end | duration |")
        lines.append("|---:|---:|---:|---:|")
        for i, interval in enumerate(summary["intervals"], start=1):
            lines.append(
                f"| {i} | {interval['start']:.3f} | {interval['end']:.3f} | {interval['duration']:.3f} |"
            )
        if not summary["intervals"]:
            lines.append("| - | - | - | - |")
        lines.append("")
        lines.append("| signal | min | max | mean |")
        lines.append("|---|---:|---:|---:|")
        for signal, stat in summary["stats"].items():
            lines.append(
                f"| {signal} | {stat['min']} | {stat['max']} | {stat['mean']} |"
            )
        lines.append("")
        lines.append("| sample | t | gain2.u | unitDelay3.y | steer_oa | delayed_path_steer | df | dl | dr | target_v | closest_index |")
        lines.append("|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
        for i, sample in enumerate(summary["first_samples"], start=1):
            lines.append(
                "| {i} | {t} | {gain2_u} | {unitDelay3_y} | {steer_oa} | {path_steer_delay} | {df} | {dl} | {dr} | {target_v} | {closest_index} |".format(
                    i=i, **sample
                )
            )
        if not summary["first_samples"]:
            lines.append("| - | - | - | - | - | - | - | - | - | - | - |")
        lines.append("")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", action="append", nargs=2, metavar=("LABEL", "CSV"), required=True)
    parser.add_argument("--json-out", required=True)
    parser.add_argument("--md-out", required=True)
    parser.add_argument("--max-dt", type=float, default=0.026)
    parser.add_argument("--interval-gap", type=float, default=0.075)
    args = parser.parse_args()

    summaries = [
        _summarize(label, Path(csv_path), max_dt=args.max_dt, interval_gap=args.interval_gap)
        for label, csv_path in args.case
    ]
    Path(args.json_out).write_text(json.dumps(summaries, indent=2), encoding="utf-8")
    _write_md(Path(args.md_out), summaries)
    print(json.dumps({"cases": len(summaries), "md_out": args.md_out, "json_out": args.json_out}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
