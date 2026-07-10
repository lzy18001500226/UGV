#!/usr/bin/env python3
"""Create a non-destructive UGV submission-candidate dry-run manifest."""
from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime
from pathlib import Path

DEFAULT_READINESS = Path("Results/deliverables/submission_dry_runs/submission_readiness_post_v67_v48_review_20260710.json")


def git_count(repo: Path, path: str) -> int:
    cp = subprocess.run(["git", "ls-files", path], cwd=repo, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    return len([x for x in cp.stdout.splitlines() if x.strip()]) if cp.returncode == 0 else 0


def path_row(repo: Path, path: str) -> dict:
    full = repo / path
    return {"path": path, "exists": full.exists(), "kind": "dir" if full.is_dir() else "file" if full.is_file() else "missing"}


def build_plan(repo: Path, readiness: Path) -> dict:
    ready_path = readiness if readiness.is_absolute() else repo / readiness
    data = json.loads(ready_path.read_text(encoding="utf-8"))
    blockers = [item["code"] for item in data.get("blockers", [])]
    include = [
        "Results/deliverables/report_drafts/initial_race_report_draft_v48_metrics_20260710.docx",
        "Results/deliverables/report_drafts/initial_race_report_draft_v48_metrics_20260710.md",
        "Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/QA_NOTE.md",
        "Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/word_com_export_qa/page_render_qa.md",
        "Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/word_com_export_qa/contact_sheet.png",
        "Results/figures/trajectory_event_review_v48_20260710/v48_track1_trajectory_events.png",
        "Results/figures/trajectory_event_review_v48_20260710/v48_track3_trajectory_events.png",
        "Results/figures/trajectory_event_review_v48_20260710/v48_track3_road_obstacle_overlay.png",
        "Results/metrics/one_track_tuning_20260708_231430.md",
        "Results/metrics/four_track_candidate_review_v48_opposing_steer_guard_20260710.md",
        "Results/metrics/post_v67_v68_attribution_decision_20260710.md",
        "Results/evidence/static_model_grounding_20260708_210142.md",
        "Results/evidence/controller_design_review_20260708_215659.md",
        "Results/evidence/controller_v1_source_notes_20260708_220257.md",
        "Results/evidence/controller_deployability_static_check_v48_reconfirmed_after_v67_20260710.md",
        readiness.as_posix(),
    ]
    return {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "readiness_report": readiness.as_posix(),
        "ready_to_create_final_zip": bool(data.get("ready")) and not blockers,
        "blockers": blockers,
        "model_tracked_files": git_count(repo, "Models/UGV"),
        "would_include": [path_row(repo, x) for x in include],
        "would_exclude": [
            "Results/tmp/",
            "Results/simulations/* scratch folders unless promoted by manifest",
            "Scripts/**/__pycache__/",
            "References/research/ large upstream snapshots unless cited in final appendix",
            "final competition email/send action until user approval",
        ],
        "non_claims": ["Does not create a zip.", "Does not send final submission email.", "Does not run MWORKS during this dry run."],
    }


def write_md(plan: dict, out: Path) -> None:
    lines = ["# UGV Submission Candidate Dry-Run Manifest", "", f"generated_at: {plan['generated_at']}", f"ready_to_create_final_zip: {str(plan['ready_to_create_final_zip']).lower()}", f"readiness_report: `{plan['readiness_report']}`", "", "## Blockers", ""]
    lines.extend(f"- {x}" for x in plan["blockers"]) if plan["blockers"] else lines.append("- none")
    lines.extend(["", "## Would Include", "", f"- `Models/UGV/` tracked files: {plan['model_tracked_files']}"])
    lines.extend(f"- `{x['path']}` -> exists={str(x['exists']).lower()}, kind={x['kind']}" for x in plan["would_include"])
    lines.extend(["", "## Would Exclude", ""])
    lines.extend(f"- `{x}`" for x in plan["would_exclude"])
    lines.extend(["", "## Non-Claims", ""])
    lines.extend(f"- {x}" for x in plan["non_claims"])
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".")
    parser.add_argument("--readiness", default=str(DEFAULT_READINESS))
    parser.add_argument("--json-out")
    parser.add_argument("--md-out")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    plan = build_plan(repo, Path(args.readiness))
    if args.json_out:
        out = Path(args.json_out)
        if not out.is_absolute():
            out = repo / out
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.md_out:
        out = Path(args.md_out)
        if not out.is_absolute():
            out = repo / out
        write_md(plan, out)
    print(json.dumps({
        "ready_to_create_final_zip": plan["ready_to_create_final_zip"],
        "blockers": plan["blockers"],
        "model_tracked_files": plan["model_tracked_files"],
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
