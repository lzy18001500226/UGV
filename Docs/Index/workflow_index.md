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
| Deployable UGV avoidance algorithm research | `References/research/deployable_ugv_avoidance_algorithms_20260709/MANIFEST.md`; `References/research/deployable_ugv_avoidance_algorithms_20260709/source_notes.md` |
| Report writing | `Docs/Workflows/report_workflow.md` |
| Submission readiness dry run | `Scripts/quality/check_submission_readiness.py`; `Results/deliverables/submission_dry_runs/submission_readiness_20260709_0153.md` |
| Controller physical-deployability static check | `Scripts/quality/check_controller_deployability.py`; `Results/evidence/controller_deployability_static_check_20260709_0222.md` |
| Model source lookup | `Docs/Index/model_index.md` |
| Competition task and scoring | `Docs/Design/赛题.md` |
| Requirements | `Docs/Design/需求.md` |
| Architecture | `Docs/Design/架构.md` |
| Final race / physical UGV migration | `Docs/Design/final_race_migration_notes.md` |

## Current Phase Cursor

Current cursor: M6 official-track API simulation blocked. This is a cursor for
the continuous M1-M9 long task, not a stop point. Update
`Docs/Workflows/long_task_status_board.md` only when phase state changes.

```text
M1-M5 completed or review-ready
M6 blocked by official track simulation-entry compile error
next safe work: validate the official parameter-evaluation setting, keep deployable-algorithm research tied to controller changes, or draft/update blocker-aware report
```

M1 source grounding is complete at `Results/evidence/static_model_grounding_20260708_210142.md`.
M2 bounded baseline runtime gate is complete at `Results/simulations/baseline_20260708_213448/`.
M3 design is complete at `Docs/Design/避障算法设计.md` and `Results/evidence/controller_design_review_20260708_215659.md`.
M4 bounded controller gate is complete at `Results/simulations/controller_refsysblock_20260708_221000/`.
M5 Race1 tuning is review-ready at `Results/metrics/one_track_tuning_20260708_231430.md`.
M6 blocker is recorded at `Results/evidence/official_track_api_simulation_blocker_20260708_231430.md`.
Do not claim full-track completion or final score from bounded M2/M4/M5 runs.
