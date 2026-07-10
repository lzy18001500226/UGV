# Trajectory Event Review

Generated from saved MWORKS `extra_timeseries.csv` and `score_timeseries.csv` exports.
When `--track` is provided, official read-only `roadMap` and `obstaclePoint` geometry is overlaid for diagnosis.
This is trajectory evidence only; it does not prove physical UGV behavior or final competition submission readiness.

| Run | T | cR | cO | P | Events | Geometry | Image |
|---|---:|---:|---:|---:|---:|---|---|
| v48_track1 | 120.0 | 2.0 | 0.0 | 9.2 | 2 | road=182, obs=24 | `Results\figures\trajectory_geometry_review_v48_all_tracks_20260710\v48_track1_trajectory_events.png` |
| v48_track2 | 60.15 | 1.0 | 0.0 | 9.6 | 1 | road=231, obs=20 | `Results\figures\trajectory_geometry_review_v48_all_tracks_20260710\v48_track2_trajectory_events.png` |
| v48_track3 | 112.45 | 1.0 | 1.0 | 9.2 | 2 | road=106, obs=20 | `Results\figures\trajectory_geometry_review_v48_all_tracks_20260710\v48_track3_trajectory_events.png` |
| v48_track4 | 112.4 | 2.0 | 0.0 | 9.2 | 2 | road=212, obs=20 | `Results\figures\trajectory_geometry_review_v48_all_tracks_20260710\v48_track4_trajectory_events.png` |

## Event Details

### v48_track1

| Event | Time/s | Changes | x | y | dRoadCenter | dNearestObs |
|---:|---:|---|---:|---:|---:|---:|
| 1 | 6.55 | cR: 0->1, P: 10->9.6 | 2.966 | 1.785 | 0.4648 | 3.83 |
| 2 | 30.35 | cR: 1->2, P: 9.6->9.2 | 12.63 | 6.126 | 0.4605 | 0.861 |

### v48_track2

| Event | Time/s | Changes | x | y | dRoadCenter | dNearestObs |
|---:|---:|---|---:|---:|---:|---:|
| 1 | 4.70 | cR: 0->1, P: 10->9.6 | 3.644 | 0.4601 | 0.4601 | 1.767 |

### v48_track3

| Event | Time/s | Changes | x | y | dRoadCenter | dNearestObs |
|---:|---:|---|---:|---:|---:|---:|
| 1 | 1.05 | cO: 0->1, P: 10->9.6 | 1.2 | 0.0799 | 0.0799 | 0.1061 |
| 2 | 4.85 | cR: 0->1, P: 9.6->9.2 | 3.364 | 0.4616 | 0.4616 | 1.397 |

### v48_track4

| Event | Time/s | Changes | x | y | dRoadCenter | dNearestObs |
|---:|---:|---|---:|---:|---:|---:|
| 1 | 4.35 | cR: 0->1, P: 10->9.6 | 3.656 | 0.4637 | 0.4637 | 0.7279 |
| 2 | 90.15 | cR: 1->2, P: 9.6->9.2 | 10.5 | 12.17 | 0.4602 | 1.102 |
