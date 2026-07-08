# Official Track API Simulation Blocker - 20260708_231430

## Scope

Phase: M6 four-track evaluation.

Official track models tested:

```text
UGV.saidao.saidao1
UGV.saidao.saidao2
UGV.saidao.saidao3
UGV.saidao.saidao4
```

No official track, road, vehicle, sensor, scoring, or example file was edited.

## Official Requirement Found In Source

Each official track source contains the same instruction:

```text
仿真前点击仿真设置-模型翻译-勾选“参数估值以便优化模型”
```

The same note appears in `UGV.Example.Race1` and `UGV.Example.Race2`.

## Attempts

The helper `Scripts/mworks/ugv_baseline_probe.py` was extended to try:

```text
SimulateModelEx
translationEvaluateParametersToReduceModels=True
translationCheckConnection_Strictly=False
compileSolver64=1
algorithm=Dassl
interval=0.05
```

The official deployment PDF was checked for related text. It confirms the
normal GUI simulation-settings route, but the extracted text did not reveal a
second API option beyond simulation settings.

Sysplorer MCP RAG was searched for:

```text
translationEvaluateParametersToReduceModels 参数估值 以便优化模型 SimulateModelEx
```

The matching documentation was about DesignOptMpe parameter estimation, not the
compile option needed for this official-track simulation failure.

## Evidence Table

| Track | CheckModel | SimulateModelEx | Error Class | Evidence |
|---|---|---|---|---|
| `UGV.saidao.saidao1` | ok | failed | Real variables missing equations | `Results/simulations/diagnostic_saidao1_ex_relaxed_1s_20260708_225637/` |
| `UGV.saidao.saidao2` | ok | failed | Real variables missing equations | `Results/simulations/diagnostic_saidao2_ex_relaxed_1s_20260708_231622/` |
| `UGV.saidao.saidao3` | ok | failed | Real variables missing equations | `Results/simulations/diagnostic_saidao3_ex_relaxed_1s_20260708_231646/` |
| `UGV.saidao.saidao4` | ok | failed | Real variables missing equations | `Results/simulations/diagnostic_saidao4_ex_relaxed_1s_20260708_231710/` |

Representative error:

```text
错误(2): 编译器错误(6141): 模型中 Real 类型缺少方程, 如下变量缺少 2 个方程
错误(3005): 编译模型“UGV.saidao.saidao1”失败。
```

The listed variables are under vehicle wheel, force application, and torque
paths, not under the obstacle-avoidance controller file.

## Current Classification

This is an M6 official-track simulation-entry blocker, not a controller-score
failure. Score variables cannot be read for the official tracks because the
models do not enter simulation.

## Next Safe Options

1. Use GUI to verify whether the official checkbox maps to additional hidden
   settings not exposed by the current Python helper.
2. Ask official/MoHub support for the exact API option corresponding to the GUI
   checkbox.
3. Continue report drafting only as blocker-aware evidence; do not claim
   four-track completion until this is resolved.
