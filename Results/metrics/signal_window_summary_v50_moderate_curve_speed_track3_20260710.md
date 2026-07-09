# Signal Window Summary

## v50_track3

Evidence: `Results\simulations\controller_v50_moderate_curve_speed_saidao3_120s_20260710`

| Time/s | Changes | pathPlanner.x | pathPlanner.y | pathPlanner.closest_index | pathPlanner.path_progress | pathPlanner.pursuit_point[1] | pathPlanner.pursuit_point[2] | pathPlanner.target_v | pathPlanner.steering_angle | ctrlAlloc.speed_pp | ctrlAlloc.speed_oa | ctrlAlloc.firstOrder1.y | ctrlAlloc.speed | ctrlAlloc.steer_pp | ctrlAlloc.steer_oa | ctrlAlloc.firstOrder.y | ctrlAlloc.steer | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 1.2 | 0.0799 | 1 | 0.84 | 3.271 | 0 | 1 | -0.03857 | 1 | -1 | -0.2804 | 0.7196 | -0.03857 | 0.6 | 0.1816 | 0.1623 | 0.8306 | 0.5677 | 0.5673 | 1 |
| 5.05 | cR: 0.0->1.0; P: 9.6->9.2 | 3.382 | 0.4603 | 3 | 0.3672 | 5.406 | 0 | 0.75 | -0.2236 | 0.75 | -1 | -0.4914 | 0.2586 | -0.2236 | 0.6 | 0.2965 | 0.1847 | 0.04202 | 0.5026 | 0.6324 | 1 |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
