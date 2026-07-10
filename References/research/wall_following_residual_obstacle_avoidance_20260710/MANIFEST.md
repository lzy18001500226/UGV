# Wall-Following Residual Obstacle Avoidance Research

timestamp: 2026-07-10 15:35 CST
status: source_notes_only

## Purpose

Find a deployable next mechanism after v80 without repeating rejected fixed
steer, broad speed clamp, longer reverse dwell, or path-authority scalar scans.

## Sources

| Source | URL | Notes |
|---|---|---|
| RoboRacer/F1TENTH Lab 3 Wall Following | https://f1tenth-coursekit.readthedocs.io/en/latest/assignments/labs/lab3.html | PID wall following: use distance-to-wall error to compute steering and speed. |
| F1TENTH CourseKit GitHub lab source | https://github.com/f1tenth/f1tenth_coursekit/blob/master/assignments/labs/lab3.rst | Same lab material in source form. |
| F1TENTH wall-following notes | https://panxiaofan.github.io/myf1tenth/2021/01/20/lab3.html | Explains cross-track error from wall distance and PID correction. |
| Disparity Extender / F1TENTH | https://www.nathanotterness.com/2019/04/the-disparity-extender-algorithm-and.html | Useful as reference only; full scan/disparity is unavailable in this UGV interface. |

## Local Evidence Inputs

```text
Results/metrics/signal_window_summary_v80_all_tracks_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v80_all_tracks_20260710.md
Results/metrics/track1_track4_candidate_review_v71_v72_steering_authority_20260710.md
Results/metrics/track3_candidate_review_v66_road_edge_initial_steer_boost_20260710.md
```

## Decision

Do not copy an F1TENTH stack. Use the idea only as a bounded residual:

```text
side-distance error -> small steering residual / mode timing correction
```

The UGV controller has only front/left/right distances and a Sysblock state
machine. Any candidate must stay within that boundary and avoid per-track
branches.
