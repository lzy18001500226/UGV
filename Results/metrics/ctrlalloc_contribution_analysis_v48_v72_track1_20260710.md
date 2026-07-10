# CtrlAlloc Contribution Analysis

This is offline analysis of saved MWORKS CSV exports. It does not rerun MWORKS.

## v48_t1

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao1_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6.55 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.4943 | 0.5057 | 0.3006 | 0.6 | 0.2981 | 0.5987 | 3.774 | 0.1037 | 0.2667 | 1 |
| 30.35 | cR: 1.0->2.0; P: 9.6->9.2 | 0.75 | -1 | -0.4965 | 0.2535 | -0.6906 | 0.6 | 0.299 | -0.04632 | 2.025 | 0.1087 | 0.2699 | 1 |

## v72_t1

Evidence: `Results\simulations\controller_v72_narrow_opposing_path_authority_saidao1_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6.55 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.4943 | 0.5057 | 0.3006 | 0.6 | 0.2981 | 0.5987 | 3.774 | 0.1037 | 0.2667 | 1 |
| 29.35 | cR: 1.0->2.0; P: 9.6->9.2 | 0.75 | -1 | -0.4906 | 0.2594 | -0.6569 | 0.6 | 0.2972 | 0.133 | 2.026 | 0.1065 | 0.2669 | 1 |

## Interpretation Rules

- `speed_pp` / `steer_pp` are path-planner commands entering `CtrlAlloc`.
- `speed_oa` / `steer_oa` are obstacle-avoidance commands entering `CtrlAlloc`.
- `oa_*_filtered` are first-order filtered obstacle-avoidance contributions after `factor_oa`.
- Large final-steer values with small obstacle steer indicate path-planner dominance.
