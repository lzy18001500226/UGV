# Collision Window Analysis

## Runs

| Label | Runtime | Exit | T/s | cR | cO | P | Events | Evidence |
|---|---|---:|---:|---:|---:|---:|---:|---|
| v97_track3 | `simulate_failed` | 2 | 32.45 | 13.0 | 1.0 | 4.3999999999999995 | 14 | `Results\simulations\controller_v97_narrow_left_squeeze_initial_override_saidao3_120s_20260710` |

## Jump Events

### v97_track3

| Time/s | Changes |
|---:|---|
| 1.05 | cO: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 6.6 | cR: 0.0 -> 1.0 (+1); P: 9.6 -> 9.2 (-0.4) |
| 7.7 | cR: 1.0 -> 2.0 (+1); P: 9.2 -> 8.8 (-0.4) |
| 11.9 | cR: 2.0 -> 3.0 (+1); P: 8.8 -> 8.4 (-0.4) |
| 16.8 | cR: 3.0 -> 4.0 (+1); P: 8.4 -> 8.0 (-0.4) |
| 18.0 | cR: 4.0 -> 5.0 (+1); P: 8.0 -> 7.6 (-0.4) |
| 19.45 | cR: 5.0 -> 6.0 (+1); P: 7.6 -> 7.2 (-0.4) |
| 20.8 | cR: 6.0 -> 7.0 (+1); P: 7.2 -> 6.8 (-0.4) |
| 21.5 | cR: 7.0 -> 8.0 (+1); P: 6.8 -> 6.4 (-0.4) |
| 24.85 | cR: 8.0 -> 9.0 (+1); P: 6.4 -> 6.0 (-0.4) |
| 25.75 | cR: 9.0 -> 10.0 (+1); P: 6.0 -> 5.6 (-0.4) |
| 27.4 | cR: 10.0 -> 11.0 (+1); P: 5.6 -> 5.2 (-0.4) |
| 28.35 | cR: 11.0 -> 12.0 (+1); P: 5.2 -> 4.8 (-0.4) |
| 30.0 | cR: 12.0 -> 13.0 (+1); P: 4.8 -> 4.4 (-0.4) |

## Notes

- This analysis uses saved `score_timeseries.csv` files only.
- It does not rerun MWORKS and does not prove physical UGV behavior.
- Use the event times to decide the next visual or state-signal inspection window.
