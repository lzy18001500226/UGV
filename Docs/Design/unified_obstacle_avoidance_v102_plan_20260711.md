# Unified Obstacle Avoidance v102 Plan

Status: planned before source edit, 2026-07-11 CST.

## Goal

Continue the long score sprint from the accepted local wrapper baseline
`v80_sharp_curve_speed_cap` toward the 80-point algorithm-model target with one
unified controller for all four tracks.

Immediate target:

```text
Track3 v80 residual: cR=1, cO=1, P=9.2, T=59.4
```

## Evidence Basis

The latest rejected candidates showed that directly changing the lateral avoid
initial state is fragile:

```text
v96: removes Track3 cR but creates a Track1 short-run artifact.
v97: narrower negative initial steer massively increases Track3 cR.
v100: damping initial steer to 0.2 increases Track3 cR.
```

The useful v99/v101 contrast is in authority interaction:

```text
v99 path centerline damping delays Track3 road event from 4.85s to 5.90s, but
final steer remains positive because obstacle steer still dominates.

v101 reduces opposing path-steer contribution even further and does not improve
Track3.
```

At the v80/v99 Track3 road window, the path planner already points back toward
the safer side:

```text
v80: steer_pp ~= -0.221, steer_oa = 0.6, final steer ~= 0.185
v99: steer_pp ~= -0.336, steer_oa = 0.6, final steer ~= 0.130
```

So v102 tests whether the accepted v48/v80 path attenuation should be relaxed
when the path recovery signal is already strong enough.

## Candidate Mechanism

Modify only:

```text
Models/UGV/Control/ControlAllocate/package.mo
```

Current v80/v48 behavior attenuates any path steering that opposes active
reverse obstacle avoidance:

```modelica
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0 then 0.5 * unitDelay1.y else unitDelay1.y;
```

v102 keeps the attenuation for weak opposing path signals, but releases full
path authority when the path recovery magnitude is already material:

```modelica
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0 and abs(unitDelay1.y) <= 0.2
  then 0.5 * unitDelay1.y
  else unitDelay1.y;
```

This is a unified control-allocation rule. It does not branch on track identity
and does not edit official vehicle, road, sensor, scoring, example, or official
materials.

## Difference From Rejected Routes

- Not v96/v97/v100: does not change lateral avoid initial steering sign or
  magnitude.
- Not v99: does not add path-level centerline damping.
- Not v101: moves in the opposite direction by releasing, not further reducing,
  strong opposing path recovery.
- Not a scalar speed scan and not a report/package task.

## Acceptance Gate

1. Static deployability checker passes with `high=0`, `medium=0`.
2. Run `UGV.Test.Saidao3Eval` first.
3. Accept expansion only if Track3 improves score variables or collision count
   without a short-run artifact.
4. If Track3 improves or is strongly diagnostic without regression, run Track1
   regression next, then Track2/Track4 if still viable.
5. If rejected, restore v80/v48 allocation semantics, write review evidence,
   update status docs, commit/push, send sparse Chinese email, and continue the
   score sprint.

## Non-Claims

- No final 80/80 claim.
- No physical UGV success claim.
- No final submission/package claim.
- No report-polish work.
