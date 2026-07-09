#!/usr/bin/env python3
"""Build a local review-only UGV submission candidate package.

This script creates a local candidate archive for user review. It does not send
competition email, does not mark final approval as granted, and refuses to build
when readiness blockers other than final approval are present.
"""
from __future__ import annotations

import argparse
import json
import zipfile
from datetime import datetime
from pathlib import Path
from typing import Iterable

DEFAULT_READINESS = Path("Results/deliverables/submission_dry_runs/submission_readiness_20260709_124115.json")
DEFAULT_PLAN = Path("Results/deliverables/submission_dry_runs/submission_candidate_plan_20260709_124115.json")
DEFAULT_OUT_DIR = Path("Results/deliverables/submission_candidates")
ALLOWED_REVIEW_BLOCKERS = {"final_submission_approval_missing"}

INCLUDE_FILES = [
    Path("Results/deliverables/report_drafts/initial_race_report_draft_m6_metrics_20260709_123905.docx"),
    Path("Results/deliverables/report_drafts/initial_race_report_draft_blocker_aware_20260709.md"),
    Path("Results/deliverables/report_drafts/render_check_20260709_0118/QA_NOTE.md"),
    Path("Results/metrics/one_track_tuning_20260708_231430.md"),
    Path("Results/metrics/four_track_summary_20260709_120547.md"),
    Path("Results/evidence/static_model_grounding_20260708_210142.md"),
    Path("Results/evidence/controller_design_review_20260708_215659.md"),
    Path("Results/evidence/controller_v1_source_notes_20260708_220257.md"),
    Path("Results/evidence/controller_deployability_static_check_20260709_0222.md"),
    Path("Results/evidence/mworks_login_license_recovery_gui_api_confirmed_20260709.md"),
]

EXCLUDE_DIR_NAMES = {"__pycache__", ".git"}
EXCLUDE_SUFFIXES = {".pyc", ".pyo"}


def read_json(repo: Path, path: Path) -> dict:
    full = path if path.is_absolute() else repo / path
    return json.loads(full.read_text(encoding="utf-8"))


def rel_walk_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        parts = set(path.parts)
        if parts & EXCLUDE_DIR_NAMES:
            continue
        if path.suffix in EXCLUDE_SUFFIXES:
            continue
        yield path


def add_file(files: dict[Path, Path], repo: Path, rel: Path) -> None:
    full = repo / rel
    if not full.exists() or not full.is_file():
        raise FileNotFoundError(rel.as_posix())
    files[rel] = full


def collect_files(repo: Path, extra_files: Iterable[Path] = ()) -> dict[Path, Path]:
    files: dict[Path, Path] = {}
    model_root = repo / "Models" / "UGV"
    if not model_root.is_dir():
        raise FileNotFoundError("Models/UGV")
    for full in rel_walk_files(model_root):
        files[full.relative_to(repo)] = full
    for rel in INCLUDE_FILES:
        add_file(files, repo, rel)
    for extra in extra_files:
        rel = extra.relative_to(repo) if extra.is_absolute() else extra
        add_file(files, repo, rel)
    return dict(sorted(files.items(), key=lambda item: item[0].as_posix()))


def blocker_codes(readiness: dict) -> list[str]:
    return [item.get("code", "") for item in readiness.get("blockers", [])]


def build_manifest(repo: Path, files: dict[Path, Path], readiness: dict, label: str) -> dict:
    codes = blocker_codes(readiness)
    return {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "label": label,
        "repo": str(repo),
        "review_only": True,
        "final_submission_approved": False,
        "blockers": codes,
        "allowed_review_blockers": sorted(ALLOWED_REVIEW_BLOCKERS),
        "file_count": len(files),
        "total_bytes": sum(full.stat().st_size for full in files.values()),
        "included_paths": [rel.as_posix() for rel in files],
        "non_claims": [
            "Does not send final competition email.",
            "Does not mark final submission approval as granted.",
            "Does not run MWORKS during package creation.",
            "Does not modify official no-edit zones.",
        ],
    }


def write_manifest_md(manifest: dict, out: Path) -> None:
    lines = [
        "# UGV Review Candidate Package Manifest",
        "",
        f"generated_at: {manifest['generated_at']}",
        f"label: {manifest['label']}",
        "review_only: true",
        "final_submission_approved: false",
        f"file_count: {manifest['file_count']}",
        f"total_bytes: {manifest['total_bytes']}",
        "",
        "## Blockers",
        "",
    ]
    lines.extend(f"- {code}" for code in manifest["blockers"]) if manifest["blockers"] else lines.append("- none")
    lines.extend(["", "## Included Paths", ""])
    lines.extend(f"- `{path}`" for path in manifest["included_paths"])
    lines.extend(["", "## Non-Claims", ""])
    lines.extend(f"- {item}" for item in manifest["non_claims"])
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".")
    parser.add_argument("--readiness", default=str(DEFAULT_READINESS))
    parser.add_argument("--candidate-plan", default=str(DEFAULT_PLAN))
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    parser.add_argument("--label", default=datetime.now().strftime("%Y%m%d_%H%M%S"))
    parser.add_argument("--allow-review-with-final-approval-blocker", action="store_true")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    readiness_path = Path(args.readiness)
    plan_path = Path(args.candidate_plan)
    readiness = read_json(repo, readiness_path)
    _ = read_json(repo, plan_path)
    codes = set(blocker_codes(readiness))
    unexpected = sorted(codes - ALLOWED_REVIEW_BLOCKERS)
    if unexpected:
        raise SystemExit(f"Refusing to build candidate; unresolved readiness blockers: {unexpected}")
    if codes and not args.allow_review_with_final_approval_blocker:
        raise SystemExit(
            "Readiness still has final-approval blocker. Re-run with "
            "--allow-review-with-final-approval-blocker to build a local review-only candidate."
        )

    files = collect_files(repo, [readiness_path, plan_path])
    out_dir = Path(args.out_dir)
    if not out_dir.is_absolute():
        out_dir = repo / out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    base = f"UGV_initial_race_review_candidate_{args.label}"
    zip_path = out_dir / f"{base}.zip"
    manifest_json = out_dir / f"{base}_manifest.json"
    manifest_md = out_dir / f"{base}_manifest.md"

    manifest = build_manifest(repo, files, readiness, args.label)
    manifest["archive_path"] = zip_path.relative_to(repo).as_posix()
    manifest["manifest_json"] = manifest_json.relative_to(repo).as_posix()
    manifest["manifest_md"] = manifest_md.relative_to(repo).as_posix()

    manifest_json.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_manifest_md(manifest, manifest_md)

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for rel, full in files.items():
            zf.write(full, rel.as_posix())
        zf.write(manifest_json, manifest_json.relative_to(repo).as_posix())
        zf.write(manifest_md, manifest_md.relative_to(repo).as_posix())

    print(json.dumps({
        "archive": zip_path.relative_to(repo).as_posix(),
        "manifest_json": manifest_json.relative_to(repo).as_posix(),
        "manifest_md": manifest_md.relative_to(repo).as_posix(),
        "file_count": manifest["file_count"],
        "review_only": True,
        "blockers": sorted(codes),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
