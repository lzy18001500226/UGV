# Collision Window Analysis

## Runs

| Label | Runtime | Exit | T/s | cR | cO | P | Events | Evidence |
|---|---|---:|---:|---:|---:|---:|---:|---|
| v115_track3 | `simulate_failed` | 2 | 51.4 | 1.0 | 1.0 | 9.2 | 2 | `Results\simulations\controller_v115_smooth_straight_front_speed_cap_saidao3_120s_20260711` |

## Jump Events

### v115_track3

| Time/s | Changes |
|---:|---|
| 1.4 | cO: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 5.95 | cR: 0.0 -> 1.0 (+1); P: 9.6 -> 9.2 (-0.4) |

## Notes

- This analysis uses saved `score_timeseries.csv` files only.
- It does not rerun MWORKS and does not prove physical UGV behavior.
- Use the event times to decide the next visual or state-signal inspection window.
