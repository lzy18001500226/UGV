# UGV Runtime Manifest - controller_v48_trajectory_export_saidao3_120s_20260710

request_id: v48_track3_trajectory_export
timestamp: controller_v48_trajectory_export_saidao3_120s_20260710
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao3Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: v48_trajectory_export
runtime: MWORKS Sysplorer 2026a Python API
status: blocked
completion: simulate_false_with_result_variables; inspect messages/assertions
time_s: 6.75
road_collisions: 1.0
obstacle_collisions: 1.0
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

- simulate_failed

## Notes

- This run label is controller_v48_trajectory_export_saidao3_120s_20260710.
- This run did not prove the full load/check/simulation path.
- Runtime stopped at status: simulate_failed.
- Do not treat this manifest as controller, track, score, or completion evidence.
