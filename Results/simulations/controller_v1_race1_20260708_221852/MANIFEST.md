# UGV Runtime Manifest - controller_v1_race1_long

request_id: M5-one-track-race1-long
timestamp: controller_v1_race1_20260708_221852
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Example.Race1
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: controller_refsysblock_v1
runtime: MWORKS Sysplorer 2026a Python API
status: bounded_runtime_gate
completion: bounded_stop_or_assertion; inspect exit_state/logs
time_s: 120.0
road_collisions: 1.0
obstacle_collisions: 3.0
avoidance_score: 8.4

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

- This run label is controller_v1_race1_long.
- SimulateModel=True proves load/check/simulation API path for the bounded stop time only.
- Do not claim final official race score unless completion and score variables are confirmed from metrics/logs.
