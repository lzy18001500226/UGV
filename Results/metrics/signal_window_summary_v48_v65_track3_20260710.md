# Signal Window Summary

## v48_track3

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao3_120s_20260710`

| Time/s | Changes | ctrlAlloc.speed | ctrlAlloc.steer | ctrlAlloc.steer_pp | ctrlAlloc.steer_oa | ctrlAlloc.firstOrder.y | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.chart.speed | pathPlanner.steering_angle | pathPlanner.target_v |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 0.7196 | 0.1623 | -0.03857 | 0.6 | 0.1816 | 0.01324 | 0.4876 | 0.6474 | 1 | -1 | -0.03857 | 1 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 | 0.5105 | 0.1849 | -0.2215 | 0.6 | 0.2957 | 2.05 | 0.106 | 0.2708 | 1 | -1 | -0.2215 | 1 |

## v65_track3

Evidence: `Results\simulations\controller_v65_front_emergency_hold_saidao3_120s_20260710`

| Time/s | Changes | ctrlAlloc.speed | ctrlAlloc.steer | ctrlAlloc.steer_pp | ctrlAlloc.steer_oa | ctrlAlloc.firstOrder.y | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.chart.speed | pathPlanner.steering_angle | pathPlanner.target_v |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.15 | cO: 0.0->1.0; P: 10.0->9.6 | 0.3623 | 0.1761 | -0.03361 | 0.6 | 0.1929 | 0.0168 | 0.4991 | 0.636 | 1 | -3 | -0.03361 | 1 |
| 5.05 | cR: 0.0->1.0; P: 9.6->9.2 | 0.497 | 0.1847 | -0.2236 | 0.6 | 0.2965 | 2.049 | 0.1024 | 0.2657 | 1 | -1 | -0.2236 | 1 |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
