# New Conversation Context

> Compact startup context for `C:\Users\HP\Desktop\UGV`.

Status: M9 review candidate zip ready; final approval still required, 2026-07-09 CST.

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

Current phase cursor: `final approval or optional Track 1/3 tuning after M9 review candidate zip`.

The cursor is not a stopping rule. This project should keep advancing through
the competition task tree after each phase commit/push unless a hard blocker or
final submission approval point is reached.

Latest runtime evidence:

```text
Results/simulations/baseline_20260708_213448/
Results/simulations/controller_refsysblock_20260708_221000/
Results/simulations/controller_v5_front_dwell_2s_race1_120s_20260708_230305/
Results/evidence/official_track_api_simulation_blocker_20260708_231430.md
Results/simulations/license_gui_confirm_1s_20260709_after_real_login/
Results/metrics/four_track_summary_20260709_120547.md
```

The M2 gate confirms baseline MWORKS Sysplorer load/check/simulate for
`UGV.Example.Race1` with bounded `stopTime=12`. The M4 gate confirms a runnable
Sysblock controller structure with bounded `stopTime=12`. Neither gate claims
full-track completion or final competition score.

MWORKS/Sysplorer GUI or MCP operations are expected in execution phases. Handle login/license/activation recovery according to `master_execution_plan.md`; final competition submission email still requires explicit user approval.

For `L5104-B0`, do not stop after seeing the text `登录失败，请检查网络后重试`.
Follow `Docs/Workflows/mworks_ugv_simulation_workflow.md`: click the real
Sysplorer login button, enter the approved in-memory credentials, activate in
`帮助 -> 使用许可`, then prove recovery with a 1 s API probe. Latest successful
probe:

```text
Results/simulations/license_gui_confirm_1s_20260709_after_real_login/
```

Current controller candidate is v5: only the avoid-to-cruise dwell changed from
1 s to 2 s. Do not re-apply rejected v2/v3/v4/v6 changes unless a new
diagnostic reason exists.

Current M6 four-track wrapper metrics:

```text
Track1 Saidao1Eval: T=86.9, cR=4, cO=3, P=7.2
Track2 Saidao2Eval: T=101.8, cR=3, cO=1, P=8.4
Track3 Saidao3Eval: T=50.4, cR=2, cO=5, P=7.2
Track4 Saidao4Eval: T=47.2, cR=2, cO=0, P=9.2
```

The final 120 s runs return `simulate_failed` with `exit_state=2`, but the
enhanced probe reads `T/cR/cO/P` and exports score timeseries after the model
terminal state. Treat this as usable review evidence, not as an optimized final
competition result.
Current M8/M9 review artifacts:

```text
Results/deliverables/report_drafts/initial_race_report_draft_blocker_aware_20260709.md
Results/deliverables/report_drafts/initial_race_report_draft_m6_metrics_20260709_123905.docx
Results/deliverables/submission_dry_runs/submission_readiness_20260709_124115.md
Results/deliverables/submission_dry_runs/submission_candidate_plan_20260709_124115.md
```

`check_submission_readiness.py` currently blocks only on `final_submission_approval_missing` when run without final approval. A local review-only candidate archive may be built for user audit, but final competition email/package sending still requires explicit user approval.
Latest local review-only package:

`	ext
Results/deliverables/submission_candidates/UGV_initial_race_review_candidate_20260709_124115.zip
Results/deliverables/submission_candidates/UGV_initial_race_review_candidate_20260709_124115_manifest.md
`

This package is for user audit only. It does not imply final submission approval and was not sent to the competition address.
