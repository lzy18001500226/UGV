# Source Notes: Curvature Speed Regulation

## Imported Idea

Regulated Pure Pursuit style controllers reduce speed when path curvature,
steering demand, or proximity risk increases. The useful part for this project
is not the full ROS/Nav2 stack; it is the bounded speed governor attached to a
Pure Pursuit path follower.

## Adaptation To UGV

The current UGV wrapper already exposes a Pure Pursuit path planner:

```text
Models/UGV/Control/PathPlanning/PathPlanner.mo
```

The v44/v45 adaptation keeps one unified algorithm for all tracks:

```text
if abs(steering_angle) > curve_slowdown_steer
   and target_v > curve_slowdown_speed then
  target_v := curve_slowdown_speed;
end if;
```

This is not a per-track patch. It is a path-authority/speed interaction
mechanism intended to reduce road-edge exposure during large steering demands.

## Scale Lesson

v44 initially used `curve_slowdown_speed = 7.5`, assuming path speeds were in
the `10`-style path table scale. Runtime evidence showed exported
`pathPlanner.target_v` and `ctrlAlloc.speed_pp` are normalized around `1.0`,
so v44 was a no-op on Track4.

v45 corrected the speed cap to `0.75`, which produced a measurable Track4
improvement and passed four-track regression.
