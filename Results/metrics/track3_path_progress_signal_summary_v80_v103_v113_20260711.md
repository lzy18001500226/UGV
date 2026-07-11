# Signal Window Summary

## v80_track3

Evidence: `Results\simulations\controller_v80_sharp_curve_speed_cap_saidao3_120s_20260710`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | ctrlAlloc.speed | ctrlAlloc.steer | ctrlAlloc.gain2.u | ctrlAlloc.unitDelay1.y | pathPlanner.closest_index | pathPlanner.path_progress | pathPlanner.target_v | pathPlanner.steering_angle |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 0.01324 | 0.4876 | 0.6474 | 0.7196 | 0.1623 |  |  |  |  | 1 | -0.03857 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 | 2.05 | 0.106 | 0.2708 | 0.5105 | 0.1849 |  |  |  |  | 1 | -0.2215 |

## v103_track1

Evidence: `Results\simulations\controller_v103_conflict_path_speed_saidao1_120s_20260711`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | ctrlAlloc.speed | ctrlAlloc.steer | ctrlAlloc.gain2.u | ctrlAlloc.unitDelay1.y | pathPlanner.closest_index | pathPlanner.path_progress | pathPlanner.target_v | pathPlanner.steering_angle |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.8 | cR: 0.0->1.0; P: 10.0->9.6 | 2.05 | 0.1031 | 0.2214 | 0.5252 | 0.5805 | 1 | 0.3636 | 10 | 0.1815 | 1 | 0.29 |
| 40.05 | cR: 1.0->2.0; P: 9.6->9.2 | 1.986 | 0.1097 | 0.2679 | -0.1411 | 0.1971 | 0.35 | 0.2709 | 15 | 1 | 1 | -0.2004 |
| 60.4 | cR: 2.0->3.0; P: 9.2->8.8 | 1.989 | 0.1042 | 0.1813 | -0.1413 | 0.1727 | 0.35 | 0.2443 | 16 | 0.4515 | 1 | -0.2493 |

## v103_track2

Evidence: `Results\simulations\controller_v103_conflict_path_speed_saidao2_120s_20260711`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | ctrlAlloc.speed | ctrlAlloc.steer | ctrlAlloc.gain2.u | ctrlAlloc.unitDelay1.y | pathPlanner.closest_index | pathPlanner.path_progress | pathPlanner.target_v | pathPlanner.steering_angle |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 18.5 | cR: 0.0->1.0; P: 10.0->9.6 | 1.986 | 0.1097 | 0.2732 | -0.1481 | 0.186 | 0.35 | -0.07813 | 2 | 0.0331 | 1 | -0.227 |

## v103_track3

Evidence: `Results\simulations\controller_v103_conflict_path_speed_saidao3_120s_20260711`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | ctrlAlloc.speed | ctrlAlloc.steer | ctrlAlloc.gain2.u | ctrlAlloc.unitDelay1.y | pathPlanner.closest_index | pathPlanner.path_progress | pathPlanner.target_v | pathPlanner.steering_angle |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 0.01324 | 0.4876 | 0.6474 | 0.7196 | 0.1623 | 1 | 8.562e-05 | 1 | 0.84 | 1 | -0.03857 |

## v113_track3

Evidence: `Results\simulations\controller_v113_conflict_speed_until25_saidao3_120s_20260711`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | ctrlAlloc.speed | ctrlAlloc.steer | ctrlAlloc.gain2.u | ctrlAlloc.unitDelay1.y | pathPlanner.closest_index | pathPlanner.path_progress | pathPlanner.target_v | pathPlanner.steering_angle |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 0.01324 | 0.4876 | 0.6474 | 0.7196 | 0.1623 | 1 | 8.562e-05 | 1 | 0.84 | 1 | -0.03857 |
| 25.7 | cR: 0.0->1.0; P: 9.6->9.2 | 2.05 | 0.1074 | 0.2711 | 0.5027 | 0.1886 | 1 | -0.1484 | 2 | 0.2022 | 1 | -0.2211 |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
