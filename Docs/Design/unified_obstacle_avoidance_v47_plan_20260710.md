# Unified Obstacle Avoidance v47 Plan

Status: planned_for_target_track_validation, 2026-07-10 CST

## Goal

Continue from accepted v45 after rejecting v46. Test one unified startup speed
cap that targets the remaining early Track3 obstacle contact without per-track
logic or obstacle-speed gain escalation.

## Evidence Basis

Current accepted best:

```text
v45 total wrapper score: 36.8
Track3 v45: T=120.0, cR=1, cO=1, P=9.2
```

Fresh Track3 failure evidence:

- v45 Track3 has an obstacle collision near `1.05 s`.
- The obstacle controller is already active there: `speed_oa=-1`.
- v46 increased the obstacle-avoidance speed-channel contribution to
  `1.2*factor_oa`, but Track3 regressed to `T=45.2`, `simulate_failed` with
  the same `P=9.2`.

Conclusion: do not continue speed-channel gain escalation. The next safe
mechanism should reduce early approach speed before the controller encounters
the first obstacle, in a way that is deployable on a physical UGV.

## Hypothesis

A short startup target-speed cap reduces the first-second obstacle contact risk
without changing obstacle state-machine logic or adding per-track behavior.
This is a deployable safety behavior: physical vehicles commonly use bounded
startup speed during sensor/actuator transient periods.

## Planned Source Change

Allowed scope:

```text
Models/UGV/Control/PathPlanning/PathPlanner.mo
```

Add parameters:

```modelica
parameter Real startup_slow_time = 2.0;
parameter Real startup_slow_speed = 0.75;
```

After interpolating the path target speed, apply:

```modelica
if time < startup_slow_time and target_v > startup_slow_speed then
  target_v := startup_slow_speed;
end if;
```

Keep the existing v45 curvature/large-steering speed cap after this step.

Do not change:

- official vehicle, road, sensor, scoring, example, or track files;
- obstacle-controller state-machine thresholds;
- `ControlAllocate`;
- per-track logic.

## Validation Gate

1. Run Track3 first.
2. Continue to four-track regression only if Track3 improves over v45 `P=9.2`
   or removes the early obstacle collision without a worse runtime terminal
   state.
3. If Track3 does not improve, reject v47, restore v45 source semantics, send
   a sparse Chinese notice, and continue with a different evidence-backed
   mechanism.

## Non-Goals

- No final submission package.
- No physical UGV success claim.
- No track-specific tuning.
