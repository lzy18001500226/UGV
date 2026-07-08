# UGV Runtime Manifest - diagnostic_saidao2_ex_relaxed_1s

request_id: M6-saidao2-simulate-ex-relaxed-diagnostic
timestamp: diagnostic_saidao2_ex_relaxed_1s_20260708_231622
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.saidao.saidao2
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: controller_v5_simulate_ex_relaxed_diagnostic
runtime: MWORKS Sysplorer 2026a Python API
status: blocked
completion: unknown
time_s: None
road_collisions: None
obstacle_collisions: None
avoidance_score: None

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

- This run label is diagnostic_saidao2_ex_relaxed_1s.
- SimulateModel=True proves load/check/simulation API path for the bounded stop time only.
- Do not claim final official race score unless completion and score variables are confirmed from metrics/logs.
