# Long Task Status Board

> Short operational board for the UGV initial-race long task. Keep this file concise; detailed evidence belongs in `Results/`.

Status: high_score_sprint_active_from_v80_after_v79_v81_v82_v83_v84_v85_v86_v87_v88_v89_v90_v91_v92_v93_v94_v95_v96_v97_v98_rejections; v80 sharp curve speed cap is the current score-leading local wrapper candidate with a Track3 runtime caveat; v78 gap-side screening is diagnostic-only and not a safe direct source-edit gate; v70 active-avoid speed clamp, v71 severe-left steering authority, v72 narrow opposing path authority, v73 curve-short lookahead, v75 moderate opposing-path neutralization, v76 front-clear side steer boost, v77 v70 speed clamp on v74, v79 final max-steer clamp, v81 sharp-curve speed cap 0.65, v82 road-edge short lookahead, v83 road-edge recovery, v84 initial-lane y bias, v85 short lateral initial hold, v86 conditional lateral release, v87 front-clear sustained side steer, v88 side-squeeze speed hold, v89 side-squeeze marker/path-neutralization, v90 early brake weight, v91 gap-directed initial steer, v92 front emergency straight hold, v93 emergency path-speed suppression, v94 obstacle-steer conflict attenuation, v95 early front brake marker, v96 severe side initial steer override, v97 narrow left-squeeze initial override, and v98 front-memory left-recovery were rejected as accepted baselines; current mainline is a long algorithm-model score sprint toward the 80-point target, not report polish or packaging, 2026-07-10 CST.

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
| M6 Four-track evaluation / score optimization | high_score_sprint_active_v80_new_best_continue_after_v98_rejected | Codex | baseline `Results/metrics/four_track_summary_20260709_120547.md`; accepted candidate chain through v74 `Results/metrics/four_track_candidate_review_v74_guarded_curve_short_lookahead_20260710.md`; current v80 review `Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md`; v80 design `Docs/Design/unified_obstacle_avoidance_v80_plan_20260710.md`; v80 gate `Results/evidence/controller_deployability_static_check_v80_sharp_curve_speed_cap_20260710.md`; v96 rejection `Results/metrics/track1_track3_candidate_review_v96_severe_side_initial_steer_override_20260710.md`; v97 rejection `Results/metrics/track3_candidate_review_v97_narrow_left_squeeze_initial_override_20260710.md`; v98 rejection `Results/metrics/track3_candidate_review_v98_front_memory_left_recovery_20260710.md`; latest diagnostic input `Results/metrics/signal_window_summary_v80_track3_pose_path_6s_20260710.md`; strategy `Docs/Design/high_score_optimization_strategy_20260709.md`; login recovery `Results/simulations/license_gui_confirm_1s_20260709_after_real_login/` | v80 is current score-leading local wrapper candidate at total `38.0`, superseding v74 `37.6` by improving Track4 from `P=9.2,cR=2` to `P=9.6,cR=1`. Keep the Track3 runtime caveat visible: score variables stay `P=9.2,cR=1,cO=1`, but runtime regresses from v74 clean `T=120.0` to v80 `simulate_failed/T=59.4`. v96 produced a useful Track3 signal but regressed Track1 to `T=4.5`; v97 narrowed the same mechanism and regressed Track3 to `T=32.45,cR=13,cO=1,P=4.4`; v98 gated the negative initial steer behind front-close memory but Track3 stayed `T=43.9,cR=1,cO=1,P=9.2`. Source semantics are restored to v80 and static gate passed. Continue the long score sprint from v80, but do not continue the direct initial-steer override family without a materially different diagnostic. |
| M7 Evidence automation | partial_completed_timeaxis_fix_done | Codex | `Scripts/mworks/ugv_baseline_probe.py`; `Scripts/quality/check_controller_deployability.py`; `Scripts/analysis/summarize_signal_windows.py`; `Scripts/analysis/analyze_ctrlalloc_contributions.py`; `Results/evidence/controller_deployability_static_check_20260709_0222.md`; `Results/evidence/ugv_baseline_probe_manifest_notes_check_20260709_0240.md`; `Results/metrics/signal_window_summary_v48_track3_timeaxis_fix_smoke_20260710.md`; `Results/metrics/ctrlalloc_contribution_analysis_v48_timeaxis_fix_smoke_20260710.md` | Helper exports extra variables, captures errors, and now writes blocker-specific manifest notes instead of bounded-simulation wording when dependency load/check/simulate is not reached; deployability checker passes the source-only high/medium risk gate. Offline MWORKS CSV analysis now binds each signal to its own left-side `Time` column, avoiding duplicate-`Time` misalignment during candidate diagnosis. |
| M8 Report draft | support_paused_while_score_sprint_active | Codex | historical M6 draft `Results/deliverables/report_drafts/initial_race_report_draft_m6_metrics_20260709_123905.docx`; historical v13 draft `Results/deliverables/report_drafts/initial_race_report_draft_v13_metrics_20260709_1535.md`; current v48/post-v69 draft `Results/deliverables/report_drafts/initial_race_report_draft_v48_metrics_20260710.md`; v48/post-v69 DOCX `Results/deliverables/report_drafts/initial_race_report_draft_v48_metrics_20260710.docx`; DOCX QA `Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/QA_NOTE.md`; page render QA `Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/word_com_export_qa/page_render_qa.md`; contact sheet `Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/word_com_export_qa/contact_sheet.png`; trajectory figures `Results/figures/trajectory_event_review_v48_20260710/` | Keep existing report evidence, but do not spend mainline time on report polish while the score sprint is active. Refresh report only after a new accepted score candidate exists or the user explicitly asks. |
| M9 Submission candidate package | support_paused_final_approval_required | Codex + user final approval | historical package `Results/deliverables/submission_candidates/UGV_initial_race_review_candidate_20260709_124115.zip`; current readiness dry-run `Results/deliverables/submission_dry_runs/submission_readiness_post_v69_v48_trajectory_report_20260710.md`; current package plan dry-run `Results/deliverables/submission_dry_runs/submission_candidate_plan_post_v69_v48_trajectory_report_20260710.md` | Do not create more zip packages and do not send final competition email during the score sprint unless the user explicitly asks. |
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
