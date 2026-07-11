# UGV Runtime Manifest - baseline

request_id: v127-saidao2-completion-gate-recovered
timestamp: controller_v127_transient_steer_saidao2_120s_recovered_20260711
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao2Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: official copied baseline; controller body not edited by this run
runtime: MWORKS Sysplorer 2026a Python API
status: bounded_runtime_gate
completion: simulation_horizon_reached_finish_not_observed
time_s: 120.0
road_collisions: 0.0
obstacle_collisions: 3.0
avoidance_score: 8.8

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

- This run label is baseline.
- Simulation API returned true for the bounded stop time only.
- Official track finish was not observed before the configured simulation horizon.
- Do not claim final official race score unless completion and score variables are confirmed from metrics/logs.
