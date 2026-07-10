# Unified Obstacle Avoidance v94 Plan

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
v93_emergency_path_speed_suppress
Results/metrics/track3_candidate_review_v93_emergency_path_speed_suppress_20260710.md
```

## Evidence Basis

The fresh v80 Track3 pose/path diagnostic shows two different events:

```text
1.05s obstacle event:
body.r_0=(1.2, 0.0799)
pathPlanner.steering_angle=-0.03857
df=0.01324, dl=0.4876, dr=0.6474
ctrlAlloc.speed=0.7196, ctrlAlloc.steer=0.1623

4.85s road event:
body.r_0=(3.364, 0.4593)
pathPlanner.steering_angle=-0.2204
df=2.05, dl=0.1083, dr=0.2731
ctrlAlloc.speed=0.5105, ctrlAlloc.steer=0.1855
```

The road event is a side-squeeze case: the path planner is steering back
negative, but final allocated steering stays positive. v92/v93 showed that
front emergency speed or reverse-dominance edits do not solve this and can add
new obstacle collisions.

## Candidate Mechanism

Modify only:

```text
Models/UGV/Control/ControlAllocate/package.mo
```

When the obstacle-avoidance steering direction conflicts with the delayed path
steering during active obstacle braking, attenuate the obstacle steering before
the existing first-order filter:

```modelica
firstOrder.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0 and abs(unitDelay1.y) > 0.15
  then 0.35 * gain.y
  else gain.y;
```

Keep the existing v48/v80 path-side opposing guard:

```modelica
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0
  then 0.5 * unitDelay1.y
  else unitDelay1.y;
```

The goal is not to remove avoidance steering globally. The gate is limited to
active braking plus opposite-sign path/avoid commands, and it only applies when
the path-side correction is non-trivial.

## Difference From Rejected Routes

- Not v70/v77/v90/v92/v93: it does not change speed or reverse behavior.
- Not v79: it does not clip final steering everywhere.
- Not v87/v88/v89: it does not boost or hold side-squeeze avoidance output.
- Not v91: it does not replace initial lateral steering with direct gap
  steering.
- Not a per-track branch: the rule uses only control-signal conflict and active
  braking state.

## Target Gate

Run Track3 first because the current evidence-backed failure window is there:

```text
UGV.Test.Saidao3Eval
```

Accept for wider four-track regression only if Track3 improves `P`, `cR`, `cO`,
or runtime comparability without adding earlier obstacle collisions. If Track3
is unchanged or worse, restore v80 semantics, run the restore static gate,
write review evidence, commit, push, email, and continue with a different
mechanism.

## Non-Claims

- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No per-track algorithm branch.
- No final 80/80 claim.
- No physical UGV success claim.
- No report/package work.
