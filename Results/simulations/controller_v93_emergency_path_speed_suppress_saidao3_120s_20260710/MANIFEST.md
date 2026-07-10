# UGV Runtime Manifest - controller_v93_emergency_path_speed_suppress_saidao3_120s_20260710

request_id: v93-emergency-path-speed-suppress-20260710
timestamp: controller_v93_emergency_path_speed_suppress_saidao3_120s_20260710
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao3Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: v93_emergency_path_speed_suppress
runtime: MWORKS Sysplorer 2026a Python API
status: blocked
completion: simulate_false_with_result_variables; inspect messages/assertions
time_s: 10.700000000000001
road_collisions: 1.0
obstacle_collisions: 2.0
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

- This run label is controller_v93_emergency_path_speed_suppress_saidao3_120s_20260710.
- This run did not prove the full load/check/simulation path.
- Runtime stopped at status: simulate_failed.
- Do not treat this manifest as controller, track, score, or completion evidence.
