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
| High-score optimization strategy after rejected v14-v29 attempts | `Docs/Design/high_score_optimization_strategy_20260709.md`; latest review `Results/metrics/track1_track4_candidate_review_v29_side_danger_speed_20260709_2130.md` |
| Report writing | `Docs/Workflows/report_workflow.md` |
| Current v13 submission readiness dry run, no package build | `Scripts/quality/check_submission_readiness.py`; `Scripts/quality/plan_submission_candidate.py`; `Results/deliverables/submission_dry_runs/submission_readiness_v13_20260709_1535.md`; `Results/deliverables/submission_dry_runs/submission_candidate_plan_v13_20260709_1535.md` |
| Historical M6 review candidate package | `Scripts/quality/build_submission_candidate.py`; `Results/deliverables/submission_dry_runs/submission_readiness_20260709_124115.md`; `Results/deliverables/submission_dry_runs/submission_candidate_plan_20260709_124115.md` |
| Controller physical-deployability static check | `Scripts/quality/check_controller_deployability.py`; `Results/evidence/controller_deployability_static_check_20260709_0222.md` |
| Track1 / Track3 weak-track tuning pass | `Results/metrics/track1_track3_tuning_pass_20260709_1425.md` |
| Current controller candidate v12 side trigger | `Results/metrics/four_track_summary_v12_side_trigger_20260709_144854.md`; `Results/evidence/controller_deployability_static_check_v12_side_trigger_postrun_20260709.md` |
| Current controller candidate v13 side trigger 0.45 | `Results/metrics/four_track_summary_v13_side_trigger045_20260709_1535.md`; `Results/evidence/controller_deployability_static_check_v13_side_trigger_045_closeout_20260709.md` |
| Collision and signal-window analysis | `Scripts/analysis/analyze_collision_windows.py`; `Scripts/analysis/summarize_signal_windows.py`; `Results/metrics/v12_collision_window_interpretation_20260709_1520.md` |
| Model source lookup | `Docs/Index/model_index.md` |
| Competition task and scoring | `Docs/Design/赛题.md` |
| Requirements | `Docs/Design/需求.md` |
| Architecture | `Docs/Design/架构.md` |
| Final race / physical UGV migration | `Docs/Design/final_race_migration_notes.md` |

## Current Phase Cursor

Current cursor: v13 report/readiness refresh completed; v14-v29 follow-up attempts rejected; next use `Docs/Design/high_score_optimization_strategy_20260709.md` and validate mechanism candidates only after failure-window diagnosis instead of blind scalar tuning. This is a
cursor for the continuous M1-M9 long task, not a stop point. Update
`Docs/Workflows/long_task_status_board.md` only when phase state changes.

```text
M1-M5 completed or review-ready
M6 wrapper-based four-track metric extraction completed
M8 report draft refreshed with v13 metrics
M9 readiness dry run and local review candidate package are historical audit artifacts; do not rebuild packages unless explicitly requested
Current controller candidate: v13 side trigger 0.45, total wrapper score 36.4
Active weak-track focus after v13: mechanism-based Track1/Track4 road-boundary recovery, then Track3 regression; v29 side-danger speed regulation was tested and rejected as no improvement
```

M1 source grounding is complete at `Results/evidence/static_model_grounding_20260708_210142.md`.
M2 bounded baseline runtime gate is complete at `Results/simulations/baseline_20260708_213448/`.
M3 design is complete at `Docs/Design/避障算法设计.md` and `Results/evidence/controller_design_review_20260708_215659.md`.
M4 bounded controller gate is complete at `Results/simulations/controller_refsysblock_20260708_221000/`.
M5 Race1 tuning is review-ready at `Results/metrics/one_track_tuning_20260708_231430.md`.
M6 wrapper baseline metrics are recorded at `Results/metrics/four_track_summary_20260709_120547.md`.
Current v13 metrics are recorded at `Results/metrics/four_track_summary_v13_side_trigger045_20260709_1535.md`.
The earlier direct-official-track API blocker remains historical evidence at `Results/evidence/official_track_api_simulation_blocker_20260708_231430.md`; current repeatable evaluation uses `UGV.Test.Saidao*Eval` wrappers.
Do not claim optimized final score, physical UGV success, or final submission approval from these review artifacts.
