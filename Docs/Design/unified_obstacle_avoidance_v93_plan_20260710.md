# Unified Obstacle Avoidance v93 Plan

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
v92_front_emergency_straight_hold
Results/metrics/track3_candidate_review_v92_front_emergency_straight_hold_20260710.md
```

## Evidence Basis

Track3 has a unique early obstacle event:

```text
time=1.05s, cO 0->1, P 10.0->9.6
df=0.01324, dl=0.4876, dr=0.6474
speed_oa=-1, steer_oa=0.6, ctrlAlloc.speed=0.7196
```

v92 changed this front-emergency region to `speed_oa=-3` and `steer_oa=0`, but
the filtered control allocation still left positive forward speed:

```text
time=1.10s, cO 0->1, P 10.0->9.6
df=0.03414, dl=0.5058, dr=0.6293
speed_oa=-3, steer_oa=0, ctrlAlloc.speed=0.4066
```

This suggests the failed part of v92 was not only the emergency speed command;
the path-speed contribution still dominated during the short front-obstacle
window.

## Candidate Mechanism

Modify two editable controller files:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
Models/UGV/Control/ControlAllocate/package.mo
```

1. In the longitudinal avoid state, emit a distinct emergency marker only for
   the very-close-front, side-open geometry:

```modelica
if df <= 0.25 and dl > 0.3 and dr > 0.3 then
  speed := -3;
else
  speed := -1;
end if;
```

2. In `CtrlAlloc`, treat `speed_oa < -2` as a temporary emergency and suppress
   the delayed path-speed contribution:

```modelica
gain2.u = if speed_oa < -2 then 0 else unitDelay3.y;
```

Keep the v80 lateral initial command `steer := 0.6`; v92 already showed that
removing lateral steering did not remove the obstacle event.

## Difference From Rejected Routes

- Not v24: it does not globally change obstacle filter time constants.
- Not v70/v77/v90: it does not broadly clamp speed or amplify reverse speed.
- Not v91: it does not change initial lateral steer sign.
- Not v92: it makes the emergency speed marker affect control allocation
  instead of only changing the upstream avoid command.
- It is gated by `speed_oa < -2`, so normal side-road events with
  `speed_oa=-1` are not targeted.

## Target Gate

Run Track3 first:

```text
UGV.Test.Saidao3Eval
```

Accept for wider regression only if Track3 improves obstacle count or total
score without adding a new road-event regression in the same saved run.

If unchanged or worse, restore v80 semantics, run the restore static gate, write
review evidence, commit, push, email, and continue with a different mechanism.

## Non-Claims

- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No per-track algorithm branch.
- No final 80/80 claim.
- No physical UGV success claim.
- No report/package work.
