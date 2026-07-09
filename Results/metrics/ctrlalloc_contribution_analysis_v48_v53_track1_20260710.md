# CtrlAlloc Contribution Analysis

This is offline analysis of saved MWORKS CSV exports. It does not rerun MWORKS.

## v48_track1

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao1_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6.55 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.4943 | 0.5057 | 0.3006 | 0.6 | 0.2981 | 0.5987 | 2.084 | 0.3914 | 0.55 | 1 |
| 30.35 | cR: 1.0->2.0; P: 9.6->9.2 | 0.75 | -1 | -0.4965 | 0.2535 | -0.6906 | 0.6 | 0.299 | -0.04632 | 2.041 | 0.2055 | 0.3704 | 1 |

## v53_track1

Evidence: `Results\simulations\controller_v53_path_conflict_neutralization_saidao1_120s_20260710`

| Time/s | Changes | speed_pp | speed_oa | oa_speed_filtered | final_speed | steer_pp | steer_oa | oa_steer_filtered | final_steer | df | dl | dr | flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6.55 | cR: 0.0->1.0; P: 10.0->9.6 | 1 | -1 | -0.4943 | 0.5057 | 0.3006 | 0.6 | 0.2981 | 0.5987 | 2.084 | 0.3914 | 0.55 | 1 |
| 25.2 | cR: 1.0->2.0; P: 9.6->9.2 | 0.75 | -1 | -0.4893 | 0.2607 | -0.4006 | 0.6 | 0.2968 | 0.2968 | 2.026 | 0.2274 | 0.3743 | 1 |
| 40.5 | cR: 2.0->3.0; P: 9.2->8.8 | 1 | -1 | -0.185 | 0.815 | -0.2684 | 0.6 | 0.2117 | 0.2117 | 2.05 | 0.1065 | 0.05653 | 1 |
| 45.05 | cR: 3.0->4.0; P: 8.8->8.4 | 1 | -1 | -0.4926 | 0.5074 | 0.08539 | 0.6 | 0.2979 | 0.3832 | 2.05 | 0.04567 | 0.1185 | 1 |

## Interpretation Rules

- `speed_pp` / `steer_pp` are path-planner commands entering `CtrlAlloc`.
- `speed_oa` / `steer_oa` are obstacle-avoidance commands entering `CtrlAlloc`.
- `oa_*_filtered` are first-order filtered obstacle-avoidance contributions after `factor_oa`.
- Large final-steer values with small obstacle steer indicate path-planner dominance.
