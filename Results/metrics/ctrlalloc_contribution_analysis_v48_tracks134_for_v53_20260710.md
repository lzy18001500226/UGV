# CtrlAlloc Contribution Analysis

This is offline analysis of saved MWORKS CSV exports. It does not rerun MWORKS.

## v48_track1

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao1_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6.55 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.4943 | 0.5057 | 0.3006 | 0.6 | 0.2981 | 0.5987 | 2.084 | 0.3914 | 0.55 | 1 |
| 30.35 | cR: 1.0->2.0; P: 9.6->9.2 | 0.75 | -1 | -0.4965 | 0.2535 | -0.6906 | 0.6 | 0.299 | -0.04632 | 2.041 | 0.2055 | 0.3704 | 1 |

## v48_track3

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao3_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.2804 | 0.7196 | -0.03857 | 0.6 | 0.1816 | 0.1623 | 0.8306 | 0.5677 | 0.5673 | 1 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 | 1 | -1 | -0.4895 | 0.5105 | -0.2215 | 0.6 | 0.2957 | 0.1849 | 0.07106 | 0.5177 | 0.6173 | 1 |

## v48_track4

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao4_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.35 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.4756 | 0.5244 | -0.2222 | 0.6 | 0.2907 | 0.1796 | 2.122 | 0.2881 | 0.1231 | 1 |
| 90.15 | cR: 1.0->2.0; P: 9.6->9.2 | 0.75 | -1 | -0.4961 | 0.2539 | 1.64 | 0.6 | 0.2988 | 1.939 | 2.025 | 0.4202 | 0.2556 | 1 |

## Interpretation Rules

- `speed_pp` / `steer_pp` are path-planner commands entering `CtrlAlloc`.
- `speed_oa` / `steer_oa` are obstacle-avoidance commands entering `CtrlAlloc`.
- `oa_*_filtered` are first-order filtered obstacle-avoidance contributions after `factor_oa`.
- Large final-steer values with small obstacle steer indicate path-planner dominance.
