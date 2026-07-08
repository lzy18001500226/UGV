# UGV Runtime Manifest - controller_v2_race1_long

request_id: M5-one-track-race1-tune-v2
timestamp: controller_v2_race1_20260708_222848
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Example.Race1
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: controller_v2_tuned_threshold_gain_bias
runtime: MWORKS Sysplorer 2026a Python API
status: bounded_runtime_gate
completion: bounded_stop_or_assertion; inspect exit_state/logs
time_s: 120.0
road_collisions: 3.0
obstacle_collisions: 4.0
avoidance_score: 7.199999999999999

## Artifacts

- probe_steps.json
- metrics.json
- stdout_or_log.txt
- native_result/
- result_variables_summary.json when available
- score_timeseries.csv when export succeeds

## Blockers

- none

## Notes

- This run label is controller_v2_race1_long.
- SimulateModel=True proves load/check/simulation API path for the bounded stop time only.
- Do not claim final official race score unless completion and score variables are confirmed from metrics/logs.
