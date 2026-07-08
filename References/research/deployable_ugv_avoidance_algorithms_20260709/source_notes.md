# Deployable UGV Avoidance Algorithm Source Notes

## Current Contest Interface

Normal implementation target:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Observed controller boundary:

```text
inputs:  front_dist, rear_dist, left_dist, right_dist
outputs: speed, steer
```

This means the current controller is a bounded reactive safety layer. It should not pretend to be a full local planner unless the contest interface changes.

## F1TENTH Follow-the-Gap

Saved evidence: `upstream_notes/f1tenth_follow_the_gap_README.md`.

Useful pattern:

- Create a safety bubble around the closest obstacle.
- Select the largest free gap.
- Drive toward a goal point inside the gap.
- Use different parameters for simulation and real-car deployment.

Current adaptation:

- Four scalar distances cannot represent a full gap array.
- Front risk can still choose the larger side clearance as a two-bin gap proxy.
- The safety bubble maps to `front_safe`, `side_safe`, emergency threshold, dwell, and release hysteresis.

## Nav2 Regulated Pure Pursuit

Saved evidence: `upstream_notes/nav2_regulated_pure_pursuit_README.md`.

Useful pattern:

- Slow by curvature / steering demand.
- Slow near potential collision.
- Use a time-limited collision horizon instead of a fixed long lookahead.
- Keep parameters explicit: max speed, min speed, lookahead, collision time, curvature regulation, and obstacle-distance scaling.

Current adaptation:

- No path or local costmap is available inside the obstacle controller.
- Use the idea, not the stack: reduce `speed` when `abs(steer)` is high or `front_dist` is below a warning threshold.

## Dynamic Window Approach

Saved evidence:

```text
upstream_notes/ros1_dwa_local_planner_package.xml
upstream_notes/pythonrobotics_dynamic_window_approach.py
```

Useful pattern:

- Respect min/max speed, yaw/steering limits, acceleration limits, and a short prediction horizon.
- Score commands by goal tracking, speed preference, and obstacle cost.
- Treat collision cost as hard infinite cost in sampled prediction.

Current adaptation:

- Current controller lacks pose, velocity state, obstacle coordinates, and a local map, so full sampling is not implementable.
- The immediate transferable rule is to keep output saturation, avoid sudden sign flips, and penalize speed during high front/side risk.

## TEB Local Planner

Saved evidence:

```text
upstream_notes/teb_local_planner_README.md
upstream_notes/teb_local_planner_LICENSE
```

Useful pattern:

- Optimize local trajectories against time, obstacle separation, and kinodynamic constraints.
- Explicitly reason about car-like robot constraints.

Current adaptation:

- TEB requires a ROS navigation stack, costmap, optimizer, pose, and trajectory representation. It is not a current implementation target.
- Its value here is the acceptance criterion: do not tune commands that a physical car cannot execute safely.

## Pure Pursuit And Stanley Path Tracking

Saved evidence:

```text
upstream_notes/pythonrobotics_pure_pursuit.py
upstream_notes/pythonrobotics_stanley_control.py
```

Useful pattern:

- Pure pursuit uses a speed-scaled lookahead and steering saturation.
- Stanley combines heading error and cross-track error and clips steering.

Current adaptation:

- Current obstacle controller is blended with the official driving/path logic; it should not replace that path authority.
- The usable idea is smooth return-to-cruise and steering saturation after avoidance release.

## Practical Controller Filter

Before accepting a new controller change, require all of the following:

1. It can be expressed using the four distance inputs and speed/steer outputs.
2. It keeps speed and steering bounded for near-zero distances.
3. It slows down when front risk or steering demand increases.
4. It has dwell or hysteresis before leaving avoidance.
5. It can be tuned on a physical UGV without knowing hidden track constants.
6. It is validated by the MWORKS evidence gate when live runtime is available.

This filter is now the main bridge between upstream algorithm research and the competition controller implementation.
