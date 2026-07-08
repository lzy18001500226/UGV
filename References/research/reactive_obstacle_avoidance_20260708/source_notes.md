# Reactive Obstacle-Avoidance Source Notes

## F1TENTH Follow-the-Gap

Useful ideas:

- Treat obstacle avoidance as a reactive method suitable for race-like vehicles.
- Find the closest obstacle, reserve a safety bubble, find the largest free
  gap, and choose a goal point inside that gap.
- Output Ackermann steering/speed commands, not a full global plan.

Mapping to this project:

- There is no LiDAR array in the current official controller boundary, so
  "gap" becomes the larger of `left_dist` and `right_dist`.
- The safety bubble becomes threshold/dwell/hysteresis around `front_dist`.
- The best goal point becomes "steer away from the smaller side distance while
  reducing speed when front distance is risky".

## Dynamic Window Approach

Useful ideas:

- Select commands inside speed/turn-rate limits and evaluate safety before
  choosing a control.
- Avoid sudden jumps that would be hard to reproduce on the real vehicle.

Mapping to this project:

- Keep `speed` and `steer` bounded.
- Avoid making `steer` proportional to an unbounded reciprocal term without
  saturation.
- A conservative real-car controller may score lower in early simulation but
  should be easier to tune and explain.

## Vector Field Histogram / VFH+

Useful ideas:

- Candidate valleys identify low-obstacle-density directions.
- Hysteresis smooths planned trajectories.
- Body size and look-ahead masking prevent steering into blocked sectors.
- Speed is reduced when approaching obstacles head-on.

Mapping to this project:

- Use a clear enter/exit threshold rather than a single `front_dist <= mindis`
  boundary.
- Keep avoidance active for a dwell period after front risk appears.
- Bias steering away from the closer side but do not oscillate every sample.

## Immediate Implementation Consequences

The next controller iteration should avoid the failed v2 changes:

- Do not simply increase `mindis` without understanding early collisions.
- Do not remove all lateral bias if it helps track centering.
- Do not reduce steering gain blindly.

Instead, first export richer runtime variables around the first collision, then
tune:

- front-risk threshold and recovery dwell;
- side-gap steering direction and gain;
- speed reduction/reverse command during front risk;
- steering saturation if Modelica/Sysblock syntax allows it safely.

## M5 Runtime Findings

Evidence paths:

```text
Results/simulations/diagnostic_v1_race1_35s_20260708_224138/
Results/simulations/controller_v4_zero_lateral_bias_race1_35s_20260708_225905/
Results/simulations/controller_v5_front_dwell_2s_race1_120s_20260708_230305/
Results/simulations/controller_v6_front_dwell_3s_race1_120s_20260708_230754/
```

Findings:

- The first v1 failure at about 27.25 s is a road-boundary collision, not a
  front obstacle collision.
- Removing lateral bias is not acceptable: v4 changes the failure mode to early
  obstacle collisions.
- Dwell/hysteresis is useful but must remain bounded: 2 s improves the 120 s
  score, while 3 s causes many road-boundary collisions.
- Current candidate is `controller_v5_front_dwell_2s`; do not re-apply v2,
  v3, v4, or v6 without a new diagnostic reason.
