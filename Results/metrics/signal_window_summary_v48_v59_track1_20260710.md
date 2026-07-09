# Signal Window Summary

## v48

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao1_120s_20260710`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.speed | obsAvoidController_Sysblock.steer | ctrlAlloc.speed | ctrlAlloc.steer | body3DOF1_1.P_vehicle[1] | body3DOF1_1.P_vehicle[2] | distanceSensor1.vehicle_position[1] | distanceSensor1.vehicle_position[2] |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6.55 | cR: 0.0->1.0; P: 10.0->9.6 | 2.084 | 0.3914 | 0.55 | 1 |  |  | 0.5057 | 0.5987 |  |  |  |  |
| 30.35 | cR: 1.0->2.0; P: 9.6->9.2 | 2.041 | 0.2055 | 0.3704 | 1 |  |  | 0.2535 | -0.04632 |  |  |  |  |

## v59

Evidence: `Results\simulations\controller_v59_close_side_initial_direction_saidao1_120s_20260710`

- no score/collision jump events detected

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
