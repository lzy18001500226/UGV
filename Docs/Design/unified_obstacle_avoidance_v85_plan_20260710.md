# Unified Obstacle Avoidance v85 Plan

Status: implementation candidate for the high-score sprint from v80. This
document does not claim a score, runtime success, physical UGV proof, report
readiness, or submission readiness.

## Baseline

Current accepted local wrapper baseline:

```text
v80 sharp curve speed cap
total wrapper score: 38.0
Track1: T=17.4, cR=1, cO=0, P=9.6, simulate_failed
Track2: T=120.0, cR=1, cO=0, P=9.6, clean
Track3: T=59.4, cR=1, cO=1, P=9.2, simulate_failed
Track4: T=120.0, cR=1, cO=0, P=9.6, clean
```

Key Track3 diagnostic evidence:

```text
Results/metrics/trajectory_event_review_diagnostic_v80_track3_pose_20260710.md
Results/figures/trajectory_event_review_diagnostic_v80_track3_pose_20260710/diagnostic_v80_track3_pose_trajectory_events.png
```

The Track3 first event is an obstacle hit at `t=1.05 s` with nearest obstacle
distance about `0.1061`, below the official `CountPoint.mindis=0.11`. The
second event is a road hit at `t=4.85 s`. Signal review shows `steer_oa=0.6`
continues through the early risk window while the path planner is already
requesting negative steering, so the controller keeps pushing the vehicle
toward the upper road edge after the first obstacle event.

## Hypothesis

The fixed `2 s` initial lateral avoid hold is too long for narrow entry
obstacle geometry. Shortening only the lateral fixed initial hold should allow
side-distance feedback to take over earlier, reducing the post-obstacle
road-edge collision risk without changing the longitudinal avoid dwell, speed
caps, path planner, official scoring, vehicle, road, or wrappers.

This is deliberately not:

- a per-track patch;
- a broad speed clamp;
- the rejected v83 `df < 0.15` road-edge recovery branch;
- a negative initial bypass;
- an abrupt initial `y` bias;
- a max-steer clip or final-steer saturation scan.

## Source Change

Allowed target:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Change:

```text
avoid_lateral.ini_state -> state transition:
after(2,sec) -> after(1.2,sec)
```

The longitudinal `avoid -> cruise after(2,sec)` transition remains unchanged.

## Acceptance

1. Static deployability checker passes with no high/medium risks.
2. Track3 v85 run improves or at least clearly diagnoses the v80 `cR=1,cO=1`
   failure without creating an earlier non-comparable stop.
3. If Track3 improves, run the same v85 controller on all four wrapper tracks.
4. Accept v85 only if total wrapper score improves above v80 or if it fixes the
   Track3 runtime caveat without reducing total score.
5. If rejected, restore v80 semantics and record the rejection with evidence.
