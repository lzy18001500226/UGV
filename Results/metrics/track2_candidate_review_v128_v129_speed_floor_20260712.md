# Track2 candidate review: v128 and v129

## Decision

Both candidates are rejected. The committed v80 source is restored. Neither
candidate produced an official Track2 finish, so neither can enter four-track
acceptance or replace the baseline.

| candidate | horizon/result | T | cR | cO | P | closest index | decision |
|---|---|---:|---:|---:|---:|---:|---|
| v80 fixed-solver reference | horizon reached | 180.0 | 1 | 0 | 9.6 | 27/231 | baseline diagnostic |
| v128 constant 0.2 floor | early stop | 157.9 | 1 | 0 | 9.6 | 35/231 | reject |
| v129 curvature-scaled floor | horizon reached | 180.0 | 1 | 0 | 9.6 | 27/231 | reject |

Official finish requires `T > 10` and `distanceSensor1.d < 0.02`; no run in
this batch met that gate. v128 demonstrated that the original allocator crawl
is real, but forced excessive speed in a sharp turn. v129 reduced the floor as
path steering increased and ran cleanly to the horizon, yet still collided and
did not finish.

## Evidence

- `Results/simulations/controller_v128_speed_floor_saidao2_1s_20260712/`
- `Results/simulations/controller_v128_speed_floor_saidao2_180s_20260712/`
- `Results/simulations/controller_v129_curvature_speed_floor_saidao2_1s_20260712/`
- `Results/simulations/controller_v129_curvature_speed_floor_saidao2_180s_20260712/`

## Next gate

Inspect the obstacle-state transition and conflict interval that keeps
`speed_oa=-1` active while path steering is large. Design a state-aware unified
handoff candidate from that evidence. Do not continue blind speed-floor scans.
