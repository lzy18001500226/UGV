# Workflow Index

| Need | Workflow |
|---|---|
| Startup context | `Docs/Workflows/new_conversation_context.md` |
| Master execution plan | `Docs/Workflows/master_execution_plan.md` |
| Long-task status board | `Docs/Workflows/long_task_status_board.md` |
| Initial race task plan | `Docs/Workflows/initial_race_task_plan.md` |
| Load and run MWORKS model | `Docs/Workflows/mworks_ugv_simulation_workflow.md` |
| Experiment evidence gate | `Docs/Workflows/experiment_gate.md` |
| Evidence manifest template | `Docs/Workflows/evidence_manifest_template.md` |
| Research manifest template | `Docs/Workflows/research_manifest_template.md` |
| Report writing | `Docs/Workflows/report_workflow.md` |
| Model source lookup | `Docs/Index/model_index.md` |
| Competition task and scoring | `Docs/Design/赛题.md` |
| Requirements | `Docs/Design/需求.md` |
| Architecture | `Docs/Design/架构.md` |

## Current First Action

Run M3 controller design from `Docs/Workflows/master_execution_plan.md`. Update `Docs/Workflows/long_task_status_board.md` only when phase state changes.

```text
read M1 source evidence and M2 baseline runtime evidence
draft Docs/Design/避障算法设计.md
write Results/evidence/controller_design_review_<timestamp>.md
```

M1 source grounding is complete at `Results/evidence/static_model_grounding_20260708_210142.md`.
M2 bounded baseline runtime gate is complete at `Results/simulations/baseline_20260708_213448/`.
Do not claim full-track completion or final score from the bounded M2 run.
