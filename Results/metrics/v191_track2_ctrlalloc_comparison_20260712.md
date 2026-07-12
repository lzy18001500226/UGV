# CtrlAlloc Contribution Analysis

This is offline analysis of saved MWORKS CSV exports. It does not rerun MWORKS.

## baseline

Evidence: `Results\simulations\baseline_head_track2_700s_20260712`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.2 | cR: 0.0->1.0; P: 10.0->9.6 |  |  |  | 1.006 |  |  |  | 0.07661 |  |  |  |  |

## v191

Evidence: `Results\simulations\controller_v191_brake_then_steer_handoff_saidao2_700s_20260712`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.65 | cO: 0.0->1.0; P: 10.0->9.6 |  |  |  | 0.9141 |  |  |  | 0.09033 |  |  |  |  |
| 13.05 | cO: 1.0->2.0; P: 9.6->9.2 |  |  |  | 0.9792 |  |  |  | 0.07083 |  |  |  |  |
| 20.65 | cO: 2.0->3.0; P: 9.2->8.8 |  |  |  | 0.9511 |  |  |  | 0.07888 |  |  |  |  |
| 26.65 | cR: 0.0->1.0; P: 8.8->8.4 |  |  |  | 0.6537 |  |  |  | 0.7909 |  |  |  |  |
| 49.9 | cR: 1.0->2.0; P: 8.4->8.0 |  |  |  | 0.555 |  |  |  | 2.469 |  |  |  |  |
| 79.95 | cR: 2.0->3.0; P: 8.0->7.6 |  |  |  | 0.5531 |  |  |  | -2.536 |  |  |  |  |
| 84.9 | cO: 3.0->4.0; P: 7.6->7.2 |  |  |  | 0.2445 |  |  |  | -2.908 |  |  |  |  |

## Interpretation Rules

- `speed_pp` / `steer_pp` are path-planner commands entering `CtrlAlloc`.
- `speed_oa` / `steer_oa` are obstacle-avoidance commands entering `CtrlAlloc`.
- `oa_*_filtered` are first-order filtered obstacle-avoidance contributions after `factor_oa`.
- Large final-steer values with small obstacle steer indicate path-planner dominance.
