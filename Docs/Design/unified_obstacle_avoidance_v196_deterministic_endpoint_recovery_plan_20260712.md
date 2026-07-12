# v196 Deterministic Endpoint Recovery Plan

Status: candidate under validation

## Evidence basis

- v162's narrow front-obstacle direction correction is the only controller
  mechanism that traversed the main Track3 loop, but it missed the origin.
- v180 reached an official Track3 finish after changing pursuit endpoint
  handling, then showed cross-track numerical instability.
- `calculatePursuitPoint` has no fallback assignment when lookahead extends
  beyond the final segment. An unassigned output is a concrete source of
  translation-dependent behavior.

## Unified candidate

1. Retain v148 longitudinal behavior.
2. Reapply v162's direction-aware steering only for `df < 0.15`.
3. Initialize `calculatePursuitPoint` to the final path point before normal
   traversal. Normal in-range pursuit calculations are unchanged; only an
   exhausted path traversal uses the deterministic fallback.

The same source applies to all tracks. It contains no track id, score, race
time, absolute-coordinate branch, or official-model edit.

## Gates

1. Source review, project tests, and Track3 1 s native gate.
2. Track3 completion request. Promotion requires the official finish assertion,
   `SimulateModel=false`, `T>10`, and finish distance squared below `0.02`.
3. A Track3 finish promotes unchanged source to Track2, Track1, and Track4.
4. Four-track retention requires official completion on every track; collision
   and score optimization follows only after completion is reproducible.
5. Any non-finish or cross-track regression restores exact v148 controller and
   original pursuit-function semantics.

No four-track completion, 80/80, physical UGV, or submission claim is made
before saved runtime evidence proves it.
