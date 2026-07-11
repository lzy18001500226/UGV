# UGV Runtime Manifest - v135_track1_120s_explicit_state

request_id: candidate-v135-motion-consistent-side-recovery-track1-120s-explicit-state
timestamp: candidate_v135_motion_consistent_side_recovery_track1_120s_explicit_state_20260712
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao1Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: v135 explicit longitudinal side-recovery state with motion-consistent lateral sign
runtime: MWORKS Sysplorer 2026a Python API
status: blocked
completion: early_stop_finish_not_observed
time_s: 86.65
finish_distance_squared: 434.2004534766413
road_collisions: 7.0
obstacle_collisions: 1.0
avoidance_score: 6.8

## Artifacts

- probe_steps.json
- metrics.json
- stdout_or_log.txt
- native_result/
- result_variables_summary.json when available
- score_timeseries.csv when export succeeds
- extra_timeseries.csv when requested variables are available

## Blockers

- simulate_failed

## Notes

- This run label is v135_track1_120s_explicit_state.
- This run did not prove the full load/check/simulation path.
- Runtime stopped at status: simulate_failed.
- Do not treat this manifest as controller, track, score, or completion evidence.
