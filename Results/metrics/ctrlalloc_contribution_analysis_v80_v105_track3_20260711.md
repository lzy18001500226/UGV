# CtrlAlloc Contribution Analysis

This is offline analysis of saved MWORKS CSV exports. It does not rerun MWORKS.

## v80_track3

Evidence: `Results\simulations\controller_v80_sharp_curve_speed_cap_saidao3_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 1 | -1 |  | 0.7196 | -0.03857 | 0.6 |  | 0.1623 | 0.01324 | 0.4876 | 0.6474 | 1 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 | 1 | -1 |  | 0.5105 | -0.2215 | 0.6 |  | 0.1849 | 2.05 | 0.106 | 0.2708 | 1 |

## v105_track3

Evidence: `Results\simulations\controller_v105_front_aligned_speed_cap_saidao3_120s_20260711`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.6 | cO: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.3733 | 0.1767 | -0.0113 | 0.6 | 0.2317 | 0.2261 | 0.04613 | 0.545 | 0.5906 | 1 |
| 18.75 | cR: 0.0->1.0; P: 9.6->9.2 | 1 | -1 | -0.4933 | 0.5067 | -0.2219 | 0.6 | 0.298 | 0.187 | 2.051 | 0.1062 | 0.2684 | 1 |

## Interpretation Rules

- `speed_pp` / `steer_pp` are path-planner commands entering `CtrlAlloc`.
- `speed_oa` / `steer_oa` are obstacle-avoidance commands entering `CtrlAlloc`.
- `oa_*_filtered` are first-order filtered obstacle-avoidance contributions after `factor_oa`.
- Large final-steer values with small obstacle steer indicate path-planner dominance.
