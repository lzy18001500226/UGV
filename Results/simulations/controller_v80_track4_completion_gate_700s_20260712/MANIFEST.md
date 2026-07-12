# UGV Runtime Manifest - controller_v80_track4_completion_gate_700s

request_id: v80-track4-completion-700s
timestamp: controller_v80_track4_completion_gate_700s_20260712
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao4Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: v80_restored
runtime: MWORKS Sysplorer 2026a Python API
status: blocked
completion: early_stop_finish_not_observed
time_s: 52.15
finish_distance_squared: 329.6641216891936
road_collisions: 1.0
obstacle_collisions: 0.0
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

- simulate_failed

## Notes

- This run label is controller_v80_track4_completion_gate_700s.
- This run did not prove the full load/check/simulation path.
- Runtime stopped at status: simulate_failed.
- Do not treat this manifest as controller, track, score, or completion evidence.
