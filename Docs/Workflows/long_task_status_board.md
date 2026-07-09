# Long Task Status Board

> Short operational board for the UGV initial-race long task. Keep this file concise; detailed evidence belongs in `Results/`.

Status: v13_side_trigger045_review_ready_candidate; v14-v29 candidates rejected; high-score optimization pivot is now research-driven mechanism validation, not blind scalar tuning, 2026-07-09 CST.

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
| M5 One-track tuning | superseded_by_v12_candidate | Codex | `Results/metrics/one_track_tuning_20260708_231430.md`; best v5 run `Results/simulations/controller_v5_front_dwell_2s_race1_120s_20260708_230305/`; weak-track pass `Results/metrics/track1_track3_tuning_pass_20260709_1425.md` | v5 remains the baseline for comparison; v7-v11 were tested and rejected or not accepted. |
| M6 Four-track evaluation | high_score_mechanism_pivot | Codex | baseline `Results/metrics/four_track_summary_20260709_120547.md`; accepted candidate `Results/metrics/four_track_summary_v13_side_trigger045_20260709_1535.md`; rejected v14-v29 reviews under `Results/metrics/`; latest closeout `Results/metrics/track1_track4_candidate_review_v29_side_danger_speed_20260709_2130.md`; strategy `Docs/Design/high_score_optimization_strategy_20260709.md`; login recovery `Results/simulations/license_gui_confirm_1s_20260709_after_real_login/` | Keep v13 as current accepted controller. Next candidate must follow strategy: failure-window diagnosis -> mechanism hypothesis -> static gate -> target-track run -> regression; do not continue blind scalar tuning. |
| M7 Evidence automation | partial_completed | Codex | `Scripts/mworks/ugv_baseline_probe.py`; `Scripts/quality/check_controller_deployability.py`; `Results/evidence/controller_deployability_static_check_20260709_0222.md`; `Results/evidence/ugv_baseline_probe_manifest_notes_check_20260709_0240.md` | Helper exports extra variables, captures errors, and now writes blocker-specific manifest notes instead of bounded-simulation wording when dependency load/check/simulate is not reached; deployability checker passes the source-only high/medium risk gate. |
| M8 Report draft | v13_metrics_refreshed_review_ready | Codex | historical M6 draft `Results/deliverables/report_drafts/initial_race_report_draft_m6_metrics_20260709_123905.docx`; current v13 draft `Results/deliverables/report_drafts/initial_race_report_draft_v13_metrics_20260709_1535.md`; v13 DOCX `Results/deliverables/report_drafts/initial_race_report_draft_v13_metrics_20260709_1535.docx`; QA note `Results/deliverables/report_drafts/render_check_v13_20260709_1535/QA_NOTE.md`; v13 summary `Results/metrics/four_track_summary_v13_side_trigger045_20260709_1535.md` | v13 report/readiness refresh is review-ready. It is not final submission material until user approval. |
| M9 Submission candidate package | historical_review_candidate_ready_not_active_cursor | Codex + user final approval | `Results/deliverables/submission_dry_runs/submission_readiness_20260709_124115.md`; `Results/deliverables/submission_dry_runs/submission_candidate_plan_20260709_124115.md`; `Results/deliverables/submission_candidates/UGV_initial_race_review_candidate_20260709_124115.zip`; `Results/deliverables/submission_candidates/UGV_initial_race_review_candidate_20260709_124115_manifest.md` | Historical audit artifact only. Do not create another zip or send final competition package unless explicitly approved. Continue engineering on Track 1/3 tuning. |

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
- M9 local review-only candidate package is historical audit evidence at `Results/deliverables/submission_candidates/UGV_initial_race_review_candidate_20260709_124115.zip`. Local commit is `407721a`. Push to GitHub failed with HTTPS connection reset; retry push later, but do not treat this as the engineering stop condition. Sparse email notice evidence: `C:\Users\HP\Desktop\MoSim\Results\coagent_gateway\email\email_alert_20260709_124542.json`. UGV note: `Results/evidence/notification_delivery_note_20260709_124542.md`.
- Active tuning pass after the user's correction is recorded at `Results/metrics/track1_track3_tuning_pass_20260709_1425.md`. No v7-v11 change is accepted. v12 side-trigger supersedes v5 as the current review-ready candidate; the next work should inspect Track1/Track4 collision windows or trajectory behavior before another controller rewrite.
- v12 side-trigger candidate is now review-ready at `Results/metrics/four_track_summary_v12_side_trigger_20260709_144854.md`. It changes the longitudinal avoid trigger to include `dl <= 0.30` or `dr <= 0.30`, improves total wrapper score from `32.0` to `34.8`, and passes the static deployability checker with `high=0`, `medium=0`. It is not a final optimized competition claim because Track1 remains collision-heavy and Track4 slightly regresses.
- Collision-window evidence is now available at `Results/metrics/v12_collision_window_interpretation_20260709_1520.md`. Track1 early obstacle collisions occur with `flag=0` and side distance around `0.46`, while Track4 later road collisions occur with `flag=1` and very small side distances. Next low-risk candidate is a narrow v13 side-threshold test such as `0.45`, not a broad state-machine rewrite.
- v13 side-trigger 0.45 is now review-ready at `Results/metrics/four_track_summary_v13_side_trigger045_20260709_1535.md`. It improves total wrapper score to `36.4` (`+1.6` vs v12, `+4.4` vs M6 baseline), with Track1 `P=8.8`, Track2 `P=9.6`, Track3 `P=9.2`, and Track4 `P=8.8`. v14-v29 follow-up candidates were tested and rejected; latest closeout is `Results/metrics/track1_track4_candidate_review_v29_side_danger_speed_20260709_2130.md`. v29 side-danger speed regulation passed the static source gate and ran Track1/Track4, but both stayed at `P=8.8`, `cR=3`, `cO=0`, so it is rejected as no improvement. The source was restored to v13 semantics and passed `Results/evidence/controller_deployability_static_check_v13_restored_after_v29_20260709_2130.md`; do not build/send a final submission package without explicit approval.
- High-score optimization pivot is documented at `Docs/Design/high_score_optimization_strategy_20260709.md`. Future candidates must be mechanism-led and evidence-backed, not v14-v29 style blind parameter scans.
- The v13 report refresh is replacing old M6 report/readiness pointers with v13 evidence while preserving old M6 artifacts as historical audit evidence.
- Do not use this board as a history ledger.
- Update only when phase state changes or a review/blocker appears.
- Long details, logs, screenshots, and metrics must stay under `Results/`.
