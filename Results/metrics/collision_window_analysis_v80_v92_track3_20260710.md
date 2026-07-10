# Collision Window Analysis

## Runs

| Label | Runtime | Exit | T/s | cR | cO | P | Events | Evidence |
|---|---|---:|---:|---:|---:|---:|---:|---|
| v80_track3 | `simulate_failed` | 2 | 59.4 | 1.0 | 1.0 | 9.2 | 2 | `Results\simulations\controller_v80_sharp_curve_speed_cap_saidao3_120s_20260710` |
| v92_track3 | `simulate_failed` | 2 | 43.9 | 1.0 | 1.0 | 9.2 | 2 | `Results\simulations\controller_v92_front_emergency_straight_hold_saidao3_120s_20260710` |

## Jump Events

### v80_track3

| Time/s | Changes |
|---:|---|
| 1.05 | cO: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 4.85 | cR: 0.0 -> 1.0 (+1); P: 9.6 -> 9.2 (-0.4) |

### v92_track3

| Time/s | Changes |
|---:|---|
| 1.1 | cO: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 6.15 | cR: 0.0 -> 1.0 (+1); P: 9.6 -> 9.2 (-0.4) |

## Notes

- This analysis uses saved `score_timeseries.csv` files only.
- It does not rerun MWORKS and does not prove physical UGV behavior.
- Use the event times to decide the next visual or state-signal inspection window.
