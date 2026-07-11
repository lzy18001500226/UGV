# UGV Runtime Manifest - v135_track1_1s_retry1

request_id: candidate-v135-motion-consistent-side-recovery-track1-1s-retry1-20260712
timestamp: candidate_v135_motion_consistent_side_recovery_track1_1s_retry1_20260712
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao1Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: v135 motion-consistent side recovery pure functions
runtime: MWORKS Sysplorer 2026a Python API
status: blocked
completion: unknown
time_s: None
finish_distance_squared: None
road_collisions: None
obstacle_collisions: None
avoidance_score: None

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
- score variables missing or unreadable: T, cR, cO, P

## Notes

- This run label is v135_track1_1s_retry1.
- This run did not prove the full load/check/simulation path.
- Runtime stopped at status: simulate_failed.
- Do not treat this manifest as controller, track, score, or completion evidence.
