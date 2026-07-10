# Long Task Status Board

> Short operational board for the UGV initial-race long task. Keep this file concise; detailed evidence belongs in `Results/`.

Status: v48_opposing_steer_guard_review_ready_new_best_with_runtime_caveat; v14-v44 rejected or no-op, v46-v52/v54-v58/v61-v67 rejected on Track3, v53/v59 rejected on Track1, v60 rejected on Track1/Track3, and v69 lateral hysteresis rejected before source edit; post-v69 sparse-reactive research found no immediate justified source patch, so continue through report/readiness and physical-transfer deliverables while keeping targeted mechanism research open; current report DOCX embeds v48 Track1/Track3 trajectory-event figures and now has 10-page Word/PDF/PNG page-render QA, 2026-07-10 CST.

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
M10 final-race / physical-transfer readiness notes
```

## Phase Board

| Phase | State | Owner | Evidence | Next Action |
|---|---|---|---|---|
| M1 Static model grounding | completed | Codex | `Results/evidence/static_model_grounding_20260708_210142.md` | Done; use source mapping for M2. |
| M2 Baseline runtime | completed_bounded_gate | Codex | `Results/simulations/baseline_20260708_213448/` | Done; load/check/simulate and score variables verified for bounded stopTime=12. |
| M3 Controller design | completed | Codex | `Docs/Design/避障算法设计.md`; `Results/evidence/controller_design_review_20260708_215659.md` | Done; use conservative reactive increment design for M4. |
| M4 Controller implementation | completed_bounded_gate | Codex | `Results/evidence/controller_v1_source_notes_20260708_220257.md`; `Results/simulations/controller_refsysblock_20260708_221000/` | Done; recovered from failed plain algorithm by using valid Sysblock reference structure. |
| M5 One-track tuning | superseded_by_v12_candidate | Codex | `Results/metrics/one_track_tuning_20260708_231430.md`; best v5 run `Results/simulations/controller_v5_front_dwell_2s_race1_120s_20260708_230305/`; weak-track pass `Results/metrics/track1_track3_tuning_pass_20260709_1425.md` | v5 remains the baseline for comparison; v7-v11 were tested and rejected or not accepted. |
| M6 Four-track evaluation | v48_review_ready_new_best_with_runtime_caveat | Codex | baseline `Results/metrics/four_track_summary_20260709_120547.md`; previous accepted candidates `Results/metrics/four_track_summary_v13_side_trigger045_20260709_1535.md` and `Results/metrics/four_track_candidate_review_v45_curvature_speed_regulation_scaled_20260710_0045.md`; v48 review `Results/metrics/four_track_candidate_review_v48_opposing_steer_guard_20260710.md`; v48 design `Docs/Design/unified_obstacle_avoidance_v48_plan_20260710.md`; v48 gate `Results/evidence/controller_deployability_static_check_v48_opposing_steer_guard_20260710.md`; latest evidence/rejected reviews `Results/metrics/trajectory_geometry_review_v48_20260710.md`, `Results/metrics/signal_geometry_window_summary_v48_20260710.md`, `Results/metrics/track1_track3_candidate_review_v60_steering_filter_20260710.md`, `Results/metrics/track3_candidate_review_v61_early_risk_arbitration_20260710.md`, `Results/metrics/track3_candidate_review_v62_front_centered_initial_bypass_20260710.md`, `Results/metrics/track3_candidate_review_v63_early_steer_feedforward_20260710.md`, `Results/metrics/track3_candidate_review_v64_front_clear_side_reentry_20260710.md`, `Results/metrics/track3_candidate_review_v65_front_emergency_hold_20260710.md`, `Results/metrics/track3_candidate_review_v66_road_edge_initial_steer_boost_20260710.md`, `Results/metrics/track3_candidate_review_v67_nearest_distance_input_diagnostic_20260710.md`, post-v67 decision `Results/metrics/post_v67_v68_attribution_decision_20260710.md`, and v69 screening `Results/metrics/lateral_hysteresis_screening_v48_20260710.md`; rejected v14-v44 and v46-v67 reviews under `Results/metrics/`; strategy `Docs/Design/high_score_optimization_strategy_20260709.md`; login recovery `Results/simulations/license_gui_confirm_1s_20260709_after_real_login/` | v48 is current review-ready best: total wrapper score `37.2` vs v45 `36.8`, with Track1 improved to `P=9.2`, `cR=2`, `cO=0`. Runtime caveat: Track2/3/4 retain their recorded `P/cR/cO` values but return `simulate_failed` with result variables and early `T`, so this is not final competition or physical UGV proof. Continue from v48. v58-v67 did not produce comparable score improvement. Post-v67/v68 attribution confirms avoidance is already active at remaining score-loss windows; the direct path-speed arbitration mechanism was already rejected by v51, nearest-distance input was rejected by v67, and lateral left/right hysteresis was rejected by saved-signal screening. Continue through report/readiness and physical-transfer deliverables unless a genuinely different deployable four-scalar mechanism is identified. |
| M7 Evidence automation | partial_completed_timeaxis_fix_done | Codex | `Scripts/mworks/ugv_baseline_probe.py`; `Scripts/quality/check_controller_deployability.py`; `Scripts/analysis/summarize_signal_windows.py`; `Scripts/analysis/analyze_ctrlalloc_contributions.py`; `Results/evidence/controller_deployability_static_check_20260709_0222.md`; `Results/evidence/ugv_baseline_probe_manifest_notes_check_20260709_0240.md`; `Results/metrics/signal_window_summary_v48_track3_timeaxis_fix_smoke_20260710.md`; `Results/metrics/ctrlalloc_contribution_analysis_v48_timeaxis_fix_smoke_20260710.md` | Helper exports extra variables, captures errors, and now writes blocker-specific manifest notes instead of bounded-simulation wording when dependency load/check/simulate is not reached; deployability checker passes the source-only high/medium risk gate. Offline MWORKS CSV analysis now binds each signal to its own left-side `Time` column, avoiding duplicate-`Time` misalignment during candidate diagnosis. |
| M8 Report draft | post_v69_v48_metrics_page_render_qa_review_ready | Codex | historical M6 draft `Results/deliverables/report_drafts/initial_race_report_draft_m6_metrics_20260709_123905.docx`; historical v13 draft `Results/deliverables/report_drafts/initial_race_report_draft_v13_metrics_20260709_1535.md`; current v48/post-v69 draft `Results/deliverables/report_drafts/initial_race_report_draft_v48_metrics_20260710.md`; v48/post-v69 DOCX `Results/deliverables/report_drafts/initial_race_report_draft_v48_metrics_20260710.docx`; DOCX QA `Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/QA_NOTE.md`; page render QA `Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/word_com_export_qa/page_render_qa.md`; contact sheet `Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/word_com_export_qa/contact_sheet.png`; trajectory figures `Results/figures/trajectory_event_review_v48_20260710/`; v48 review `Results/metrics/four_track_candidate_review_v48_opposing_steer_guard_20260710.md`; post-v67 decision `Results/metrics/post_v67_v68_attribution_decision_20260710.md`; v69 screening `Results/metrics/lateral_hysteresis_screening_v48_20260710.md`; sparse-reactive research `References/research/sparse_reactive_obstacle_avoidance_20260710/source_notes.md` | v48 report/readiness refresh now includes v49-v67 rejections, post-v67 attribution, v69 screening, post-v69 sparse-reactive research boundary, embedded Track1/Track3 trajectory-event figures, tracked figure source PNGs, and a 10-page Word/PDF/PNG render QA with no suspected blank pages. It keeps Track2/3/4 terminal-state caveats visible and is not final submission material until user approval. |
| M9 Submission candidate package | post_v69_plan_final_approval_blocked_no_zip_created | Codex + user final approval | historical package `Results/deliverables/submission_candidates/UGV_initial_race_review_candidate_20260709_124115.zip`; current readiness dry-run `Results/deliverables/submission_dry_runs/submission_readiness_post_v69_v48_trajectory_report_20260710.md`; current package plan dry-run `Results/deliverables/submission_dry_runs/submission_candidate_plan_post_v69_v48_trajectory_report_20260710.md` | Current readiness and package-plan dry runs include v48/post-v69 trajectory report evidence, report figure source PNGs, and page-render QA, and block only on `final_submission_approval_missing`; this is expected. No zip was created and no final competition email was sent. |
| M10 Final-race / physical transfer | review_ready_v48_transfer_baseline | Codex | `Docs/Design/final_race_migration_notes.md`; v48 review `Results/metrics/four_track_candidate_review_v48_opposing_steer_guard_20260710.md`; post-v67 attribution `Results/metrics/post_v67_v68_attribution_decision_20260710.md`; v69 screening `Results/metrics/lateral_hysteresis_screening_v48_20260710.md`; deployability gate `Results/evidence/controller_deployability_static_check_v48_reconfirmed_after_v67_20260710.md` | v48 now has a transfer baseline parameter table, exhausted-mechanism list, and final-race/physical retuning order. This is review-ready planning evidence only; it does not claim generated-code artifact, final-race proof, physical UGV success, or final submission approval. Continue long task through report QA, targeted research, or a genuinely new unified mechanism when evidence appears. |

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
- Current accepted M6/v48 metrics are available, but they are not
  final-submission quality scores. Track1/Track3/Track4 still have collision
  or terminal-state weaknesses, so targeted unified-algorithm tuning remains
  active before any final package.

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
- Physical-transfer research and M10 transfer notes have been added so controller tuning stays aligned
  with later real-car robustness instead of only one-track simulation scoring.
  Current reference packs:
  `References/research/physical_ugv_obstacle_avoidance_20260708/`,
  `References/research/robust_physical_ugv_navigation_20260709/`, and
  `References/research/deployable_ugv_avoidance_algorithms_20260709/`.
  Current executable transfer summary:
  `Docs/Design/final_race_migration_notes.md`.
- Controller deployability source-only check now reports
  `ready_for_physical_claim=true`, `high=0`, and `medium=0` after replacing
  reciprocal distance steering terms (`1 / dl`, `1 / dr`) with bounded linear
  steering. This removes the source-level spike risk gate only; it does not
  prove MWORKS runtime, official four-track score, or physical UGV success.
  Evidence: `Results/evidence/controller_deployability_static_check_20260709_0222.md`.
- M8 current DOCX report draft has both structure/content QA and page-render
  QA. Word COM exported the current v48/post-v69 DOCX to a 10-page PDF,
  Poppler rendered all pages to PNG, and the generated contact sheet shows no
  suspected blank pages. Evidence:
  `Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/QA_NOTE.md`
  and `Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/word_com_export_qa/page_render_qa.md`.
- Email send evidence can prove SMTP accepted a notice, but it does not prove
  the user saw it; keep terminal notices in project evidence as well. Latest
  email recheck used the default recipient `1062771286@qq.com` with
  `recipient_explicit=false`, so mailbox visibility must be checked separately
  if the user still sees no mail. Latest notice evidence:
  `Results/evidence/notification_delivery_note_20260709_024813.md`.
- M9 local review-only candidate package is historical audit evidence at `Results/deliverables/submission_candidates/UGV_initial_race_review_candidate_20260709_124115.zip`. The earlier GitHub push blocker was cleared on 2026-07-10: local commits through `73bf87c` were pushed to `origin/main`. Sparse email notice evidence: `C:\Users\HP\Desktop\MoSim\Results\coagent_gateway\email\email_alert_20260709_124542.json`. UGV note: `Results/evidence/notification_delivery_note_20260709_124542.md`.
- Active tuning pass after the user's correction is recorded at `Results/metrics/track1_track3_tuning_pass_20260709_1425.md`. No v7-v11 change is accepted. v12 side-trigger supersedes v5 as the current review-ready candidate; the next work should inspect Track1/Track4 collision windows or trajectory behavior before another controller rewrite.
- v12 side-trigger candidate is now review-ready at `Results/metrics/four_track_summary_v12_side_trigger_20260709_144854.md`. It changes the longitudinal avoid trigger to include `dl <= 0.30` or `dr <= 0.30`, improves total wrapper score from `32.0` to `34.8`, and passes the static deployability checker with `high=0`, `medium=0`. It is not a final optimized competition claim because Track1 remains collision-heavy and Track4 slightly regresses.
- Collision-window evidence is now available at `Results/metrics/v12_collision_window_interpretation_20260709_1520.md`. Track1 early obstacle collisions occur with `flag=0` and side distance around `0.46`, while Track4 later road collisions occur with `flag=1` and very small side distances. Next low-risk candidate is a narrow v13 side-threshold test such as `0.45`, not a broad state-machine rewrite.
- v13 side-trigger 0.45 is now review-ready at `Results/metrics/four_track_summary_v13_side_trigger045_20260709_1535.md`. It improves total wrapper score to `36.4` (`+1.6` vs v12, `+4.4` vs M6 baseline), with Track1 `P=8.8`, Track2 `P=9.6`, Track3 `P=9.2`, and Track4 `P=8.8`. v14-v43 follow-up candidates were tested and rejected; latest closeout is `Results/metrics/track1_candidate_review_v43_decoupled_side_guard_20260710_0022.md`. v31 avoid-release dwell 3 s regressed Track1 badly, v32-v35 front-open braking failed syntax/no-op/no-improvement checks, v36-v38 final steering guards showed Track4 local improvement but Track3 regression, v39 planner-steering attenuation regressed Track4, v40 side-trigger widening had no effect, v41 guarded release regressed Track4, v42 open-side steering regressed Track1, and v43 side-only decoupling regressed Track1. The source was restored to v13 semantics and passed `Results/evidence/controller_deployability_static_check_v13_restored_after_v43_20260710_0022.md`; do not build/send a final submission package without explicit approval.
- v45 curvature-speed regulation is now superseded review evidence at `Results/metrics/four_track_candidate_review_v45_curvature_speed_regulation_scaled_20260710_0045.md`. v44 used the wrong speed scale and was a no-op; v45 corrected the normalized speed cap to `0.75`, improving total wrapper score from v13 `36.4` to `36.8`. Track4 improved from `P=8.8`, `cR=3`, `cO=0` to `P=9.2`, `cR=2`, `cO=0`; Track1/2/3 stayed at v13 score levels. v46 speed-channel 1.2x was rejected on Track3 at `Results/metrics/track3_candidate_review_v46_speed_channel_120pct_20260710.md`; v47 startup speed cap was rejected at `Results/metrics/track3_candidate_review_v47_startup_speed_cap_20260710.md`. Continue from v48 unless later review rejects it. Do not build/send a final submission package without explicit approval.
- v48 opposing-steer guard is now review-ready at `Results/metrics/four_track_candidate_review_v48_opposing_steer_guard_20260710.md`. It attenuates only the opposing path-steering contribution during active reverse obstacle avoidance, improving total wrapper score from v45 `36.8` to `37.2`. Track1 improves from `P=8.8`, `cR=3`, `cO=0` to `P=9.2`, `cR=2`, `cO=0`; Track2/3/4 keep the same recorded `P/cR/cO` score variables but carry an early-terminal `simulate_failed` caveat. v49 broad path-speed attenuation is rejected at `Results/metrics/track3_candidate_review_v49_path_speed_attenuation_20260710.md` because Track3 ended at `T=5.75` with a non-comparable early stop. v50 moderate curve-speed threshold lowering is rejected at `Results/metrics/track3_candidate_review_v50_moderate_curve_speed_20260710.md` because Track3 remained `P=9.2`, `cR=1`, `cO=1` despite a cleaner `simulate_returned_true` runtime. v51 straight brake arbitration is rejected at `Results/metrics/track3_candidate_review_v51_straight_brake_arbitration_20260710.md` because it early-stopped at `T=2.25` with non-comparable `P=10.0`. v52 brake-turn coupling is rejected at `Results/metrics/track3_candidate_review_v52_brake_turn_coupling_20260710.md` because it kept Track3 at `P=9.2`, `cR=1`, `cO=1` and ended much earlier than v48 (`T=8.35`). v53 complete path-steer neutralization is rejected at `Results/metrics/track1_candidate_review_v53_path_conflict_neutralization_20260710.md` because it regressed Track1 to `T=50.55`, `cR=4`, `P=8.4`. v54 path-authority `0.35`, v55 low-speed lookahead floor, v56 speed-filter-only acceleration, and v57 front `safeF` entry are all rejected on Track3 because they kept `P=9.2`, `cR=1`, `cO=1` while shortening the run versus v48. Continue from v48 unless later review rejects it. Do not build/send a final submission package without explicit approval.
- High-score optimization pivot is documented at `Docs/Design/high_score_optimization_strategy_20260709.md` and the latest unified-controller rejection evidence is `Docs/Design/unified_obstacle_avoidance_v41_plan_20260709.md` plus `Results/metrics/track4_candidate_review_v41_guarded_release_20260710_0007.md`. Future candidates must be one track-agnostic algorithm evaluated across all four tracks, not v14-v41 style blind parameter/timing scans or per-track patches.
- The v48 report refresh is replacing old v13 report/readiness pointers with current v48 evidence while preserving old M6/v13 artifacts as historical audit evidence.
- Do not use this board as a history ledger.
- Update only when phase state changes or a review/blocker appears.
- Long details, logs, screenshots, and metrics must stay under `Results/`.
