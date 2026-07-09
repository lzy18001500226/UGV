# Collision Window Analysis

## Runs

| Label | Runtime | Exit | T/s | cR | cO | P | Events | Evidence |
|---|---|---:|---:|---:|---:|---:|---:|---|
| v48 | `simulate_failed` | 2 | 112.45 | 1.0 | 1.0 | 9.2 | 2 | `Results\simulations\controller_v48_opposing_steer_guard_saidao3_120s_20260710` |
| v67_nearest_obstacle_front | `simulate_returned_true` | 0 | 120.0 | 1.0 | 1.0 | 9.2 | 2 | `Results\simulations\diagnostic_v67_nearest_obstacle_front_saidao3_120s_20260710` |

## Jump Events

### v48

| Time/s | Changes |
|---:|---|
| 1.05 | cO: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 4.85 | cR: 0.0 -> 1.0 (+1); P: 9.6 -> 9.2 (-0.4) |

### v67_nearest_obstacle_front

| Time/s | Changes |
|---:|---|
| 1.05 | cO: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 4.5 | cR: 0.0 -> 1.0 (+1); P: 9.6 -> 9.2 (-0.4) |

## Notes

- This analysis uses saved `score_timeseries.csv` files only.
- It does not rerun MWORKS and does not prove physical UGV behavior.
- Use the event times to decide the next visual or state-signal inspection window.
