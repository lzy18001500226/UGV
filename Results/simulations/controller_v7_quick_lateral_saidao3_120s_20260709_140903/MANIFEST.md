# UGV Runtime Manifest - controller_v7_quick_lateral_saidao3_120s

request_id: M7-v7-track3-quick-lateral
timestamp: controller_v7_quick_lateral_saidao3_120s_20260709_140903
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao3Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: controller_v7_quick_lateral_0p5s
runtime: MWORKS Sysplorer 2026a Python API
status: blocked
completion: simulate_false_with_result_variables; inspect messages/assertions
time_s: 73.5
road_collisions: 7.0
obstacle_collisions: 6.0
avoidance_score: 4.8

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

- This run label is controller_v7_quick_lateral_saidao3_120s.
- This run did not prove the full load/check/simulation path.
- Runtime stopped at status: simulate_failed.
- Do not treat this manifest as controller, track, score, or completion evidence.
