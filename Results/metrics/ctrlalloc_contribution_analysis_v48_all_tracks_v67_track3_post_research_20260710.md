# CtrlAlloc Contribution Analysis

This is offline analysis of saved MWORKS CSV exports. It does not rerun MWORKS.

## v48_t1

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao1_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6.55 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.4943 | 0.5057 | 0.3006 | 0.6 | 0.2981 | 0.5987 | 3.774 | 0.1037 | 0.2667 | 1 |
| 30.35 | cR: 1.0->2.0; P: 9.6->9.2 | 0.75 | -1 | -0.4965 | 0.2535 | -0.6906 | 0.6 | 0.299 | -0.04632 | 2.025 | 0.1087 | 0.2699 | 1 |

## v48_t2

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao2_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.7 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.4776 | 0.5224 | -0.2205 | 0.6 | 0.2919 | 0.1816 | 2.052 | 0.1089 | 0.271 | 1 |

## v48_t3

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao3_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.2804 | 0.7196 | -0.03857 | 0.6 | 0.1816 | 0.1623 | 0.01324 | 0.4876 | 0.6474 | 1 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 | 1 | -1 | -0.4895 | 0.5105 | -0.2215 | 0.6 | 0.2957 | 0.1849 | 2.05 | 0.106 | 0.2708 | 1 |

## v48_t4

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao4_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.35 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.4756 | 0.5244 | -0.2222 | 0.6 | 0.2907 | 0.1796 | 2.052 | 0.1052 | 0.2674 | 1 |
| 90.15 | cR: 1.0->2.0; P: 9.6->9.2 | 0.75 | -1 | -0.4961 | 0.2539 | 1.64 | 0.6 | 0.2988 | 1.939 | 2.025 | 0.1087 | 0.271 | 1 |

## v67_t3

Evidence: `Results\simulations\diagnostic_v67_nearest_obstacle_front_saidao3_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 1 | -1 |  | 0.7316 | -0.04167 | 0.6 |  | 0.1572 | 0.1066 | 0.4811 | 0.6461 | 1 |
| 4.5 | cR: 0.0->1.0; P: 9.6->9.2 | 1 | -1 |  | 0.5155 | -0.2226 | 0.6 |  | 0.1824 | 1.562 | 0.1036 | 0.2679 | 1 |

## Interpretation Rules

- `speed_pp` / `steer_pp` are path-planner commands entering `CtrlAlloc`.
- `speed_oa` / `steer_oa` are obstacle-avoidance commands entering `CtrlAlloc`.
- `oa_*_filtered` are first-order filtered obstacle-avoidance contributions after `factor_oa`.
- Large final-steer values with small obstacle steer indicate path-planner dominance.
