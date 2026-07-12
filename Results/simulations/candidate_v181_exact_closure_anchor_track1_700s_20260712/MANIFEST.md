# UGV Runtime Manifest - v181_track1_regression

request_id: UGV-V181-TRACK1-REGRESSION-20260712
timestamp: candidate_v181_exact_closure_anchor_track1_700s_20260712
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao1Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: v181_exact_closure_anchor
runtime: MWORKS Sysplorer 2026a Python API
status: blocked
completion: early_stop_finish_not_observed
time_s: 67.2
finish_distance_squared: 1023.9219022541444
road_collisions: 4.0
obstacle_collisions: 1.0
avoidance_score: 8.0

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

- This run label is v181_track1_regression.
- This run did not prove the full load/check/simulation path.
- Runtime stopped at status: simulate_failed.
- Do not treat this manifest as controller, track, score, or completion evidence.
