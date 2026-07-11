# Track1 Candidate Review - v135 Motion-Consistent Side Recovery

Decision: rejected; restored v80 controller semantics.

## Comparable Results

| Run | T (s) | cR | cO | P | Completion |
|---|---:|---:|---:|---:|---|
| v80 Track1 25 s | 25.0 | 2 | 0 | 9.2 | horizon only |
| v135 Track1 25 s | 25.0 | 1 | 0 | 9.6 | horizon only |
| v135 Track1 120 s request | 86.65 | 7 | 1 | 6.8 | early stop, no finish |

The 25-second gate showed a real local benefit, so the candidate was correctly
promoted to the long gate. The long gate then showed collision accumulation
and one obstacle collision. `SimulateModel=false` was not the official finish
assertion because `distanceSensor1.d=434.2004534766413`, far above `0.02`.

## Implementation Evidence

- Inline conditional state actions failed `CheckModel` with MWORKS error 549.
- Pure local functions passed `CheckModel` but failed embedded compilation with
  errors 7000/3005 and internal code 175.
- An explicit longitudinal side-recovery state plus arithmetic steering sign
  passed native compilation and the one-second simulation gate.

## Durable Runs

- `Results/simulations/candidate_v135_motion_consistent_side_recovery_track1_1s_20260712/`
- `Results/simulations/candidate_v135_motion_consistent_side_recovery_track1_1s_retry1_20260712/`
- `Results/simulations/candidate_v135_motion_consistent_side_recovery_track1_1s_retry2_explicit_state_20260712/`
- `Results/simulations/candidate_v135_motion_consistent_side_recovery_track1_25s_explicit_state_20260712/`
- `Results/simulations/candidate_v135_motion_consistent_side_recovery_track1_120s_explicit_state_20260712/`

## Follow-up Boundary

Do not scan the v135 side threshold or forward dwell as the next candidate.
The next mechanism must prevent repeated long-horizon recovery cycles or use a
stateful progress/escape decision supported by Sysblock code generation. It
must still use one unified controller across all four tracks.
