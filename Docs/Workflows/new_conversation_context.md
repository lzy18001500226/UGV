# New Conversation Context

> Compact startup context for `C:\Users\HP\Desktop\UGV`.

Status: v13 side-trigger 0.45 controller remains the current review-ready four-track candidate; Track4 v14/v15, Track1/Track3 v16-v18, Track1 v19 recovery, v20/v21 follow-up, and v22 lateral-dwell candidates were tested and rejected, 2026-07-09 CST.

## 0. Startup Chain

```text
1. AGENTS.md
2. Docs/Workflows/new_conversation_context.md
3. Docs/Index/workflow_index.md
4. Docs/Workflows/master_execution_plan.md
5. Docs/Workflows/long_task_status_board.md when running or resuming long work
6. Topic-specific design/workflow docs only as needed
```

This is a standalone MWORKS/Sysplorer/Sysblock UGV obstacle-avoidance project. It is not MoSim's UAV/ROS1/Sunray/UE mainline.

## 1. Current Goal

```text
load official UGV model
  -> run baseline official examples
  -> implement/tune obstacle avoidance controller
  -> run four official tracks
  -> collect time/collision/score evidence
  -> write simulation report
```

## 2. Current Scope

Normal implementation target:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Hard no-edit zones during normal development:

```text
Models/UGV/Vehicle/
Models/UGV/Road/
Models/UGV/saidao/
Models/UGV/CountPoint/
Models/UGV/Example/
References/official_materials/
```

## 3. Current Long Task

Follow `Docs/Workflows/master_execution_plan.md` and status in `Docs/Workflows/long_task_status_board.md`.

Current phase cursor: `v13 accepted and restored; Track4 v14/v15, Track1/Track3 v16-v18, Track1 v19 recovery, v20/v21 follow-up, and v22 lateral-dwell candidates rejected; next attempt should inspect ControlAllocate/path-planner interaction before another controller rewrite`.

The cursor is not a stopping rule. This project should keep advancing through
the competition task tree after each phase commit/push unless a hard blocker or
final submission approval point is reached.

Latest runtime evidence:

```text
Results/simulations/baseline_20260708_213448/
Results/simulations/controller_refsysblock_20260708_221000/
Results/simulations/controller_v5_front_dwell_2s_race1_120s_20260708_230305/
Results/evidence/official_track_api_simulation_blocker_20260708_231430.md
Results/simulations/license_gui_confirm_1s_20260709_after_real_login/
Results/metrics/four_track_summary_20260709_120547.md
```

The M2 gate confirms baseline MWORKS Sysplorer load/check/simulate for
`UGV.Example.Race1` with bounded `stopTime=12`. The M4 gate confirms a runnable
Sysblock controller structure with bounded `stopTime=12`. Neither gate claims
full-track completion or final competition score.

MWORKS/Sysplorer GUI or MCP operations are expected in execution phases. Handle login/license/activation recovery according to `master_execution_plan.md`; final competition submission email still requires explicit user approval.

For `L5104-B0`, do not stop after seeing the text `登录失败，请检查网络后重试`.
Follow `Docs/Workflows/mworks_ugv_simulation_workflow.md`: click the real
Sysplorer login button, enter the approved in-memory credentials, activate in
`帮助 -> 使用许可`, then prove recovery with a 1 s API probe. Latest successful
probe:

```text
Results/simulations/license_gui_confirm_1s_20260709_after_real_login/
```

Current controller candidate is v13: keep the v5 avoid-to-cruise dwell and add
side proximity to the longitudinal avoid trigger:

```text
df <= mindis or dl <= 0.45 or dr <= 0.45
```

Do not re-apply rejected v2-v11 scalar changes unless a new diagnostic reason
exists. v13 was accepted because v12 collision-window analysis showed Track1
obstacle collisions at side distance around `0.46` while `flag=0`, and v13
improved total wrapper score without worsening v12 Track4 score.

Current M6 four-track wrapper metrics:

```text
Track1 Saidao1Eval: T=86.9, cR=4, cO=3, P=7.2
Track2 Saidao2Eval: T=101.8, cR=3, cO=1, P=8.4
Track3 Saidao3Eval: T=50.4, cR=2, cO=5, P=7.2
Track4 Saidao4Eval: T=47.2, cR=2, cO=0, P=9.2
```

The final 120 s runs return `simulate_failed` with `exit_state=2`, but the
enhanced probe reads `T/cR/cO/P` and exports score timeseries after the model
terminal state. Treat this as usable review evidence, not as an optimized final
competition result.

Latest weak-track tuning and accepted candidate:

```text
Results/metrics/track1_track3_tuning_pass_20260709_1425.md
Results/metrics/four_track_summary_v12_side_trigger_20260709_144854.md
Results/metrics/four_track_summary_v13_side_trigger045_20260709_1535.md
```

No v7-v11 scalar tuning change is accepted. v13 side-trigger 0.45 is the
current review-ready controller candidate with total wrapper score `36.4`
versus v12 `34.8` and M6 baseline `32.0`. Later Track4, Track1/Track3, and
Track1 road-edge recovery attempts were rejected, so do not replace v13 without
new target-track evidence and regression checks.

Track4 recovery follow-up:

```text
Results/metrics/track4_recovery_candidate_review_20260709_1715.md
```

Track1/Track3 follow-up:

```text
Results/metrics/collision_window_analysis_v13_track1_track3_20260709_1705.md
Results/metrics/signal_window_summary_v13_track1_track3_20260709_1705.md
Results/metrics/track1_track3_candidate_review_v16_v18_20260709_1755.md
```

Track1 road-edge recovery follow-up:

```text
Results/metrics/track1_v19_road_edge_recovery_review_20260709_1835.md
Results/evidence/controller_deployability_static_check_v13_restored_after_v19_20260709_1835.md
```

Track1 / Track3 v20/v21 follow-up:

```text
Results/metrics/track1_track3_candidate_review_v20_v21_20260709_1855.md
Results/evidence/controller_deployability_static_check_v13_restored_after_v20_v21_20260709_1855.md
```

Track1 v22 lateral-dwell follow-up:

```text
Results/metrics/track1_candidate_review_v22_lateral_init_dwell15_20260709_1815.md
Results/evidence/controller_deployability_static_check_v13_restored_after_v22_20260709_1815.md
```

Rejected candidates:

```text
v14: avoid-lateral initial fixed steer 0.6 -> 0.45
v15: side-trigger/front-clear branch uses low-speed forward instead of reverse
v16: front avoid trigger df <= mindis -> df <= safeF
v17: avoid-lateral initial fixed steer 0.6 -> 0.8
v18: avoid-lateral initial fixed steer 0.6 -> 0.45 on Track1
v19: directed side-clearance initial steering for road-edge recovery on Track1
v20: front-gated side-clearance initial steering on Track1
v21: avoid speed -1 -> -1.2 on Track1/Track3
v22: avoid-lateral initialization dwell 2s -> 1.5s on Track1
```

v14/v15 kept Track4 at `P=8.8` and worsened timing. v16 did not improve
Track3, v17 regressed Track3, and v18 regressed Track1. v19 first failed
`CheckModel` because the Sysblock state machine does not support the attempted
inline `if` expression; the arithmetic fallback removed Track1 road collisions
but increased obstacle collisions to `cO=13`, `P=4.8`. None of these source
changes is accepted. v20 removed Track1 road collisions but increased obstacle
collisions to `cO=10`, `P=6.0`; v21 kept Track3 unchanged and caused Track1 to
stop early with `simulate_false_with_result_variables`; v22 shortened lateral
initialization dwell and badly regressed Track1 to `cR=15`, `cO=1`, `P=3.6`.
The controller source was restored to v13 semantics. The next attempt should be
justified by ControlAllocate/path-planner interaction evidence, then run the
target weak track first and Track1/Track3/Track4 regression checks.
Current M8/M9 review artifacts:

```text
Results/deliverables/report_drafts/initial_race_report_draft_blocker_aware_20260709.md
Results/deliverables/report_drafts/initial_race_report_draft_m6_metrics_20260709_123905.docx
Results/deliverables/report_drafts/initial_race_report_draft_v13_metrics_20260709_1535.md
Results/deliverables/report_drafts/initial_race_report_draft_v13_metrics_20260709_1535.docx
Results/deliverables/submission_dry_runs/submission_readiness_20260709_124115.md
Results/deliverables/submission_dry_runs/submission_candidate_plan_20260709_124115.md
```

`check_submission_readiness.py` currently blocks only on `final_submission_approval_missing` when run without final approval. A local review-only candidate archive may be built for user audit, but final competition email/package sending still requires explicit user approval.

Historical local review-only package:

```text
Results/deliverables/submission_candidates/UGV_initial_race_review_candidate_20260709_124115.zip
Results/deliverables/submission_candidates/UGV_initial_race_review_candidate_20260709_124115_manifest.md
```

This package is for user audit only. It does not imply final submission approval and was not sent to the competition address.
Do not create more submission zip packages unless the user explicitly asks for
another packaging dry run. Push/network failures are operational follow-up
items, not a reason to stop controller tuning.
