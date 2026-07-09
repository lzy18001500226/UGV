# Collision Window Analysis

## Runs

| Label | Runtime | Exit | T/s | cR | cO | P | Events | Evidence |
|---|---|---:|---:|---:|---:|---:|---:|---|
| v48_track3 | `simulate_failed` | 2 | 112.45 | 1.0 | 1.0 | 9.2 | 2 | `Results\simulations\controller_v48_opposing_steer_guard_saidao3_120s_20260710` |
| v58_track3 | `simulate_failed` | 2 | 38.800000000000004 | 0.0 | 3.0 | 8.8 | 3 | `Results\simulations\controller_v58_reactive_gap_initial_bypass_saidao3_120s_20260710` |

## Jump Events

### v48_track3

| Time/s | Changes |
|---:|---|
| 1.05 | cO: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 4.85 | cR: 0.0 -> 1.0 (+1); P: 9.6 -> 9.2 (-0.4) |

### v58_track3

| Time/s | Changes |
|---:|---|
| 1.05 | cO: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 6.15 | cO: 1.0 -> 2.0 (+1); P: 9.6 -> 9.2 (-0.4) |
| 18.0 | cO: 2.0 -> 3.0 (+1); P: 9.2 -> 8.8 (-0.4) |

## Notes

- This analysis uses saved `score_timeseries.csv` files only.
- It does not rerun MWORKS and does not prove physical UGV behavior.
- Use the event times to decide the next visual or state-signal inspection window.
