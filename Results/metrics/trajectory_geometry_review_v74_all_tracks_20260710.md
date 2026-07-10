# Trajectory Event Review

Generated from saved MWORKS `extra_timeseries.csv` and `score_timeseries.csv` exports.
When `--track` is provided, official read-only `roadMap` and `obstaclePoint` geometry is overlaid for diagnosis.
This is trajectory evidence only; it does not prove physical UGV behavior or final competition submission readiness.

| Run | T | cR | cO | P | Events | Geometry | Image |
|---|---:|---:|---:|---:|---:|---|---|
| v74_track1 | 17.4 | 1.0 | 0.0 | 9.6 | 1 | road=182, obs=24 | `Results\figures\trajectory_geometry_review_v74_all_tracks_20260710\v74_track1_trajectory_events.png` |
| v74_track2 | 120.0 | 1.0 | 0.0 | 9.6 | 1 | road=231, obs=20 | `Results\figures\trajectory_geometry_review_v74_all_tracks_20260710\v74_track2_trajectory_events.png` |
| v74_track3 | 120.0 | 1.0 | 1.0 | 9.2 | 2 | road=106, obs=20 | `Results\figures\trajectory_geometry_review_v74_all_tracks_20260710\v74_track3_trajectory_events.png` |
| v74_track4 | 120.0 | 2.0 | 0.0 | 9.2 | 2 | road=212, obs=20 | `Results\figures\trajectory_geometry_review_v74_all_tracks_20260710\v74_track4_trajectory_events.png` |

## Event Details

### v74_track1

| Event | Time/s | Changes | x | y | dRoadCenter | dNearestObs |
|---:|---:|---|---:|---:|---:|---:|
| 1 | 4.45 | cR: 0->1, P: 10->9.6 | 3.007 | 1.851 | 0.5009 | 3.767 |

### v74_track2

| Event | Time/s | Changes | x | y | dRoadCenter | dNearestObs |
|---:|---:|---|---:|---:|---:|---:|
| 1 | 4.70 | cR: 0->1, P: 10->9.6 | 3.644 | 0.4601 | 0.4601 | 1.767 |

### v74_track3

| Event | Time/s | Changes | x | y | dRoadCenter | dNearestObs |
|---:|---:|---|---:|---:|---:|---:|
| 1 | 1.05 | cO: 0->1, P: 10->9.6 | 1.2 | 0.0799 | 0.0799 | 0.1061 |
| 2 | 4.85 | cR: 0->1, P: 9.6->9.2 | 3.364 | 0.4616 | 0.4616 | 1.397 |

### v74_track4

| Event | Time/s | Changes | x | y | dRoadCenter | dNearestObs |
|---:|---:|---|---:|---:|---:|---:|
| 1 | 4.35 | cR: 0->1, P: 10->9.6 | 3.656 | 0.4637 | 0.4637 | 0.7279 |
| 2 | 104.00 | cR: 1->2, P: 9.6->9.2 | 10.5 | 12.16 | 0.4601 | 1.109 |
