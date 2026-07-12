# UGV Runtime Manifest - controller_v193_side_clearance_stop_saidao2_1s_20260712_retry2

request_id: v193_track2_1s_retry2
timestamp: controller_v193_side_clearance_stop_saidao2_1s_20260712_retry2
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao2Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: v193_side_clearance_stop
runtime: MWORKS Sysplorer 2026a Python API
status: bounded_runtime_gate
completion: simulation_horizon_reached_finish_not_observed
time_s: 1.0
finish_distance_squared: 1.8743692509284726
road_collisions: 0.0
obstacle_collisions: 0.0
avoidance_score: 10.0

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

- This run label is controller_v193_side_clearance_stop_saidao2_1s_20260712_retry2.
- Simulation API returned true for the bounded stop time only.
- Official track finish was not observed before the configured simulation horizon.
- Do not claim final official race score unless completion and score variables are confirmed from metrics/logs.
