"""Extract read-only evaluation-track geometry and compute closed-loop length."""

from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path


ROAD_MAP_RE = re.compile(r"roadMap\s*=\s*(\{\{.*?\}\})\s*,\s*\n+\s*surface\(", re.DOTALL)


def extract_road_map(model_path: Path) -> list[list[float]]:
    text = model_path.read_text(encoding="utf-8")
    match = ROAD_MAP_RE.search(text)
    if not match:
        raise ValueError(f"roadMap literal not found in {model_path}")
    rows = json.loads(match.group(1).replace("{", "[").replace("}", "]"))
    if len(rows) < 2 or any(len(row) < 3 for row in rows):
        raise ValueError(f"invalid roadMap shape in {model_path}")
    return rows


def analyze_road_map(rows: list[list[float]]) -> dict:
    segments = [
        math.hypot(right[0] - left[0], right[1] - left[1])
        for left, right in zip(rows, rows[1:])
    ]
    closed = math.hypot(rows[0][0] - rows[-1][0], rows[0][1] - rows[-1][1])
    speed_weighted_time = sum(
        distance / max(float(rows[index][2]), 1e-9)
        for index, distance in enumerate(segments)
    )
    speed_weighted_time += closed / max(float(rows[-1][2]), 1e-9)
    return {
        "point_count": len(rows),
        "open_polyline_length_m": sum(segments),
        "closing_segment_length_m": closed,
        "closed_loop_length_m": sum(segments) + closed,
        "nominal_speed_min": min(float(row[2]) for row in rows),
        "nominal_speed_max": max(float(row[2]) for row in rows),
        "ideal_time_at_map_speed_s": speed_weighted_time,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    tracks = {}
    for track in range(1, 5):
        model = root / "Models" / "UGV" / "Test" / f"Saidao{track}Eval.mo"
        tracks[f"track{track}"] = {
            "source": str(model),
            **analyze_road_map(extract_road_map(model)),
        }

    output = Path(args.out).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({"tracks": tracks}, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(output), "tracks": tracks}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
