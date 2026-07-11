# UGV Runtime Manifest - v109_asymmetric_left_squeeze_track1

request_id: v109-asymmetric-left-squeeze-track1
timestamp: controller_v109_asymmetric_left_squeeze_saidao1_120s_20260711
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao1Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: v109_asymmetric_left_squeeze
runtime: MWORKS Sysplorer 2026a Python API
status: blocked
completion: simulate_false_with_result_variables; inspect messages/assertions
time_s: 17.400000000000002
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

- This run label is v109_asymmetric_left_squeeze_track1.
- This run did not prove the full load/check/simulation path.
- Runtime stopped at status: simulate_failed.
- Do not treat this manifest as controller, track, score, or completion evidence.
