# v190 Signed-Front Release Candidate

## Goal

Restore official Track2 completion before score optimization. The same
controller must remain eligible for all four tracks; this candidate contains
no track, time, score, or absolute-position branch.

## Evidence Behind The Change

- Path-only v187 returned near the Track2 origin but hit both default
  obstacles and missed the strict finish threshold.
- Continuous OA steering v188 avoided obstacle contacts but prevented route
  completion.
- v189 showed that the old OA output is not a reliable collision-risk signal.
- The official sensor can produce a negative front obstacle distance after
  the vehicle passes an obstacle. The current controller applies `abs` before
  the state machine, so a passed obstacle can remain indistinguishable from an
  approaching obstacle.

## Candidate

1. Feed the raw signed `front_dist` to the existing Sysblock chart. Keep side
   distances absolute for this bounded experiment.
2. Increase the generic front safety threshold from `1.0` to `1.5` metres.
3. Enter avoid only while the front reading is positive and inside the safety
   threshold, or while either side clearance is below the existing `0.45`
   threshold.
4. Release after the existing two-second minimum dwell only when front risk
   has cleared and both side clearances are safe.
5. Preserve the existing bounded speed and steering actions, allocator, path
   planner, official models, sensor, and scoring files.

## Gates

1. Source deployability checker: high=0 and medium=0.
2. Repository tests pass.
3. Track2 1 s native gate passes.
4. Track2 strict 700 s run is classified only by the official finish
   assertion evidence. Horizon or early termination alone is not completion.
5. Expand to Track3 and then all four tracks only if Track2 officially
   finishes or the run yields a clearly new diagnostic mechanism.

## Rollback

If the candidate does not improve completion evidence, restore the exact
controller bytes from `HEAD`. Do not retain a rejected semantic change.
