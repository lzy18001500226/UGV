# UGV Runtime Manifest - diagnostic_v5_signals_saidao3_120s

request_id: M7-diagnostic-v5-signals-track3
timestamp: diagnostic_v5_signals_saidao3_120s_20260709_143235
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao3Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: controller_v5_bounded_linear_deployability
runtime: MWORKS Sysplorer 2026a Python API
status: blocked
completion: simulate_false_with_result_variables; inspect messages/assertions
time_s: 50.4
road_collisions: 2.0
obstacle_collisions: 5.0
avoidance_score: 7.199999999999999

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

- This run label is diagnostic_v5_signals_saidao3_120s.
- This run did not prove the full load/check/simulation path.
- Runtime stopped at status: simulate_failed.
- Do not treat this manifest as controller, track, score, or completion evidence.
