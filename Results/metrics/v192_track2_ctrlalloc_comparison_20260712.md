# CtrlAlloc Contribution Analysis

This is offline analysis of saved MWORKS CSV exports. It does not rerun MWORKS.

## baseline

Evidence: `Results\simulations\baseline_head_track2_700s_20260712`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.2 | cR: 0.0->1.0; P: 10.0->9.6 |  |  |  | 1.006 |  |  |  | 0.07661 |  |  |  |  |

## v192

Evidence: `Results\simulations\controller_v192_safety_priority_speed_saidao2_700s_20260712_retry1`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5.25 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | 0 | 0.001736 | 1.002 | -0.2155 | 0.6 | 0.2922 | 0.07676 | 2.1 | 0.1082 | 0.2727 | 1 |
| 101.5 | cR: 1.0->2.0; P: 9.6->9.2 | 0.55 | 0 | 0.002007 | 0.552 | 1.351 | 0.6 | 0.2988 | 1.65 | 2.055 | 0.3361 | 0.1711 | 1 |

## Interpretation Rules

- `speed_pp` / `steer_pp` are path-planner commands entering `CtrlAlloc`.
- `speed_oa` / `steer_oa` are obstacle-avoidance commands entering `CtrlAlloc`.
- `oa_*_filtered` are first-order filtered obstacle-avoidance contributions after `factor_oa`.
- Large final-steer values with small obstacle steer indicate path-planner dominance.
