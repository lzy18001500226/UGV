# Collision Window Analysis

## Runs

| Label | Runtime | Exit | T/s | cR | cO | P | Events | Evidence |
|---|---|---:|---:|---:|---:|---:|---:|---|
| v48_t1 | `simulate_returned_true` | 0 | 120.0 | 2.0 | 0.0 | 9.2 | 2 | `Results\simulations\controller_v48_opposing_steer_guard_saidao1_120s_20260710` |
| v48_t4 | `simulate_failed` | 2 | 112.4 | 2.0 | 0.0 | 9.2 | 2 | `Results\simulations\controller_v48_opposing_steer_guard_saidao4_120s_20260710` |
| v71_t1 | `simulate_returned_true` | 0 | 120.0 | 1.0 | 0.0 | 9.6 | 1 | `Results\simulations\controller_v71_severe_left_steer_authority_saidao1_120s_20260710` |
| v71_t4 | `simulate_returned_true` | 0 | 120.0 | 2.0 | 1.0 | 8.8 | 3 | `Results\simulations\controller_v71_severe_left_steer_authority_saidao4_120s_20260710` |

## Jump Events

### v48_t1

| Time/s | Changes |
|---:|---|
| 6.55 | cR: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 30.35 | cR: 1.0 -> 2.0 (+1); P: 9.6 -> 9.2 (-0.4) |

### v48_t4

| Time/s | Changes |
|---:|---|
| 4.35 | cR: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 90.15 | cR: 1.0 -> 2.0 (+1); P: 9.6 -> 9.2 (-0.4) |

### v71_t1

| Time/s | Changes |
|---:|---|
| 6.55 | cR: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |

### v71_t4

| Time/s | Changes |
|---:|---|
| 4.35 | cR: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |
| 94.6 | cO: 0.0 -> 1.0 (+1); P: 9.6 -> 9.2 (-0.4) |
| 101.2 | cR: 1.0 -> 2.0 (+1); P: 9.2 -> 8.8 (-0.4) |

## Notes

- This analysis uses saved `score_timeseries.csv` files only.
- It does not rerun MWORKS and does not prove physical UGV behavior.
- Use the event times to decide the next visual or state-signal inspection window.
