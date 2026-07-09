# New Conversation Context

> Compact startup context for `C:\Users\HP\Desktop\UGV`.

Status: v13 side-trigger 0.45 remains the accepted four-track baseline; Track4 v14/v15, Track1/Track3 v16-v18, Track1 v19 recovery, v20/v21 follow-up, v22 lateral-dwell, v23 cruise-speed, v24 ControlAllocate filter, v25 PathPlanner max-steer, v26 CtrlAlloc steer-weight, v27 CtrlAlloc default obstacle-weight no-op, v28 CtrlAlloc speed-channel, v29 side-danger speed-regulation, v30 side-danger steering-floor, and v31 avoid-release 3s candidates were tested and rejected, 2026-07-09 CST.

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

Current phase cursor: `v13 accepted and restored; Track4 v14/v15, Track1/Track3 v16-v18, Track1 v19 recovery, v20/v21 follow-up, v22 lateral-dwell, v23 cruise-speed, v24 ControlAllocate filter, v25 PathPlanner max-steer, v26 CtrlAlloc steer-weight, v27 CtrlAlloc default obstacle-weight no-op, v28 CtrlAlloc speed-channel, v29 side-danger speed-regulation, v30 side-danger steering-floor, and v31 avoid-release 3s candidates rejected; next attempt should not be blind scalar tuning and should start from fresh failure evidence or a new mechanism hypothesis`.

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

Track1 / Track3 v23 cruise-speed follow-up:

```text
Results/metrics/ctrlalloc_contribution_analysis_v13_v20_20260709_1925.md
Results/metrics/track1_track3_candidate_review_v23_20260709_2000.md
Results/evidence/controller_deployability_static_check_v13_restored_after_v23_20260709_2000.md
```

Track1 / Track3 v24/v25 ControlAllocate and PathPlanner follow-up:

```text
Results/metrics/track1_track3_candidate_review_v24_v25_20260709_1915.md
Results/metrics/ctrlalloc_contribution_analysis_v24_fast_oa_filter_20260709_1840.md
Results/metrics/final_steer_extreme_scan_v13_v20_v24_20260709_1850.md
Results/evidence/controller_deployability_static_check_v13_restored_after_v25_20260709_1915.md
```

Track4 v13 diagnostic and v26 CtrlAlloc steer-weight follow-up:

```text
Results/simulations/diagnostic_v13_signals_saidao4_120s_20260709_1910/
Results/metrics/collision_window_analysis_v13_track4_20260709_1910.md
Results/metrics/signal_window_summary_v13_track4_20260709_1910.md
Results/metrics/ctrlalloc_contribution_analysis_v13_track1_track3_track4_20260709_1915.md
Results/metrics/track4_candidate_review_v26_ctrlalloc_steerpp06_20260709_1930.md
Results/evidence/controller_deployability_static_check_v13_restored_after_v26_20260709_1930.md
```

Track3 v27 CtrlAlloc default obstacle-weight no-op follow-up:

```text
Results/simulations/controller_v27_ctrlalloc_factoroa05_saidao3_120s_20260709_1940/
Results/metrics/collision_window_analysis_v27_ctrlalloc_factoroa05_20260709_1945.md
Results/metrics/ctrlalloc_contribution_analysis_v27_ctrlalloc_factoroa05_20260709_1945.md
Results/metrics/track3_candidate_review_v27_ctrlalloc_factoroa05_20260709_1950.md
Results/evidence/controller_deployability_static_check_v13_restored_after_v27_20260709_1950.md
```

Track3 v28 CtrlAlloc speed-channel follow-up:

```text
Results/simulations/controller_v28_ctrlalloc_speedoa2x_saidao3_120s_20260709_1930/
Results/metrics/collision_window_analysis_v28_ctrlalloc_speedoa2x_20260709_1935.md
Results/metrics/ctrlalloc_contribution_analysis_v28_ctrlalloc_speedoa2x_20260709_1935.md
Results/metrics/track3_candidate_review_v28_ctrlalloc_speedoa2x_20260709_1940.md
Results/evidence/controller_deployability_static_check_v13_restored_after_v28_20260709_1940.md
```

Track1 / Track4 v29 side-danger speed-regulation follow-up:

```text
Docs/Design/high_score_optimization_strategy_20260709.md
Results/evidence/controller_deployability_static_check_v29_side_danger_speed_20260709_2105.md
Results/simulations/controller_v29_side_danger_speed_saidao1_120s_20260709_2105/
Results/simulations/controller_v29_side_danger_speed_saidao4_120s_20260709_2115/
Results/metrics/track1_track4_candidate_review_v29_side_danger_speed_20260709_2130.md
Results/evidence/controller_deployability_static_check_v13_restored_after_v29_20260709_2130.md
```

v30 side-danger steering-floor follow-up:

```text
Docs/Design/unified_obstacle_avoidance_v30_plan_20260709.md
Results/evidence/controller_deployability_static_check_v30_side_danger_steering_floor_20260709_2109.md
Results/simulations/controller_v30_side_danger_steering_floor_saidao1_120s_20260709_2110/
Results/simulations/controller_v30_side_danger_steering_floor_saidao4_120s_20260709_2112/
Results/metrics/track1_track4_candidate_review_v30_side_danger_steering_floor_20260709_2116.md
Results/evidence/controller_deployability_static_check_v13_restored_after_v30_20260709_2116.md
```

v30 remained one algorithm and passed the static source gate, but Track1 and
Track4 both stayed at `P=8.8`, `cR=3`, `cO=0`, so the candidate is rejected as
no improvement and the source was restored to v13 semantics. Do not continue to
Track2/Track3 regression for v30 because the target evidence did not improve.

v31 avoid-release 3s follow-up:

```text
Results/metrics/v13_pre_collision_control_attribution_20260709_2140.md
Docs/Design/unified_obstacle_avoidance_v31_plan_20260709.md
Results/evidence/controller_deployability_static_check_v31_avoid_release3s_20260709_2153.md
Results/simulations/controller_v31_avoid_release3s_saidao1_120s_20260709_2155/
Results/metrics/track1_candidate_review_v31_avoid_release3s_20260709_2200.md
Results/evidence/controller_deployability_static_check_v13_restored_after_v31_20260709_2200.md
```

v31 extended the avoid-to-cruise release dwell from 2 seconds to 3 seconds. It
passed the static source gate but badly regressed Track1 to `P=2.0`, `cR=17`,
`cO=3`, versus accepted v13 `P=8.8`, `cR=3`, `cO=0`. The source was restored
to v13 semantics. Do not continue v31 to Track4/Track2/Track3 regression and
do not continue the longer reverse/avoid dwell route without a new mechanism
reason.

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
v23: cruise speed 1 -> 0.8 on Track1/Track3
v24: ControlAllocate obstacle-avoidance filters T=1 -> T=0.5 on Track3
v25: PathPlanner uses declared max_steer clamp on Track1
v26: ControlAllocate path-planner steering weight factor 1.0 -> 0.6 on Track4
v27: ControlAllocate default obstacle-avoidance weight factor_oa 0.3 -> 0.5 on Track3; no-op because generated wrappers instantiate ctrlAlloc(factor_oa = 0.5)
v28: ControlAllocate speed-channel gain1 factor_oa -> 2 * factor_oa on Track3
v29: avoid-mode side-danger speed regulation on Track1/Track4
v30: avoid-lateral bounded steering floor on Track1/Track4
v31: avoid-to-cruise release dwell 2s -> 3s on Track1
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
v23 lowered cruise speed to `0.8`; Track3 score stayed `P=9.2`, while Track1
stopped early with a non-comparable `T=4.95`, so it is also rejected. v24
removed Track3 final-steer extremes but kept `P=9.2` and stopped much earlier
at `T=29.85`; v25 clamped PathPlanner steering but kept Track1 at `P=8.8`.
v26 reduced the path-planner steering contribution in `CtrlAlloc`, but Track4
regressed to `P=4.8`, `cR=11`, `cO=2`, so that route is rejected. v27 changed
the `ControlAllocate` class default for obstacle-avoidance weighting, but the
generated `Saidao*Eval` wrappers already instantiate `ctrlAlloc(factor_oa =
0.5)`, so exported v13/v27 evidence both show `ctrlAlloc.factor_oa=0.5`; v27 is
rejected as a no-op rather than as a valid stronger-weight test. The source was
restored to v13 semantics. v28 doubled only the obstacle-avoidance speed
channel in `CtrlAlloc`, but Track3 stopped at `T=4.0` with
`simulate_failed`/`exit_state=2`, so the readable `P=10.0` is non-comparable
and the candidate is rejected. v29 side-danger speed regulation passed the
static source gate and ran Track1/Track4, but both target tracks stayed at
`P=8.8`, `cR=3`, `cO=0`, matching v13 instead of improving it; the candidate
is rejected and the source was restored to v13 semantics. v30 added a bounded
avoid-lateral steering floor, also passed the static source gate, and ran
Track1/Track4; both target tracks again stayed at `P=8.8`, `cR=3`, `cO=0`, so
it is rejected as no improvement and the source was restored to v13 semantics.
v31 extended avoid release to 3 s, passed the static gate, but regressed Track1
to `P=2.0`, `cR=17`, `cO=3`, so it is rejected and the source was restored to
v13 semantics. The next attempt should start from fresh collision-window,
control-attribution, or trajectory evidence, then run the target weak track
first and only expand to regression when target evidence improves.
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
