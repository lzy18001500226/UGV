# Track2 Candidate Review - v138 Adaptive Lateral Magnitude

## Decision

Reject v138 and retain restored v80 source semantics.

| Gate | Result | Decision |
|---|---|---|
| Static deployability | `high=0, medium=0` | pass |
| Project tests | `11 passed` | pass |
| Native Track2 1 s | `T=1, cR=0, cO=0, P=10.0` | pass |
| Track2 120 s | `T=120, cR=1, cO=0, P=9.6` | no gain over v80 |
| Official finish | `distanceSensor1.d=813.7304` | not reached |
| 700 s / other tracks | not run | prerequisite not met |

v138 changed only the final lateral avoidance magnitude from a maximum of
`0.8` to `0.6`, using the existing `min(limit, 2*abs(dl-dr))` form. The 120 s
run is comparable with v80 but does not improve progress or score, so the
candidate is rejected. It does not justify a longer run or cross-track
expansion.

Evidence:

- `Results/evidence/controller_deployability_static_check_v138_adaptive_lateral_magnitude_20260712.md`
- `Results/simulations/candidate_v138_adaptive_lateral_magnitude_track2_1s_20260712/`
- `Results/simulations/candidate_v138_adaptive_lateral_magnitude_track2_120s_20260712/`
- v80 comparison: `Results/simulations/controller_v80_finish_gate_saidao2_120s_20260711/`

No official track finish, 80-point result, or physical-vehicle claim is made.
