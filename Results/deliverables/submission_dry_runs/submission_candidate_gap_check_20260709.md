# Submission Candidate Gap Check - 20260709

Status: dry-run gap check only. This is not a final submission package and must not be sent.

## Competition Deliverables

Official initial-race deliverables from project docs:

```text
1. 仿真模型
2. 仿真报告
```

Full acceptance requires four official tracks with time, road-collision count, obstacle-collision count, and score evidence.

## Current Candidate Contents

### Model / Source

| Item | Status | Path / Evidence | Notes |
|---|---|---|---|
| Working UGV package | present | `Models/UGV/` | Official working copy. Hard no-edit zones preserved. |
| Controller implementation target | present | `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo` | Current candidate is `controller_v5_front_dwell_2s`. |
| Helper scripts | present | `Scripts/mworks/ugv_baseline_probe.py` | Supports dependency `.mol` loading and SimulateModelEx option overrides. |

### Evidence

| Gate | Status | Evidence | Notes |
|---|---|---|---|
| M1 source grounding | complete | `Results/evidence/static_model_grounding_20260708_210142.md` | Source/interface/scoring mapping only. |
| M2 baseline bounded runtime | complete_bounded | `Results/simulations/baseline_20260708_213448/` | Bounded run, not full contest score. |
| M3 controller design | complete | `Docs/Design/避障算法设计.md`; `Results/evidence/controller_design_review_20260708_215659.md` | Design is bounded reactive safety layer. |
| M4 controller bounded runtime | complete_bounded | `Results/simulations/controller_refsysblock_20260708_221000/` | Bounded run, not full contest score. |
| M5 one-track tuning | review_ready | `Results/metrics/one_track_tuning_20260708_231430.md` | Current best candidate is v5. |
| M6 four-track evaluation | blocked | `Results/evidence/m6_mworks_activation_blocker_20260708_235918.md`; `Results/evidence/m6_mworks_activation_recheck_20260709_000731.md` | MWORKS activation blocks loading `TADynamics.mol`; no four-track score claim. |

### Report

| Item | Status | Path | Notes |
|---|---|---|---|
| Official template | present | `References/official_materials/5-仿真报告模板（仅供参考）/仿真报告模板.docx` | Read-only official material. |
| Blocker-aware draft | draft_only | `Results/deliverables/report_drafts/initial_race_report_draft_blocker_aware_20260709.md` | Useful for review, not final because M6 is missing. |

## Blocking Gap

The current package is not submission-ready because full initial-race acceptance requires:

```text
4 official track runs
per-track completion status
time_s
road_collisions
obstacle_collisions
avoidance_score
report tables tied to run folders
```

Current live blocker:

```text
MWORKS L5104-B0 software not activated while opening TADynamics.mol.
```

This happens before official-track `CheckModel` or `SimulateModelEx` can prove or disprove controller performance.

## After Activation Recovery

1. Rerun the dependency-load diagnostic command in `Results/evidence/m6_mworks_activation_blocker_20260708_235918.md`.
2. If `UGV.saidao.saidao1` dependency loading and `CheckModel` pass, run the official-track `SimulateModelEx` option matrix.
3. If one track produces readable score variables, run all four official tracks with the same controller candidate.
4. Update `Results/metrics/four_track_summary_<timestamp>.md`.
5. Convert the blocker-aware report draft into a final report with real four-track tables.
6. Build a local submission candidate package and stop for user final approval before sending.

## Explicit Non-Claims

- No four-track completion is claimed.
- No final initial-race score is claimed.
- No final submission package is claimed.
- No physical UGV readiness is claimed.
- No official no-edit zone was modified.
