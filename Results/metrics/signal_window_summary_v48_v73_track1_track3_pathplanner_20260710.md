# Signal Window Summary

## v48_track1

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao1_120s_20260710`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | ctrlAlloc.speed | ctrlAlloc.steer | ctrlAlloc.steer_oa | ctrlAlloc.steer_pp | pathPlanner.lookahead_dist | pathPlanner.steering_angle | pathPlanner.target_v | pathPlanner.x | pathPlanner.y |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6.55 | cR: 0.0->1.0; P: 10.0->9.6 | 3.774 | 0.1037 | 0.2667 | 1 | 0.5057 | 0.5987 | 0.6 | 0.3006 | 2.05 | 0.3006 | 1 | 2.966 | 1.785 |
| 30.35 | cR: 1.0->2.0; P: 9.6->9.2 | 2.025 | 0.1087 | 0.2699 | 1 | 0.2535 | -0.04632 | 0.6 | -0.6906 | 2.025 | -0.6906 | 0.75 | 12.63 | 6.126 |

## v73_track1

Evidence: `Results\simulations\controller_v73_curve_short_lookahead_saidao1_120s_20260710`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | ctrlAlloc.speed | ctrlAlloc.steer | ctrlAlloc.steer_oa | ctrlAlloc.steer_pp | pathPlanner.lookahead_dist | pathPlanner.steering_angle | pathPlanner.target_v | pathPlanner.x | pathPlanner.y |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.45 | cR: 0.0->1.0; P: 10.0->9.6 | 2.051 | 0.1012 | 0.1971 | 1 | 0.5358 | 0.5705 | 0.6 | 0.284 | 2.051 | 0.284 | 1 | 3.007 | 1.851 |

## v48_track3

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao3_120s_20260710`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | ctrlAlloc.speed | ctrlAlloc.steer | ctrlAlloc.steer_oa | ctrlAlloc.steer_pp | pathPlanner.lookahead_dist | pathPlanner.steering_angle | pathPlanner.target_v | pathPlanner.x | pathPlanner.y |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 0.01324 | 0.4876 | 0.6474 | 1 | 0.7196 | 0.1623 | 0.6 | -0.03857 | 2.071 | -0.03857 | 1 | 1.2 | 0.0799 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 | 2.05 | 0.106 | 0.2708 | 1 | 0.5105 | 0.1849 | 0.6 | -0.2215 | 2.05 | -0.2215 | 1 | 3.364 | 0.4616 |

## v73_track3

Evidence: `Results\simulations\controller_v73_curve_short_lookahead_saidao3_120s_20260710`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | ctrlAlloc.speed | ctrlAlloc.steer | ctrlAlloc.steer_oa | ctrlAlloc.steer_pp | pathPlanner.lookahead_dist | pathPlanner.steering_angle | pathPlanner.target_v | pathPlanner.x | pathPlanner.y |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 0.01324 | 0.4876 | 0.6474 | 1 | 0.7196 | 0.1623 | 0.6 | -0.03857 | 2.071 | -0.03857 | 1 | 1.2 | 0.0799 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 | 2.05 | 0.106 | 0.2708 | 1 | 0.5105 | 0.1849 | 0.6 | -0.2215 | 2.05 | -0.2215 | 1 | 3.364 | 0.4616 |
| 116.7 | cR: 1.0->2.0; P: 9.2->8.8 | 2.758 | 0.1091 | 0.2732 | 1 | 0.2519 | 2.274 | 0.6 | 1.974 | 1.316 | 1.974 | 0.75 | 9.595 | 17.33 |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
