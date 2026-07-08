# Long Task Status Board

> Short operational board for the UGV initial-race long task. Keep this file concise; detailed evidence belongs in `Results/`.

Status: M6_mworks_activation_blocks_official_track_dependency_load; M8 blocker-aware DOCX draft render-QA ready; controller deployability source-only gate pass, 2026-07-09 CST.

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
| M6 Four-track evaluation | blocked_on_mworks_activation_for_tadynamics | Codex | `Results/metrics/four_track_summary_20260708_231430.md`; `Results/evidence/official_track_api_simulation_blocker_20260708_231430.md`; `Results/evidence/m6_mworks_activation_blocker_20260708_235918.md`; `Results/evidence/m6_mworks_activation_recheck_20260709_023421.md` | Restore MWORKS activation/license, then rerun the official-track dependency-load diagnostic before any four-track score claims. |
| M7 Evidence automation | partial_completed | Codex | `Scripts/mworks/ugv_baseline_probe.py`; `Scripts/quality/check_controller_deployability.py`; `Results/evidence/controller_deployability_static_check_20260709_0222.md`; `Results/evidence/ugv_baseline_probe_manifest_notes_check_20260709_0240.md` | Helper exports extra variables, captures errors, and now writes blocker-specific manifest notes instead of bounded-simulation wording when dependency load/check/simulate is not reached; deployability checker passes the source-only high/medium risk gate. |
| M8 Report draft | blocker_aware_docx_render_qa_ready | Codex | `References/research/physical_ugv_obstacle_avoidance_20260708/`; `Docs/Design/final_race_migration_notes.md`; `References/research/robust_physical_ugv_navigation_20260709/`; `References/research/deployable_ugv_avoidance_algorithms_20260709/`; `Results/deliverables/report_drafts/initial_race_report_draft_blocker_aware_20260709.md`; `Results/deliverables/report_drafts/initial_race_report_draft_blocker_aware_20260709.docx`; `Results/deliverables/report_drafts/render_check_20260709_0118/QA_NOTE.md` | Draft can describe Race1 evidence, physical-transfer constraints, and official-track blocker; final report still needs M6 four-track metrics. |
| M9 Submission candidate package | dry_run_gap_check_ready | Codex + user final approval | `Results/deliverables/submission_dry_runs/submission_readiness_20260709_0235.md`; `Results/deliverables/submission_dry_runs/submission_candidate_plan_20260709_0235.md` | Static readiness checker and package plan report not ready: four-track metrics blocked/unavailable and final approval missing. DOCX draft, render QA, latest deployability static check, and model tree are identified for a future package; do not build/send final submission until M6 metrics and user approval exist. |

## Blockers

- Official four-track API simulation blocker: `UGV.saidao.saidao1` through
  `UGV.saidao.saidao4` pass `CheckModel` but fail `SimulateModelEx` at compile
  time with Real variables missing equations under vehicle wheel/force
  application components. Evidence:
  `Results/evidence/official_track_api_simulation_blocker_20260708_231430.md`.
- Current higher-priority MWORKS activation blocker: fresh API sessions still
  cannot open the installed `TADynamics.mol` dependency because MWORKS reports
  `L5104-B0` software not activated. Latest bounded recheck evidence:
  `Results/evidence/m6_mworks_activation_recheck_20260709_023421.md`.

## Review Notes

- M1 is source/static only. It does not claim MWORKS load, translate, simulate, lap completion, score, or GUI health.
- M2 confirms bounded runtime load/check/simulate for `UGV.Example.Race1`; it does not claim full-track completion or final competition score.
- M4 confirms a first runnable Sysblock controller structure with bounded `stopTime=12` metrics `T=12`, `cR=0`, `cO=0`, `P=10`; it does not claim full-track completion.
- M5 Race1 candidate v5 changes only the front avoid-to-cruise dwell from 1 s
  to 2 s and improves 120 s Race1 from `P=8.4` to `P=8.8`.
- M6 does not claim official four-track failure of the controller; it records
  an official track simulation-entry blocker before score variables can be read.
  The latest bounded recheck shows the immediate blocker is MWORKS activation/license while
  loading `TADynamics.mol`; do not continue runtime diagnosis until that is
  recovered.
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
  `Results/evidence/notification_delivery_note_20260709_023537.md`.
- Do not use this board as a history ledger.
- Update only when phase state changes or a review/blocker appears.
- Long details, logs, screenshots, and metrics must stay under `Results/`.
