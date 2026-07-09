# Signal Window Summary

## v48_track3

Evidence: `Results\simulations\controller_v48_opposing_steer_guard_saidao3_120s_20260710`

| Time/s | Changes | ctrlAlloc.firstOrder.u | ctrlAlloc.firstOrder.y | ctrlAlloc.gain3.u | ctrlAlloc.steer | ctrlAlloc.steer_pp | ctrlAlloc.steer_oa | obsAvoidController_Sysblock.chart.steer | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | pathPlanner.x | pathPlanner.y |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 | 0.3 | 0.1816 | -0.01928 | 0.1623 | -0.03857 | 0.6 | 0.6 | 0.8306 | 0.5677 | 0.5673 | 1.2 | 0.0799 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 | 0.3 | 0.2957 | -0.1107 | 0.1849 | -0.2215 | 0.6 | 0.6 | 0.07106 | 0.5177 | 0.6173 | 3.364 | 0.4616 |

## v62_track3

Evidence: `Results\simulations\controller_v62_front_centered_initial_bypass_saidao3_120s_20260710`

| Time/s | Changes | ctrlAlloc.firstOrder.u | ctrlAlloc.firstOrder.y | ctrlAlloc.gain3.u | ctrlAlloc.steer | ctrlAlloc.steer_pp | ctrlAlloc.steer_oa | obsAvoidController_Sysblock.chart.steer | obsAvoidController_Sysblock.chart.df | obsAvoidController_Sysblock.chart.dl | obsAvoidController_Sysblock.chart.dr | pathPlanner.x | pathPlanner.y |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | cO: 0.0->1.0; P: 10.0->9.6 | 0.3 | 0.05857 | -0.00544 | 0.05313 | -0.01088 | 0.6 | -0.45 | 0.8469 | 0.5674 | 0.5676 | 1.17 | 0.02255 |
| 5.15 | cR: 0.0->1.0; P: 9.6->9.2 | 0.3 | 0.295 | -0.1135 | 0.1815 | -0.2269 | 0.6 | 0.6 | 0.02366 | 0.5366 | 0.5984 | 3.487 | 0.4735 |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
