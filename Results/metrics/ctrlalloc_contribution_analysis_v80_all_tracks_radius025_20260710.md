# CtrlAlloc Contribution Analysis

This is offline analysis of saved MWORKS CSV exports. It does not rerun MWORKS.

## v80_track1

Evidence: `Results\simulations\controller_v80_sharp_curve_speed_cap_saidao1_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.45 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 |  | 0.5358 | 0.284 | 0.6 |  | 0.5705 | 2.051 | 0.1012 | 0.1971 | 1 |

## v80_track2

Evidence: `Results\simulations\controller_v80_sharp_curve_speed_cap_saidao2_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.7 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 |  | 0.5224 | -0.2205 | 0.6 |  | 0.1816 | 2.052 | 0.1089 | 0.271 | 1 |

## v80_track3

Evidence: `Results\simulations\controller_v80_sharp_curve_speed_cap_saidao3_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 1 | -1 |  | 0.7196 | -0.03857 | 0.6 |  | 0.1623 | 0.01324 | 0.4876 | 0.6474 | 1 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 | 1 | -1 |  | 0.5105 | -0.2215 | 0.6 |  | 0.1849 | 2.05 | 0.106 | 0.2708 | 1 |

## v80_track4

Evidence: `Results\simulations\controller_v80_sharp_curve_speed_cap_saidao4_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.35 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 |  | 0.5244 | -0.2222 | 0.6 |  | 0.1796 | 2.052 | 0.1052 | 0.2674 | 1 |

## Interpretation Rules

- `speed_pp` / `steer_pp` are path-planner commands entering `CtrlAlloc`.
- `speed_oa` / `steer_oa` are obstacle-avoidance commands entering `CtrlAlloc`.
- `oa_*_filtered` are first-order filtered obstacle-avoidance contributions after `factor_oa`.
- Large final-steer values with small obstacle steer indicate path-planner dominance.
