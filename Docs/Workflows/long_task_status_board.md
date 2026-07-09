# Long Task Status Board

> Short operational board for the UGV initial-race long task. Keep this file concise; detailed evidence belongs in `Results/`.

Status: M9_review_candidate_zip_ready; final submission approval still missing, 2026-07-09 CST.

## Current Long Task

```text
UGV initial-race M1-M9 autonomous loop:
M1 static model grounding
M2 baseline runtime
M3 controller design
M4 controller implementation
M5 one-track tuning
M6 four-track evaluation
M7 evidence automation as needed
M8 report draft
M9 submission candidate package, without final send
```

## Phase Board

| Phase | State | Owner | Evidence | Next Action |
|---|---|---|---|---|
| M1 Static model grounding | completed | Codex | `Results/evidence/static_model_grounding_20260708_210142.md` | Done; use source mapping for M2. |
| M2 Baseline runtime | completed_bounded_gate | Codex | `Results/simulations/baseline_20260708_213448/` | Done; load/check/simulate and score variables verified for bounded stopTime=12. |
| M3 Controller design | completed | Codex | `Docs/Design/避障算法设计.md`; `Results/evidence/controller_design_review_20260708_215659.md` | Done; use conservative reactive increment design for M4. |
| M4 Controller implementation | completed_bounded_gate | Codex | `Results/evidence/controller_v1_source_notes_20260708_220257.md`; `Results/simulations/controller_refsysblock_20260708_221000/` | Done; recovered from failed plain algorithm by using valid Sysblock reference structure. |
| M5 One-track tuning | review_ready_candidate | Codex | `Results/metrics/one_track_tuning_20260708_231430.md`; best run `Results/simulations/controller_v5_front_dwell_2s_race1_120s_20260708_230305/` | Use v5 as current Race1 candidate; do not keep v6. |
| M6 Four-track evaluation | completed_wrapper_metrics_review_ready | Codex | `Results/metrics/four_track_summary_20260709_120547.md`; final run folders `Results/simulations/eval_saidao*_connected_120s_final_20260709_120547/`; login recovery `Results/simulations/license_gui_confirm_1s_20260709_after_real_login/` | Done for review evidence. Track 1/3 tuning remains valuable, but M6 no longer blocks M8/M9 review package preparation. |
| M7 Evidence automation | partial_completed | Codex | `Scripts/mworks/ugv_baseline_probe.py`; `Scripts/quality/check_controller_deployability.py`; `Results/evidence/controller_deployability_static_check_20260709_0222.md`; `Results/evidence/ugv_baseline_probe_manifest_notes_check_20260709_0240.md` | Helper exports extra variables, captures errors, and now writes blocker-specific manifest notes instead of bounded-simulation wording when dependency load/check/simulate is not reached; deployability checker passes the source-only high/medium risk gate. |
| M8 Report draft | m6_metrics_refreshed_review_ready | Codex | `Results/deliverables/report_drafts/initial_race_report_draft_blocker_aware_20260709.md`; `Results/deliverables/report_drafts/initial_race_report_draft_m6_metrics_20260709_123905.docx`; `Results/deliverables/report_drafts/render_check_20260709_0118/QA_NOTE.md`; `Results/metrics/four_track_summary_20260709_120547.md` | Review draft now includes M6 four-track wrapper metrics. It is not final submission material until user approval and any optional Track 1/3 tuning decision. |
| M9 Submission candidate package | review_candidate_zip_ready | Codex + user final approval | `Results/deliverables/submission_dry_runs/submission_readiness_20260709_124115.md`; `Results/deliverables/submission_dry_runs/submission_candidate_plan_20260709_124115.md`; `Results/deliverables/submission_candidates/UGV_initial_race_review_candidate_20260709_124115.zip`; `Results/deliverables/submission_candidates/UGV_initial_race_review_candidate_20260709_124115_manifest.md` | Local review-only candidate zip is ready for user audit. Readiness still blocks only on final submission approval; do not send final competition email/package until explicitly approved. |

## Blockers

- Official four-track API simulation blocker: `UGV.saidao.saidao1` through
  `UGV.saidao.saidao4` pass `CheckModel` but fail `SimulateModelEx` at compile
  time with Real variables missing equations under vehicle wheel/force
  application components. Evidence:
  `Results/evidence/official_track_api_simulation_blocker_20260708_231430.md`.
- MWORKS login/license recovery is verified by the real Sysplorer login button,
  `帮助 -> 使用许可` activation, and a successful 1 s API probe:
  `Results/simulations/license_gui_confirm_1s_20260709_after_real_login/`.
  If `L5104-B0` reappears, follow
  `Docs/Workflows/mworks_ugv_simulation_workflow.md` and do not treat
  `登录失败，请检查网络后重试` as a network blocker before retrying the real
  login/activation flow.
- Direct official `UGV.saidao.saidao1` through `saidao4` entries are source
  geometry/scoring entries without the obstacle controller wiring needed for
  current API evaluation. Use generated `UGV.Test.Saidao*Eval` wrappers for M6
  controller evaluation unless a later source audit changes that route.
- Current M6 metrics are available, but they are not final-submission quality
  scores. Track 1 and Track 3 both score `P=7.2`; targeted tuning is still
  valuable before a final package.

## Review Notes

- M1 is source/static only. It does not claim MWORKS load, translate, simulate, lap completion, score, or GUI health.
- M2 confirms bounded runtime load/check/simulate for `UGV.Example.Race1`; it does not claim full-track completion or final competition score.
- M4 confirms a first runnable Sysblock controller structure with bounded `stopTime=12` metrics `T=12`, `cR=0`, `cO=0`, `P=10`; it does not claim full-track completion.
- M5 Race1 candidate v5 changes only the front avoid-to-cruise dwell from 1 s
  to 2 s and improves 120 s Race1 from `P=8.4` to `P=8.8`.
- M6 now has four-track wrapper metrics from 120 s runs. All final runs return
  `simulate_failed` with `exit_state=2`, but the enhanced probe reads
  `T/cR/cO/P` and exports score timeseries after the model terminal state. Use
  `Results/metrics/four_track_summary_20260709_120547.md` as the current
  four-track evidence. This is review-ready evidence, not a claim that the
  controller is optimal.
- Physical-transfer research has been added so controller tuning stays aligned
  with later real-car robustness instead of only one-track simulation scoring.
  Current reference packs:
  `References/research/physical_ugv_obstacle_avoidance_20260708/`,
  `References/research/robust_physical_ugv_navigation_20260709/`, and
  `References/research/deployable_ugv_avoidance_algorithms_20260709/`.
- Controller deployability source-only check now reports
  `ready_for_physical_claim=true`, `high=0`, and `medium=0` after replacing
  reciprocal distance steering terms (`1 / dl`, `1 / dr`) with bounded linear
  steering. This removes the source-level spike risk gate only; it does not
  prove MWORKS runtime, official four-track score, or physical UGV success.
  Evidence: `Results/evidence/controller_deployability_static_check_20260709_0222.md`.
- M8 DOCX report draft was regenerated from the Markdown source using the
  official report template as reference. Render QA produced four page PNGs and
  a contact sheet with no blank tail page, obvious overlap, or obvious
  clipping. Evidence:
  `Results/deliverables/report_drafts/render_check_20260709_0118/QA_NOTE.md`.
- Email send evidence can prove SMTP accepted a notice, but it does not prove
  the user saw it; keep terminal notices in project evidence as well. Latest
  email recheck used the default recipient `1062771286@qq.com` with
  `recipient_explicit=false`, so mailbox visibility must be checked separately
  if the user still sees no mail. Latest notice evidence:
  `Results/evidence/notification_delivery_note_20260709_024813.md`.
- Do not use this board as a history ledger.
- Update only when phase state changes or a review/blocker appears.
- Long details, logs, screenshots, and metrics must stay under `Results/`.
