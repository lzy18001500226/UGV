# UGV Runtime Manifest - controller_v6_front_dwell_3s_race1_120s

request_id: M5-race1-v6-front-dwell-3s-120s
timestamp: controller_v6_front_dwell_3s_race1_120s_20260708_230754
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Example.Race1
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: controller_v6_front_dwell_3s
runtime: MWORKS Sysplorer 2026a Python API
status: bounded_runtime_gate
completion: bounded_stop_or_assertion; inspect exit_state/logs
time_s: 120.0
road_collisions: 17.0
obstacle_collisions: 0.0
avoidance_score: 3.1999999999999993

## Artifacts

- probe_steps.json
- metrics.json
- stdout_or_log.txt
- native_result/
- result_variables_summary.json when available
- score_timeseries.csv when export succeeds
- extra_timeseries.csv when requested variables are available

## Blockers

- none

## Notes

- This run label is controller_v6_front_dwell_3s_race1_120s.
- SimulateModel=True proves load/check/simulation API path for the bounded stop time only.
- Do not claim final official race score unless completion and score variables are confirmed from metrics/logs.
