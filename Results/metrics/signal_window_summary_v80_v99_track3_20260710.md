# Signal Window Summary

## v80_track3

Evidence: `Results\simulations\controller_v80_sharp_curve_speed_cap_saidao3_120s_20260710`

| Time/s | Changes | pathPlanner.centerline_error_signed | pathPlanner.centerline_correction | pathPlanner.steering_angle | pathPlanner.base_steering_angle | ctrlAlloc.speed | ctrlAlloc.steer | ctrlAlloc.steer_pp | ctrlAlloc.steer_oa | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 |  |  | -0.03857 |  | 0.7196 | 0.1623 | -0.03857 | 0.6 | 0.01324 | 0.4876 | 0.6474 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 |  |  | -0.2215 |  | 0.5105 | 0.1849 | -0.2215 | 0.6 | 2.05 | 0.106 | 0.2708 |

## v99_track3

Evidence: `Results\simulations\controller_v99_centerline_damping_saidao3_120s_20260710`

| Time/s | Changes | pathPlanner.centerline_error_signed | pathPlanner.centerline_correction | pathPlanner.steering_angle | pathPlanner.base_steering_angle | ctrlAlloc.speed | ctrlAlloc.steer | ctrlAlloc.steer_pp | ctrlAlloc.steer_oa | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | -0.0799 | 0 | -0.03857 | -0.03857 | 0.7196 | 0.1623 | -0.03857 | 0.6 | 0.01324 | 0.4876 | 0.6474 |
| 5.9 | cR: 0.0->1.0; P: 9.6->9.2 | -0.461 | -0.1152 | -0.3364 | -0.2212 | 0.5037 | 0.1303 | -0.3364 | 0.6 | 2.05 | 0.1072 | 0.2708 |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
