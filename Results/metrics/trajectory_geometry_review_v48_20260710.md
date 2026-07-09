# Trajectory Event Review

Generated from saved MWORKS `extra_timeseries.csv` and `score_timeseries.csv` exports.
When `--track` is provided, official read-only `roadMap` and `obstaclePoint` geometry is overlaid for diagnosis.
This is trajectory evidence only; it does not prove physical UGV behavior or final competition submission readiness.

| Run | T | cR | cO | P | Events | Geometry | Image |
|---|---:|---:|---:|---:|---:|---|---|
| v48_track1 | 120.0 | 2.0 | 0.0 | 9.2 | 2 | road=182, obs=24 | `Results\figures\trajectory_geometry_review_v48_20260710\v48_track1_trajectory_events.png` |
| v48_track3 | 6.75 | 1.0 | 1.0 | 9.2 | 2 | road=106, obs=20 | `Results\figures\trajectory_geometry_review_v48_20260710\v48_track3_trajectory_events.png` |

## Event Details

### v48_track1

| Event | Time/s | Changes | x | y | dRoadCenter | dNearestObs |
|---:|---:|---|---:|---:|---:|---:|
| 1 | 6.65 | cR: 0->1, P: 10->9.6 | 3.261 | 1.953 | 0.4627 | 3.493 |
| 2 | 29.90 | cR: 1->2, P: 9.6->9.2 | 12.63 | 6.126 | 0.4612 | 0.8638 |

### v48_track3

| Event | Time/s | Changes | x | y | dRoadCenter | dNearestObs |
|---:|---:|---|---:|---:|---:|---:|
| 1 | 1.05 | cO: 0->1, P: 10->9.6 | 1.2 | 0.0799 | 0.0799 | 0.1061 |
| 2 | 4.85 | cR: 0->1, P: 9.6->9.2 | 3.364 | 0.4593 | 0.4593 | 1.396 |
