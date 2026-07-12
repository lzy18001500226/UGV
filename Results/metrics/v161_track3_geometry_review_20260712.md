# Trajectory Event Review

Generated from saved MWORKS `extra_timeseries.csv` and `score_timeseries.csv` exports.
When `--track` is provided, official read-only `roadMap` and `obstaclePoint` geometry is overlaid for diagnosis.
This is trajectory evidence only; it does not prove physical UGV behavior or final competition submission readiness.

| Run | T | cR | cO | P | Events | Geometry | Image |
|---|---:|---:|---:|---:|---:|---|---|
| v148_track3 | 21.1 | 1.0 | 1.0 | 9.2 | 2 | road=106, obs=20 | `Results\figures\v161_track3_geometry_review_20260712\v148_track3_trajectory_events.png` |
| v161_track3 | 72.7 | 2.0 | 3.0 | 8.0 | 5 | road=106, obs=20 | `Results\figures\v161_track3_geometry_review_20260712\v161_track3_trajectory_events.png` |

## Event Details

### v148_track3

| Event | Time/s | Changes | x | y | dRoadCenter | dNearestObs |
|---:|---:|---|---:|---:|---:|---:|
| 1 | 1.00 | cO: 0->1, P: 10->9.6 | 1.216 | 0.09575 | 0.09575 | 0.1096 |
| 2 | 4.10 | cR: 0->1, P: 9.6->9.2 | 4.147 | 0.4614 | 0.4614 | 0.707 |

### v161_track3

| Event | Time/s | Changes | x | y | dRoadCenter | dNearestObs |
|---:|---:|---|---:|---:|---:|---:|
| 1 | 1.00 | cO: 0->1, P: 10->9.6 | 1.218 | 0.08931 | 0.08931 | 0.1032 |
| 2 | 4.85 | cO: 1->2, P: 9.6->9.2 | 4.646 | 0.09177 | 0.09177 | 0.09861 |
| 3 | 14.90 | cR: 0->1, P: 9.2->8.8 | 14.6 | 0.4905 | 0.4707 | 0.8804 |
| 4 | 66.00 | cO: 2->3, P: 8.8->8.4 | 2.604 | 13.32 | 0.09552 | 0.1047 |
| 5 | 68.80 | cR: 1->2, P: 8.4->8 | 2.716 | 12.73 | 0.4878 | 0.6101 |
