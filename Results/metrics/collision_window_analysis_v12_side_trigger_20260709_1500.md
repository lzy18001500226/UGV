# Collision Window Analysis

## Runs

| Label | Runtime | Exit | T/s | cR | cO | P | Events | Evidence |
|---|---|---:|---:|---:|---:|---:|---:|---|
| v5_track1 | `simulate_failed` | 2 | 86.9 | 4.0 | 3.0 | 7.199999999999999 | 7 | `Results\simulations\eval_saidao1_connected_120s_final_20260709_120547` |
| v12_track1 | `simulate_returned_true` | 0 | 120.0 | 3.0 | 3.0 | 7.6 | 6 | `Results\simulations\controller_v12_side_trigger_saidao1_120s_20260709_144006` |
| v5_track4 | `simulate_failed` | 2 | 47.2 | 2.0 | 0.0 | 9.2 | 2 | `Results\simulations\eval_saidao4_connected_120s_final_20260709_120547` |
| v12_track4 | `simulate_failed` | 2 | 94.95 | 3.0 | 0.0 | 8.8 | 3 | `Results\simulations\controller_v12_side_trigger_saidao4_120s_20260709_144434` |

## Jump Events

### v5_track1

| Time/s | Changes |
|---:|---|
| 24.0 | cR: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 47.9 | cO: 0.0 -> 1.0 (+1); P: 9.6 -> 9.2 (-0.4) |
| 50.3 | cO: 1.0 -> 2.0 (+1); P: 9.2 -> 8.8 (-0.4) |
| 61.2 | cR: 1.0 -> 2.0 (+1); P: 8.8 -> 8.4 (-0.4) |
| 68.9 | cR: 2.0 -> 3.0 (+1); P: 8.4 -> 8.0 (-0.4) |
| 72.05 | cO: 2.0 -> 3.0 (+1); P: 8.0 -> 7.6 (-0.4) |
| 80.9 | cR: 3.0 -> 4.0 (+1); P: 7.6 -> 7.2 (-0.4) |

### v12_track1

| Time/s | Changes |
|---:|---|
| 21.75 | cO: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 22.3 | cO: 1.0 -> 2.0 (+1); P: 9.6 -> 9.2 (-0.4) |
| 25.95 | cR: 0.0 -> 1.0 (+1); P: 9.2 -> 8.8 (-0.4) |
| 29.3 | cR: 1.0 -> 2.0 (+1); P: 8.8 -> 8.4 (-0.4) |
| 99.95 | cO: 2.0 -> 3.0 (+1); P: 8.4 -> 8.0 (-0.4) |
| 106.45 | cR: 2.0 -> 3.0 (+1); P: 8.0 -> 7.6 (-0.4) |

### v5_track4

| Time/s | Changes |
|---:|---|
| 41.85 | cR: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 44.25 | cR: 1.0 -> 2.0 (+1); P: 9.6 -> 9.2 (-0.4) |

### v12_track4

| Time/s | Changes |
|---:|---|
| 5.1 | cR: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 55.25 | cR: 1.0 -> 2.0 (+1); P: 9.6 -> 9.2 (-0.4) |
| 78.1 | cR: 2.0 -> 3.0 (+1); P: 9.2 -> 8.8 (-0.4) |

## Notes

- This analysis uses saved `score_timeseries.csv` files only.
- It does not rerun MWORKS and does not prove physical UGV behavior.
- Use the event times to decide the next visual or state-signal inspection window.
