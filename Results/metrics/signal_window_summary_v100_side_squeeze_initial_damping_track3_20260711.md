# Signal Window Summary

## v100_track3

Evidence: `Results\simulations\controller_v100_side_squeeze_initial_damping_stmt_saidao3_120s_20260711`

| Time/s | Changes | ctrlAlloc.speed | ctrlAlloc.steer | ctrlAlloc.steer_oa | ctrlAlloc.steer_pp | pathPlanner.steering_angle | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 0.7196 | 0.1623 | 0.6 | -0.03857 | -0.03857 | 0.01324 | 0.4876 | 0.6474 | 1 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 | 0.5105 | 0.1304 | 0.2 | -0.2211 | -0.2211 | 2.05 | 0.1068 | 0.2717 | 1 |
| 26.35 | cR: 1.0->2.0; P: 9.2->8.8 | 0.5104 | 0.05043 | 0.2 | -0.09706 | -0.09706 | 2.051 | 0.1098 | 0.2746 | 1 |
| 32.45 | cR: 2.0->3.0; P: 8.8->8.4 | 0.2643 | 0.7139 | 0.2 | 0.6055 | 0.6055 | 1.317 | 0.109 | 0.2738 | 1 |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
