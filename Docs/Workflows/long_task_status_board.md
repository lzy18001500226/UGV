# Long Task Status Board

> Short operational board for the UGV initial-race long task. Keep this file concise; detailed evidence belongs in `Results/`.

Status: completion-first optimization from accepted v148. Tracks 1, 2, and 4 have verified official finishes; Track3 remains the only completion blocker at `T=21.1,cR=1,cO=1,P=9.2`, path index 36. The official origin-return gate remains the first acceptance criterion: `SimulateModel=false`, `T>10`, and `distanceSensor1.d<0.02` at termination. A fixed stop horizon is not a finish. v180/v182 produced the first saved Track3 official finishes, but each regressed an existing finished track; v183 preserved 120 s progress on Tracks 1/3 but Track2 stopped at `T=28.55`. Exact v148 source semantics are restored, 2026-07-12 CST.

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
| M6 Four-track completion / score optimization | active_3_of_4_finished_v148 | Codex | `Results/metrics/four_track_completion_review_v148_20260712.md`; `Results/metrics/candidate_batch_v180_v183_review_20260712.md` | Keep exact v148. Track3 finish remains the hard gate. v180-v183 prove Track3 can finish, but endpoint perturbation is numerically fragile and open-side recovery still loses Track2. Next work must improve deterministic road-boundary margin before four-track expansion. |
| M7 Evidence automation | partial_completed_timeaxis_fix_done | Codex | `Scripts/mworks/ugv_baseline_probe.py`; `Scripts/quality/check_controller_deployability.py`; `Scripts/analysis/summarize_signal_windows.py`; `Scripts/analysis/analyze_ctrlalloc_contributions.py`; `Results/evidence/controller_deployability_static_check_20260709_0222.md`; `Results/evidence/ugv_baseline_probe_manifest_notes_check_20260709_0240.md`; `Results/metrics/signal_window_summary_v48_track3_timeaxis_fix_smoke_20260710.md`; `Results/metrics/ctrlalloc_contribution_analysis_v48_timeaxis_fix_smoke_20260710.md` | Helper exports extra variables, captures errors, and now writes blocker-specific manifest notes instead of bounded-simulation wording when dependency load/check/simulate is not reached; deployability checker passes the source-only high/medium risk gate. Offline MWORKS CSV analysis now binds each signal to its own left-side `Time` column, avoiding duplicate-`Time` misalignment during candidate diagnosis. |
| M8 Report draft | support_paused_while_score_sprint_active | Codex | historical M6 draft `Results/deliverables/report_drafts/initial_race_report_draft_m6_metrics_20260709_123905.docx`; historical v13 draft `Results/deliverables/report_drafts/initial_race_report_draft_v13_metrics_20260709_1535.md`; current v48/post-v69 draft `Results/deliverables/report_drafts/initial_race_report_draft_v48_metrics_20260710.md`; v48/post-v69 DOCX `Results/deliverables/report_drafts/initial_race_report_draft_v48_metrics_20260710.docx`; DOCX QA `Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/QA_NOTE.md`; page render QA `Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/word_com_export_qa/page_render_qa.md`; contact sheet `Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/word_com_export_qa/contact_sheet.png`; trajectory figures `Results/figures/trajectory_event_review_v48_20260710/` | Keep existing report evidence, but do not spend mainline time on report polish while the score sprint is active. Refresh report only after a new accepted score candidate exists or the user explicitly asks. |
| M9 Submission candidate package | support_paused_final_approval_required | Codex + user final approval | historical package `Results/deliverables/submission_candidates/UGV_initial_race_review_candidate_20260709_124115.zip`; current readiness dry-run `Results/deliverables/submission_dry_runs/submission_readiness_post_v69_v48_trajectory_report_20260710.md`; current package plan dry-run `Results/deliverables/submission_dry_runs/submission_candidate_plan_post_v69_v48_trajectory_report_20260710.md` | Do not create more zip packages and do not send final competition email during the score sprint unless the user explicitly asks. |
| M10 Final-race / physical transfer | review_ready_v48_transfer_baseline | Codex | `Docs/Design/final_race_migration_notes.md`; v48 review `Results/metrics/four_track_candidate_review_v48_opposing_steer_guard_20260710.md`; post-v67 attribution `Results/metrics/post_v67_v68_attribution_decision_20260710.md`; v69 screening `Results/metrics/lateral_hysteresis_screening_v48_20260710.md`; deployability gate `Results/evidence/controller_deployability_static_check_v48_reconfirmed_after_v67_20260710.md` | v48 now has a transfer baseline parameter table, exhausted-mechanism list, and final-race/physical retuning order. This is review-ready planning evidence only; it does not claim generated-code artifact, final-race proof, physical UGV success, or final submission approval. Continue long task through report QA, targeted research, or a genuinely new unified mechanism when evidence appears. |

## Blockers

- The former `L5104-B0` gate is not current: the `-gui` MWORKS Python lane has
  since passed 1 s translation/simulation gates and produced v117-v119 target
  runs. Keep the old incident only as historical recovery evidence.

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
- Current runtime-channel blocker is recovered: after v107/v108 candidate
  timeouts, restored v80 Track3 and official Race1 probes initially timed out
  with only empty `native_result`, but the recovered route now passes official
  `UGV.Example.Race1` 1 s and restored v80 `UGV.Test.Saidao3Eval` 1 s probes
  with readable `T/cR/cO/P`; the restored v80 Track3 120 s recheck reproduces
  the known v80 caveat at `T=59.4,cR=1,cO=1,P=9.2`. Evidence:
  `Results/metrics/runtime_channel_blocker_v80_after_v108_20260711.md` and
  `Results/metrics/runtime_channel_recovery_v80_after_v108_20260711.md`.

## Review Notes

- v179 pursuit wrapping is rejected at
  `Results/metrics/track3_candidate_review_v179_pursuit_wrap_20260712.md`.
  Combining v162 with final-to-first pursuit traversal stopped at
  `T=110.4,cR=1,cO=1,P=9.2`, materially behind v162's `T=286.55`. The path
  change was active but did not produce an official finish. Exact v148 source
  semantics are restored; do not stack more pursuit-wrap parameters.

- v162 rear-observability diagnostic is closed at
  `Results/metrics/v162_rear_observability_diagnostic_20260712.md`. `db`
  separates initial departure from later motion but does not uniquely identify
  the return-to-finish window; rear-close predicates recur on the main loop.
  No `db` candidate was promoted and exact v148 is restored.

- v178 preemptive narrow recovery is rejected at
  `Results/metrics/track3_candidate_review_v178_preemptive_narrow_recovery_20260712.md`.
  Moving the v162 branch from `df<0.15` to `df<0.20` yielded a long but
  unfinished `T=228.15,cR=2,cO=1,P=8.8` run and regressed v162. Exact v148 is
  restored; nearby narrow-front thresholds are closed.

- v177 fixed-entry offset correction is rejected at
  `Results/metrics/track3_candidate_review_v177_offset_correction_20260712.md`.
  Reducing `+0.60` to `+0.55` removed the first obstacle collision but produced
  an early non-finish at `T=18.50,cR=1,cO=0,P=9.6`; the readable score is not
  completion. Exact v148 is restored and fixed-entry magnitude scans are closed.

- v176 phase-aligned feedback is rejected at
  `Results/metrics/track3_candidate_review_v176_phase_aligned_feedback_20260712.md`.
  It made the existing lateral gap states reachable for 0.1 s and extended
  Track3 beyond v148, but stopped without a finish at
  `T=108.10,cR=2,cO=1,P=8.8`, materially behind v162's near-loop diagnostic.
  Exact v148 source semantics are restored; do not scan dwell alignment.

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
- v100 side-squeeze initial damping is rejected at
  `Results/metrics/track3_candidate_review_v100_side_squeeze_initial_damping_20260711.md`.
  It changed the lateral avoid initial action from fixed `0.6` to a side-squeeze
  `0.2` damping rule, but Track3 regressed to `T=120.0,cR=3,cO=1,P=8.4`.
  Source was restored to v80 semantics and passed
  `Results/evidence/controller_deployability_static_check_v80_restored_after_v100_20260711.md`.
- v101 narrow conflict handoff is rejected at
  `Results/metrics/track3_candidate_review_v101_narrow_conflict_handoff_20260711.md`.
  It reduced the opposing path-steer contribution from `0.5` to `0.25` when
  obstacle avoidance was braking and steering positive, but Track3 stayed
  `T=40.3,cR=1,cO=1,P=9.2`, shorter than v80 and with no score improvement.
  Source was restored to v80/v48 `ControlAllocate` arbitration semantics.
- v102 opposing path recovery release is rejected at
  `Results/metrics/track3_candidate_review_v102_opposing_path_recovery_release_20260711.md`.
  It released full opposing path-steer authority when the active reverse avoid
  path recovery was stronger than `0.2`, reducing Track3 final road-window
  steering to about `0.074`, but Track3 still stayed
  `T=32.3,cR=1,cO=1,P=9.2`, shorter than v80 and with no score improvement.
  Source was restored to v80/v48 control-allocation semantics and passed
  `Results/evidence/controller_deployability_static_check_v80_restored_after_v102_20260711.md`.
- v103 conflict path-speed gate is rejected at
  `Results/metrics/four_track_candidate_review_v103_conflict_path_speed_20260711.md`.
  It improved Track3 from `P=9.2,cR=1,cO=1` to `P=9.6,cR=0,cO=1`, but
  regressed Track1 from `P=9.6,cR=1,cO=0` to `P=8.8,cR=3,cO=0`, reducing
  total wrapper score from `38.0` to `37.6`. Source was restored to v80
  semantics and passed
  `Results/evidence/controller_deployability_static_check_v80_restored_after_v103_20260711.md`.
- v109 asymmetric left squeeze is rejected at
  `Results/metrics/four_track_candidate_review_v109_asymmetric_left_squeeze_20260711.md`.
  Track2 has no usable score values, and Track3/Track4 apparent high scores are
  short-run artifacts at `T=11.6` and `T=7.2`, not comparable 120 s evidence.
  Source was restored to v80 semantics and passed
  `Results/evidence/controller_deployability_static_check_v80_restored_after_v109_20260711.md`.
- v110 negative moderate short-lookahead is rejected at
  `Results/metrics/track3_candidate_review_v110_negative_moderate_short_lookahead_20260711.md`.
  Track3 exported `P=9.6`, but only after a non-comparable `T=4.8` early stop,
  so it is not an accepted improvement over v80. Source was restored to v80
  semantics and passed
  `Results/evidence/controller_deployability_static_check_v80_restored_after_v110_20260711.md`.
- v112 early conflict speed-window is rejected at
  `Results/metrics/track3_candidate_review_v112_early_conflict_speed_window_20260711.md`.
  After recovering the MWORKS license channel with
  `Results/evidence/mworks_license_recovery_v112_20260711.md`, Track3 stayed
  `T=26.3,cR=1,cO=1,P=9.2`, worse than the v80 Track3 runtime caveat
  `T=59.4,cR=1,cO=1,P=9.2`. Source was restored to v80 semantics and passed
  `Results/evidence/controller_deployability_static_check_v80_restored_after_v112_20260711.md`.
- v113 conflict speed-window until 25 s is rejected at
  `Results/metrics/track3_candidate_review_v113_conflict_speed_until25_20260711.md`.
  It extended the bounded v103-style conflict speed cap beyond v112, but Track3
  stayed at `T=76.7,cR=1,cO=1,P=9.2`. Collision-window analysis shows the
  obstacle event remained at `t=1.05` and the road event shifted to `t=25.7`.
  Source was restored to v80 semantics and passed
  `Results/evidence/controller_deployability_static_check_v80_restored_after_v113_20260711.md`.
- v114 straight-front speed cap is rejected at
  `Results/metrics/track3_candidate_review_v114_straight_front_speed_cap_20260711.md`.
  It targeted the fixed Track3 `t=1.05` obstacle event by capping path speed
  during straight-front braking, but the resulting `P=10.0` came from a
  non-comparable `T=1.6` short run. Source was restored to v80 semantics and
  passed
  `Results/evidence/controller_deployability_static_check_v80_restored_after_v114_20260711.md`.
- v115 smoother straight-front speed cap is rejected at
  `Results/metrics/track3_candidate_review_v115_smooth_straight_front_speed_cap_20260711.md`.
  It avoided the v114 `T=1.6` artifact but did not improve score variables:
  Track3 stayed `T=51.4,cR=1,cO=1,P=9.2`, shorter than the v80 caveat
  `T=59.4,cR=1,cO=1,P=9.2`. Source was restored to v80 semantics and passed
  `Results/evidence/controller_deployability_static_check_v80_restored_after_v115_20260711.md`.
- v116 early negative-curve speed guard is rejected at
  `Results/metrics/track3_candidate_review_v116_early_negative_curve_speed_guard_20260711.md`.
  Track3 shortened from v80 `T=59.4` to `T=50.2` with unchanged
  `cR=1,cO=1,P=9.2` and no official finish. Source is restored to v80 semantics
  and passed
  `Results/evidence/controller_deployability_static_check_v80_restored_after_v116_20260711.md`.
- Current completion audit is
  `Results/metrics/four_track_completion_gate_v80_20260711.md`: Tracks 1-3 have
  zero verified finishes and Track4 remains unverified. Historical avoidance
  score sums cannot be converted into official 80-point claims.
- Track2 v128/v129 anti-crawl candidates are rejected at
  `Results/metrics/track2_candidate_review_v128_v129_speed_floor_20260712.md`.
  v128 improved path progress but early-stopped at `T=157.9,cR=1`; v129 ran
  to 180 s but still had `cR=1` and no official finish. Source is restored to
  committed v80. Next work is state-transition/conflict diagnosis, not another
  blind speed-floor scan.
- Track2 v130/v131 same-direction steering handoff review is at
  `Results/metrics/track2_candidate_review_v130_v131_handoff_20260712.md`.
  v130 passed 1 s but its 180 s run produced no result after a bounded ~10 min
  and is rejected for runtime-efficiency regression. v131 static gates passed,
  but three 1 s attempts remained blocked in `StartSysplorer` before model
  check, including after restarting only the stale client. Source is restored
  to committed v80. Recovery must prove an unchanged v80 1 s probe before
  reapplying v131; no finish or score gain is claimed.
- Historical recovery note: the unchanged-v80 recovery probe found the API root blocker:
  `Results/evidence/sysplorer_auto_recovery_blocker_v80_20260712.md`.
  Sysplorer is responsive but blocked by an `自动恢复` modal for a UGV backup
  from approximately 00:46. Closing it asks permission to discard all listed
  backups. The recovery state no longer blocks the API: the subsequent v80
  one-second control probe passed load/check/simulate. Do not treat this
  historical modal note as an active blocker.
- Sysplorer recovery is now operational: the unchanged v80 Track2 1 s probe
  reached load/check/simulate with `exit_state=0`. v131 also passed its static
  and 1 s gates, but its bounded Track2 180 s run timed out after eight minutes
  without metrics or exports. It is rejected for the same runtime-efficiency
  regression as v130 and source is restored to v80. Evidence:
  `Results/metrics/track2_candidate_review_v131_noevent_handoff_20260712.md`.
  The next step is an unchanged-v80 Track2 700 s completion-horizon baseline:
  the existing 120 s and 180 s samples are too short to decide whether this
  route can ever return to the official origin. Do not interpret a horizon-only
  stop as an algorithm rejection. After that baseline, any new candidate must
  be distinct from same-direction threshold handoff and speed-floor variants.
- v148 is the current completion baseline. It separates front reverse authority
  from side-only neutral longitudinal authority and has verified official
  origin-assertion finishes on Tracks 1, 2, and 4. Track3 remains blocked at
  `T=21.1`, path index 36, finish distance squared `301.4313`. Evidence:
  `Results/metrics/four_track_completion_review_v148_20260712.md`.
- v149-v154 completion-first follow-ups are rejected. v150 only delayed the
  same Track3 path-index-36 departure; v151/v152 clearance-gated persistence
  caused collision accumulation; v153/v154 shorter lateral commitment and
  side hysteresis increased collisions or terminated earlier. Exact v148
  source semantics are restored. Do not continue speed-cap, release-dwell,
  lateral-commitment, or side-hysteresis scalar scans. Next Track3 work must
  diagnose path/pose geometry and allocator interaction before a new unified
  candidate. Evidence: `Results/metrics/track3_candidate_review_v150_moderate_side_braking_20260712.md`
  through `Results/metrics/track3_candidate_review_v154_lateral_direction_hysteresis_20260712.md`.
  Do not call 3/4 completion or wrapper score `80/80`.
- v155/v156 same-sign OA suppression candidates are rejected. v155 looped over
  path indices 11-29 and accumulated `cR=7,cO=6`; v156 stayed a Track3
  non-finish at `T=21.65,cR=1,cO=1,P=9.2`. Direct v148 allocator semantics are
  restored and this family is closed. The next candidate must be structurally
  distinct and target the neutral side-only opposite-sign path/OA conflict.
  Evidence: `Results/metrics/track3_candidate_review_v155_extreme_same_sign_oa_suppression_20260712.md`
  and `Results/metrics/track3_candidate_review_v156_terminal_only_oa_suppression_20260712.md`.
- v157 neutral side-only opposite-sign OA attenuation is rejected. Its Track3
  1 s gate passed, but the strict run stopped at
  `T=20.40,cR=1,cO=1,P=9.2` with finish-distance squared `305.6024`, slightly
  worse than v148. Exact v148 allocator semantics are restored. Do not scan
  more OA attenuation factors; the next work must inspect path/pose geometry
  and a bounded local recovery state. Evidence:
  `Results/metrics/track3_candidate_review_v157_neutral_opposite_sign_oa_attenuation_20260712.md`.
- Official-geometry diagnosis confirms v148 leaves the Track3 straight road:
  the vehicle reaches `(4.147,0.4614)` at the first road event while the center
  is `y=0`. v158/v159 neutral path-recovery candidates extend progress from
  path index 36 to about 76 and reduce terminal finish-distance squared from
  `301.4313` to `122.2830`/`96.9383`, but regress to `P=8.0`/`7.6` with five or
  six total collisions. Both are rejected and v148 is restored. This closes
  stateless OA cancellation and magnitude-trigger scans. Next work requires
  bounded state continuity between obstacle authority and path recovery.
  Evidence: `Results/metrics/v158_track3_geometry_review_20260712.md`,
  `Results/metrics/track3_candidate_review_v158_neutral_path_heading_recovery_20260712.md`,
  and `Results/metrics/track3_candidate_review_v159_immediate_neutral_path_recovery_20260712.md`.
- v160 first-order stateful path recovery is rejected. The new state exported
  successfully, but Track3 stopped at `T=18.75,cR=1,cO=1,P=9.2`, earlier than
  v148, with no completion gain. Exact v148 allocator semantics are restored.
  Do not scan recovery-filter time constants or add more allocator filters.
  Next state continuity must use side-clearance geometry in the avoidance
  state machine, or be preceded by an explicit bounded interface design.
  Evidence: `Results/metrics/track3_candidate_review_v160_stateful_path_recovery_20260712.md`.
- v162 narrow front-obstacle recovery is the strongest structural diagnostic:
  it traversed the main Track3 loop but missed the official origin and began a
  second lap. v163 side-only path recentering regressed collision counts. v164
  endpoint capture passed static, test, and 1 s native gates but terminated at
  `T=20.15,cR=1,cO=1,P=9.2`, finish-distance squared `302.2936`; it is rejected
  because the new departure event perturbed the early trajectory before
  endpoint capture was needed. Exact v148 source semantics are restored. Next
  work must inspect the official finish assertion and shared start/end segment
  semantics without adding a start-of-run discrete event. Evidence:
  `Results/metrics/track3_candidate_review_v162_v148_narrow_recovery_20260712.md`,
  `Results/metrics/track3_candidate_review_v163_side_only_path_recentering_20260712.md`,
  and `Results/metrics/track3_candidate_review_v164_endpoint_capture_20260712.md`.
- v165 stateless closure-segment capture corrected the official path-array
  representation and passed static, test, and corrected 1 s native gates. Its
  strict Track3 run still terminated early at
  `T=18.1,cR=1,cO=1,P=9.2`, finish-distance squared `295.2941`; no exported
  sample satisfied the capture predicate before termination. Adding planner
  equations perturbed this numerically sensitive trajectory before the finish
  area, so direct `PathPlanner` endpoint-helper additions are closed for this
  pass. Exact v148 source semantics are restored. Evidence:
  `Results/metrics/track3_candidate_review_v165_final_segment_capture_20260712.md`.
- v166/v167 directional lateral-entry candidates are rejected. v166 removed
  road events but drove through obstacles when `dl≈dr`, ending at
  `T=39.8,cR=0,cO=5,P=8.0`. v167 kept fixed bypass authority until
  `df>safeF`, but still ended at `T=42.8,cR=2,cO=3,P=8.0`. Global
  front-clear/directional entry changes are closed and exact v148 semantics
  are restored. Next work may use v162 plus existing `closest_index` and
  `path_progress` only near the generic closure segment; do not add planner
  geometry calculations or departure events. Evidence:
  `Results/metrics/track3_candidate_review_v166_v167_directional_entry_20260712.md`.
- v168 reused existing `closest_index/path_progress` for a closure-only pursuit
  override, but still terminated at `T=18.1,cR=1,cO=1,P=9.2`, exactly matching
  v165 before the endpoint predicate was needed. All `PathPlanner` endpoint
  capture edits are closed for this task because even inactive helper branches
  perturb the translated trajectory. Exact v148 semantics are restored. Next
  work must avoid planner equation changes. Evidence:
  `Results/metrics/track3_candidate_review_v168_closure_progress_capture_20260712.md`.
- v169/v170 combined v162 with guarded allocator recovery and are rejected.
  v169 immediate cancellation reached `T=116.75` but accumulated
  `cR=7,cO=2,P=6.4`. v170 bounded decay reached
  `T=84.6,cR=2,cO=2,P=8.4`; its small origin distance was at path index `81`,
  not the closure segment. This closes v162 plus stateless allocator recovery
  and attenuation scans. Exact v148 controller/allocator semantics are
  restored. Next work requires a structurally different reference-backed
  controller architecture. Evidence:
  `Results/metrics/track3_candidate_review_v169_v170_v162_allocator_recovery_20260712.md`.
- v171 encounter-latched recovery is rejected. Its source and 1 s native gates
  passed, but strict Track3 ended at `T=17.75,cR=1,cO=2,P=8.8`, official
  finish distance `292.9712`. A front-obstacle encounter latch still cannot
  identify a safe recentering window with the four scalar distances. Exact
  v148 semantics are restored. Evidence:
  `Results/metrics/track3_candidate_review_v171_encounter_latched_recovery_20260712.md`.
- v172 consistent emergency-steer cap is rejected as a runtime no-op. It
  reproduced v162 exactly at `T=286.55,cR=2,cO=1,P=8.8`, finish-distance
  squared `295.9073`; the old `0.6` cap was not active. Exact v148 semantics
  are restored, and this cap must not be scanned further. Evidence:
  `Results/metrics/track3_candidate_review_v172_consistent_emergency_steer_20260712.md`.
- v173/v174 sampled path-progress planners are rejected. v173's two-segment
  backward/eight-segment forward window and v174's monotonic all-remaining
  forward search both ended at `T=49.30,cR=1,cO=1,P=9.2`, path index `48`,
  finish-distance squared `385.5061`. The failure is a mid-route departure,
  not only a final-to-first index wrap or a narrow reacquisition window. Exact
  v148 controller semantics and the original global planner are restored.
  Do not continue sampled nearest-segment window scans. Evidence:
  `Results/metrics/track3_candidate_review_v173_progress_continuous_planner_20260712.md`
  and `Results/metrics/track3_candidate_review_v174_monotonic_forward_planner_20260712.md`.
- v175 combined v162 narrow recovery with v138 adaptive side-state caps, but
  reproduced v162 exactly at `T=286.55,cR=2,cO=1,P=8.8`, finish-distance
  squared `295.90730013110414`. The side-state `0.8` cap never activated, so
  this candidate is a runtime no-op. Exact v148 semantics are restored; do not
  scan these lateral magnitude caps further. Evidence:
  `Results/metrics/track3_candidate_review_v175_narrow_recovery_adaptive_side_20260712.md`.
- The historical v148 Track2 finish is not reproducible in the current cold
  lane: exact committed bytes now terminate at
  `T=28.55,cR=1,cO=0,P=9.6`, finish-distance squared `791.4783`. Therefore the
  hard gate is no longer only Track3; Track2 completion robustness must be
  restored before four-track acceptance.
- v184/v185 front-clear severe-side recovery candidates are rejected. v184
  reached the 120 s horizon but exploded to `cR=61,cO=1,P=-14.8`; v185's
  proportional `0.3` cap terminated at `T=28.75,cR=17,cO=0,P=3.2`, finish
  distance squared `787.6683`. Exact committed controller semantics are
  restored and pass `high=0, medium=0` plus 14 tests. Do not scan smaller
  steering magnitudes in this family. Next work must evaluate a structurally
  different narrow-window speed/path-authority arbitration, with Track2 120 s
  as the first runtime gate. Evidence:
  `Results/metrics/track2_candidate_review_v184_v185_edge_recovery_20260712.md`.
- v186 coupled edge braking is rejected. Static and 1 s gates passed, but the
  Track2 120 s run returned `SimulateModel=false` at `T=25.15` with
  `cR=17,cO=0,P=3.2` and finish-distance squared `530.7769`. The narrow
  `df>safeF and min(dl,dr)<0.10` speed/steer coupling is therefore closed for
  now; exact committed controller semantics are restored. Do not expand v186
  to Track3. Evidence:
  `Results/metrics/track2_candidate_review_v186_coupled_edge_braking_20260712.md`.
- v187 path-only isolation reproducibly returned near the Track2 origin at
  `T=198.5`, but missed the strict finish threshold (`d=0.0305001871`) and
  accumulated `cR=7,cO=8,P=4.0`. v188 restored only OA steering and removed
  obstacle collisions, but terminated at `T=29.1,cR=1,cO=0,P=9.6`, far from
  the origin (`d=793.6885770`). Both are rejected and the committed allocator
  is restored. The next mechanism must be a bounded collision-imminent steer
  intervention with explicit release to path authority, not continuous old OA
  steering or another edge-magnitude scan. Evidence:
  `Results/metrics/track2_candidate_review_v187_v188_path_overlay_20260712.md`.
- v189 front-risk steer gating is rejected. It passed static, tests, and the
  Track2 1 s gate, but the strict run ended at
  `T=164.95,cR=15,cO=2,P=3.2`, finish-distance squared `377.9933562`.
  Exported signals show neither obstacle event satisfied the proposed
  `speed_oa<0` predicate, so allocator gating inferred from old OA output state
  is closed. The committed allocator is restored. Next work requires a
  controller-level risk signal from actual distance inputs or a
  reference-backed local-planner interface. Evidence:
  `Results/metrics/track2_candidate_review_v189_front_risk_steer_gate_20260712.md`.
- v190 signed-front release is rejected. It passed static (`high=0,medium=0`),
  14 tests, and the Track2 1 s native gate, but strict Track2 terminated at
  `T=28.95,cR=4,cO=1,P=8.0` with finish-distance squared `794.0116508`.
  The controller was restored exactly to `HEAD`; no candidate is accepted and
  the four-track completion gate remains open. Evidence:
  `Results/metrics/track2_candidate_review_v190_signed_front_release_20260712.md`.
- The exact `HEAD` Track2 cold baseline was reproduced again at
  `T=28.55,cR=1,cO=0,P=9.6`, finish-distance squared `791.4782768`; it remains
  a non-finish. v191 brake-then-steer handoff extended runtime to `T=87.4` and
  reduced finish distance to `332.5612519`, but accumulated `cR=3,cO=4,P=7.2`
  and still did not finish. v191 is rejected and both controller/allocator are
  restored exactly. Do not repeat larger-front-threshold plus OA-speed-sign
  steering gates. Evidence:
  `Results/metrics/track2_candidate_review_v191_brake_then_steer_handoff_20260712.md`.

