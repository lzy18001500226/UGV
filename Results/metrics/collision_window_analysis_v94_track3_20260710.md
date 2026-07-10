# Collision Window Analysis

## Runs

| Label | Runtime | Exit | T/s | cR | cO | P | Events | Evidence |
|---|---|---:|---:|---:|---:|---:|---:|---|
| controller_v94_oa_steer_conflict_attenuation_saidao3_120s_20260710 | `simulate_failed` | 2 | 2.4 | 0.0 | 1.0 | 9.6 | 1 | `Results\simulations\controller_v94_oa_steer_conflict_attenuation_saidao3_120s_20260710` |

## Jump Events

### controller_v94_oa_steer_conflict_attenuation_saidao3_120s_20260710

| Time/s | Changes |
|---:|---|
| 1.05 | cO: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |

## Notes

- This analysis uses saved `score_timeseries.csv` files only.
- It does not rerun MWORKS and does not prove physical UGV behavior.
- Use the event times to decide the next visual or state-signal inspection window.
