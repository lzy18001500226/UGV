# UGV Runtime Manifest - baseline

request_id: v60_track3_steering_filter
timestamp: controller_v60_steering_filter_saidao3_120s_20260710
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao3Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: v60_steering_filter
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
- score variables missing or unreadable: T, cR, cO, P

## Notes

- This run label is baseline.
- This run did not prove the full load/check/simulation path.
- Runtime stopped at status: simulate_failed.
- Do not treat this manifest as controller, track, score, or completion evidence.
