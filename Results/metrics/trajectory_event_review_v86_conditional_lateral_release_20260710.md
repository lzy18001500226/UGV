# Trajectory Event Review

Generated from saved MWORKS `extra_timeseries.csv` and `score_timeseries.csv` exports.
When `--track` is provided, official read-only `roadMap` and `obstaclePoint` geometry is overlaid for diagnosis.
This is trajectory evidence only; it does not prove physical UGV behavior or final competition submission readiness.

| Run | T | cR | cO | P | Events | Geometry | Image |
|---|---:|---:|---:|---:|---:|---|---|
| controller_v86_conditional_lateral_release_saidao3 | 120.0 | 4.0 | 1.0 | 8.0 | 5 | road=106, obs=20 | `Results\figures\trajectory_event_review_v86_conditional_lateral_release_20260710\controller_v86_conditional_lateral_release_saidao3_trajectory_events.png` |

## Event Details

### controller_v86_conditional_lateral_release_saidao3

| Event | Time/s | Changes | x | y | dRoadCenter | dNearestObs |
|---:|---:|---|---:|---:|---:|---:|
| 1 | 1.05 | cO: 0->1, P: 10->9.6 | 1.2 | 0.0799 | 0.0799 | 0.1061 |
| 2 | 5.65 | cR: 0->1, P: 9.6->9.2 | 3.786 | 0.4642 | 0.4642 | 1.01 |
| 3 | 7.70 | cR: 1->2, P: 9.2->8.8 | 4.816 | 0.4591 | 0.4591 | 0.4783 |
| 4 | 8.95 | cR: 2->3, P: 8.8->8.4 | 5.45 | 0.4653 | 0.4653 | 0.898 |
| 5 | 12.70 | cR: 3->4, P: 8.4->8 | 7.522 | 0.4627 | 0.4627 | 1.417 |
