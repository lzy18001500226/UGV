# v135 Motion-Consistent Side-Recovery Plan

Status: rejected after explicit-state implementation passed compile and short
gate but regressed the Track1 120-second run; v80 semantics restored.

## Evidence Basis

The restored v80 controller remains in reverse avoidance when the front is
clear but a side distance remains small:

- Track1 road contacts at 8.05 s and 11.85 s have `df=2.05..2.59 m`,
  `dl~=0.10 m`, `speed_oa=-1`, and `steer_oa=+0.6`.
- Track2 spends most of 30.15..120 s with `df>1.31 m`, one side near
  `0.15 m`, `speed_oa=-1`, and `steer_oa=+0.6`.

v132 proved that switching a side-hold phase to forward speed while retaining
the reverse steering map adds a collision.  v133 proved that swapping the
lateral map while still reversing causes an early stop.  Neither tested the
kinematically consistent pair: forward recovery with the corresponding
opposite steering sign.

## Candidate

Inside the existing `avoid` state:

```modelica
speed := if df > safeF and (dl <= 0.45 or dr <= 0.45) then 1 else -1;
```

The side-recovery condition is unified and uses only existing physical sensor
thresholds.  Front danger still commands the unchanged full reverse action.

Inside the three existing `avoid_lateral` output states, preserve the v80
steering map while reversing and invert it only when `speed > 0`.  This keeps
the intended lateral escape direction consistent when longitudinal motion
changes direction.  It does not change steering magnitude, thresholds, dwell,
path planning, or control allocation.

MWORKS error 549 showed that inline `if` expressions are not supported inside
state-machine actions. A second implementation with pure local functions
passed `CheckModel` but failed embedded compilation with internal error 175.
The final implementation therefore used an explicit longitudinal
`side_recovery` state and only supported arithmetic in lateral state actions.
It passed native compilation and the one-second gate.

## Decision

The explicit-state candidate improved the Track1 25-second comparison from
v80 `cR=2,cO=0,P=9.2` to `cR=1,cO=0,P=9.6`. It did not remain safe over the
long run: the 120-second request terminated at `T=86.65` with
`cR=7,cO=1,P=6.8` and did not satisfy the official finish assertion. This is
a short-horizon improvement followed by collision accumulation, not a
completion candidate. v135 is rejected and must not be expanded to Track2-4.

## Gates

1. Deployability checker and all unit tests pass.
2. Native Track1 one-second load/check/simulation gate passes.
3. Native Track1 25-second comparison reaches the full horizon, has fewer than
   two road collisions, no obstacle collision, and no lower score than v80.
4. Only after gate 3 passes, run Track1 for 120 seconds.  Only an official
   origin-return finish or material comparable progress permits Track2.
5. Any early stop, collision/score regression, or non-comparable runtime
   rejects v135 and restores v80 immediately.

No fixed-horizon run is an official finish. No result from this plan proves an
80-point score or physical-vehicle performance. Future candidates must address
long-horizon recovery stability rather than scan the v135 side threshold or
hide unsupported state-action syntax behind functions.
