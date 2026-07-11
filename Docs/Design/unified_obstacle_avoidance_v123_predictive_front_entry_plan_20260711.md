# v123 Predictive Front-Entry Plan

Status: planned candidate, not accepted

## Evidence And Reference Basis

The restored v80 Track3 controller enters avoidance before the first obstacle
penalty, but forward speed remains high and the front distance collapses to
about `0.013 m` by `t=1.05 s`. Stronger reverse commands and path-speed
suppression previously created non-comparable early stops.

Regulated Pure Pursuit uses time-to-collision projection to react before the
current pose reaches an obstacle. The official controller does not expose pose,
velocity, a costmap, or a scan array, so it cannot implement full RPP. It can,
however, estimate front closing rate from the existing 100 Hz front-distance
signal.

Local reference:
`References/research/deployable_ugv_avoidance_algorithms_20260709/upstream_notes/nav2_regulated_pure_pursuit_README.md`

## Candidate

Inside the editable obstacle-controller model:

1. delay front distance by one `0.01 s` sample;
2. calculate bounded positive closing rate
   `max(0, (previous_df - df) / 0.01)`;
3. add a predictive front-entry condition when projected distance at a
   `0.60 s` horizon reaches the existing `mindis` threshold.

Conceptually:

```modelica
front_closing_rate = max(0, (previous_df - df) / 0.01);
front_risk = df <= mindis or
  (front_closing_rate > 0.05 and
   df - 0.60 * front_closing_rate <= mindis);
```

Keep the v80 avoid speed, fixed initial steer, lateral state, dwell, path
planning, control allocation, and official models unchanged. This tests
earlier state entry without repeating stronger braking, speed attenuation,
initial-steer, state-continuity, or hysteresis candidates.

## Gates

1. Deployability checker and targeted tests pass.
2. Track3 1 s `-gui` translation/simulation gate passes and exposes the new
   closing-rate signal.
3. Track3 target run must finish or materially improve comparable progress
   without increasing collisions or creating a shorter abnormal stop.
4. Only then run Track2 regression and remaining tracks.
5. On failure, restore exact v80 source and do not scan prediction horizons.

No official completion, 80-point score, physical-car success, report,
package, or submission claim is made by this plan.
