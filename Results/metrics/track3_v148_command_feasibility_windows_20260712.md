# Signal Window Summary

## v148

Evidence: `Results\simulations\diagnostic_v148_track3_command_feasibility_700s_20260712`

| Time/s | Changes | ctrlAlloc.steer | ctrlAlloc.speed | pID_Ackermann.psi_desired | pID_Ackermann.current_psi | pID_Ackermann.psi_pid_control1.omega_d | pathPlanner.steering_angle | pathPlanner.target_v | obsAvoidController_Sysblock.steer | obsAvoidController_Sysblock.speed | obsAvoidController_Sysblock.chart.flag | distanceSensor1.front_dist | distanceSensor1.left_dist | distanceSensor1.right_dist |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | cO: 0.0->1.0; P: 10.0->9.6 | 0.1296 | 0.8361 | 0.1296 | 0.01618 | 11.11 | -0.04595 | 1 | 0.6 | 0 | 1 | 2.082 | -0.1791 | -0.0141 |
| 4.1 | cR: 0.0->1.0; P: 9.6->9.2 | 0.07762 | 0.9933 | 0.07762 | 0.07818 | -0.03943 | -0.2164 | 1 | 0.6 | 0 | 1 | 2.099 | 0.1064 | 0.2709 |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
