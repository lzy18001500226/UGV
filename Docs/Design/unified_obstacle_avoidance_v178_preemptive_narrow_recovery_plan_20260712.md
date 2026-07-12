# Unified Obstacle Avoidance v178 Preemptive Narrow Recovery Plan

Status: rejected; exact v148 source restored

## Goal

Preserve v162's loop traversal while moving its narrow direction correction
early enough to act before the first Track3 road event.

## Evidence Basis

The saved v162 trajectory shows:

- the first obstacle event occurs with `df` around `0.83`, so a narrow
  front-distance branch remains inactive there;
- `df` falls below `0.20` at about `t=3.85 s`;
- the v162 `df<0.15` branch starts around `t=4.15 s`;
- the first road event occurs around `t=4.30 s`.

The current branch therefore has only about 0.15 s to affect the road event.
Using `df<0.20` gives roughly 0.30 s more corrective authority while remaining
well separated from the first obstacle encounter. This is an event-boundary
correction from saved runtime evidence, not a threshold scan.

## Unified Candidate

Starting from exact v148 semantics, use v162's direction-aware entry action
with only the narrow activation boundary changed:

```modelica
if df < 0.20 and dl < dr then
  steer := -min(0.6, 2 * abs(dl - dr));
elseif df < 0.20 and dr < dl then
  steer := min(0.6, 2 * abs(dl - dr));
else
  steer := 0.6;
end if;
```

All timings, speeds, side thresholds, path planning, allocation, and official
models remain unchanged. The same four-sensor rule applies to every track.

## Gates

1. Deployability checker and project tests.
2. Track3 1 s native gate.
3. Strict Track3 700 s completion request.
4. Only a verified Track3 finish promotes unchanged source to Tracks 4, 1,
   and 2.
5. Any non-finish or collision regression restores exact v148 semantics. Do
   not scan nearby thresholds after this evidence-based boundary.

No finish, 80/80, physical-car, package, or submission claim precedes saved
runtime evidence.

## Result

Static checks, 14 tests, and the Track3 1 s native gate passed. The strict
request ended without a finish at `T=228.15,cR=2,cO=1,P=8.8`, with official
finish distance squared `385.5204`. Earlier activation preserved a long run but
regressed v162's `T=286.55` near-loop behavior and ended far from the finish.
Reject v178, restore exact v148 semantics, and close nearby narrow-threshold
changes.
