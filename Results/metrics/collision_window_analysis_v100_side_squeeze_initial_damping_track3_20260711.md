# Collision Window Analysis

## Runs

| Label | Runtime | Exit | T/s | cR | cO | P | Events | Evidence |
|---|---|---:|---:|---:|---:|---:|---:|---|
| v100_track3 | `simulate_returned_true` | 0 | 120.0 | 3.0 | 1.0 | 8.4 | 4 | `Results\simulations\controller_v100_side_squeeze_initial_damping_stmt_saidao3_120s_20260711` |

## Jump Events

### v100_track3

| Time/s | Changes |
|---:|---|
| 1.05 | cO: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 4.85 | cR: 0.0 -> 1.0 (+1); P: 9.6 -> 9.2 (-0.4) |
| 26.35 | cR: 1.0 -> 2.0 (+1); P: 9.2 -> 8.8 (-0.4) |
| 32.45 | cR: 2.0 -> 3.0 (+1); P: 8.8 -> 8.4 (-0.4) |

## Notes

- This analysis uses saved `score_timeseries.csv` files only.
- It does not rerun MWORKS and does not prove physical UGV behavior.
- Use the event times to decide the next visual or state-signal inspection window.
