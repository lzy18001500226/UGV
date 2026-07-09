# Collision Window Analysis

## Runs

| Label | Runtime | Exit | T/s | cR | cO | P | Events | Evidence |
|---|---|---:|---:|---:|---:|---:|---:|---|
| v48_track1 | `simulate_returned_true` | 0 | 120.0 | 2.0 | 0.0 | 9.2 | 2 | `Results\simulations\controller_v48_opposing_steer_guard_saidao1_120s_20260710` |
| v53_track1 | `simulate_failed` | 2 | 50.550000000000004 | 4.0 | 0.0 | 8.4 | 4 | `Results\simulations\controller_v53_path_conflict_neutralization_saidao1_120s_20260710` |

## Jump Events

### v48_track1

| Time/s | Changes |
|---:|---|
| 6.55 | cR: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 30.35 | cR: 1.0 -> 2.0 (+1); P: 9.6 -> 9.2 (-0.4) |

### v53_track1

| Time/s | Changes |
|---:|---|
| 6.55 | cR: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 25.2 | cR: 1.0 -> 2.0 (+1); P: 9.6 -> 9.2 (-0.4) |
| 40.5 | cR: 2.0 -> 3.0 (+1); P: 9.2 -> 8.8 (-0.4) |
| 45.05 | cR: 3.0 -> 4.0 (+1); P: 8.8 -> 8.4 (-0.4) |

## Notes

- This analysis uses saved `score_timeseries.csv` files only.
- It does not rerun MWORKS and does not prove physical UGV behavior.
- Use the event times to decide the next visual or state-signal inspection window.
