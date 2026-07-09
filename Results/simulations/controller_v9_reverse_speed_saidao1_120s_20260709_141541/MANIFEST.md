# UGV Runtime Manifest - controller_v9_reverse_speed_saidao1_120s

request_id: M7-v9-track1-reverse-speed
timestamp: controller_v9_reverse_speed_saidao1_120s_20260709_141541
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao1Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: controller_v9_reverse_speed_neg0p85
runtime: MWORKS Sysplorer 2026a Python API
status: blocked
completion: simulate_false_with_result_variables; inspect messages/assertions
time_s: 84.45
road_collisions: 4.0
obstacle_collisions: 3.0
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

- This run label is controller_v9_reverse_speed_saidao1_120s.
- This run did not prove the full load/check/simulation path.
- Runtime stopped at status: simulate_failed.
- Do not treat this manifest as controller, track, score, or completion evidence.
