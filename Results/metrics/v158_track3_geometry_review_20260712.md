# Trajectory Event Review

Generated from saved MWORKS `extra_timeseries.csv` and `score_timeseries.csv` exports.
When `--track` is provided, official read-only `roadMap` and `obstaclePoint` geometry is overlaid for diagnosis.
This is trajectory evidence only; it does not prove physical UGV behavior or final competition submission readiness.

| Run | T | cR | cO | P | Events | Geometry | Image |
|---|---:|---:|---:|---:|---:|---|---|
| v148_track3 | 21.1 | 1.0 | 1.0 | 9.2 | 2 | road=106, obs=20 | `Results\figures\v158_track3_geometry_review_20260712\v148_track3_trajectory_events.png` |
| v158_track3 | 79.8 | 2.0 | 3.0 | 8.0 | 5 | road=106, obs=20 | `Results\figures\v158_track3_geometry_review_20260712\v158_track3_trajectory_events.png` |

## Event Details

### v148_track3

| Event | Time/s | Changes | x | y | dRoadCenter | dNearestObs |
|---:|---:|---|---:|---:|---:|---:|
| 1 | 1.00 | cO: 0->1, P: 10->9.6 | 1.216 | 0.09575 | 0.09575 | 0.1096 |
| 2 | 4.10 | cR: 0->1, P: 9.6->9.2 | 4.147 | 0.4614 | 0.4614 | 0.707 |

### v158_track3

| Event | Time/s | Changes | x | y | dRoadCenter | dNearestObs |
|---:|---:|---|---:|---:|---:|---:|
| 1 | 1.00 | cO: 0->1, P: 10->9.6 | 1.216 | 0.09575 | 0.09575 | 0.1096 |
| 2 | 13.80 | cR: 0->1, P: 9.6->9.2 | 13.71 | 0.4701 | 0.4701 | 1.687 |
| 3 | 65.60 | cO: 1->2, P: 9.2->8.8 | 2.603 | 13.33 | 0.08933 | 0.1065 |
| 4 | 68.25 | cR: 1->2, P: 8.8->8.4 | 2.731 | 12.76 | 0.4872 | 0.5906 |
| 5 | 79.70 | cO: 2->3, P: 8.4->8 | 1.345 | 10.95 | 0.1912 | 0.1036 |
