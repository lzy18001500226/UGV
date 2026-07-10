# Unified Obstacle Avoidance v79 Plan

Status: rejected_target_track_no_score_gain, 2026-07-10 CST

## Goal

Continue from accepted v74 and test one physically deployable PathPlanner
mechanism: enforce the already-declared `max_steer` limit on the final
pure-pursuit steering output.

This is not a per-track branch and does not edit official vehicle, road,
sensor, scoring, example, or official material files.

## Evidence Basis

Current accepted best:

```text
v74 total wrapper score: 37.6
```

Remaining v74 event evidence shows that Track4's late road collision occurs
with an extreme path-planner command:

```text
Track4 t=104 s:
pathPlanner.steering_angle = 1.638
pathPlanner.target_v = 0.75
ctrlAlloc.steer = 1.937
cR: 1 -> 2
```

`PathPlanner.mo` already declares:

```modelica
parameter Real max_steer = 0.523599 "最大转向角(30度)";
```

but the accepted v74 algorithm does not clamp the final `steering_angle` to
that physical value.

## Planned Source Change

Allowed source:

```text
Models/UGV/Control/PathPlanning/PathPlanner.mo
```

Add a final output clamp after the v74 guarded short-lookahead logic and
curvature speed cap:

```modelica
if steering_angle > max_steer then
  steering_angle := max_steer;
elseif steering_angle < -max_steer then
  steering_angle := -max_steer;
end if;
```

## Validation Gate

1. Run the source deployability checker as a source-only sanity gate.
2. Run Track4 first because the target event has the clearest extreme steering
   attribution.
3. Continue to Track1/3 only if Track4 improves or is non-regressive without a
   new early-stop artifact.
4. Accept only after four-track regression improves total wrapper score over
   v74 and keeps early-stop caveats visible.

## Non-Goals

- No final competition score claim.
- No physical UGV success claim.
- No report/package work.
- No official material or scoring edits.

## Result

Target Track4 was tested first:

```text
Results/simulations/controller_v79_max_steer_clamp_saidao4_120s_20260710/
Results/metrics/collision_window_analysis_v74_v79_track4_20260710.md
```

v79 kept the same final Track4 score as v74:

```text
v74: T=120, cR=2, cO=0, P=9.2
v79: T=120, cR=2, cO=0, P=9.2
```

It also moved the second road-collision event earlier in the score time series
from `104.0 s` to `59.45 s`. Therefore v79 is rejected and must not be expanded
to Track1/2/3 regression.
