# Signal Window Summary

## v48_track1_signal

Evidence: `Results\simulations\controller_v48_signal_geometry_saidao1_120s_20260710`

| Time/s | Changes | distanceSensor1.distF | distanceSensor1.distL | distanceSensor1.distR | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.chart.speed | obsAvoidController_Sysblock.chart.steer | pathPlanner.target_v | pathPlanner.steering_angle | ctrlAlloc.speed_pp | ctrlAlloc.speed_oa | ctrlAlloc.steer_pp | ctrlAlloc.steer_oa | ctrlAlloc.gain3.u | ctrlAlloc.gain3.y | ctrlAlloc.speed | ctrlAlloc.steer |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 6.65 | cR: 0.0->1.0; P: 10.0->9.6 | 3.416 | -0.4758 | -0.3108 | 2.083 | 0.3878 | 0.5467 | 1 | -1 | 0.6 | 1 | 0.3016 | 1 | -1 | 0.3016 | 0.6 | 0.3016 | 0.4417 | 0.5051 | 0.5999 |
| 29.9 | cR: 1.0->2.0; P: 9.6->9.2 | -0.7464 | -0.6003 | -0.4353 | 2.051 | 0.1968 | 0.3567 | 1 | -1 | 0.6 | 0.75 | -0.6915 | 0.75 | -1 | -0.6915 | 0.6 | -0.3457 | 0.3766 | 0.2554 | -0.04738 |

## v48_track3_signal

Evidence: `Results\simulations\controller_v48_signal_geometry_saidao3_120s_20260710`

| Time/s | Changes | distanceSensor1.distF | distanceSensor1.distL | distanceSensor1.distR | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.chart.speed | obsAvoidController_Sysblock.chart.steer | pathPlanner.target_v | pathPlanner.steering_angle | ctrlAlloc.speed_pp | ctrlAlloc.speed_oa | ctrlAlloc.steer_pp | ctrlAlloc.steer_oa | ctrlAlloc.gain3.u | ctrlAlloc.gain3.y | ctrlAlloc.speed | ctrlAlloc.steer |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 0.01324 | -0.1637 | 0.001283 | 0.8306 | 0.5677 | 0.5673 | 1 | -1 | 0.6 | 1 | -0.03857 | 1 | -1 | -0.03857 | 0.6 | -0.01928 | 8.562e-05 | 0.7196 | 0.1623 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 | 1.244 | -0.594 | -0.429 | 0.07106 | 0.5177 | 0.6173 | 1 | -1 | 0.6 | 1 | -0.2204 | 1 | -1 | -0.2204 | 0.6 | -0.1102 | 0.01098 | 0.5105 | 0.1855 |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
