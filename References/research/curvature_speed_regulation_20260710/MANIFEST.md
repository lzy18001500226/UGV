# Curvature Speed Regulation Research

generated_at: 2026-07-10 CST
scope: unified one-algorithm four-track obstacle-avoidance tuning

## Purpose

Use a deployable, track-agnostic path-speed mechanism after v14-v43 showed
that side-threshold, steering clipping, planner suppression, reverse braking,
and release-dwell scans either did not improve the target failure windows or
regressed another track.

## Local Sources

| Source | Use |
|---|---|
| `References/research/deployable_ugv_avoidance_algorithms_20260709/upstream_notes/nav2_regulated_pure_pursuit_README.md` | Regulated Pure Pursuit concept: lower commanded speed when path curvature or steering demand is high. |
| `References/research/robust_physical_ugv_navigation_20260709/upstream_notes/nav2_regulated_pure_pursuit_README.md` | Cross-check of speed regulation as a physical-navigation robustness pattern. |
| `References/research/deployable_ugv_avoidance_algorithms_20260709/upstream_notes/pythonrobotics_pure_pursuit.py` | Pure Pursuit path-following context; not copied into the controller. |

## Boundary

- This research does not introduce a new local planner, map, LiDAR scan, or
  per-track branch.
- The implemented mechanism only uses existing path-planner steering demand and
  the existing normalized target-speed scale observed in runtime evidence.
- The mechanism is review-ready only after four-track wrapper runtime evidence.
