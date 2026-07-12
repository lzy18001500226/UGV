# CtrlAlloc Contribution Analysis

This is offline analysis of saved MWORKS CSV exports. It does not rerun MWORKS.

## v80_track1

Evidence: `Results\simulations\diagnostic_v80_track1_allocator_state_25s_20260712`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8.05 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.4941 | 0.5059 | 0.3007 | 0.6 | 0.2981 | 0.5989 | 2.587 | 0.1045 | 0.2665 | 1 |
| 11.85 | cR: 1.0->2.0; P: 9.6->9.2 | 1 | -1 | -0.4937 | 0.5063 | 0.2992 | 0.6 | 0.2981 | 0.5973 | 2.05 | 0.1002 | 0.2639 | 1 |

## v80_track2

Evidence: `Results\simulations\diagnostic_v80_track2_allocator_state_120s_20260712_retry1`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.7 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.4776 | 0.5224 | -0.2205 | 0.6 | 0.2919 | 0.1816 | 2.052 | 0.1089 | 0.271 | 1 |

## v80_track4

Evidence: `Results\simulations\controller_v80_track4_completion_gate_700s_20260712`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.3 | cR: 0.0->1.0; P: 10.0->9.6 |  | -1 |  | 0.5257 |  | 0.6 |  | 0.1802 | 2.052 | 0.1096 | 0.2718 |  |

## Interpretation Rules

- `speed_pp` / `steer_pp` are path-planner commands entering `CtrlAlloc`.
- `speed_oa` / `steer_oa` are obstacle-avoidance commands entering `CtrlAlloc`.
- `oa_*_filtered` are first-order filtered obstacle-avoidance contributions after `factor_oa`.
- Large final-steer values with small obstacle steer indicate path-planner dominance.
