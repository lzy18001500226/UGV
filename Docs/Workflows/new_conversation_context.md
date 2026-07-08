# New Conversation Context

> Compact startup context for `C:\Users\HP\Desktop\UGV`.

Status: M5 one-track tuning in progress, 2026-07-08 CST.

## 0. Startup Chain

```text
1. AGENTS.md
2. Docs/Workflows/new_conversation_context.md
3. Docs/Index/workflow_index.md
4. Docs/Workflows/master_execution_plan.md
5. Docs/Workflows/long_task_status_board.md when running or resuming long work
6. Topic-specific design/workflow docs only as needed
```

This is a standalone MWORKS/Sysplorer/Sysblock UGV obstacle-avoidance project. It is not MoSim's UAV/ROS1/Sunray/UE mainline.

## 1. Current Goal

```text
load official UGV model
  -> run baseline official examples
  -> implement/tune obstacle avoidance controller
  -> run four official tracks
  -> collect time/collision/score evidence
  -> write simulation report
```

## 2. Current Scope

Normal implementation target:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Hard no-edit zones during normal development:

```text
Models/UGV/Vehicle/
Models/UGV/Road/
Models/UGV/saidao/
Models/UGV/CountPoint/
Models/UGV/Example/
References/official_materials/
```

## 3. Current Long Task

Follow `Docs/Workflows/master_execution_plan.md` and status in `Docs/Workflows/long_task_status_board.md`.

Current phase cursor: `M5 one-track tuning in progress`.

The cursor is not a stopping rule. This project should keep advancing through
the competition task tree after each phase commit/push unless a hard blocker or
final submission approval point is reached.

Latest runtime evidence:

```text
Results/simulations/baseline_20260708_213448/
Results/simulations/controller_refsysblock_20260708_221000/
```

The M2 gate confirms baseline MWORKS Sysplorer load/check/simulate for
`UGV.Example.Race1` with bounded `stopTime=12`. The M4 gate confirms a runnable
Sysblock controller structure with bounded `stopTime=12`. Neither gate claims
full-track completion or final competition score.

MWORKS/Sysplorer GUI or MCP operations are expected in execution phases. Handle login/license/activation recovery according to `master_execution_plan.md`; final competition submission email still requires explicit user approval.
