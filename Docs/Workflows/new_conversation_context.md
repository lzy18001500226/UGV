# New Conversation Context

> Compact startup context for `C:\Users\HP\Desktop\UGV`.

Status: completion-first structural controller redesign. The old `38/40` value is only the sum of avoidance variables and is not an approximately `76/80` official result. Tracks 1-3 have zero verified finishes and Track4 remains unverified. The MWORKS `-gui` API lane is operational. v120 persistent lateral continuity, v121 continuity plus direction hysteresis, and v122 coherent gap-directed entry all regressed Track3; all were rejected and v80 source semantics are restored, 2026-07-11 CST.

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
  -> improve algorithm-model score toward 80/80
  -> keep report/package evidence as support work only
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

Current phase cursor: `Treat official completion as the first hard gate. Continue from restored v80 source only as a comparison baseline. v117-v122 are rejected. Do not repeat scalar speed caps, obstacle-steer attenuation/sign reversal, dwell scans, initial-steer reversals, broad conflict gates, short-lookahead scans, persistent lateral-state release, direction-hysteresis widths, or combinations of those rejected gap-state pieces. Reassess the four-distance controller's observable-state limits and choose a different code-generation-safe completion mechanism; run a target-track completion/progress gate first, then collision regression, then four-track expansion only after a material repeatable gain.`

The cursor is not a stopping rule. This project should keep advancing through
the competition task tree after each phase commit/push unless a hard blocker or
final submission approval point is reached.
Rejected candidates are evidence, not stop conditions. After a rejected
candidate, restore the accepted baseline semantics, save the review/static gate
evidence, send the sparse terminal email, then continue with the next
evidence-backed unified mechanism or targeted research.

Latest runtime evidence:

```text
Results/metrics/four_track_completion_gate_v80_20260711.md
Results/metrics/track3_candidate_review_v117_closed_loop_path_blocked_20260711.md
Results/metrics/track3_candidate_review_v119_conflicting_avoid_offset_suppression_20260711.md
Results/simulations/controller_v80_finish_gate_saidao1_120s_20260711/
Results/simulations/controller_v80_finish_gate_saidao2_120s_20260711/
Results/simulations/controller_v80_finish_gate_saidao3_120s_20260711/
Results/simulations/controller_v80_finish_gate_saidao4_120s_20260711/
Results/metrics/track3_candidate_review_v116_early_negative_curve_speed_guard_20260711.md
Results/evidence/controller_deployability_static_check_v80_restored_after_v116_20260711.md
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

Previous accepted controller candidate was v13: keep the v5 avoid-to-cruise dwell and add
side proximity to the longitudinal avoid trigger:

```text
df <= mindis or dl <= 0.45 or dr <= 0.45
```

Do not re-apply rejected v2-v11 scalar changes unless a new diagnostic reason
exists. v13 was accepted because v12 collision-window analysis showed Track1
obstacle collisions at side distance around `0.46` while `flag=0`, and v13
improved total wrapper score without worsening v12 Track4 score.

Current review-ready best candidate is v45: keep v13 obstacle-controller
semantics and add curvature/large-steering speed regulation in the path
planner:

```text
curve_slowdown_steer = 0.35
curve_slowdown_speed = 0.75
if abs(pathPlanner.steering_angle) > curve_slowdown_steer
   and pathPlanner.target_v > curve_slowdown_speed then
  pathPlanner.target_v := curve_slowdown_speed;
end if;
```

Current v45 four-track wrapper metrics:

```text
Track1 Saidao1Eval: T=120.0, cR=3, cO=0, P=8.8
Track2 Saidao2Eval: T=120.0, cR=1, cO=0, P=9.6
Track3 Saidao3Eval: T=120.0, cR=1, cO=1, P=9.2
Track4 Saidao4Eval: T=120.0, cR=2, cO=0, P=9.2
Total: 36.8
```

v45 evidence:

```text
Docs/Design/unified_obstacle_avoidance_v45_plan_20260710.md
Results/metrics/four_track_candidate_review_v45_curvature_speed_regulation_scaled_20260710_0045.md
```

The historical M6 wrapper baseline is `Results/metrics/four_track_summary_20260709_120547.md`.
Treat v45 as usable review evidence, not as an optimized final competition
result or physical UGV proof.

Current review-ready best candidate is v48: keep v45 path-speed regulation and
add an opposing-steer guard in `ControlAllocate`:

```text
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0
  then 0.5 * unitDelay1.y
  else unitDelay1.y
```

Current v48 four-track wrapper metrics:

```text
Track1 Saidao1Eval: T=120.0, cR=2, cO=0, P=9.2
Track2 Saidao2Eval: T=60.15, cR=1, cO=0, P=9.6
Track3 Saidao3Eval: T=112.45, cR=1, cO=1, P=9.2
Track4 Saidao4Eval: T=112.4, cR=2, cO=0, P=9.2
Total: 37.2
```

v48 evidence:

```text
Docs/Design/unified_obstacle_avoidance_v48_plan_20260710.md
Results/metrics/four_track_candidate_review_v48_opposing_steer_guard_20260710.md
Results/evidence/controller_deployability_static_check_v48_opposing_steer_guard_20260710.md
```

v48 superseded v45 by improving total wrapper score from `36.8` to `37.2`,
mainly from Track1 road-collision reduction. It is now superseded by v74.
Keep v48's runtime caveat visible when comparing historical evidence: Track2,
Track3, and Track4 were scored from exported result variables after
`SimulateModel` returned false with `exit_state=2`.

Current review-ready best candidate is v74: keep v45/v48 speed/allocation
semantics and add guarded medium-curve short lookahead in `PathPlanner`:

```text
only try short lookahead when 0.35 < abs(base_steering_angle) < 1.0;
if the recomputed steering exceeds 1.0 rad, restore the original pursuit point.
```

Current v74 four-track wrapper metrics:

```text
Track1 Saidao1Eval: T=17.4, cR=1, cO=0, P=9.6, simulate_failed / exit_state=2
Track2 Saidao2Eval: T=120.0, cR=1, cO=0, P=9.6, simulate_returned_true / exit_state=0
Track3 Saidao3Eval: T=120.0, cR=1, cO=1, P=9.2, simulate_returned_true / exit_state=0
Track4 Saidao4Eval: T=120.0, cR=2, cO=0, P=9.2, simulate_returned_true / exit_state=0
Total: 37.6
```

v74 evidence:

```text
Docs/Design/unified_obstacle_avoidance_v74_plan_20260710.md
Results/metrics/four_track_candidate_review_v74_guarded_curve_short_lookahead_20260710.md
Results/evidence/controller_deployability_static_check_v74_guarded_curve_short_lookahead_20260710.md
```

v74 supersedes v48 as the review-ready best by improving total wrapper score
from `37.2` to `37.6` and making Track2/3/4 runtime states clean. Keep the
Track1 early-terminal caveat visible; this is not final competition or physical
UGV proof.

v50 moderate curve-speed follow-up:

```text
Docs/Design/unified_obstacle_avoidance_v50_plan_20260710.md
Results/simulations/controller_v50_moderate_curve_speed_saidao3_120s_20260710/
Results/metrics/track3_candidate_review_v50_moderate_curve_speed_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v50_20260710.md
```

v50 is rejected: it improved Track3 runtime comparability to
`simulate_returned_true`, but did not improve Track3 score or collisions
(`T=120.0`, `cR=1`, `cO=1`, `P=9.2`). Do not continue lowering the curvature
speed-regulation threshold as a scalar scan. Continue from v48.

v51 straight brake-arbitration follow-up:

```text
Docs/Design/unified_obstacle_avoidance_v51_plan_20260710.md
Results/simulations/controller_v51_straight_brake_arbitration_saidao3_120s_20260710/
Results/metrics/track3_candidate_review_v51_straight_brake_arbitration_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v51_20260710.md
```

v51 is rejected: the narrow straight-line path-speed arbitration produced an
early Track3 stop at `T=2.25` with readable but non-comparable `P=10.0`. Do not
continue path-speed attenuation or straight-brake arbitration scans. Continue
from v48.

v52 brake-turn coupling follow-up:

```text
Docs/Design/unified_obstacle_avoidance_v52_plan_20260710.md
Results/simulations/controller_v52_brake_turn_coupling_saidao3_120s_20260710/
Results/metrics/track3_candidate_review_v52_brake_turn_coupling_20260710.md
Results/metrics/collision_window_analysis_v52_brake_turn_coupling_track3_20260710.md
Results/metrics/signal_window_summary_v52_brake_turn_coupling_track3_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v52_20260710.md
```

v52 is rejected: it kept Track3 at `P=9.2`, `cR=1`, `cO=1` and ended much
earlier than v48 (`T=8.35` versus v48 `T=112.45`) with
`simulate_failed`/`exit_state=2`. Do not continue brake-turn coupling,
path-speed attenuation, or straight-brake arbitration scans without a new
mechanism reason. Continue from v48.

v53 path-conflict neutralization follow-up:

```text
Docs/Design/unified_obstacle_avoidance_v53_plan_20260710.md
Results/simulations/controller_v53_path_conflict_neutralization_saidao1_120s_20260710/
Results/metrics/track1_candidate_review_v53_path_conflict_neutralization_20260710.md
Results/metrics/collision_window_analysis_v48_v53_track1_20260710.md
Results/metrics/signal_window_summary_v48_v53_track1_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_v53_track1_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v53_20260710.md
```

v53 is rejected: complete path-steer neutralization regressed Track1 from v48
`T=120.0`, `cR=2`, `cO=0`, `P=9.2` to `T=50.55`, `cR=4`, `cO=0`, `P=8.4`
with `simulate_failed`/`exit_state=2`. Do not continue full path-steer
neutralization; v48's half attenuation is safer. Continue from v48.

v54 path-authority 0.35 follow-up:

```text
Docs/Design/unified_obstacle_avoidance_v54_plan_20260710.md
Results/simulations/controller_v54_path_authority_035_saidao3_120s_20260710/
Results/metrics/track3_candidate_review_v54_path_authority_035_20260710.md
Results/metrics/collision_window_analysis_v48_v54_track3_20260710.md
Results/metrics/signal_window_summary_v48_v54_track3_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_v54_track3_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v54_20260710.md
```

v54 is rejected: reducing v48's opposing path-steer contribution from `0.5` to
`0.35` did not improve Track3 collision count or score and shortened Track3
from v48 `T=112.45`, `cR=1`, `cO=1`, `P=9.2` to `T=7.3`, `cR=1`, `cO=1`,
`P=9.2`. Do not continue scanning the path-authority scalar between `0.5` and
`0`. Continue from v48 and inspect obstacle-controller initial/front-risk
structure or a new mechanism.

v55-v57 follow-up:

```text
Docs/Design/unified_obstacle_avoidance_v55_plan_20260710.md
Docs/Design/unified_obstacle_avoidance_v56_plan_20260710.md
Docs/Design/unified_obstacle_avoidance_v57_plan_20260710.md
Results/metrics/track3_candidate_review_v55_low_speed_lookahead_20260710.md
Results/metrics/track3_candidate_review_v56_speed_filter_only_20260710.md
Results/metrics/track3_candidate_review_v57_front_safeF_entry_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_v55_track3_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_v56_track3_20260710.md
```

v55-v57 are rejected. v55 low-speed lookahead floor kept Track3 at `P=9.2`
and shortened the run to `T=27.55`; v56 speed-filter-only acceleration kept
Track3 at `P=9.2` and shortened the run to `T=54.45`; v57 front `safeF` entry
kept Track3 at `P=9.2` and shortened the run to `T=55.35`. Do not continue
low-speed lookahead-floor, filter-time, or simple front-threshold scans without
a new mechanism reason. Continue from v48.

v58 reactive gap initial-bypass follow-up:

```text
Docs/Design/unified_obstacle_avoidance_v58_plan_20260710.md
References/research/reactive_gap_obstacle_avoidance_20260710/MANIFEST.md
Results/simulations/controller_v58_reactive_gap_initial_bypass_saidao3_120s_20260710/
Results/metrics/track3_candidate_review_v58_reactive_gap_initial_bypass_20260710.md
Results/metrics/collision_window_analysis_v48_v58_track3_20260710.md
Results/metrics/signal_window_summary_v48_v58_track3_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_v58_track3_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v58_20260710.md
```

v58 is rejected. It removed the v48 Track3 road-collision event in exported
score variables, but added obstacle collisions and regressed Track3 to
`T=38.80`, `cR=0`, `cO=3`, `P=8.8`. Do not continue stronger initial
side-gap bypass scans without a new mechanism reason. Continue from v48.

v59 close-side initial-direction follow-up:

```text
Docs/Design/unified_obstacle_avoidance_v59_plan_20260710.md
Results/simulations/controller_v59_close_side_initial_direction_saidao1_120s_20260710/
Results/metrics/track1_candidate_review_v59_close_side_initial_direction_20260710.md
Results/metrics/collision_window_analysis_v48_v59_track1_20260710.md
Results/metrics/signal_window_summary_v48_v59_track1_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_v59_track1_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v59_20260710.md
```

v59 is rejected. Track1 exported `P=10.0`, but only after
`simulate_failed`/`exit_state=2` at `T=3.85`, so it is a non-comparable
early-stop artifact rather than a full-track improvement over v48 Track1
`T=120.0`, `cR=2`, `cO=0`, `P=9.2`. Do not continue close-side
initial-direction scans without a new mechanism reason. Continue from v48.

v60 steering-filter follow-up:

```text
Docs/Design/unified_obstacle_avoidance_v60_plan_20260710.md
Results/metrics/trajectory_geometry_review_v48_20260710.md
Results/metrics/signal_geometry_window_summary_v48_20260710.md
Results/simulations/controller_v60_steering_filter_saidao3_120s_20260710/
Results/simulations/controller_v60_steering_filter_saidao3_120s_20260710_retry1/
Results/simulations/controller_v60_steering_filter_saidao1_120s_20260710/
Results/metrics/track1_track3_candidate_review_v60_steering_filter_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v60_20260710.md
```

v60 is rejected. It targeted a measured v48 steering build-up lag by changing
only the obstacle-steering first-order filter from `T=1` to `T=0.35`, but
Track3 produced repeated service communication failure without result
variables and Track1 produced a non-comparable early-stop result
`T=5.3`, `cR=1`, `cO=0`, `P=9.6`. Do not continue direct
steering-filter time-constant scans without a new mechanism reason. Continue
from v48.

v49 path-speed attenuation follow-up:

```text
Docs/Design/unified_obstacle_avoidance_v49_plan_20260710.md
Results/simulations/controller_v49_path_speed_attenuation_saidao3_120s_20260710/
Results/metrics/track3_candidate_review_v49_path_speed_attenuation_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v49_20260710.md
```

v49 is rejected: it produced a non-comparable early Track3 stop at `T=5.75`
despite exported `P=9.6`. Do not continue broad path-speed attenuation.
Continue from v48.

v46 speed-channel 1.2x follow-up:

```text
Docs/Design/unified_obstacle_avoidance_v46_plan_20260710.md
Results/simulations/controller_v46_speed_channel_120pct_saidao3_120s_20260710/
Results/metrics/track3_candidate_review_v46_speed_channel_120pct_20260710.md
```

v46 kept one unified mechanism but is rejected: Track3 stayed at `P=9.2` and
regressed from v45 `T=120.0`, `simulate_returned_true` to `T=45.2`,
`simulate_failed`. Do not continue speed-channel gain escalation.

v47 startup speed-cap follow-up:

```text
Docs/Design/unified_obstacle_avoidance_v47_plan_20260710.md
Results/simulations/controller_v47_startup_speed_cap_saidao3_120s_20260710/
Results/metrics/track3_candidate_review_v47_startup_speed_cap_20260710.md
```

v47 is rejected: Track3 remained comparable at `T=120.0`, but still had
`cR=1`, `cO=1`, `P=9.2`, so it did not improve over v45. Do not continue
simple startup target-speed caps without a new mechanism reason.

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

v32-v35 front-open braking follow-up:

```text
Docs/Design/unified_obstacle_avoidance_v32_plan_20260709.md
Docs/Design/unified_obstacle_avoidance_v33_plan_20260709.md
Docs/Design/unified_obstacle_avoidance_v34_plan_20260709.md
Docs/Design/unified_obstacle_avoidance_v35_plan_20260709.md
Results/metrics/track3_candidate_review_v32_v35_front_open_brake_20260709_2230.md
Results/evidence/controller_deployability_static_check_v13_restored_after_v35_20260709_2227.md
```

v32 failed `CheckModel` because Sysblock state-machine actions do not support
inline conditional expressions. v33 and v34 compiled but the explicit
`front_open_brake` state did not trigger. v35 used a normal algorithm
`if ... then ... end if` in the existing `avoid` state and did trigger stronger
reverse braking, but Track3 stopped earlier at `T=106.35` without improving
`P=9.2`. The source was restored to v13 semantics. Do not keep increasing
reverse braking or avoid dwell without a new mechanism reason.

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
v13 semantics. v32-v35 front-open braking also failed to improve target-track evidence. v40 side-safety bubble produced identical Track4 evidence, v41 guarded release regressed Track4, v42 open-side steering regressed Track1, and v43 side-only longitudinal/lateral decoupling regressed Track1. v44 curvature-speed regulation used the wrong target-speed scale and was a no-op. v45 corrected the scale and improved total wrapper score to `36.8`; v48 later superseded it at `37.2` with a runtime caveat; v49 broad path-speed attenuation is rejected because it early-stopped Track3 at `T=5.75`. The next attempt should start from fresh collision-window,
control-attribution, or trajectory evidence, then run the target weak track
first and only expand to regression when target evidence improves. Do not
continue side-clearance initial-steer gain/cap scans or side-only decoupling
without a new obstacle-horizon/path-authority mechanism.

v61 early-risk allocation arbitration is rejected on Track3:

```text
Docs/Design/unified_obstacle_avoidance_v61_plan_20260710.md
Results/simulations/controller_v61_early_risk_arbitration_saidao3_120s_20260710/
Results/metrics/track3_candidate_review_v61_early_risk_arbitration_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v61_20260710.md
```

It increased final steering at the 1.05 s obstacle event from about `0.162` to
about `0.193`, but the obstacle collision still occurred and the road event
moved earlier (`4.85 s` -> `4.25 s`). Continue from v48; do not retry this
exact small-opposing-path boost without new mechanism evidence.

v62 front-centered initial negative bypass is rejected on Track3:

```text
Docs/Design/unified_obstacle_avoidance_v62_plan_20260710.md
Results/simulations/controller_v62_front_centered_initial_bypass_saidao3_120s_20260710/
Results/metrics/track3_candidate_review_v62_front_centered_initial_bypass_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v62_20260710.md
```

It changed the first obstacle event from `1.05 s` to `1.00 s`, kept
`cR=1`, `cO=1`, `P=9.2`, and shortened Track3 to `T=51.8`. Continue from v48;
do not continue front-centered negative initial-bypass scans without a new
source-level explanation for the controller/allocation coupling.

v63 early steer feedforward is rejected on Track3:

```text
Results/metrics/track3_v48_countpoint_event_diagnostic_20260710.md
Docs/Design/unified_obstacle_avoidance_v63_plan_20260710.md
Results/simulations/controller_v63_early_steer_feedforward_saidao3_120s_20260710/
Results/metrics/track3_candidate_review_v63_early_steer_feedforward_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v63_20260710.md
```

It kept `cR=1`, `cO=1`, `P=9.2`, shortened Track3 to `T=51.45`, made the
first obstacle-distance violation deeper (`~0.106` -> `~0.088`), and moved the
road event earlier (`4.85 s` -> `4.65 s`). Continue from v48; do not continue
direct early steering-feedforward scans without a different trajectory-level
mechanism.

v64 front-clear side-reentry steering is rejected on Track3:

```text
Docs/Design/unified_obstacle_avoidance_v64_plan_20260710.md
Results/simulations/controller_v64_front_clear_side_reentry_saidao3_120s_20260710/
Results/metrics/track3_candidate_review_v64_front_clear_side_reentry_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v64_20260710.md
```

It early-stopped Track3 at `T=3.85`, `cO=1`, `P=9.6`, before a comparable
road-event window. Continue from v48; do not continue front-clear side-reentry
steering scans.

v65 front emergency hold is rejected on Track3:

```text
Docs/Design/unified_obstacle_avoidance_v65_plan_20260710.md
References/research/post_v64_limited_sensor_behaviors_20260710/MANIFEST.md
Results/simulations/controller_v65_front_emergency_hold_saidao3_120s_20260710/
Results/metrics/track3_candidate_review_v65_front_emergency_hold_20260710.md
Results/metrics/collision_window_analysis_v48_v65_track3_20260710.md
Results/metrics/signal_window_summary_v48_v65_track3_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v65_20260710.md
```

It reduced allocated speed at the first Track3 obstacle event and delayed that
event from `1.05 s` to `1.15 s`, but still kept `cR=1`, `cO=1`, `P=9.2` and
shortened Track3 to `T=36.55`. Continue from v48; do not continue this route
by increasing reverse speed, widening the emergency-front threshold, or
scanning emergency-hold constants.

v66 road-edge initial steering boost is rejected on Track3:

```text
Docs/Design/unified_obstacle_avoidance_v66_plan_20260710.md
Results/simulations/controller_v66_road_edge_initial_steer_boost_saidao3_120s_20260710/
Results/metrics/track3_candidate_review_v66_road_edge_initial_steer_boost_20260710.md
Results/metrics/signal_window_summary_v48_v66_track3_20260710.md
Results/evidence/controller_deployability_static_check_v66_road_edge_initial_steer_boost_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v66_20260710.md
```

It boosted the initial avoid steering from `0.6` to `0.8` when either side road
distance was below `0.16`, but Track3 produced a non-comparable early stop at
`T=2.65`, `cO=1`, `P=9.6`. The accepted source semantics were restored to v48
and the restored static gate passed. Continue from v48; do not continue
road-edge initial-steering magnitude scans without a different mechanism.

v67 nearest-distance input diagnostic is rejected as a final route but useful:

```text
Docs/Design/unified_obstacle_avoidance_v67_nearest_distance_input_diagnostic_plan_20260710.md
Models/UGV/Test/Saidao3NearestObstacleDiag.mo
Results/simulations/diagnostic_v67_nearest_obstacle_front_saidao3_120s_20260710/
Results/metrics/track3_candidate_review_v67_nearest_distance_input_diagnostic_20260710.md
Results/metrics/collision_window_analysis_v48_v67_track3_20260710.md
Results/metrics/signal_window_summary_v48_v67_track3_20260710.md
```

It changed the diagnostic wrapper so `distanceSensor1.DisObstacle` feeds the
controller `front_dist`. The run became clean (`simulate_returned_true`,
`exit_state=0`) but Track3 stayed at `T=120.0`, `cR=1`, `cO=1`, `P=9.2`, with
the first obstacle event still at `1.05 s`. Reject nearest-distance input as a
score-improvement route. Continue from v48 and research a deployable
four-direction-only trajectory/reactive safety mechanism instead of repeating
initial-steering or threshold scans.

Post-v67/v68 attribution decision:

```text
Results/metrics/post_v67_v68_attribution_decision_20260710.md
Results/metrics/signal_window_summary_v48_all_tracks_v67_track3_post_research_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_all_tracks_v67_track3_post_research_20260710.md
```

Decision: do not patch v68 immediately. Continue the long task through report,
readiness, and physical-transfer work unless new evidence identifies a
materially different four-distance mechanism.

v69 lateral hysteresis screening:

```text
Docs/Design/unified_obstacle_avoidance_v69_lateral_hysteresis_screening_20260710.md
Results/metrics/lateral_hysteresis_screening_v48_20260710.md
```

Decision: do not patch lateral left/right hysteresis. Saved v48 signals show
zero `chart.steer` sign flips on all four tracks, so remaining Track3 events
are not caused by lateral switching chatter.

Current M8/M9 review artifacts:

```text
Results/deliverables/report_drafts/initial_race_report_draft_blocker_aware_20260709.md
Results/deliverables/report_drafts/initial_race_report_draft_m6_metrics_20260709_123905.docx
Results/deliverables/report_drafts/initial_race_report_draft_v13_metrics_20260709_1535.md
Results/deliverables/report_drafts/initial_race_report_draft_v13_metrics_20260709_1535.docx
Results/deliverables/report_drafts/initial_race_report_draft_v48_metrics_20260710.md
Results/deliverables/report_drafts/initial_race_report_draft_v48_metrics_20260710.docx
Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/QA_NOTE.md
Results/deliverables/submission_dry_runs/submission_readiness_post_v69_v48_trajectory_report_20260710.md
Results/deliverables/submission_dry_runs/submission_candidate_plan_post_v69_v48_trajectory_report_20260710.md
Results/deliverables/submission_dry_runs/submission_readiness_20260709_124115.md
Results/deliverables/submission_dry_runs/submission_candidate_plan_20260709_124115.md
```

The v48/post-v69 report draft is the current review-ready report surface. The
DOCX has a structure/content/image-count QA note and embeds v48 Track1/Track3
trajectory-event figures, but no page-render QA because LibreOffice is not
available on this machine. The M6 and v13 report drafts remain historical audit
artifacts.

`check_submission_readiness.py` currently blocks only on `final_submission_approval_missing` when run without final approval. A local review-only candidate archive may be built for user audit, but final competition email/package sending still requires explicit user approval.
`plan_submission_candidate.py` can consume the current v48/post-v69 readiness
JSON and produces only a non-destructive dry-run manifest unless the user
explicitly asks for packaging.

Historical local review-only package:

```text
Results/deliverables/submission_candidates/UGV_initial_race_review_candidate_20260709_124115.zip
Results/deliverables/submission_candidates/UGV_initial_race_review_candidate_20260709_124115_manifest.md
```

This package is for user audit only. It does not imply final submission approval and was not sent to the competition address.
Do not create more submission zip packages unless the user explicitly asks for
another packaging dry run. Push/network failures are operational follow-up
items, not a reason to stop controller tuning.
