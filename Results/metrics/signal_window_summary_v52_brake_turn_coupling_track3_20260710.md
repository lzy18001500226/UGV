# Signal Window Summary

## v52_track3

Evidence: `Results\simulations\controller_v52_brake_turn_coupling_saidao3_120s_20260710`

| Time/s | Changes | pathPlanner.x | pathPlanner.y | pathPlanner.closest_index | pathPlanner.path_progress | pathPlanner.pursuit_point[1] | pathPlanner.pursuit_point[2] | pathPlanner.target_v | pathPlanner.steering_angle | ctrlAlloc.speed_pp | ctrlAlloc.speed_oa | ctrlAlloc.gain2.u | ctrlAlloc.gain3.u | ctrlAlloc.firstOrder1.y | ctrlAlloc.speed | ctrlAlloc.steer_pp | ctrlAlloc.steer_oa | ctrlAlloc.firstOrder.y | ctrlAlloc.steer | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.1 | cO: 0.0->1.0; P: 10.0->9.6 | 1.181 | 0.04592 | 1 | 0.8265 | 3.225 | 0 | 1 | -0.02246 | 1 | -1 | 0.75 | 0.01123 | -0.2911 | 0.4589 | -0.02246 | 0.6 | 0.1874 | 0.1986 | 0.8146 | 0.5677 | 0.5673 | 1 |
| 5.9 | cR: 0.0->1.0; P: 9.6->9.2 | 3.526 | 0.4628 | 3 | 0.468 | 5.575 | 0 | 1 | -0.2221 | 1 | -1 | 1 | -0.1111 | -0.4963 | 0.5037 | -0.2221 | 0.6 | 0.2985 | 0.1874 | 0.001587 | 0.1471 | 0.01789 | 1 |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
