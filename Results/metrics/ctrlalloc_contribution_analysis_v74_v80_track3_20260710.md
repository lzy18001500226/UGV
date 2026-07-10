# CtrlAlloc Contribution Analysis

This is offline analysis of saved MWORKS CSV exports. It does not rerun MWORKS.

## v74_track3

Evidence: `Results\simulations\controller_v74_guarded_curve_short_lookahead_saidao3_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.2804 | 0.7196 | -0.03857 | 0.6 | 0.1816 | 0.1623 | 0.01324 | 0.4876 | 0.6474 | 1 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 | 1 | -1 | -0.4895 | 0.5105 | -0.2215 | 0.6 | 0.2957 | 0.1849 | 2.05 | 0.106 | 0.2708 | 1 |

## v80_track3

Evidence: `Results\simulations\controller_v80_sharp_curve_speed_cap_saidao3_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 1 | -1 |  | 0.7196 | -0.03857 | 0.6 |  | 0.1623 | 0.01324 | 0.4876 | 0.6474 | 1 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 | 1 | -1 |  | 0.5105 | -0.2215 | 0.6 |  | 0.1849 | 2.05 | 0.106 | 0.2708 | 1 |

## Interpretation Rules

- `speed_pp` / `steer_pp` are path-planner commands entering `CtrlAlloc`.
- `speed_oa` / `steer_oa` are obstacle-avoidance commands entering `CtrlAlloc`.
- `oa_*_filtered` are first-order filtered obstacle-avoidance contributions after `factor_oa`.
- Large final-steer values with small obstacle steer indicate path-planner dominance.
