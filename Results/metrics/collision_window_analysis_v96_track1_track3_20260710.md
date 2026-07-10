# Collision Window Analysis

## Runs

| Label | Runtime | Exit | T/s | cR | cO | P | Events | Evidence |
|---|---|---:|---:|---:|---:|---:|---:|---|
| v96_track3 | `simulate_failed` | 2 | 35.9 | 0.0 | 1.0 | 9.6 | 1 | `Results\simulations\controller_v96_severe_side_initial_steer_override_saidao3_120s_20260710` |
| v96_track1 | `simulate_failed` | 2 | 4.5 | 0.0 | 0.0 | 10.0 | 0 | `Results\simulations\controller_v96_severe_side_initial_steer_override_saidao1_120s_20260710` |

## Jump Events

### v96_track3

| Time/s | Changes |
|---:|---|
| 1.05 | cO: 0.0 -> 1.0 (+1); P: 10.0 -> 9.6 (-0.4) |

### v96_track1

- no score/collision jumps detected

## Notes

- This analysis uses saved `score_timeseries.csv` files only.
- It does not rerun MWORKS and does not prove physical UGV behavior.
- Use the event times to decide the next visual or state-signal inspection window.
