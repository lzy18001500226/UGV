# Unified Obstacle Avoidance v115 Plan

Status: planned before source edit, 2026-07-11 CST.

## Goal

Continue from the current accepted local wrapper baseline:

```text
v80_sharp_curve_speed_cap
wrapper score: 38.0 / 40
```

v115 keeps the v114 mechanism family but reduces its abruptness. The target is
the fixed Track3 early obstacle event at `t=1.05s` without creating the v114
`T=1.6` short-run artifact.

## Evidence Basis

v80/v103/v113 show the same early obstacle event:

```text
df ~= 0.013
speed_oa = -1
pathPlanner.target_v = 1
ctrlAlloc.speed ~= 0.72
```

v114 proves a hard path-speed cap to `0.35` is too abrupt:

```text
v114 Track3: T=1.6, cR=0, cO=0, P=10.0
```

That is rejected as a short-run artifact, but it confirms the early event is
sensitive to path-speed dominance.

## Candidate Mechanism

Modify only:

```text
Models/UGV/Control/ControlAllocate/package.mo
```

Use a smoother straight-front braking cap:

```modelica
gain2.u = if speed_oa < 0 and abs(unitDelay1.y) < 0.05 and unitDelay3.y > 0.65
  then 0.65
  else unitDelay3.y;
```

This keeps enough path speed to avoid the v114 immediate stop while reducing
the positive speed at the fixed early obstacle event.

## Validation Gate

1. Run the static deployability checker.
2. Run Track3 first.
3. Reject immediately if Track3 remains `P=9.2` or becomes a short-run
   artifact.
4. If Track3 improves with a comparable runtime window, run Track1 regression.
5. If Track1 is v80-equivalent or better, run Track2 and Track4.
6. Accept only if total four-track wrapper score beats v80 `38.0 / 40`.

## Non-Claims

- No final `80 / 80` claim.
- No physical UGV success claim.
- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No report/package work.
