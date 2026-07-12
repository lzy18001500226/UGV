# Track3 v150 Candidate Review

Status: rejected.

## Comparison

| Candidate | Terminal time | Road collisions | Obstacle collisions | Path index | Finish distance squared | Finish |
|---|---:|---:|---:|---:|---:|---|
| v148 | 21.10 s | 1 | 1 | 36 | 301.4313 | no |
| v150 | 35.35 s | 1 | 1 | 36 | 288.8562 | no |

v150's moderate side-only braking delays termination but does not move the
vehicle beyond the v148 failure geometry. It is not a completion gain and is
rejected. The accepted completion baseline remains v148: Tracks 1, 2, and 4
finish; Track3 does not.

Evidence:

- `Results/simulations/candidate_v150_moderate_side_braking_track3_1s_20260712/`
- `Results/simulations/candidate_v150_moderate_side_braking_track3_120s_20260712/`
- `Results/metrics/track3_v150_terminal_progress_20260712.json`

## Decision

Restore `speed := min(0, max(-1, df - mindis))`. Do not scan more side-only
speed constants. The next candidate must alter lateral/state persistence and
must preserve one unified controller for all tracks.
