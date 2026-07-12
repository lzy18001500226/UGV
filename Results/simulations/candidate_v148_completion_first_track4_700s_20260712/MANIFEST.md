# UGV Runtime Manifest - v148_track4_700s

request_id: UGV-V148-TRACK4-700S-20260712
timestamp: candidate_v148_completion_first_track4_700s_20260712
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao4Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: v148
runtime: MWORKS Sysplorer 2026a Python API
status: official_track_finish
completion: finish_reached_official_origin_assertion
time_s: 89.75
finish_distance_squared: 0.022927755299465936
road_collisions: 3.0
obstacle_collisions: 0.0
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

- This run label is v148_track4_700s.
- Official track finish was observed: simulation time exceeded 10 s and distanceSensor1.d was below 0.02 at termination.
- The failed simulation return is the expected official origin-finish assertion, not an abnormal early stop.
- Score variables still require separate validation before claiming an official race score.
