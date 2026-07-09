# Four-Track Evaluation Summary - 20260709_120547

## Scope

Phase: M6 four-track evaluation after MWORKS login/license recovery.

Evaluation route:

```text
UGV.Test.Saidao1Eval
UGV.Test.Saidao2Eval
UGV.Test.Saidao3Eval
UGV.Test.Saidao4Eval
```

These generated wrappers preserve official `Models/UGV/saidao/` source
geometry and add the obstacle-controller wiring needed for API evaluation. The
official `Models/UGV/saidao/` source files were not edited.

Controller version:

```text
controller_v5_bounded_linear_deployability
```

Runtime:

```text
MWORKS Sysplorer 2026a Python API
SimulateModelEx
stopTime=120
compileOptions=0
translationCheckConnection_Strictly=false
```

## Result Table

| Track | Model | Runtime status | Exit state | T/s | Road collisions cR | Obstacle collisions cO | Score P | Evidence |
|---|---|---|---:|---:|---:|---:|---:|---|
| 1 | `UGV.Test.Saidao1Eval` | `simulate_failed` with result variables readable | 2 | 86.9 | 4 | 3 | 7.2 | `Results/simulations/eval_saidao1_connected_120s_final_20260709_120547/` |
| 2 | `UGV.Test.Saidao2Eval` | `simulate_failed` with result variables readable | 2 | 101.8 | 3 | 1 | 8.4 | `Results/simulations/eval_saidao2_connected_120s_final_20260709_120547/` |
| 3 | `UGV.Test.Saidao3Eval` | `simulate_failed` with result variables readable | 2 | 50.4 | 2 | 5 | 7.2 | `Results/simulations/eval_saidao3_connected_120s_final_20260709_120547/` |
| 4 | `UGV.Test.Saidao4Eval` | `simulate_failed` with result variables readable | 2 | 47.2 | 2 | 0 | 9.2 | `Results/simulations/eval_saidao4_connected_120s_final_20260709_120547/` |

## Interpretation

- The 120 s command returns `simulate_failed` for all four tracks, but the
  enhanced probe can still read final result variables and export score
  timeseries after the simulation stops.
- `exit_state=2` plus readable `T/cR/cO/P` is treated here as an assertion or
  model-stop terminal state with usable metrics, not as a missing-evidence
  runtime failure.
- The current controller completes all four wrapper evaluation runs with
  score-variable evidence, but the collision counts show that the controller is
  not yet a strong competition candidate.
- Track 3 is the weakest result (`cO=5`, `P=7.2`), followed by Track 1
  (`cR=4`, `cO=3`, `P=7.2`). Track 4 is the best current result (`P=9.2`).

## Supporting Diagnostics

Short gates confirmed the wrapper route before the final 120 s run:

```text
Results/simulations/eval_connected_10s_summary_20260709_114542.json
Results/simulations/eval_connected_60s_summary_20260709_114848.json
Results/simulations/eval_connected_60s_postfalse_summary_20260709_120308.json
Results/simulations/eval_connected_120s_final_summary_20260709_120547.json
```

The `postfalse` diagnostic confirmed that `SimulateModelEx=false` can still
leave readable result variables and exported score timeseries.

## Remaining Work

1. Use this M6 evidence to update the report draft and submission dry-run.
2. Consider targeted controller tuning for Track 1 and Track 3 before final
   submission candidate packaging.
3. Keep the official no-edit zones unchanged.
