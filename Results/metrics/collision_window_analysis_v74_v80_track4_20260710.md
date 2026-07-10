# Collision Window Analysis

## Runs

| Label | Runtime | Exit | T/s | cR | cO | P | Events | Evidence |
|---|---|---:|---:|---:|---:|---:|---:|---|
| v74_track4 | `simulate_returned_true` | 0 | 120.0 | 2.0 | 0.0 | 9.2 | 2 | `Results\simulations\controller_v74_guarded_curve_short_lookahead_saidao4_120s_20260710` |
| v80_track4 | `simulate_returned_true` | 0 | 120.0 | 1.0 | 0.0 | 9.6 | 1 | `Results\simulations\controller_v80_sharp_curve_speed_cap_saidao4_120s_20260710` |

## Jump Events

### v74_track4

| Time/s | Changes |
|---:|---|
| 4.35 | cR: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 104.0 | cR: 1.0 -> 2.0 (+1); P: 9.6 -> 9.2 (-0.4) |

### v80_track4

| Time/s | Changes |
|---:|---|
| 4.35 | cR: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |

## Notes

- This analysis uses saved `score_timeseries.csv` files only.
- It does not rerun MWORKS and does not prove physical UGV behavior.
- Use the event times to decide the next visual or state-signal inspection window.
