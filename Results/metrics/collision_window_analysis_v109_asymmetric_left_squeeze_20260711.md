# Collision Window Analysis

## Runs

| Label | Runtime | Exit | T/s | cR | cO | P | Events | Evidence |
|---|---|---:|---:|---:|---:|---:|---:|---|
| v109_track1 | `simulate_failed` | 2 | 17.400000000000002 | 1.0 | 0.0 | 9.6 | 1 | `Results\simulations\controller_v109_asymmetric_left_squeeze_saidao1_120s_20260711` |
| v109_track3 | `simulate_failed` | 2 | 11.6 | 0.0 | 1.0 | 9.6 | 1 | `Results\simulations\controller_v109_asymmetric_left_squeeze_saidao3_120s_20260711` |
| v109_track4 | `simulate_failed` | 2 | 7.2 | 0.0 | 0.0 | 10.0 | 0 | `Results\simulations\controller_v109_asymmetric_left_squeeze_saidao4_120s_20260711` |

## Jump Events

### v109_track1

| Time/s | Changes |
|---:|---|
| 4.45 | cR: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |

### v109_track3

| Time/s | Changes |
|---:|---|
| 1.05 | cO: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |

### v109_track4

- no score/collision jumps detected

## Notes

- This analysis uses saved `score_timeseries.csv` files only.
- It does not rerun MWORKS and does not prove physical UGV behavior.
- Use the event times to decide the next visual or state-signal inspection window.
