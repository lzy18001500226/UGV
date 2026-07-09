# CtrlAlloc Contribution Analysis

This is offline analysis of saved MWORKS CSV exports. It does not rerun MWORKS.

## v48

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao3_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.2804 | 0.7196 | -0.03857 | 0.6 | 0.1816 | 0.1623 | 0.8306 | 0.5677 | 0.5673 | 1 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 | 1 | -1 | -0.4895 | 0.5105 | -0.2215 | 0.6 | 0.2957 | 0.1849 | 0.07106 | 0.5177 | 0.6173 | 1 |

## v58

Evidence: `Results\simulations\controller_v58_reactive_gap_initial_bypass_saidao3_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.2804 | 0.7196 | -0.03809 | -0.7578 | 0.149 | 0.1109 | 0.8306 | 0.5677 | 0.5673 | 1 |
| 6.15 | cO: 1.0->2.0; P: 9.6->9.2 | 1 | -1 | -0.3329 | 0.6671 | -0.03201 | -0.7324 | -0.06702 | -0.09903 | 2.067 | 0.4228 | 0.5876 | 1 |
| 18 | cO: 2.0->3.0; P: 9.2->8.8 | 0.75 | -1 | -0.401 | 0.349 | 0.8261 | -0.765 | -0.05739 | 0.3557 | 2.052 | 0.5353 | 0.6007 | 1 |

## Interpretation Rules

- `speed_pp` / `steer_pp` are path-planner commands entering `CtrlAlloc`.
- `speed_oa` / `steer_oa` are obstacle-avoidance commands entering `CtrlAlloc`.
- `oa_*_filtered` are first-order filtered obstacle-avoidance contributions after `factor_oa`.
- Large final-steer values with small obstacle steer indicate path-planner dominance.
