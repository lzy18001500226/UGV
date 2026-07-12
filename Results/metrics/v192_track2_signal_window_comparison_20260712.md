# Signal Window Summary

## baseline

Evidence: `Results\simulations\baseline_head_track2_700s_20260712`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.speed | obsAvoidController_Sysblock.steer | ctrlAlloc.speed | ctrlAlloc.steer | body3DOF1_1.P_vehicle[1] | body3DOF1_1.P_vehicle[2] | distanceSensor1.vehicle_position[1] | distanceSensor1.vehicle_position[2] |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.2 | cR: 0.0->1.0; P: 10.0->9.6 |  |  |  |  | 0 | 0.6 | 1.006 | 0.07661 |  |  | 4.675 | 0.4578 |

## v192

Evidence: `Results\simulations\controller_v192_safety_priority_speed_saidao2_700s_20260712_retry1`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.speed | obsAvoidController_Sysblock.steer | ctrlAlloc.speed | ctrlAlloc.steer | body3DOF1_1.P_vehicle[1] | body3DOF1_1.P_vehicle[2] | distanceSensor1.vehicle_position[1] | distanceSensor1.vehicle_position[2] |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5.25 | cR: 0.0->1.0; P: 10.0->9.6 | 2.1 | 0.1082 | 0.2727 | 1 | 0 | 0.6 | 1.002 | 0.07676 |  |  | 3.831 | 0.4596 |
| 101.5 | cR: 1.0->2.0; P: 9.6->9.2 | 2.055 | 0.3361 | 0.1711 | 1 | 0 | 0.6 | 0.552 | 1.65 |  |  | 12.54 | 11 |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
