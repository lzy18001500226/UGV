# Trajectory Event Review

Generated from saved MWORKS `extra_timeseries.csv` and `score_timeseries.csv` exports.
When `--track` is provided, official read-only `roadMap` and `obstaclePoint` geometry is overlaid for diagnosis.
This is trajectory evidence only; it does not prove physical UGV behavior or final competition submission readiness.

| Run | T | cR | cO | P | Events | Geometry | Image |
|---|---:|---:|---:|---:|---:|---|---|
| v162 | 286.55 | 2.0 | 1.0 | 8.8 | 3 | road=0, obs=0 | `Results\figures\v173_progress_continuity_review_20260712\v162_trajectory_events.png` |
| v173 | 49.3 | 1.0 | 1.0 | 9.2 | 2 | road=0, obs=0 | `Results\figures\v173_progress_continuity_review_20260712\v173_trajectory_events.png` |

## Event Details

### v162

| Event | Time/s | Changes | x | y | dRoadCenter | dNearestObs |
|---:|---:|---|---:|---:|---:|---:|
| 1 | 1.00 | cO: 0->1, P: 10->9.6 | 1.217 | 0.09592 |  |  |
| 2 | 4.30 | cR: 0->1, P: 9.6->9.2 | 4.344 | 0.4609 |  |  |
| 3 | 181.35 | cR: 1->2, P: 9.2->8.8 | 2.368 | 0.4656 |  |  |

### v173

| Event | Time/s | Changes | x | y | dRoadCenter | dNearestObs |
|---:|---:|---|---:|---:|---:|---:|
| 1 | 1.00 | cO: 0->1, P: 10->9.6 | 1.217 | 0.09599 |  |  |
| 2 | 4.30 | cR: 0->1, P: 9.6->9.2 | 4.349 | 0.4624 |  |  |
