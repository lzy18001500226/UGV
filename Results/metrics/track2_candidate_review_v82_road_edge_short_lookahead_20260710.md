# Track2 Candidate Review - v82 Road-Edge Short Lookahead

Status: rejected_target_track_regression, 2026-07-10 CST

## Candidate

v82 continued from accepted v80 and tested a narrow PathPlanner geometry
mechanism:

```text
Models/UGV/Control/PathPlanning/PathPlanner.mo
```

Mechanism:

- add a small-angle short-lookahead branch for
  `0.08 < abs(base_steering_angle) < 0.35`;
- recompute the pursuit point with `road_edge_short_lookahead_factor=0.55`;
- restore the original pursuit point if the recomputed steering exceeds `0.6`.

This was intended to improve early road-edge margin without repeating
ControlAllocate path-authority scans, fixed obstacle-steering boosts, speed
clamps, or side-trigger threshold scans.

## Evidence

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v82_plan_20260710.md
```

Static gate:

```text
Results/evidence/controller_deployability_static_check_v82_road_edge_short_lookahead_20260710.md
```

Pre-candidate diagnostic:

```text
Results/simulations/diagnostic_v80_track2_geometry_120s_20260710/
Results/metrics/trajectory_geometry_review_v80_track2_diagnostic_20260710.md
```

Target run:

```text
Results/simulations/controller_v82_road_edge_short_lookahead_saidao2_120s_20260710/
Results/metrics/trajectory_geometry_review_v82_track2_20260710.md
```

## Result

| Candidate | Track | Runtime | Exit | T/s | cR | cO | P |
|---|---|---|---:|---:|---:|---:|---:|
| v80 | Saidao2Eval | `simulate_returned_true` | 0 | 120.0 | 1 | 0 | 9.6 |
| v82 | Saidao2Eval | `simulate_returned_true` | 0 | 120.0 | 1 | 1 | 9.2 |

v82 kept the clean runtime state but introduced one obstacle collision on the
target track and reduced the score from `9.6` to `9.2`.

## Decision

Reject v82. Do not expand to Track1/3/4 because the target gate regressed.
Restore v80 semantics:

```text
v74 guarded medium-curve short lookahead
v80 sharp-curve speed cap
v48 ControlAllocate opposing-steer guard
v13 obstacle-controller side trigger
```

## Follow-Up Direction

Do not continue small-angle short-lookahead scans. The next candidate should
come from a different mechanism family or from stronger evidence about why the
first Track2 road event and new v82 obstacle event trade off.

## Non-Claims

- No final competition score is claimed.
- No physical UGV success is claimed.
- No report/package readiness change is claimed.
- No official vehicle, road, sensor, scoring, example, or material files were
  edited.
