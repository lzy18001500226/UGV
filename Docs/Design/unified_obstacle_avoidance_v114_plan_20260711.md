# Unified Obstacle Avoidance v114 Plan

Status: planned before source edit, 2026-07-11 CST.

## Goal

Continue from the current accepted local wrapper baseline:

```text
v80_sharp_curve_speed_cap
wrapper score: 38.0 / 40
```

The target remains one unified obstacle-avoidance algorithm across all four
tracks. This candidate focuses on the fixed Track3 early obstacle loss at
`t=1.05s`.

## Evidence Basis

v80, v103, and v113 all share the same Track3 early obstacle event:

```text
t=1.05s: cO 0 -> 1, P 10.0 -> 9.6
```

Signal evidence:

```text
Results/metrics/track3_event_signal_summary_v80_v103_v113_ctrlalloc_20260711.md
Results/metrics/track3_path_progress_signal_summary_v80_v103_v113_20260711.md
```

At that event:

```text
df ~= 0.013
speed_oa = -1
steer_oa = 0.6
pathPlanner.target_v = 1
path steering ~= -0.039
ctrlAlloc.speed ~= 0.72
ctrlAlloc.steer ~= 0.16
```

So the controller has already requested obstacle avoidance, but the path-speed
contribution is still dominant while the path is almost straight. Repeating
v103/v112/v113 time-window conflict gates does not affect this first loss.

## Candidate Mechanism

Modify only:

```text
Models/UGV/Control/ControlAllocate/package.mo
```

Replace the direct path-speed connection with a narrow straight-front braking
cap:

```modelica
gain2.u = if speed_oa < 0 and abs(unitDelay1.y) < 0.05 and unitDelay3.y > 0.35
  then 0.35
  else unitDelay3.y;
```

This keeps the accepted v80 steering arbitration unchanged:

```modelica
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0
  then 0.5 * unitDelay1.y
  else unitDelay1.y;
```

## Why This Is Different From Rejected Routes

- Not v24/v56: it does not globally reduce `FirstOrder` filter time constants.
- Not v103/v112/v113: it targets the early straight-front obstacle window,
  not the later conflict path-speed window.
- Not per-track: the rule uses controller signals only, not track id, score
  variables, official geometry, or model names.

## Validation Gate

1. Run the static deployability checker.
2. Run Track3 first.
3. If Track3 improves without a short-run artifact, run Track1 regression.
4. If Track1 is v80-equivalent or better, run Track2 and Track4.
5. Accept only if total four-track wrapper score beats v80 `38.0 / 40`.
6. If rejected, restore v80 semantics, write rejection evidence, send sparse
   Chinese email, commit/push, and continue.

## Non-Claims

- No final `80 / 80` claim.
- No physical UGV success claim.
- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No report/package work.
