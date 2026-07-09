# Signal Window Summary

## v48

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao3_120s_20260710`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.speed | obsAvoidController_Sysblock.steer | ctrlAlloc.speed | ctrlAlloc.steer | body3DOF1_1.P_vehicle[1] | body3DOF1_1.P_vehicle[2] | distanceSensor1.vehicle_position[1] | distanceSensor1.vehicle_position[2] |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 0.8306 | 0.5677 | 0.5673 | 1 |  |  | 0.7196 | 0.1623 |  |  |  |  |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 | 0.07106 | 0.5177 | 0.6173 | 1 |  |  | 0.5105 | 0.1849 |  |  |  |  |

## v58

Evidence: `Results\simulations\controller_v58_reactive_gap_initial_bypass_saidao3_120s_20260710`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.speed | obsAvoidController_Sysblock.steer | ctrlAlloc.speed | ctrlAlloc.steer | body3DOF1_1.P_vehicle[1] | body3DOF1_1.P_vehicle[2] | distanceSensor1.vehicle_position[1] | distanceSensor1.vehicle_position[2] |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 0.8306 | 0.5677 | 0.5673 | 1 | -1 | 0.6 | 0.7196 | 0.1109 |  |  |  |  |
| 6.15 | cO: 1.0->2.0; P: 9.6->9.2 | 2.067 | 0.4228 | 0.5876 | 1 | -1 | -0.7648 | 0.6671 | -0.09903 |  |  |  |  |
| 18 | cO: 2.0->3.0; P: 9.2->8.8 | 2.052 | 0.5353 | 0.6007 | 1 | -1 | 0.6 | 0.349 | 0.3557 |  |  |  |  |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
