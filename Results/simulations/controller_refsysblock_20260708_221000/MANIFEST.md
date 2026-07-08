# UGV Runtime Manifest - controller_reference_sysblock_bounded_gate

request_id: M4-reference-sysblock-bounded-runtime-gate
timestamp: controller_refsysblock_20260708_221000
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Example.Race1
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: reference_sysblock_training_structure_first_runnable_controller
runtime: MWORKS Sysplorer 2026a Python API
status: bounded_runtime_gate
completion: bounded_stop_or_assertion; inspect exit_state/logs
time_s: 12.0
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

## Blockers

- none

## Notes

- This run label is controller_reference_sysblock_bounded_gate.
- SimulateModel=True proves load/check/simulation API path for the bounded stop time only.
- Do not claim final official race score unless completion and score variables are confirmed from metrics/logs.
