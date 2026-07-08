#!/usr/bin/env python3
"""Source-only physical deployability risk checker for the UGV controller."""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path

DEFAULT_CONTROLLER = Path("Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo")


def hits(lines: list[str], pattern: str) -> list[dict]:
    rx = re.compile(pattern)
    return [
        {"line": i, "text": line.strip()}
        for i, line in enumerate(lines, 1)
        if rx.search(line)
    ]


def build_report(repo: Path, controller: Path) -> dict:
    source = controller if controller.is_absolute() else repo / controller
    text = source.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    reciprocal = hits(lines, r"\b1\s*/\s*d[flbr]\b")
    steer = hits(lines, r"\bsteer\s*:=")
    speed = hits(lines, r"\bspeed\s*:=")
    dwell = hits(lines, r"after\s*\(\s*\d+(?:\.\d+)?\s*,\s*sec\s*\)")
    release_dwell = []
    init_dwell = []
    other_dwell = []
    for row in dwell:
        m = re.search(r"after\s*\(\s*(\d+(?:\.\d+)?)\s*,\s*sec\s*\)", row["text"])
        if not m:
            continue
        item = {**row, "value_s": float(m.group(1))}
        if re.search(r"transition\s*\(\s*avoid\s*,\s*cruise\s*,", row["text"]):
            release_dwell.append(item)
        elif re.search(r"transition\s*\(\s*ini_state\s*,", row["text"]):
            init_dwell.append(item)
        elif "displayText" not in row["text"]:
            other_dwell.append(item)

    def unique_values(rows: list[dict]) -> list[float]:
        return sorted({float(row["value_s"]) for row in rows})

    high = []
    medium = []
    low = []
    if reciprocal:
        high.append({
            "code": "reciprocal_distance_terms_present",
            "reason": "1/distance steering can spike near zero sensor readings; replace or prove saturation before physical-ready claims.",
            "hits": reciprocal,
        })
    if not steer:
        high.append({"code": "no_steer_assignments_found", "hits": []})
    if not speed:
        high.append({"code": "no_speed_assignments_found", "hits": []})
    release_values = unique_values(release_dwell)
    if len(release_values) > 1:
        medium.append({
            "code": "mixed_release_dwell_values",
            "reason": "Multiple avoid-to-cruise dwell durations exist; confirm release timing before physical tuning.",
            "values_s": release_values,
            "hits": release_dwell,
        })
    elif release_dwell:
        low.append({
            "code": "avoid_release_dwell_present",
            "values_s": release_values,
            "hits": release_dwell,
        })
    if init_dwell:
        low.append({
            "code": "initialization_dwell_observed",
            "values_s": unique_values(init_dwell),
            "hits": init_dwell,
        })
    if other_dwell:
        low.append({
            "code": "other_dwell_observed",
            "values_s": unique_values(other_dwell),
            "hits": other_dwell,
        })

    return {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "controller": str(controller.as_posix()),
        "ready_for_physical_claim": not high,
        "summary": {"high": len(high), "medium": len(medium), "low": len(low)},
        "findings": {"high": high, "medium": medium, "low": low},
        "observed": {"steer_assignments": steer, "speed_assignments": speed},
        "non_claims": [
            "Does not run MWORKS.",
            "Does not validate race score.",
            "Does not prove physical UGV readiness.",
        ],
    }


def write_markdown(report: dict, out: Path) -> None:
    lines = [
        "# UGV Controller Deployability Static Check",
        "",
        f"generated_at: {report['generated_at']}",
        f"controller: `{report['controller']}`",
        f"ready_for_physical_claim: {str(report['ready_for_physical_claim']).lower()}",
        "",
        "## Summary",
        "",
        f"- high: {report['summary']['high']}",
        f"- medium: {report['summary']['medium']}",
        f"- low: {report['summary']['low']}",
    ]
    for level in ("high", "medium", "low"):
        lines.extend(["", f"## {level.title()} Findings", ""])
        rows = report["findings"][level]
        if not rows:
            lines.append("- none")
            continue
        for item in rows:
            lines.append(f"- {item['code']}: {item.get('reason', '')}".rstrip())
            if "values_s" in item:
                lines.append(f"  - values_s: {item['values_s']}")
            for hit in item.get("hits", [])[:20]:
                lines.append(f"  - line {hit['line']}: `{hit['text']}`")
    lines.extend(["", "## Non-Claims", ""])
    lines.extend(f"- {item}" for item in report["non_claims"])
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".")
    parser.add_argument("--controller", default=str(DEFAULT_CONTROLLER))
    parser.add_argument("--json-out")
    parser.add_argument("--md-out")
    parser.add_argument("--fail-on-high", action="store_true")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    report = build_report(repo, Path(args.controller))
    if args.json_out:
        out = Path(args.json_out)
        if not out.is_absolute():
            out = repo / out
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.md_out:
        out = Path(args.md_out)
        if not out.is_absolute():
            out = repo / out
        write_markdown(report, out)
    print(json.dumps({
        "ready_for_physical_claim": report["ready_for_physical_claim"],
        "high": report["summary"]["high"],
        "medium": report["summary"]["medium"],
    }, ensure_ascii=False))
    return 1 if args.fail_on_high and report["summary"]["high"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
