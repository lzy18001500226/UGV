# Robust Physical UGV Navigation Source Notes

## Current Constraint

The official editable obstacle controller currently behaves like a safety-overlay interface:

```text
inputs:  front_dist, rear_dist, left_dist, right_dist
outputs: speed, steer
normal edit target: Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

This is enough for robust reactive avoidance, but not enough for a full map-based or scan-array local planner. Therefore each external algorithm must be translated into a small set of deployable rules rather than copied.

## TEB Local Planner

Stored evidence: `upstream_notes/teb_local_planner_README.md`.

Core idea from README: Timed Elastic Band optimizes local trajectory execution time, obstacle separation, and kinodynamic constraints at runtime.

Useful for UGV:

- Keep speed and steering commands dynamically feasible.
- Treat obstacle clearance and execution time as competing objectives.
- Avoid changes that improve score by demanding physically abrupt commands.

Not directly reusable now:

- TEB expects trajectory/costmap/pose interfaces and an optimizer stack.
- The official controller boundary exposes only four scalar distances.

## Nav2 Regulated Pure Pursuit

Stored evidence: `upstream_notes/nav2_regulated_pure_pursuit_README.md`.

Core idea from README: pure pursuit is augmented with velocity regulation based on collision checking, path curvature, obstacle proximity, and lookahead.

Useful for UGV:

- Couple speed reduction to steering magnitude or implied curvature.
- Slow near obstacles instead of steering aggressively at full speed.
- Keep lookahead or dwell behavior speed-aware when the interface allows it.
- Make tuning parameters explicit: max speed, min speed, steering gain, obstacle distance threshold, dwell time.

Not directly reusable now:

- It assumes a path, robot pose, local costmap, and collision projection; the current controller only receives range-like distances.

## F1TENTH Follow-the-Gap

Stored evidence: `upstream_notes/f1tenth_follow_the_gap_README.md`.

Core idea from README: preprocess scan ranges, draw a safety bubble around the closest obstacle, find the largest free gap, choose a goal point, and actuate the car toward it.

Useful for UGV:

- In front-risk, steer toward the side with larger clearance.
- The safety bubble maps to front/side thresholds plus dwell.
- Real-car deployment may need a different parameter set than simulation.

Not directly reusable now:

- The full method assumes a LiDAR array and Ackermann command topic; the official model currently exposes four scalar distances and Modelica outputs.

## DWA / Dynamic Window Pattern

Local README evidence for ROS1 DWA was not saved because the attempted upstream README URL returned 404. Prior PythonRobotics DWA snippets are in `References/research/physical_ugv_obstacle_avoidance_20260708/`.

Useful pattern:

- Respect speed/steering feasibility.
- Prefer short-horizon risk evaluation over instantaneous maximum steering.
- Penalize speed near obstacles and during high-turn commands.

Not directly reusable now:

- DWA normally samples velocity commands using pose, velocity, obstacle coordinates, and a motion model.

## Controller Design Consequences

The next implementation work should stay conservative:

1. Keep v5 as baseline until M6 official-track entry is unblocked.
2. Add diagnostics before more tuning: first-collision windows and distance/speed/steer traces.
3. Prefer speed-turn coupling and front-risk exit hysteresis over more states.
4. Keep every parameter explainable in physical units or clear simulation units.
5. Do not add a new planner stack inside the controller unless official inputs expose the required state.

## Email / Review Consequence

Because the user reported missing emails, each terminal UGV notice must have both:

```text
MoSim email evidence JSON path
UGV local evidence note or manifest entry
```

SMTP `ok=true` is send evidence only. It is not proof that the user read the email.