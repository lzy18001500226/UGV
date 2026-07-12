# v195 Segment-Tangent Cross-Track Heading Plan

Status: candidate under validation

## Evidence basis

The current `PathPlanner` output is consumed as desired yaw by the Ackermann
heading controller. Its existing `purePursuitControl` function returns only
the global bearing to a pursuit point; it does not calculate a front-wheel
steering angle. Earlier v99 added a small centerline correction after that
bearing and only delayed the road event.

The local research snapshot at
`References/research/deployable_ugv_obstacle_avoidance_20260709/` records the
Stanley pattern: combine path-segment heading with signed cross-track error.
v195 applies that pattern using signals already available inside the planner.

## Unified candidate

For the globally closest path segment:

1. Compute the segment tangent heading.
2. Compute signed cross-track displacement from the segment projection.
3. Generate desired heading as tangent heading minus a bounded
   speed-normalized cross-track correction.
4. Keep obstacle avoidance, control allocation, official tracks, vehicle,
   sensors, scoring, and evaluation wrappers unchanged.

This rule contains no track id, time, score, absolute-coordinate branch, or
official-model edit.

## Gates

1. PathPlanner source checker and all project tests pass.
2. Plain `SimulateModel` Track2 1 s gate passes.
3. Plain `SimulateModel` Track2 120 s gate must pass the known early failure
   with bounded collisions; otherwise reject immediately.
4. Only a positive Track2 result may expand to Track3 and a strict completion
   horizon.
5. Failure restores the exact pre-candidate PathPlanner bytes.

## Boundary

This candidate is not evidence of four-track completion, 80/80, physical UGV
success, or submission readiness until all corresponding gates pass.
