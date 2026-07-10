# Unified Obstacle Avoidance v95 Plan

Status: planned, 2026-07-10 CST.

## Baseline

Accepted local wrapper baseline:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper score: 38.0 / 40
```

Latest rejected candidate:

```text
v94_oa_steer_conflict_attenuation
Results/metrics/track3_candidate_review_v94_oa_steer_conflict_attenuation_20260710.md
```

## Evidence Basis

The v80 Track3 0-1.0 s diagnostic shows the controller requests braking early,
but the allocated speed remains high because path speed and the speed filter
decay slowly:

```text
t=0.10, df=1.0207, speed_oa=-1, ctrlAlloc.speed=0.8806
t=0.20, df=0.8469, speed_oa=-1, ctrlAlloc.speed=0.7308
t=0.50, df=0.4486, speed_oa=-1, ctrlAlloc.speed=0.5584
t=1.00, df=0.0493, speed_oa=-1, ctrlAlloc.speed=0.5090
```

v93 only emitted a stronger emergency marker when the front obstacle was very
close; by then the collision window was already reached. v94 did not trigger
at the first event because path steer was too small.

## Candidate Mechanism

Modify only:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

In the longitudinal avoid state, emit a stronger but bounded early-brake marker
when the front distance is already below `1.1` and both sides still have basic
clearance:

```modelica
if df < 1.1 and dl > 0.5 and dr > 0.5 then
  speed := -2;
else
  speed := -1;
end if;
```

This targets the early front-risk window before `df` collapses below `0.25`.
It does not change path planning, official tracks, scoring, final steering, or
control allocation.

## Difference From Rejected Routes

- Not v70/v77: no global path-speed clamp during active avoidance.
- Not v92/v93: the marker starts earlier and uses `-2`, not very-close-only
  `-3` plus allocation suppression.
- Not v94: no steer-conflict attenuation.
- Not a per-track branch: the rule uses only four-distance geometry available
  to the obstacle controller.

## Target Gate

Run Track3 first:

```text
UGV.Test.Saidao3Eval
```

Accept for wider regression only if Track3 improves `cO`, `cR`, `P`, or runtime
comparability without becoming a shorter early-stop artifact. If unchanged or
worse, restore v80 semantics, run the restore static gate, write review
evidence, commit, push/email, and continue with another mechanism.

## Non-Claims

- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No per-track algorithm branch.
- No final 80/80 claim.
- No physical UGV success claim.
- No report/package work.
