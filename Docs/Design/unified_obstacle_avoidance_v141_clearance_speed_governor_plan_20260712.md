# v141 Clearance-Based Avoidance Speed Governor

## Status

Candidate design only. v80 remains the accepted rollback baseline until the
Track2 comparable gate passes.

## Evidence Basis

- v80 remains in reverse avoidance after the front has recovered above
  `mindis`, leaving the final speed near `0.05 m/s` and stalling near path
  index 30.
- v132 changed side-only avoidance to a full forward command and added a road
  collision.
- v137 changed side-only avoidance to neutral authority and removed the stall,
  but also added a road collision.
- The next candidate therefore uses continuous front-clearance authority,
  rather than a binary reverse/neutral/forward handoff.

## Unified Mechanism

In the existing longitudinal avoid state, map front clearance to a bounded
speed command:

```modelica
speed := min(0.25, max(-1, df - safeF));
```

This preserves full reverse authority when the front is close, reaches zero at
the existing `safeF=1.5` margin, and permits only a limited forward crawl as
the front opens. Side-risk triggering and the existing lateral direction logic
remain unchanged. No track id, new port, timer, planner change, allocator
change, or parameter-specific branch is introduced.

## Scope and Gates

Only edit `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`.

1. Run the deployability checker and project tests.
2. Run Track2 for 1 s to prove load/check/simulate.
3. Run Track2 for 120 s. Require horizon completion, `cO=0`, no increase over
   v80 `cR=1`, and material path progress.
4. Only after gate 3 passes, run the 700 s official finish gate. A finish
   requires `SimulateModel=false`, `T>10`, and `distanceSensor1.d<0.02`.
5. Only after a Track2 finish, expand the same source and parameters to the
   other three tracks.

Any failed gate rejects v141 and restores exact v80 semantics. This plan does
not claim official completion, an 80/80 score, physical UGV performance, or
submission readiness.
