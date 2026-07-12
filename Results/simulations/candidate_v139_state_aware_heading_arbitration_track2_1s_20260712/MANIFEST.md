# UGV Runtime Manifest - candidate_v139_state_aware_heading_arbitration_track2_1s_20260712

request_id: v139-track2-1s
timestamp: candidate_v139_state_aware_heading_arbitration_track2_1s_20260712
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao2Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: v139_state_aware_heading_arbitration
runtime: MWORKS Sysplorer 2026a Python API
status: bounded_runtime_gate
completion: simulation_horizon_reached_finish_not_observed
time_s: 1.0
finish_distance_squared: 1.7898033023854996
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

- This run label is candidate_v139_state_aware_heading_arbitration_track2_1s_20260712.
- Simulation API returned true for the bounded stop time only.
- Official track finish was not observed before the configured simulation horizon.
- Do not claim final official race score unless completion and score variables are confirmed from metrics/logs.
