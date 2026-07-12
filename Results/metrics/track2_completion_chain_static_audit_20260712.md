# Track2 Completion-Chain Static Audit

## Decision

The Track2 completion chain is structurally reachable. Do not modify the
official track, evaluation wrapper, or finish assertion. Continue controller
work from restored v80 semantics and treat official completion as the first
gate.

## Path And Wrapper Parity

The `roadMap` arrays extracted from the official model and evaluation wrapper
are identical after numeric normalization:

| Source | Points | First point | Last point | Closure distance | Normalized SHA-256 |
|---|---:|---|---|---:|---|
| `Models/UGV/saidao/saidao2.mo` | 231 | `(0,0,1)` | `(0,0,1)` | `0` | `89e39f611929bfa2ad916b064bab94abf1ffbdd379e571d4f40e720ac21fc965` |
| `Models/UGV/Test/Saidao2Eval.mo` | 231 | `(0,0,1)` | `(0,0,1)` | `0` | `89e39f611929bfa2ad916b064bab94abf1ffbdd379e571d4f40e720ac21fc965` |

Both instantiate `PathPlanner(path=road.roadMap, ...)` and
`distanceSensor1(..., is_closed=true)`. The wrapper therefore preserves the
official Track2 path and finish-distance source.

## Finish Semantics

`distanceSensor1` computes squared distance to the origin:

```modelica
d := vec_p[1]^2 + vec_p[2]^2;
assert(d >= 0.02 or time <= 10, "已跑完赛道全程，仿真结束");
```

After 10 s, returning inside the squared-distance threshold terminates the
simulation. Completion does not depend on `closest_index`, wrapper score, or a
fixed simulation horizon. The accepted evidence gate remains:

```text
SimulateModel=false
T>10
distanceSensor1.d<0.02
```

## Path-Planner Review

`findClosestSegment` searches all `230` path segments each evaluation and has
no previous-index continuity constraint. This is a theoretical branch-switch
risk on a figure-eight crossing. `calculatePursuitPoint` also lacks an explicit
fallback assignment if lookahead extends beyond the final path point.

Neither issue is currently proven to cause the observed Track2 failures:

- v80 120 s: index range `1..26`, no backward or greater-than-two index jump.
- v80 305.15 s diagnostic: index range `1..30`, no backward or
  greater-than-two index jump.
- v137 120 s: index range `1..112`, no backward or greater-than-two index jump.

Do not change PathPlanner on this evidence alone. Reopen that boundary only if
a run reaches the crossing/final segment and records a discontinuity or
unassigned pursuit-point symptom.

## Next Engineering Gate

v137 proves that neutral side-only longitudinal authority removes v80's
persistent reverse stall, reaching index `112` rather than `26` at 120 s. It
also adds one road collision. The next candidate must preserve that progress
mechanism while adding a separately measurable, track-agnostic lateral safety
constraint. First locate the added collision in a fresh diagnostic export;
then run Track2 1 s and 120 s gates before any 700 s or four-track expansion.

This audit does not claim a finish, an official score, physical validation, or
submission readiness.
