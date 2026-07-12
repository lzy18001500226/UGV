# Unified Obstacle Avoidance v172 Consistent Emergency Steer Plan

Status: rejected as runtime no-op; exact v148 source restored.

## Goal

Retest the only mechanism that traversed the complete Track3 loop while making
its extreme-front steering authority consistent with the controller's normal
bypass state.

## Evidence Basis

v162 used direction-aware steering only for `df < 0.15`, with a `0.6` cap. It
reached `T=286.55,cR=2,cO=1,P=8.8` and traversed the main loop, while v148
stopped at `T=21.1`. The normal left/right bypass states already use a bounded
`0.8` cap. Therefore v172 tests one structurally consistent value rather than
opening a threshold or gain scan.

PathPlanner endpoint-state and helper-branch candidates v164/v165/v168 are not
reopened: they changed the numerical trajectory before the intended closure
logic could help. v172 changes only the existing obstacle-controller entry
action.

## Candidate

```modelica
if df < 0.15 and dl < dr then
  steer := -min(0.8, 2 * abs(dl - dr));
elseif df < 0.15 and dr < dl then
  steer := min(0.8, 2 * abs(dl - dr));
else
  steer := 0.6;
end if;
```

The candidate uses the same four sensor inputs and the same bounded steering
law on every track. It does not inspect track identity, position, score,
official geometry, or race time.

## Gates

1. Deployability checker, project tests, and diff review.
2. Track3 1 s native translation/simulation gate.
3. Strict Track3 700 s official completion request.
4. Only a verified Track3 finish promotes to Tracks 4, 1, and 2.
5. A non-finish or collision regression restores exact v148 semantics.

No finish, 80/80, physical, package, or submission claim precedes saved
runtime evidence.

## Result

Static checks, tests, and the 1 s native gate passed. The strict Track3 run was
bit-for-metric identical to v162 at `T=286.55,cR=2,cO=1,P=8.8`, official
finish distance squared `295.9073`. The emergency direction correction did not
reach the old `0.6` cap, so raising it to `0.8` had no runtime effect. Reject
v172, restore exact v148, and do not scan this cap further.
