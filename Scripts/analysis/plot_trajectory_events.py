"""Plot UGV trajectory exports and annotate collision/score events."""

from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
import pandas as pd


POSITION_PAIRS = [
    ("body3DOF1_1.P_vehicle[1]", "body3DOF1_1.P_vehicle[2]"),
    ("distanceSensor1.vehicle_position[1]", "distanceSensor1.vehicle_position[2]"),
    ("body3DOF1_1.body.frame_a.r_0[1]", "body3DOF1_1.body.frame_a.r_0[2]"),
]


def _extract_braced_value(text: str, key: str) -> str:
    match = re.search(rf"{re.escape(key)}\s*=", text)
    if not match:
        raise ValueError(f"{key} not found")
    start = text.find("{", match.end())
    if start < 0:
        raise ValueError(f"{key} has no braced value")
    depth = 0
    for idx in range(start, len(text)):
        char = text[idx]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start : idx + 1]
    raise ValueError(f"{key} braced value is not closed")


def _parse_point_table(value: str) -> list[list[float]]:
    rows: list[list[float]] = []
    for row in re.findall(r"\{([^{}]+)\}", value):
        numbers = [float(item) for item in re.findall(r"[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?", row)]
        if len(numbers) >= 2:
            rows.append(numbers)
    return rows


def _extract_number(text: str, key: str) -> float | None:
    match = re.search(rf"{re.escape(key)}\s*=\s*([-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?)", text)
    if not match:
        return None
    return float(match.group(1))


def load_track_geometry(path: Path | None) -> dict[str, object] | None:
    if path is None:
        return None
    text = path.read_text(encoding="utf-8")
    road_map = _parse_point_table(_extract_braced_value(text, "roadMap"))
    obstacle_points = _parse_point_table(_extract_braced_value(text, "obstaclePoint"))
    return {
        "track_path": str(path),
        "road_map": road_map,
        "obstacle_points": obstacle_points,
        "road_width": _extract_number(text, "roadWidth"),
        "obstacle_size": _extract_number(text, "obstacleSize"),
    }


def distance_to_polyline(x: float, y: float, points: list[list[float]]) -> float | None:
    if len(points) < 2:
        return None
    best = math.inf
    for start, end in zip(points, points[1:]):
        x1, y1 = start[0], start[1]
        x2, y2 = end[0], end[1]
        dx = x2 - x1
        dy = y2 - y1
        length2 = dx * dx + dy * dy
        if length2 <= 1e-12:
            dist = math.hypot(x - x1, y - y1)
        else:
            t = max(0.0, min(1.0, ((x - x1) * dx + (y - y1) * dy) / length2))
            proj_x = x1 + t * dx
            proj_y = y1 + t * dy
            dist = math.hypot(x - proj_x, y - proj_y)
        best = min(best, dist)
    return best


def nearest_point_distance(x: float, y: float, points: list[list[float]]) -> float | None:
    if not points:
        return None
    return min(math.hypot(x - point[0], y - point[1]) for point in points)


def load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path)


def find_time_column(df: pd.DataFrame) -> str:
    for candidate in ("Time", "time", "time/s"):
        if candidate in df.columns:
            return candidate
    return df.columns[0]


def find_position_pair(df: pd.DataFrame) -> tuple[str, str]:
    best_pair: tuple[str, str] | None = None
    best_span = -1.0
    for x_col, y_col in POSITION_PAIRS:
        if x_col in df.columns and y_col in df.columns:
            span = float((df[x_col].max() - df[x_col].min()) + (df[y_col].max() - df[y_col].min()))
            if span > best_span:
                best_pair = (x_col, y_col)
                best_span = span
    if best_pair is not None and best_span > 1e-6:
        return best_pair
    raise ValueError(
        "No dynamic supported position pair found. Export one of: "
        + ", ".join(f"{x}/{y}" for x, y in POSITION_PAIRS)
    )


def score_events(score: pd.DataFrame) -> list[dict[str, object]]:
    time_col = find_time_column(score)
    events: list[dict[str, object]] = []
    for idx in range(1, len(score)):
        changes: list[str] = []
        for col in ("cR", "cO", "P"):
            if col not in score.columns:
                continue
            prev = score.iloc[idx - 1][col]
            cur = score.iloc[idx][col]
            if pd.notna(prev) and pd.notna(cur) and cur != prev:
                changes.append(f"{col}: {prev:g}->{cur:g}")
        if changes:
            events.append(
                {
                    "time": float(score.iloc[idx][time_col]),
                    "changes": changes,
                }
            )
    return events


def nearest_row(df: pd.DataFrame, time_col: str, t: float) -> pd.Series:
    idx = (df[time_col] - t).abs().idxmin()
    return df.loc[idx]


def plot_run(label: str, run_dir: Path, out_dir: Path, track_geometry: dict[str, object] | None) -> dict[str, object]:
    extra = load_csv(run_dir / "extra_timeseries.csv")
    score = load_csv(run_dir / "score_timeseries.csv")
    time_col = find_time_column(extra)
    x_col, y_col = find_position_pair(extra)
    events = score_events(score)

    fig, ax = plt.subplots(figsize=(8, 7), dpi=160)
    road_map = []
    obstacle_points = []
    road_width = None
    obstacle_size = None
    if track_geometry:
        road_map = track_geometry.get("road_map", [])  # type: ignore[assignment]
        obstacle_points = track_geometry.get("obstacle_points", [])  # type: ignore[assignment]
        road_width = track_geometry.get("road_width")
        obstacle_size = track_geometry.get("obstacle_size")
        if isinstance(road_map, list) and len(road_map) >= 2:
            ax.plot(
                [point[0] for point in road_map],
                [point[1] for point in road_map],
                linewidth=1.0,
                color="#64748b",
                alpha=0.7,
                label="roadMap",
            )
        if isinstance(obstacle_points, list) and obstacle_points:
            ax.scatter(
                [point[0] for point in obstacle_points],
                [point[1] for point in obstacle_points],
                color="#7c2d12",
                s=22,
                marker="s",
                alpha=0.85,
                label="obstaclePoint",
                zorder=3,
            )
    ax.plot(extra[x_col], extra[y_col], linewidth=1.4, color="#2563eb", label=label)
    ax.scatter(extra[x_col].iloc[0], extra[y_col].iloc[0], color="#16a34a", s=50, label="start", zorder=4)
    ax.scatter(extra[x_col].iloc[-1], extra[y_col].iloc[-1], color="#dc2626", s=50, label="end", zorder=4)

    event_rows: list[dict[str, object]] = []
    for number, event in enumerate(events, start=1):
        row = nearest_row(extra, time_col, float(event["time"]))
        x = float(row[x_col])
        y = float(row[y_col])
        ax.scatter(x, y, color="#f97316", s=70, marker="x", linewidths=2.0, zorder=5)
        ax.annotate(
            f"E{number}\n{event['time']:.2f}s",
            xy=(x, y),
            xytext=(6, 6),
            textcoords="offset points",
            fontsize=8,
            color="#9a3412",
        )
        event_rows.append(
            {
                "event": number,
                "time_s": float(event["time"]),
                "changes": event["changes"],
                "x": x,
                "y": y,
                "distance_to_road_center": distance_to_polyline(x, y, road_map) if road_map else None,
                "distance_to_nearest_obstacle": nearest_point_distance(x, y, obstacle_points) if obstacle_points else None,
            }
        )

    ax.set_title(label)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.axis("equal")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="best", fontsize=8)
    fig.tight_layout()

    image_path = out_dir / f"{label}_trajectory_events.png"
    fig.savefig(image_path)
    plt.close(fig)

    last_score = score.iloc[-1].to_dict()
    return {
        "label": label,
        "run_dir": str(run_dir),
        "image": str(image_path),
        "position_columns": [x_col, y_col],
        "time_column": time_col,
        "score_end": {k: last_score.get(k) for k in ("T", "cR", "cO", "P") if k in last_score},
        "track_geometry": {
            "track_path": track_geometry.get("track_path") if track_geometry else None,
            "road_points": len(road_map),
            "obstacle_points": len(obstacle_points),
            "road_width": road_width,
            "obstacle_size": obstacle_size,
        },
        "events": event_rows,
    }


def markdown_table(rows: Iterable[dict[str, object]]) -> str:
    lines = ["| Run | T | cR | cO | P | Events | Geometry | Image |", "|---|---:|---:|---:|---:|---:|---|---|"]
    for row in rows:
        score = row["score_end"]  # type: ignore[index]
        geometry = row.get("track_geometry", {})
        assert isinstance(score, dict)
        assert isinstance(geometry, dict)
        lines.append(
            "| {label} | {T} | {cR} | {cO} | {P} | {events} | road={road_points}, obs={obstacle_points} | `{image}` |".format(
                label=row["label"],
                T=score.get("T", ""),
                cR=score.get("cR", ""),
                cO=score.get("cO", ""),
                P=score.get("P", ""),
                events=len(row["events"]),  # type: ignore[arg-type]
                road_points=geometry.get("road_points", ""),
                obstacle_points=geometry.get("obstacle_points", ""),
                image=row["image"],
            )
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", nargs=2, action="append", metavar=("LABEL", "RUN_DIR"), required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--json-out", required=True)
    parser.add_argument("--md-out", required=True)
    parser.add_argument("--track", nargs=2, action="append", metavar=("LABEL", "TRACK_MO"))
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    track_by_label = {label: load_track_geometry(Path(path)) for label, path in (args.track or [])}
    results = [plot_run(label, Path(run_dir), out_dir, track_by_label.get(label)) for label, run_dir in args.run]

    json_path = Path(args.json_out)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps({"runs": results}, ensure_ascii=False, indent=2), encoding="utf-8")

    md_path = Path(args.md_out)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    sections = [
        "# Trajectory Event Review",
        "",
        "Generated from saved MWORKS `extra_timeseries.csv` and `score_timeseries.csv` exports.",
        "When `--track` is provided, official read-only `roadMap` and `obstaclePoint` geometry is overlaid for diagnosis.",
        "This is trajectory evidence only; it does not prove physical UGV behavior or final competition submission readiness.",
        "",
        markdown_table(results),
        "",
        "## Event Details",
    ]
    for result in results:
        sections.extend(["", f"### {result['label']}", ""])
        if not result["events"]:
            sections.append("No score-change events detected.")
            continue
        sections.append("| Event | Time/s | Changes | x | y | dRoadCenter | dNearestObs |")
        sections.append("|---:|---:|---|---:|---:|---:|---:|")
        for event in result["events"]:  # type: ignore[index]
            d_road = event.get("distance_to_road_center")
            d_obs = event.get("distance_to_nearest_obstacle")
            sections.append(
                "| {event} | {time_s:.2f} | {changes} | {x:.4g} | {y:.4g} | {d_road} | {d_obs} |".format(
                    event=event["event"],
                    time_s=event["time_s"],
                    changes=", ".join(event["changes"]),
                    x=event["x"],
                    y=event["y"],
                    d_road="" if d_road is None else f"{d_road:.4g}",
                    d_obs="" if d_obs is None else f"{d_obs:.4g}",
                )
            )
    md_path.write_text("\n".join(sections) + "\n", encoding="utf-8")

    print(json.dumps({"ok": True, "runs": len(results), "md_out": str(md_path), "json_out": str(json_path)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
