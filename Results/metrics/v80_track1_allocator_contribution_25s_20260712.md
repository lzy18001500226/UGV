# CtrlAlloc Contribution Analysis

This is offline analysis of saved MWORKS CSV exports. It does not rerun MWORKS.

## v80_track1_allocator_25s

Evidence: `Results\simulations\diagnostic_v80_track1_allocator_state_25s_20260712`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8.05 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.4941 | 0.5059 | 0.3007 | 0.6 | 0.2981 | 0.5989 | 2.587 | 0.1045 | 0.2665 | 1 |
| 11.85 | cR: 1.0->2.0; P: 9.6->9.2 | 1 | -1 | -0.4937 | 0.5063 | 0.2992 | 0.6 | 0.2981 | 0.5973 | 2.05 | 0.1002 | 0.2639 | 1 |

## Interpretation Rules

- `speed_pp` / `steer_pp` are path-planner commands entering `CtrlAlloc`.
- `speed_oa` / `steer_oa` are obstacle-avoidance commands entering `CtrlAlloc`.
- `oa_*_filtered` are first-order filtered obstacle-avoidance contributions after `factor_oa`.
- Large final-steer values with small obstacle steer indicate path-planner dominance.
