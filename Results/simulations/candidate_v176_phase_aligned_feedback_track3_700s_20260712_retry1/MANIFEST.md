# UGV Runtime Manifest - candidate_v176_phase_aligned_feedback_track3_700s_20260712_retry1

request_id: v176_track3_700s_retry1
timestamp: candidate_v176_phase_aligned_feedback_track3_700s_20260712_retry1
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao3Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: v176_phase_aligned_feedback
runtime: MWORKS Sysplorer 2026a Python API
status: blocked
completion: early_stop_finish_not_observed
time_s: 108.10000000000001
finish_distance_squared: 295.54091666298325
road_collisions: 2.0
obstacle_collisions: 1.0
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

- simulate_failed

## Notes

- This run label is candidate_v176_phase_aligned_feedback_track3_700s_20260712_retry1.
- This run did not prove the full load/check/simulation path.
- Runtime stopped at status: simulate_failed.
- Do not treat this manifest as controller, track, score, or completion evidence.
