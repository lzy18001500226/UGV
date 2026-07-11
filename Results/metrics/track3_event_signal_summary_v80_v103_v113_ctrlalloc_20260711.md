# Signal Window Summary

## v80_track3

Evidence: `Results\simulations\controller_v80_sharp_curve_speed_cap_saidao3_120s_20260710`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.chart.speed | obsAvoidController_Sysblock.chart.steer | ctrlAlloc.speed_oa | ctrlAlloc.steer_oa | ctrlAlloc.unitDelay1.y | ctrlAlloc.unitDelay3.y | ctrlAlloc.gain1.u | ctrlAlloc.gain1.y | ctrlAlloc.gain2.u | ctrlAlloc.gain2.y | ctrlAlloc.gain3.u | ctrlAlloc.gain3.y | ctrlAlloc.speed | ctrlAlloc.steer | pathPlanner.target_v | pathPlanner.steering_angle |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 0.01324 | 0.4876 | 0.6474 | 1 | -1 | 0.6 | -1 | 0.6 |  |  |  |  |  |  |  |  | 0.7196 | 0.1623 | 1 | -0.03857 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 | 2.05 | 0.106 | 0.2708 | 1 | -1 | 0.6 | -1 | 0.6 |  |  |  |  |  |  |  |  | 0.5105 | 0.1849 | 1 | -0.2215 |

## v103_track3

Evidence: `Results\simulations\controller_v103_conflict_path_speed_saidao3_120s_20260711`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.chart.speed | obsAvoidController_Sysblock.chart.steer | ctrlAlloc.speed_oa | ctrlAlloc.steer_oa | ctrlAlloc.unitDelay1.y | ctrlAlloc.unitDelay3.y | ctrlAlloc.gain1.u | ctrlAlloc.gain1.y | ctrlAlloc.gain2.u | ctrlAlloc.gain2.y | ctrlAlloc.gain3.u | ctrlAlloc.gain3.y | ctrlAlloc.speed | ctrlAlloc.steer | pathPlanner.target_v | pathPlanner.steering_angle |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 0.01324 | 0.4876 | 0.6474 | 1 | -1 | 0.6 | -1 | 0.6 | 8.562e-05 | 1 | -1 | -0.5 | 1 | 1 | -0.01928 | 8.562e-05 | 0.7196 | 0.1623 | 1 | -0.03857 |

## v113_track3

Evidence: `Results\simulations\controller_v113_conflict_speed_until25_saidao3_120s_20260711`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.chart.speed | obsAvoidController_Sysblock.chart.steer | ctrlAlloc.speed_oa | ctrlAlloc.steer_oa | ctrlAlloc.unitDelay1.y | ctrlAlloc.unitDelay3.y | ctrlAlloc.gain1.u | ctrlAlloc.gain1.y | ctrlAlloc.gain2.u | ctrlAlloc.gain2.y | ctrlAlloc.gain3.u | ctrlAlloc.gain3.y | ctrlAlloc.speed | ctrlAlloc.steer | pathPlanner.target_v | pathPlanner.steering_angle |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 0.01324 | 0.4876 | 0.6474 | 1 | -1 | 0.6 | -1 | 0.6 | 8.562e-05 | 1 | -1 | -0.5 | 1 | 1 | -0.01928 | 8.562e-05 | 0.7196 | 0.1623 | 1 | -0.03857 |
| 25.7 | cR: 0.0->1.0; P: 9.6->9.2 | 2.05 | 0.1074 | 0.2711 | 1 | -1 | 0.6 | -1 | 0.6 | -0.1484 | 1 | -1 | -0.5 | 1 | 1 | -0.1106 | -0.07418 | 0.5027 | 0.1886 | 1 | -0.2211 |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
