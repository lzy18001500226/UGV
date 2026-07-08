# Four-Track Summary - 20260708_231430

## Status

Phase M6 is blocked before controller scoring. All four official track models
pass `CheckModel`, but fail `SimulateModelEx` before score variables can be
read.

## Table

| Track | Controller | Completion | time_s | cR | cO | P | Evidence | Notes |
|---|---|---|---:|---:|---:|---:|---|---|
| `UGV.saidao.saidao1` | v5 candidate | blocked_before_simulation | n/a | n/a | n/a | n/a | `Results/simulations/diagnostic_saidao1_ex_relaxed_1s_20260708_225637/` | `CheckModel=ok`, simulation compile fails with missing Real equations. |
| `UGV.saidao.saidao2` | v5 candidate | blocked_before_simulation | n/a | n/a | n/a | n/a | `Results/simulations/diagnostic_saidao2_ex_relaxed_1s_20260708_231622/` | `CheckModel=ok`, simulation compile fails with missing Real equations. |
| `UGV.saidao.saidao3` | v5 candidate | blocked_before_simulation | n/a | n/a | n/a | n/a | `Results/simulations/diagnostic_saidao3_ex_relaxed_1s_20260708_231646/` | `CheckModel=ok`, simulation compile fails with missing Real equations. |
| `UGV.saidao.saidao4` | v5 candidate | blocked_before_simulation | n/a | n/a | n/a | n/a | `Results/simulations/diagnostic_saidao4_ex_relaxed_1s_20260708_231710/` | `CheckModel=ok`, simulation compile fails with missing Real equations. |

## Interpretation

This table does not claim the v5 controller failed the official tracks. It
records that the official track simulation entry itself is blocked through the
current API route.

See:

```text
Results/evidence/official_track_api_simulation_blocker_20260708_231430.md
```
