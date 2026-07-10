# Signal Window Summary

## v48_t1

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao1_120s_20260710`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.speed | obsAvoidController_Sysblock.steer | ctrlAlloc.speed | ctrlAlloc.steer | body3DOF1_1.P_vehicle[1] | body3DOF1_1.P_vehicle[2] | distanceSensor1.vehicle_position[1] | distanceSensor1.vehicle_position[2] |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6.55 | cR: 0.0->1.0; P: 10.0->9.6 | 3.774 | 0.1037 | 0.2667 | 1 |  |  | 0.5057 | 0.5987 |  |  |  |  |
| 30.35 | cR: 1.0->2.0; P: 9.6->9.2 | 2.025 | 0.1087 | 0.2699 | 1 |  |  | 0.2535 | -0.04632 |  |  |  |  |

## v48_t4

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao4_120s_20260710`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.speed | obsAvoidController_Sysblock.steer | ctrlAlloc.speed | ctrlAlloc.steer | body3DOF1_1.P_vehicle[1] | body3DOF1_1.P_vehicle[2] | distanceSensor1.vehicle_position[1] | distanceSensor1.vehicle_position[2] |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.35 | cR: 0.0->1.0; P: 10.0->9.6 | 2.052 | 0.1052 | 0.2674 | 1 |  |  | 0.5244 | 0.1796 |  |  |  |  |
| 90.15 | cR: 1.0->2.0; P: 9.6->9.2 | 2.025 | 0.1087 | 0.271 | 1 |  |  | 0.2539 | 1.939 |  |  |  |  |

## v71_t1

Evidence: `Results\simulations\controller_v71_severe_left_steer_authority_saidao1_120s_20260710`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.speed | obsAvoidController_Sysblock.steer | ctrlAlloc.speed | ctrlAlloc.steer | body3DOF1_1.P_vehicle[1] | body3DOF1_1.P_vehicle[2] | distanceSensor1.vehicle_position[1] | distanceSensor1.vehicle_position[2] |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6.55 | cR: 0.0->1.0; P: 10.0->9.6 | 3.774 | 0.1037 | 0.2667 | 1 |  |  | 0.5057 | 0.6064 | 0.055 | 0 | 2.966 | 1.785 |

## v71_t4

Evidence: `Results\simulations\controller_v71_severe_left_steer_authority_saidao4_120s_20260710`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.speed | obsAvoidController_Sysblock.steer | ctrlAlloc.speed | ctrlAlloc.steer | body3DOF1_1.P_vehicle[1] | body3DOF1_1.P_vehicle[2] | distanceSensor1.vehicle_position[1] | distanceSensor1.vehicle_position[2] |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.35 | cR: 0.0->1.0; P: 10.0->9.6 | 2.052 | 0.1056 | 0.2677 | 1 |  |  | 0.5244 | 0.1936 | 0.055 | 0 | 3.656 | 0.4633 |
| 94.6 | cO: 0.0->1.0; P: 9.6->9.2 | 0.01685 | 0.3229 | 0.4878 | 1 |  |  | 0.2613 | 1.937 | 0.055 | 0 | 11.05 | 10.45 |
| 101.2 | cR: 1.0->2.0; P: 9.2->8.8 | 2.026 | 0.1083 | 0.2708 | 1 |  |  | 0.2564 | 1.943 | 0.055 | 0 | 10.52 | 12.04 |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
