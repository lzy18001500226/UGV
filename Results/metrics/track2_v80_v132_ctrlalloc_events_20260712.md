# CtrlAlloc Contribution Analysis

This is offline analysis of saved MWORKS CSV exports. It does not rerun MWORKS.

## v80_track2

Evidence: `Results\simulations\diagnostic_v80_track2_speed_state_120s_20260712`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.7 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 |  | 0.5224 | -0.2205 | 0.6 |  | 0.1816 | 2.052 | 0.1089 | 0.271 | 1 |

## v132_track2

Evidence: `Results\simulations\diagnostic_v132_side_hold_progress_track2_120s_20260712`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5.4 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 |  | 0.6841 | -0.2196 | 0.6 |  | 0.09993 | 2.066 | 0.107 | 0.2706 | 1 |
| 39.55 | cR: 1.0->2.0; P: 9.6->9.2 | 0.75 | -1 |  | 0.2641 | 0.6255 | 0.09331 |  | 0.6455 | 1.306 | 0.1517 | 0.105 | 1 |

## Interpretation Rules

- `speed_pp` / `steer_pp` are path-planner commands entering `CtrlAlloc`.
- `speed_oa` / `steer_oa` are obstacle-avoidance commands entering `CtrlAlloc`.
- `oa_*_filtered` are first-order filtered obstacle-avoidance contributions after `factor_oa`.
- Large final-steer values with small obstacle steer indicate path-planner dominance.
