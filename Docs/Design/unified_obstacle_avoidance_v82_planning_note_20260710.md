# Unified Obstacle Avoidance v82 Planning Note

Status: planned_not_implemented, 2026-07-10 CST

## Goal

Continue from v80 without blind parameter tuning. The next candidate should try
to reduce the repeated early road-edge collision pattern that remains on all
four tracks.

## Current Baseline

v80 is the current score-leading local wrapper candidate:

```text
Track1: P=9.6, cR=1, cO=0, simulate_failed/T=17.4
Track2: P=9.6, cR=1, cO=0, clean T=120
Track3: P=9.2, cR=1, cO=1, simulate_failed/T=59.4
Track4: P=9.6, cR=1, cO=0, clean T=120
Total wrapper score: 38.0
```

## Evidence

```text
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
Results/metrics/signal_window_summary_v80_all_tracks_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v80_all_tracks_20260710.md
References/research/wall_following_residual_obstacle_avoidance_20260710/MANIFEST.md
```

## What Not To Repeat

Do not implement v82 as:

- a fixed initial steer magnitude boost;
- a broad side-danger speed-only change;
- a side-danger steering floor;
- a longer avoid release / stronger reverse dwell;
- a path-authority scalar scan;
- max-steer clipping.

These families have already been tested and rejected or shown to create
non-comparable early-stop artifacts.

## Candidate Shape

Use the wall-following idea only as a bounded residual:

```text
side-distance error -> small steering residual or mode-timing correction
```

The candidate must remain one unified algorithm across all four tracks and must
not edit official vehicle, road, sensor, scoring, example, or official material
files.

## Gate Before Source Edit

Do not edit source until the exact expression and state location are selected
from current `ObsAvoidController_Sysblock2.mo` source. The first runtime gate
should be Track2 or Track4 because they have clean v80 runtime and only one
early road collision. Expand to four tracks only if the target score/collision
count improves without early-stop artifact.
