# Signal Window Summary

## baseline

Evidence: `Results\simulations\baseline_head_track2_700s_20260712`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.speed | obsAvoidController_Sysblock.steer | ctrlAlloc.speed | ctrlAlloc.steer | body3DOF1_1.P_vehicle[1] | body3DOF1_1.P_vehicle[2] | distanceSensor1.vehicle_position[1] | distanceSensor1.vehicle_position[2] |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.2 | cR: 0.0->1.0; P: 10.0->9.6 |  |  |  |  | 0 | 0.6 | 1.006 | 0.07661 |  |  | 4.675 | 0.4578 |

## v191

Evidence: `Results\simulations\controller_v191_brake_then_steer_handoff_saidao2_700s_20260712`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.speed | obsAvoidController_Sysblock.steer | ctrlAlloc.speed | ctrlAlloc.steer | body3DOF1_1.P_vehicle[1] | body3DOF1_1.P_vehicle[2] | distanceSensor1.vehicle_position[1] | distanceSensor1.vehicle_position[2] |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.65 | cO: 0.0->1.0; P: 10.0->9.6 |  |  |  |  | -1 | 0.6 | 0.9141 | 0.09033 |  |  | 1.873 | 0.05428 |
| 13.05 | cO: 1.0->2.0; P: 9.6->9.2 |  |  |  |  | 0 | 0.6 | 0.9792 | 0.07083 |  |  | 15.38 | 0.1018 |
| 20.65 | cO: 2.0->3.0; P: 9.2->8.8 |  |  |  |  | -1 | 0.6 | 0.9511 | 0.07888 |  |  | 22.56 | 0.0754 |
| 26.65 | cR: 0.0->1.0; P: 8.8->8.4 |  |  |  |  | -0.1579 | 0.6 | 0.6537 | 0.7909 |  |  | 27.29 | 1.306 |
| 49.9 | cR: 1.0->2.0; P: 8.4->8.0 |  |  |  |  | 0 | 0.6 | 0.555 | 2.469 |  |  | 27.28 | 16.71 |
| 79.95 | cR: 2.0->3.0; P: 8.0->7.6 |  |  |  |  | 0 | 0.6 | 0.5531 | -2.536 |  |  | 19.1 | 6.147 |
| 84.9 | cO: 3.0->4.0; P: 7.6->7.2 |  |  |  |  | 0 | 0.6 | 0.2445 | -2.908 |  |  | 17.62 | 5.316 |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
