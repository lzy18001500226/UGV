# AGENTS.md

> Compact project constitution for Codex / AI assistants working on the 2026 UGV obstacle-avoidance challenge.

This project is independent from `C:\Users\HP\Desktop\MoSim`. Reuse MoSim/MWORKS habits only as reference; do not merge this race into MoSim's UAV/Sunray/UE mainline.

## 0. Start Here

For every new or resumed UGV conversation:

```text
1. AGENTS.md
2. Docs/Workflows/new_conversation_context.md
3. Docs/Index/workflow_index.md
4. Docs/Workflows/master_execution_plan.md for execution scope
5. Topic-specific workflow / design docs only as needed
```

Do not load old MoSim dispatch, visible-thread, ROS1/Sunray, UE, packet, or chat-dump workflows as routine context.

## 1. Hard Boundaries

1. Work inside `C:\Users\HP\Desktop\UGV` unless the user explicitly names an external path and reason.
2. Treat `References/official_materials/` as read-only source evidence.
3. The editable working model copy is `Models/UGV/`.
4. Normal implementation target is `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`.
5. Do not modify official vehicle, road, sensor, scoring, or example systems during normal development:

```text
Models/UGV/Vehicle/
Models/UGV/Road/
Models/UGV/saidao/
Models/UGV/CountPoint/
Models/UGV/Example/
```

6. Do not claim score, lap completion, collision count, report readiness, or submission readiness without saved evidence under `Results/`.
7. Use `Docs/Workflows/master_execution_plan.md` for autonomy, login/activation recovery, email notification, research, blocker, and stop conditions. Do not duplicate those detailed operating rules here.
8. Each completed task should be committed promptly with path-limited Git operations according to `Docs/Workflows/master_execution_plan.md`; do not stage the whole tree with a broad command.
9. Final competition submission email/package send requires explicit user approval.

## 2. Project Goal

Initial race line:

```text
official UGV model
  -> obstacle-avoidance controller in Sysblock-compatible form
  -> four official track simulations
  -> score/time/collision evidence
  -> simulation report
  -> submission candidate package
```

Final race relevance:

```text
MWORKS model validation
  -> generated control code
  -> physical UGV download and tuning
```

## 3. Operating Documents

| Need | Source |
|---|---|
| Startup context | `Docs/Workflows/new_conversation_context.md` |
| Workflow index | `Docs/Index/workflow_index.md` |
| Master execution plan | `Docs/Workflows/master_execution_plan.md` |
| Long-task status board | `Docs/Workflows/long_task_status_board.md` |
| Model source index | `Docs/Index/model_index.md` |
| Competition task and scoring | `Docs/Design/赛题.md` |
| Requirements and deliverables | `Docs/Design/需求.md` |
| System architecture | `Docs/Design/架构.md` |
| MWORKS simulation workflow | `Docs/Workflows/mworks_ugv_simulation_workflow.md` |
| Evidence gate | `Docs/Workflows/experiment_gate.md` |
| Report workflow | `Docs/Workflows/report_workflow.md` |

## 4. Directory Map

| Directory | Purpose |
|---|---|
| `Docs/Design/` | Competition task, requirements, architecture, algorithm design. |
| `Docs/Workflows/` | Repeatable execution procedures, status board, and task plans. |
| `Docs/Index/` | Model, workflow, and evidence indexes. |
| `Models/UGV/` | Working copy of the official UGV Modelica/MWORKS package. |
| `References/official_materials/` | Original PDFs, report template, and official material. |
| `References/research/` | Targeted external reference notes and manifests. |
| `Scripts/` | MWORKS helpers, metrics extraction, quality checks. |
| `Results/` | Reproducible evidence and deliverables. |

## 5. When Uncertain

1. Prefer official competition materials over memory.
2. Prefer local model source over assumptions.
3. Prefer baseline evidence before algorithm claims.
4. Prefer bounded recovery and clear evidence over waiting idly.
5. Prefer a clear blocker over changing contest scope or touching hard no-edit zones.
