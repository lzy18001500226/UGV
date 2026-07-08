#!/usr/bin/env python3
"""Check whether the UGV initial-race submission candidate is ready.

Static/control-plane checker only: it does not run MWORKS, create a final zip,
or send a competition submission email.
"""
from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

REQUIRED_PATHS = {
    "model_root": Path("Models/UGV"),
    "model_package": Path("Models/UGV/package.mo"),
    "controller": Path("Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo"),
    "official_report_template": Path("References/official_materials/5-仿真报告模板（仅供参考）/仿真报告模板.docx"),
    "report_draft": Path("Results/deliverables/report_drafts/initial_race_report_draft_blocker_aware_20260709.md"),
    "report_docx_draft": Path("Results/deliverables/report_drafts/initial_race_report_draft_blocker_aware_20260709.docx"),
    "report_render_qa_note": Path("Results/deliverables/report_drafts/render_check_20260709_0118/QA_NOTE.md"),
    "controller_deployability_static_check": Path("Results/evidence/controller_deployability_static_check_20260709_0153.md"),
    "one_track_metrics": Path("Results/metrics/one_track_tuning_20260708_231430.md"),
    "four_track_summary": Path("Results/metrics/four_track_summary_20260708_231430.md"),
    "activation_blocker": Path("Results/evidence/m6_mworks_activation_blocker_20260708_235918.md"),
}

NO_EDIT_ZONES = [
    Path("Models/UGV/Vehicle"),
    Path("Models/UGV/Road"),
    Path("Models/UGV/saidao"),
    Path("Models/UGV/CountPoint"),
    Path("Models/UGV/Example"),
    Path("References/official_materials"),
]

TRACK_NAMES = [
    "UGV.saidao.saidao1",
    "UGV.saidao.saidao2",
    "UGV.saidao.saidao3",
    "UGV.saidao.saidao4",
]


def run_git(repo: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args], cwd=repo, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False
    )


def git_list(repo: Path, *args: str) -> list[str]:
    cp = run_git(repo, list(args))
    if cp.returncode != 0:
        return []
    return [line for line in cp.stdout.splitlines() if line.strip()]


def path_status(repo: Path, path: Path) -> dict[str, Any]:
    full = repo / path
    return {
        "path": path.as_posix(),
        "exists": full.exists(),
        "is_file": full.is_file(),
        "is_dir": full.is_dir(),
        "size_bytes": full.stat().st_size if full.exists() and full.is_file() else None,
    }


def no_edit_status(repo: Path) -> list[dict[str, Any]]:
    rows = []
    for zone in NO_EDIT_ZONES:
        cp = run_git(repo, ["status", "--porcelain", "--", zone.as_posix()])
        rows.append({
            "path": zone.as_posix(),
            "exists": (repo / zone).exists(),
            "dirty_entries": [line for line in cp.stdout.splitlines() if line.strip()],
        })
    return rows


def four_track_gate(repo: Path, summary_path: Path) -> dict[str, Any]:
    full = repo / summary_path
    if not full.exists():
        return {"ready": False, "reason": "four_track_summary_missing", "tracks": []}
    text = full.read_text(encoding="utf-8", errors="replace")
    rows = []
    ready = True
    for name in TRACK_NAMES:
        present = name in text
        blocked = False
        unavailable = False
        if present:
            idx = text.find(name)
            window = text[idx: idx + 500].lower()
            blocked = "blocked" in window
            unavailable = "n/a" in window
        if (not present) or blocked or unavailable:
            ready = False
        rows.append({
            "track": name,
            "present": present,
            "blocked_or_unavailable": blocked or unavailable,
        })
    return {
        "ready": ready,
        "reason": None if ready else "four_track_metrics_blocked_or_unavailable",
        "tracks": rows,
    }


def build_report(repo: Path, final_approval: bool) -> dict[str, Any]:
    required = {key: path_status(repo, path) for key, path in REQUIRED_PATHS.items()}
    missing_required = [key for key, row in required.items() if not row["exists"]]
    no_edit = no_edit_status(repo)
    dirty_no_edit = [row for row in no_edit if row["dirty_entries"]]
    model_files = git_list(repo, "ls-files", "Models/UGV")
    evidence_files = git_list(repo, "ls-files", "Results/metrics", "Results/evidence")
    report_files = git_list(repo, "ls-files", "Results/deliverables", "Docs/Design", "Docs/Workflows")
    four_track = four_track_gate(repo, REQUIRED_PATHS["four_track_summary"])

    blockers = []
    if missing_required:
        blockers.append({"code": "missing_required_paths", "items": missing_required})
    if dirty_no_edit:
        blockers.append({"code": "hard_no_edit_zone_dirty", "items": dirty_no_edit})
    if not four_track["ready"]:
        blockers.append({"code": four_track["reason"], "items": four_track["tracks"]})
    if not final_approval:
        blockers.append({"code": "final_submission_approval_missing", "items": []})

    package_plan = {
        "include": [
            "Models/UGV/",
            "Results/deliverables/report_drafts/initial_race_report_draft_blocker_aware_20260709.md",
            "Results/deliverables/report_drafts/initial_race_report_draft_blocker_aware_20260709.docx",
            "Results/metrics/four_track_summary_<final_timestamp>.md once available",
            "Results/metrics/one_track_tuning_20260708_231430.md",
            "Results/evidence/static_model_grounding_20260708_210142.md",
            "Results/evidence/controller_design_review_20260708_215659.md",
            "Results/evidence/controller_v1_source_notes_20260708_220257.md",
            "Results/evidence/controller_deployability_static_check_20260709_0153.md",
        ],
        "exclude": [
            "Results/tmp/",
            "Scripts/mworks/__pycache__/",
            "untracked scratch simulation folders unless promoted by manifest",
            "References/research/ large upstream sources unless cited in report appendix",
            "final competition email/send action until user approval",
        ],
    }

    return {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "repo": str(repo),
        "ready": not blockers,
        "final_approval": final_approval,
        "required_paths": required,
        "counts": {
            "tracked_model_files": len(model_files),
            "tracked_metric_or_evidence_files": len(evidence_files),
            "tracked_report_or_workflow_files": len(report_files),
        },
        "hard_no_edit_zones": no_edit,
        "four_track_gate": four_track,
        "blockers": blockers,
        "package_plan": package_plan,
        "non_claims": [
            "Does not run MWORKS.",
            "Does not create final zip.",
            "Does not send final competition submission email.",
            "Does not convert blocked four-track evidence into score claims.",
        ],
    }


def write_markdown(report: dict[str, Any], path: Path) -> None:
    blockers = report["blockers"]
    lines = [
        "# UGV Submission Readiness Dry Run",
        "",
        f"generated_at: {report['generated_at']}",
        f"ready: {str(report['ready']).lower()}",
        f"final_approval: {str(report['final_approval']).lower()}",
        "",
        "## Summary",
        "",
        f"- tracked_model_files: {report['counts']['tracked_model_files']}",
        f"- tracked_metric_or_evidence_files: {report['counts']['tracked_metric_or_evidence_files']}",
        f"- tracked_report_or_workflow_files: {report['counts']['tracked_report_or_workflow_files']}",
        "",
        "## Blockers",
        "",
    ]
    if blockers:
        for blocker in blockers:
            lines.append(f"- {blocker['code']}")
    else:
        lines.append("- none")
    lines.extend(["", "## Required Paths", ""])
    for key, row in report["required_paths"].items():
        lines.append(f"- {key}: {row['path']} -> exists={str(row['exists']).lower()}")
    lines.extend(["", "## Four Track Gate", ""])
    lines.append(f"ready: {str(report['four_track_gate']['ready']).lower()}")
    for row in report["four_track_gate"]["tracks"]:
        lines.append(
            f"- {row['track']}: present={str(row['present']).lower()}, "
            f"blocked_or_unavailable={str(row['blocked_or_unavailable']).lower()}"
        )
    lines.extend(["", "## Package Plan", "", "### Include", ""])
    for item in report["package_plan"]["include"]:
        lines.append(f"- `{item}`")
    lines.extend(["", "### Exclude", ""])
    for item in report["package_plan"]["exclude"]:
        lines.append(f"- `{item}`")
    lines.extend(["", "## Non-Claims", ""])
    for item in report["non_claims"]:
        lines.append(f"- {item}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="UGV repository root")
    parser.add_argument("--json-out", help="Write JSON report to this path")
    parser.add_argument("--md-out", help="Write Markdown report to this path")
    parser.add_argument("--final-approval", action="store_true", help="User explicitly approved final submission send/package")
    parser.add_argument("--fail-on-not-ready", action="store_true", help="Exit 1 when not ready")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    report = build_report(repo, args.final_approval)

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
        "ready": report["ready"],
        "blocker_codes": [item["code"] for item in report["blockers"]],
        "tracked_model_files": report["counts"]["tracked_model_files"],
        "tracked_metric_or_evidence_files": report["counts"]["tracked_metric_or_evidence_files"],
    }, ensure_ascii=False))

    if args.fail_on_not_ready and not report["ready"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
