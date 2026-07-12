# UGV Runtime Manifest - candidate_v180_closure_anchor_track3_700s_20260712

request_id: v180-track3-700s
timestamp: candidate_v180_closure_anchor_track3_700s_20260712
model_root: C:\Users\HP\Desktop\UGV\Models\UGV
example_or_track: UGV.Test.Saidao3Eval
controller_file: C:\Users\HP\Desktop\UGV\Models\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
controller_version: v180_closure_anchor
runtime: MWORKS Sysplorer 2026a Python API
status: official_track_finish
completion: finish_reached_official_origin_assertion
time_s: 89.5
finish_distance_squared: 0.026689244432116753
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

- none

## Notes

- This run label is candidate_v180_closure_anchor_track3_700s_20260712.
- Official track finish was observed: simulation time exceeded 10 s and distanceSensor1.d was below 0.02 at termination.
- The failed simulation return is the expected official origin-finish assertion, not an abnormal early stop.
- Score variables still require separate validation before claiming an official race score.
