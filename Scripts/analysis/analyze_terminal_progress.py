#!/usr/bin/env python3
"""Summarize the final valid window of grouped MWORKS CSV signal exports."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from statistics import mean


def as_float(value: str) -> float | None:
    if value == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None


def read_series(path: Path) -> dict[str, list[tuple[float, float]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader)
        time_index: int | None = None
        columns: list[tuple[int, str, int]] = []
        for index, name in enumerate(header):
            if name == "Time":
                time_index = index
            elif time_index is not None:
                columns.append((index, name, time_index))

        series: dict[str, list[tuple[float, float]]] = {name: [] for _, name, _ in columns}
        for row in reader:
            for value_index, name, bound_time_index in columns:
                if value_index >= len(row) or bound_time_index >= len(row):
                    continue
                timestamp = as_float(row[bound_time_index])
                value = as_float(row[value_index])
                if timestamp is not None and value is not None:
                    series[name].append((timestamp, value))
    return series


def summarize(path: Path, window: float) -> dict[str, object]:
    result: dict[str, object] = {"csv": str(path), "window_s": window, "signals": {}}
    signal_result = result["signals"]
    assert isinstance(signal_result, dict)
    for name, samples in read_series(path).items():
        if not samples:
            continue
        final_time = samples[-1][0]
        tail = [(timestamp, value) for timestamp, value in samples if timestamp >= final_time - window]
        values = [value for _, value in tail]
        signal_result[name] = {
            "samples": len(samples),
            "final_time": final_time,
            "final": samples[-1][1],
            "window_min": min(values),
            "window_max": max(values),
            "window_mean": mean(values),
        }
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", type=Path)
    parser.add_argument("--window", type=float, default=5.0)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()

    result = summarize(args.csv, args.window)
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
