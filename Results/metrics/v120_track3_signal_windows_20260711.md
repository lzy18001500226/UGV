# Signal Window Summary

## v120_track3

Evidence: `Results\simulations\controller_v120_lateral_state_continuity_saidao3_120s_20260711`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.speed | obsAvoidController_Sysblock.steer | ctrlAlloc.speed | ctrlAlloc.steer | body3DOF1_1.P_vehicle[1] | body3DOF1_1.P_vehicle[2] | distanceSensor1.vehicle_position[1] | distanceSensor1.vehicle_position[2] |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 0.01324 | 0.4876 | 0.6474 | 1 |  |  | 0.7196 | 0.1623 |  |  | 1.2 | 0.0799 |
| 6.85 | cO: 1.0->2.0; P: 9.6->9.2 | 0.01784 | 0.5493 | 0.612 | 1 |  |  | 0.845 | -0.02585 |  |  | 4.616 | 0.03136 |
| 10.7 | cR: 0.0->1.0; P: 9.2->8.8 | 2.041 | 0.09739 | 0.1728 | 1 |  |  | 0.5185 | -0.2918 |  |  | 6.812 | 0.5149 |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
