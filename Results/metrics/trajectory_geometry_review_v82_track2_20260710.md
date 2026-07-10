# Trajectory Event Review

Generated from saved MWORKS `extra_timeseries.csv` and `score_timeseries.csv` exports.
When `--track` is provided, official read-only `roadMap` and `obstaclePoint` geometry is overlaid for diagnosis.
This is trajectory evidence only; it does not prove physical UGV behavior or final competition submission readiness.

| Run | T | cR | cO | P | Events | Geometry | Image |
|---|---:|---:|---:|---:|---:|---|---|
| v82_track2 | 120.0 | 1.0 | 1.0 | 9.2 | 2 | road=231, obs=20 | `Results\figures\trajectory_geometry_review_v82_track2_20260710\v82_track2_trajectory_events.png` |

## Event Details

### v82_track2

| Event | Time/s | Changes | x | y | dRoadCenter | dNearestObs |
|---:|---:|---|---:|---:|---:|---:|
| 1 | 1.65 | cO: 0->1, P: 10->9.6 | 1.898 | 0.09861 | 0.09861 | 0.1062 |
| 2 | 7.55 | cR: 0->1, P: 9.6->9.2 | 4.728 | 0.459 | 0.459 | 2.168 |
