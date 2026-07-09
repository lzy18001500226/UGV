# UGV Runtime Manifest - controller_v22_lateral_init_dwell15_saidao1

request_id: M7-v22-track1-lateral-init-dwell15
timestamp: controller_v22_lateral_init_dwell15_saidao1_120s_20260709_1808
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao1Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: controller_v22_lateral_init_dwell15
runtime: MWORKS Sysplorer 2026a Python API
status: bounded_runtime_gate
completion: bounded_stop_or_assertion; inspect exit_state/logs
time_s: 120.0
road_collisions: 15.0
obstacle_collisions: 1.0
avoidance_score: 3.5999999999999996

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

- This run label is controller_v22_lateral_init_dwell15_saidao1.
- Simulation API returned true for the bounded stop time only.
- Do not claim final official race score unless completion and score variables are confirmed from metrics/logs.
