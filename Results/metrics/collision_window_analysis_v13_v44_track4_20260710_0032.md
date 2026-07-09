# Collision Window Analysis

## Runs

| Label | Runtime | Exit | T/s | cR | cO | P | Events | Evidence |
|---|---|---:|---:|---:|---:|---:|---:|---|
| v13_track4 | `simulate_failed` | 2 | 113.10000000000001 | 3.0 | 0.0 | 8.8 | 3 | `Results\simulations\diagnostic_v13_signals_saidao4_120s_20260709_1910` |
| v44_track4 | `simulate_failed` | 2 | 113.10000000000001 | 3.0 | 0.0 | 8.8 | 3 | `Results\simulations\controller_v44_curvature_speed_regulation_saidao4_120s_20260710_0029` |

## Jump Events

### v13_track4

| Time/s | Changes |
|---:|---|
| 6.4 | cR: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 59.15 | cR: 1.0 -> 2.0 (+1); P: 9.6 -> 9.2 (-0.4) |
| 91.8 | cR: 2.0 -> 3.0 (+1); P: 9.2 -> 8.8 (-0.4) |

### v44_track4

| Time/s | Changes |
|---:|---|
| 6.4 | cR: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 59.15 | cR: 1.0 -> 2.0 (+1); P: 9.6 -> 9.2 (-0.4) |
| 91.8 | cR: 2.0 -> 3.0 (+1); P: 9.2 -> 8.8 (-0.4) |

## Notes

- This analysis uses saved `score_timeseries.csv` files only.
- It does not rerun MWORKS and does not prove physical UGV behavior.
- Use the event times to decide the next visual or state-signal inspection window.
