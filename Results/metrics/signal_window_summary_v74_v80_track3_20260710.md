# Signal Window Summary

## v74_track3

Evidence: `Results\simulations\controller_v74_guarded_curve_short_lookahead_saidao3_120s_20260710`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.speed | obsAvoidController_Sysblock.steer | ctrlAlloc.speed | ctrlAlloc.steer | body3DOF1_1.P_vehicle[1] | body3DOF1_1.P_vehicle[2] | distanceSensor1.vehicle_position[1] | distanceSensor1.vehicle_position[2] |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 0.01324 | 0.4876 | 0.6474 | 1 |  |  | 0.7196 | 0.1623 | 0.055 | 0 | 1.2 | 0.0799 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 | 2.05 | 0.106 | 0.2708 | 1 |  |  | 0.5105 | 0.1849 | 0.055 | 0 | 3.364 | 0.4616 |

## v80_track3

Evidence: `Results\simulations\controller_v80_sharp_curve_speed_cap_saidao3_120s_20260710`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.speed | obsAvoidController_Sysblock.steer | ctrlAlloc.speed | ctrlAlloc.steer | body3DOF1_1.P_vehicle[1] | body3DOF1_1.P_vehicle[2] | distanceSensor1.vehicle_position[1] | distanceSensor1.vehicle_position[2] |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 0.01324 | 0.4876 | 0.6474 | 1 |  |  | 0.7196 | 0.1623 |  |  |  |  |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 | 2.05 | 0.106 | 0.2708 | 1 |  |  | 0.5105 | 0.1849 |  |  |  |  |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
