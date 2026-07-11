# Unified Obstacle Avoidance v125 Plan

Status: planned before source edit, 2026-07-11 CST.

## Goal

Restore forward progress under persistent side-triggered avoidance without
removing the longitudinal safety margin that v43 proved necessary.

The first acceptance gate is official track completion, not the historical
avoidance-variable score sum.

## Evidence Basis

The restored v80 controller enters avoid mode when the front or either side is
near and always commands `speed := -1`. The generated wrappers apply
`factor_oa = 0.5`, so persistent side proximity reduces the final speed to
about `0.25` on ordinary curves and `0.05` on sharp curves. Track2 therefore
continues progressing but reaches only about 6.7 percent path progress by
120 s.

v43 removed side-triggered longitudinal braking completely. It reduced road
contacts but regressed Track1 to five obstacle contacts. v29 and v88 increased
reverse strength and did not improve their target gates. v125 tests the missing
middle mechanism: retain reverse braking for real front risk, but use bounded
negative speed for side-only risk.

## Candidate Mechanism

Modify only:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

In the longitudinal avoid state:

```modelica
if df <= mindis then
  speed := -1;
else
  speed := -0.4;
end if;
flag := true;
```

The transition, lateral state machine, 2 s release, allocator, and path planner
remain unchanged. The rule uses only existing instantaneous distance inputs and
does not inspect track identity, score state, result files, or official model
geometry.

## Difference From Rejected Routes

- Not v43: side-triggered avoidance still contributes negative longitudinal
  authority.
- Not v29/v88: v125 reduces persistent side-only reverse authority instead of
  strengthening braking in an extreme side band.
- Not a threshold, dwell, planner-speed, steering-authority, derivative, or
  prediction-horizon scan.

## Gates

1. Run the source deployability checker and targeted Python tests.
2. Run `UGV.Test.Saidao2Eval` for 1 s as the translation gate.
3. Run Track2 for 120 s. Accept expansion only for an official finish or a
   material, comparable path-progress/runtime gain without new collisions or
   abnormal early termination.
4. If Track2 passes, run Track1 for 120 s immediately. Reject if the v43
   obstacle-collision regression returns.
5. Only after both gates pass, expand to Tracks 3 and 4.
6. On rejection, restore exact committed v80 source and save a restore gate.

## Non-Claims

- No final 80/80 score claim.
- No physical UGV success claim.
- No report, package, or official submission claim.
- No edits to official vehicle, road, sensor, scoring, example, or material
  paths.
