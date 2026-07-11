# UGV Runtime Manifest - diagnostic_v80_track2_termination_classification

request_id: v80-track2-termination-classification-rerun
timestamp: diagnostic_v80_track2_termination_classification_700s_20260712_rerun
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao2Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: v80_restored_comparison_baseline
runtime: MWORKS Sysplorer 2026a Python API
status: blocked
completion: early_stop_finish_not_observed
time_s: 305.15000000000003
finish_distance_squared: 1004.6703042278752
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

- This run label is diagnostic_v80_track2_termination_classification.
- This run did not prove the full load/check/simulation path.
- Runtime stopped at status: simulate_failed.
- Do not treat this manifest as controller, track, score, or completion evidence.
