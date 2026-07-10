# Signal Window Summary

## v80_track3

Evidence: `Results\simulations\controller_v80_sharp_curve_speed_cap_saidao3_120s_20260710`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.chart.speed | obsAvoidController_Sysblock.chart.steer | ctrlAlloc.speed | ctrlAlloc.steer | ctrlAlloc.speed_pp | ctrlAlloc.steer_pp | ctrlAlloc.speed_oa | ctrlAlloc.steer_oa |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 0.01324 | 0.4876 | 0.6474 | 1 | -1 | 0.6 | 0.7196 | 0.1623 | 1 | -0.03857 | -1 | 0.6 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 | 2.05 | 0.106 | 0.2708 | 1 | -1 | 0.6 | 0.5105 | 0.1849 | 1 | -0.2215 | -1 | 0.6 |

## v93_track3

Evidence: `Results\simulations\controller_v93_emergency_path_speed_suppress_saidao3_120s_20260710`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.chart.speed | obsAvoidController_Sysblock.chart.steer | ctrlAlloc.speed | ctrlAlloc.steer | ctrlAlloc.speed_pp | ctrlAlloc.steer_pp | ctrlAlloc.speed_oa | ctrlAlloc.steer_oa |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.4 | cO: 0.0->1.0; P: 10.0->9.6 | 2.049 | 0.1819 | 0.01687 | 1 | -1 | 0.6 | 0.5001 | 0.2328 | 1 | -0.04606 | -1 | 0.6 |
| 5 | cO: 1.0->2.0; P: 9.6->9.2 | 0.1475 | 0.5013 | 0.6473 | 1 | -3 | 0.6 | -0.8934 | 0.2564 | 1 | -0.03863 | -3 | 0.6 |
| 9.35 | cR: 0.0->1.0; P: 9.2->8.8 | 2.043 | 0.1004 | 0.09662 | 1 | -1 | 0.6 | 0.5231 | 0.1432 | 1 | -0.2637 | -1 | 0.6 |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
