# UGV Runtime Manifest - v182_track2_regression

request_id: UGV-V182-TRACK2-REGRESSION-20260712
timestamp: candidate_v182_v148_exact_closure_track2_700s_20260712
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao2Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: v182_v148_exact_closure
runtime: MWORKS Sysplorer 2026a Python API
status: blocked
completion: early_stop_finish_not_observed
time_s: 28.55
finish_distance_squared: 791.4782768388438
road_collisions: 1.0
obstacle_collisions: 0.0
avoidance_score: 9.6

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

- This run label is v182_track2_regression.
- This run did not prove the full load/check/simulation path.
- Runtime stopped at status: simulate_failed.
- Do not treat this manifest as controller, track, score, or completion evidence.
