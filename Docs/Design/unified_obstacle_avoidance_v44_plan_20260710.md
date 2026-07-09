# Unified Obstacle Avoidance v44 Plan

Status: rejected_noop_after_scale_check, 2026-07-10 CST

## Hypothesis

After v42/v43 rejected side-only behavior, try a Regulated Pure Pursuit style
path-speed mechanism: when the path planner asks for a large steering angle,
reduce path target speed so the vehicle spends less time in high-speed,
high-curvature road-edge risk.

## Edit Scope

Allowed source edit:

```text
Models/UGV/Control/PathPlanning/PathPlanner.mo
```

No edits to official vehicle, road, scoring, sensor, or track geometry.
No per-track branch.

## Implemented Mechanism

```text
curve_slowdown_steer = 0.35
curve_slowdown_speed = 7.5
if abs(steering_angle) > curve_slowdown_steer
   and target_v > curve_slowdown_speed then
  target_v := curve_slowdown_speed;
end if;
```

## Result

Track4 evidence:

```text
Results/simulations/controller_v44_curvature_speed_regulation_saidao4_120s_20260710_0029/
Results/metrics/collision_window_analysis_v13_v44_track4_20260710_0032.md
Results/metrics/signal_window_summary_v13_v44_track4_20260710_0032.md
```

v44 matched v13 on Track4:

```text
T=113.1, cR=3, cO=0, P=8.8
```

The scale was wrong: exported `pathPlanner.target_v` and
`ctrlAlloc.speed_pp` are normalized around `1.0`, so a cap of `7.5` did not
actually cap runtime speed. v44 is rejected as a no-op, not as evidence that
curvature speed regulation is ineffective.
