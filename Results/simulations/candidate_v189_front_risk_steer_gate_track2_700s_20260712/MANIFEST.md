# UGV Runtime Manifest - candidate_v189_front_risk_steer_gate_track2_700s

request_id: M2-baseline-runtime-gate
timestamp: candidate_v189_front_risk_steer_gate_track2_700s_20260712
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao2Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: v189_front_risk_steer_gate
runtime: MWORKS Sysplorer 2026a Python API
status: blocked
completion: early_stop_finish_not_observed
time_s: 164.95000000000002
finish_distance_squared: 377.9933562181551
road_collisions: 15.0
obstacle_collisions: 2.0
avoidance_score: 3.1999999999999993

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

- This run label is candidate_v189_front_risk_steer_gate_track2_700s.
- This run did not prove the full load/check/simulation path.
- Runtime stopped at status: simulate_failed.
- Do not treat this manifest as controller, track, score, or completion evidence.
