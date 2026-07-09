# UGV Runtime Manifest - controller_v45_curvature_speed_regulation_scaled_saidao4_120s_20260710_0035

request_id: v45_curvature_speed_regulation_scaled_saidao4_20260710_0035
timestamp: controller_v45_curvature_speed_regulation_scaled_saidao4_120s_20260710_0035
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao4Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: v45_curvature_speed_regulation_scaled
runtime: MWORKS Sysplorer 2026a Python API
status: bounded_runtime_gate
completion: bounded_stop_or_assertion; inspect exit_state/logs
time_s: 120.0
road_collisions: 2.0
obstacle_collisions: 0.0
avoidance_score: 9.2

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

- This run label is controller_v45_curvature_speed_regulation_scaled_saidao4_120s_20260710_0035.
- Simulation API returned true for the bounded stop time only.
- Do not claim final official race score unless completion and score variables are confirmed from metrics/logs.
