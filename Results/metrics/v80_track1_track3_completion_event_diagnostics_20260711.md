# Signal Window Summary

## v80_track1

Evidence: `Results\simulations\controller_v80_finish_gate_saidao1_120s_20260711`

| Time/s | Changes | body3DOF1_1.r[1] | body3DOF1_1.r[2] | body3DOF1_1.rr_speed | ctrlAlloc.speed | ctrlAlloc.steer | pathPlanner.target_v | pathPlanner.steering_angle | pathPlanner.closest_index | pathPlanner.path_progress | distanceSensor1.d |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4.45 | cR: 0.0->1.0; P: 10.0->9.6 | 3.007 | 1.851 | 1.724 |  |  |  |  | 10 | 0.03196 | 12.47 |

## v80_track3

Evidence: `Results\simulations\controller_v80_finish_gate_saidao3_120s_20260711`

| Time/s | Changes | body3DOF1_1.r[1] | body3DOF1_1.r[2] | body3DOF1_1.rr_speed | ctrlAlloc.speed | ctrlAlloc.steer | pathPlanner.target_v | pathPlanner.steering_angle | pathPlanner.closest_index | pathPlanner.path_progress | distanceSensor1.d |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1.05 | cO: 0.0->1.0; P: 10.0->9.6 |  |  |  | 0.7196 | 0.1623 |  |  | 1 | 0.84 | 1.446 |
| 4.85 | cR: 0.0->1.0; P: 9.6->9.2 |  |  |  | 0.5105 | 0.1849 |  |  | 3 | 0.3548 | 11.53 |

## Notes

- Values are nearest exported samples at the collision/score jump time.
- Use the JSON output for min/max/mean over the configured window radius.
- This is post-run evidence analysis only; it does not rerun MWORKS.
