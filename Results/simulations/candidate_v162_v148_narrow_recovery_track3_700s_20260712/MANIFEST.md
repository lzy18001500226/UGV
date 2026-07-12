# UGV Runtime Manifest - candidate_v162_v148_narrow_recovery_track3_700s_20260712

request_id: v162-track3-700s
timestamp: candidate_v162_v148_narrow_recovery_track3_700s_20260712
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao3Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: v162_v148_narrow_recovery
runtime: MWORKS Sysplorer 2026a Python API
status: blocked
completion: early_stop_finish_not_observed
time_s: 286.55
finish_distance_squared: 295.90730013110414
road_collisions: 2.0
obstacle_collisions: 1.0
avoidance_score: 8.8

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

- This run label is candidate_v162_v148_narrow_recovery_track3_700s_20260712.
- This run did not prove the full load/check/simulation path.
- Runtime stopped at status: simulate_failed.
- Do not treat this manifest as controller, track, score, or completion evidence.
