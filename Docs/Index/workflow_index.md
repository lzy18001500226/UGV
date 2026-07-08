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

Run M1 static model grounding from `Docs/Workflows/master_execution_plan.md`. Update `Docs/Workflows/long_task_status_board.md` only when phase state changes.

```text
inspect Race1/Race2, official track files, controller interface,
ControlAllocate, CountPoint, and distance sensors
write Results/evidence/static_model_grounding_<timestamp>.md using experiment_gate.md
```

Then proceed to M2 baseline runtime autonomously unless the user explicitly pauses runtime work.
