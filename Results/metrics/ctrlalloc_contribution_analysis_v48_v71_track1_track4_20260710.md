# CtrlAlloc Contribution Analysis

This is offline analysis of saved MWORKS CSV exports. It does not rerun MWORKS.

## v48_t1

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao1_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6.55 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.4943 | 0.5057 | 0.3006 | 0.6 | 0.2981 | 0.5987 | 3.774 | 0.1037 | 0.2667 | 1 |
| 30.35 | cR: 1.0->2.0; P: 9.6->9.2 | 0.75 | -1 | -0.4965 | 0.2535 | -0.6906 | 0.6 | 0.299 | -0.04632 | 2.025 | 0.1087 | 0.2699 | 1 |

## v48_t4

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao4_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.35 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.4756 | 0.5244 | -0.2222 | 0.6 | 0.2907 | 0.1796 | 2.052 | 0.1052 | 0.2674 | 1 |
| 90.15 | cR: 1.0->2.0; P: 9.6->9.2 | 0.75 | -1 | -0.4961 | 0.2539 | 1.64 | 0.6 | 0.2988 | 1.939 | 2.025 | 0.1087 | 0.271 | 1 |

## v71_t1

Evidence: `Results\simulations\controller_v71_severe_left_steer_authority_saidao1_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6.55 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.4943 | 0.5057 | 0.3006 | 0.8 | 0.3058 | 0.6064 | 3.774 | 0.1037 | 0.2667 | 1 |

## v71_t4

Evidence: `Results\simulations\controller_v71_severe_left_steer_authority_saidao4_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.35 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.4756 | 0.5244 | -0.222 | 0.8 | 0.3047 | 0.1936 | 2.052 | 0.1056 | 0.2677 | 1 |
| 94.6 | cO: 0.0->1.0; P: 9.6->9.2 | 0.75 | -1 | -0.4887 | 0.2613 | 1.641 | 0.6 | 0.2966 | 1.937 | 0.01685 | 0.3229 | 0.4878 | 1 |
| 101.2 | cR: 1.0->2.0; P: 9.2->8.8 | 0.75 | -1 | -0.4936 | 0.2564 | 1.618 | 0.8 | 0.3248 | 1.943 | 2.026 | 0.1083 | 0.2708 | 1 |

## Interpretation Rules

- `speed_pp` / `steer_pp` are path-planner commands entering `CtrlAlloc`.
- `speed_oa` / `steer_oa` are obstacle-avoidance commands entering `CtrlAlloc`.
- `oa_*_filtered` are first-order filtered obstacle-avoidance contributions after `factor_oa`.
- Large final-steer values with small obstacle steer indicate path-planner dominance.
