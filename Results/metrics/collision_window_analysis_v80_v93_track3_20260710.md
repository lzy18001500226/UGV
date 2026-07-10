# Collision Window Analysis

## Runs

| Label | Runtime | Exit | T/s | cR | cO | P | Events | Evidence |
|---|---|---:|---:|---:|---:|---:|---:|---|
| v80_track3 | `simulate_failed` | 2 | 59.4 | 1.0 | 1.0 | 9.2 | 2 | `Results\simulations\controller_v80_sharp_curve_speed_cap_saidao3_120s_20260710` |
| v93_track3 | `simulate_failed` | 2 | 10.700000000000001 | 1.0 | 2.0 | 8.8 | 3 | `Results\simulations\controller_v93_emergency_path_speed_suppress_saidao3_120s_20260710` |

## Jump Events

### v80_track3

| Time/s | Changes |
|---:|---|
| 1.05 | cO: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 4.85 | cR: 0.0 -> 1.0 (+1); P: 9.6 -> 9.2 (-0.4) |

### v93_track3

| Time/s | Changes |
|---:|---|
| 4.4 | cO: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 5.0 | cO: 1.0 -> 2.0 (+1); P: 9.6 -> 9.2 (-0.4) |
| 9.35 | cR: 0.0 -> 1.0 (+1); P: 9.2 -> 8.8 (-0.4) |

## Notes

- This analysis uses saved `score_timeseries.csv` files only.
- It does not rerun MWORKS and does not prove physical UGV behavior.
- Use the event times to decide the next visual or state-signal inspection window.
