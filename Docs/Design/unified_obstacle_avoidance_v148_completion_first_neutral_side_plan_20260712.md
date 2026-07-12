# v148 Completion-First Neutral Side Longitudinal Plan

Status: retained as the 3/4 completion baseline; Track3 remains blocked.

## Reason For Reopening This Mechanism

The current priority is official completion before score optimization. v137
was stopped after its 120 s Track2 gate because road collisions increased from
one to two, even though it advanced from path index 26 to 112 and reduced the
finish-distance squared from 813.7304 to 329.7867. That score-first gate never
answered whether the mechanism can finish the track.

v148 is a completion-first extended validation of the same unified
longitudinal separation:

```modelica
speed := min(0, max(-1, df - mindis));
```

Front risk retains reverse authority. Side-only risk contributes neutral
longitudinal authority, allowing the path planner to continue moving the
vehicle. The existing lateral state machine, thresholds, allocator, path, and
all official models remain unchanged.

## Gates

1. Static deployability and all project tests must pass.
2. Track2 1 s must pass native load/check/simulation.
3. Track2 120 s must reproduce material progress without obstacle collisions.
4. A reproducible progress gain promotes directly to a 700 s completion gate,
   even if the short-run road-collision score is below v80. Official completion
   still requires `SimulateModel=false`, `T>10`, and
   `distanceSensor1.d<0.02`.
5. If Track2 does not finish, restore v80 immediately. If it finishes, retain
   v148 only as a completion baseline and then optimize collisions with the
   same unified controller before four-track expansion.

No fixed horizon, high wrapper score, or reduced finish distance is itself a
finish. This plan does not claim 80/80 or physical-vehicle readiness.

## Result

Track1, Track2, and Track4 reached the official origin assertion. Track3
stopped at `T=21.1` with finish distance squared `301.4313`. v148 therefore
supersedes v80 as the completion baseline, but it is not a four-track finish.
Detailed evidence is in
`Results/metrics/four_track_completion_review_v148_20260712.md`.
