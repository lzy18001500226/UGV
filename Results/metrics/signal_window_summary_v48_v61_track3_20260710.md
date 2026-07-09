# Signal Window Summary

## v48_track3

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao3_120s_20260710`

| Time/s | Changes | ctrlAlloc.pathSmallOpposingAvoid | ctrlAlloc.firstOrder.u | ctrlAlloc.firstOrder.y | ctrlAlloc.gain3.u | ctrlAlloc.steer | ctrlAlloc.steer_pp | ctrlAlloc.steer_oa | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 |  | 0.3 | 0.1816 | -0.01928 | 0.1623 | -0.03857 | 0.6 | 0.8306 | 0.5677 | 0.5673 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 |  | 0.3 | 0.2957 | -0.1107 | 0.1849 | -0.2215 | 0.6 | 0.07106 | 0.5177 | 0.6173 |

## v61_track3

Evidence: `Results\simulations\controller_v61_early_risk_arbitration_saidao3_120s_20260710`

| Time/s | Changes | ctrlAlloc.pathSmallOpposingAvoid | ctrlAlloc.firstOrder.u | ctrlAlloc.firstOrder.y | ctrlAlloc.gain3.u | ctrlAlloc.steer | ctrlAlloc.steer_pp | ctrlAlloc.steer_oa | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 0 | 0.36 | 0.1925 | 0 | 0.1925 | -0.03852 | 0.6 | 0.8306 | 0.5677 | 0.5673 |
| 4.25 | cR: 0.0->1.0; P: 9.6->9.2 | 0 | 0.3 | 0.2989 | -0.1115 | 0.1875 | -0.2229 | 0.6 | 0.16 | 0.5638 | 0.5712 |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
