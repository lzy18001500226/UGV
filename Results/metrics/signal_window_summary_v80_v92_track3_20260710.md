# Signal Window Summary

## v80_track3

Evidence: `Results\simulations\controller_v80_sharp_curve_speed_cap_saidao3_120s_20260710`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.chart.speed | obsAvoidController_Sysblock.chart.steer | ctrlAlloc.speed | ctrlAlloc.steer | ctrlAlloc.speed_pp | ctrlAlloc.steer_pp | ctrlAlloc.speed_oa | ctrlAlloc.steer_oa |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 0.01324 | 0.4876 | 0.6474 | 1 | -1 | 0.6 | 0.7196 | 0.1623 | 1 | -0.03857 | -1 | 0.6 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 | 2.05 | 0.106 | 0.2708 | 1 | -1 | 0.6 | 0.5105 | 0.1849 | 1 | -0.2215 | -1 | 0.6 |

## v92_track3

Evidence: `Results\simulations\controller_v92_front_emergency_straight_hold_saidao3_120s_20260710`

| Time/s | Changes | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | obsAvoidController_Sysblock.chart.flag | obsAvoidController_Sysblock.chart.speed | obsAvoidController_Sysblock.chart.steer | ctrlAlloc.speed | ctrlAlloc.steer | ctrlAlloc.speed_pp | ctrlAlloc.steer_pp | ctrlAlloc.speed_oa | ctrlAlloc.steer_oa |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.1 | cO: 0.0->1.0; P: 10.0->9.6 | 0.03414 | 0.5058 | 0.6293 | 1 | -3 | 0 | 0.4066 | 0.06645 | 1 | -0.03026 | -3 | 0 |
| 6.15 | cR: 0.0->1.0; P: 9.6->9.2 | 2.048 | 0.1089 | 0.271 | 1 | -1 | 0.6 | 0.5102 | 0.1846 | 1 | -0.2209 | -1 | 0.6 |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
