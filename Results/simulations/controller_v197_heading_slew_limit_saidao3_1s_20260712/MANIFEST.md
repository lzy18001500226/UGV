# UGV Runtime Manifest - controller_v197_heading_slew_limit_saidao3_1s

request_id: UGV-V197-TRACK3-1S-20260712
timestamp: controller_v197_heading_slew_limit_saidao3_1s_20260712
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao3Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: official copied baseline; controller body not edited by this run
runtime: MWORKS Sysplorer 2026a Python API
status: bounded_runtime_gate
completion: simulation_horizon_reached_finish_not_observed
time_s: 1.0
finish_distance_squared: 1.4889755400660947
road_collisions: 0.0
obstacle_collisions: 1.0
avoidance_score: 9.6

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

- This run label is controller_v197_heading_slew_limit_saidao3_1s.
- Simulation API returned true for the bounded stop time only.
- Official track finish was not observed before the configured simulation horizon.
- Do not claim final official race score unless completion and score variables are confirmed from metrics/logs.
