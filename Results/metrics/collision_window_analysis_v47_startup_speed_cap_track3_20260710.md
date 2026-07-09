# Collision Window Analysis

## Runs

| Label | Runtime | Exit | T/s | cR | cO | P | Events | Evidence |
|---|---|---:|---:|---:|---:|---:|---:|---|
| v47_track3 | `simulate_returned_true` | 0 | 120.0 | 1.0 | 1.0 | 9.2 | 2 | `Results\simulations\controller_v47_startup_speed_cap_saidao3_120s_20260710` |

## Jump Events

### v47_track3

| Time/s | Changes |
|---:|---|
| 1.2 | cO: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 6.15 | cR: 0.0 -> 1.0 (+1); P: 9.6 -> 9.2 (-0.4) |

## Notes

- This analysis uses saved `score_timeseries.csv` files only.
- It does not rerun MWORKS and does not prove physical UGV behavior.
- Use the event times to decide the next visual or state-signal inspection window.
