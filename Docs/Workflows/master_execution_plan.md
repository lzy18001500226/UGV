# Master Execution Plan

> Full execution plan for the 2026 UGV obstacle-avoidance project. This file is the main review surface before autonomous execution.

Status: planning and control document. It does not claim model load, simulation, lap completion, score, report completion, or submission.

## 1. Operating Principle

Default mode is autonomous execution with durable evidence and timely sparse email notices. The agent should first try to solve ordinary implementation choices, routine debugging, source inspection, online research, GUI evidence capture, login/activation recovery, parameter tuning, report drafting, and packaging dry runs without waiting for the user.

Do not wait idly for the user when a bounded recovery path exists. Send email notices at meaningful terminal or review points so the user can check in asynchronously. Stop instead of improvising only when continuing would require guessing unavailable credentials, violating hard boundaries, changing contest scope, or making irreversible external actions.

Use the approved MoSim sparse email gateway for UGV terminal notices until this
project grows its own local notifier:

```powershell
python C:\Users\HP\Desktop\MoSim\Scripts\agent\send_gateway_email_alert.py `
  --subject "<short Chinese subject>" `
  --body "<short Chinese body>" `
  --cooldown-key "<task-specific-key>" `
  --cooldown-minutes 0 `
  --timeout 30
```

Record the generated MoSim email evidence JSON path in the relevant UGV phase
evidence. If the command fails or no approved email route is available, write
the same notice text into `Results/evidence/` or the run manifest and continue
when safe; do not pretend that email was sent.

## 2. Human Intervention Policy

| Situation | Default Action |
|---|---|
| MWORKS login, license, or activation dialog appears | Use the approved credential path if the current task/user/project document names one. Do not scan personal folders for credentials. Do not treat `L5104-B0` or `登录失败，请检查网络后重试` as a network blocker by default. First operate the real Sysplorer `登录` button, enter the approved in-memory credentials, activate through `帮助 -> 使用许可`, verify with a 1 s API probe, capture redacted evidence, then send or record a short Chinese notice. |
| Unknown modal or GUI error appears | Inspect, screenshot, send an email if it affects progress, search local/official/community docs, try bounded recovery if low risk, then record evidence. Stop only if continued action would be destructive, credential-guessing, or scope-changing. |
| Model load/translate/simulate bug | Inspect local model source and logs first, send an email if the phase is delayed or blocked, then search official docs, MoHub, blogs, and reference projects. Record what was tried before declaring a blocker. |
| Need an open-source reference | Search and ingest it under `References/research/` with a manifest; do not mix it into the official model tree. |
| Need to edit official road, vehicle, sensor, scoring, or official example files | Do not edit. Treat as a hard boundary; redesign the controller or create separate non-scoring diagnostic notes only. |
| Need to send final competition email/submission | Stop for user confirmation of team/archive name and final approval. |
| Credentials unavailable or rejected repeatedly | Send a blocker email if an approved route exists; otherwise record a blocker notice in evidence and stop. Do not guess credentials. |

## 3. Hard No-Edit Zones

These are hard boundaries during normal development:

```text
Models/UGV/Vehicle/
Models/UGV/Road/
Models/UGV/saidao/
Models/UGV/CountPoint/
Models/UGV/Example/
References/official_materials/
```

Allowed normal edit target:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
Docs/
Scripts/
Results/
```

If a problem appears to require editing a hard no-edit zone, the correct response is not to ask whether to break the rule. The correct response is to redesign within the controller boundary, produce a diagnostic note, or report that the official material blocks further progress.

## 4. Research And Reference Policy

The agent may perform targeted online research and local reference inspection
without asking first when blocked by APIs, MWORKS behavior, Sysblock modeling
details, real-car transfer risk, or algorithm design uncertainty. Research is
part of execution, not a substitute for evidence: use it to choose safer,
deployable controller patterns, then validate the actual MWORKS model when the
runtime gate is available.

Research outputs should be stored as:

```text
References/research/<topic>_<date>/MANIFEST.md
References/research/<topic>_<date>/source_notes.md
```

Rules:

1. Prefer official MWORKS/Tongyuan/MoHub material first.
2. Use open-source projects as references, not as copy-paste competition submissions.
3. Record URL, license if visible, what was learned, and what was not reused.
4. Do not overwrite official material or model files with crawled content.
5. If a reference project is large, save only manifest and notes unless the source itself is clearly needed.
6. For obstacle-avoidance algorithms, reject simulation-only tricks that would
   be unsafe or hard to tune on a physical UGV. Prefer bounded, explainable,
   low-latency patterns: safety bubble / gap selection, speed reduction near
   obstacles, curvature or steering-based speed scaling, command saturation,
   hysteresis, dwell, and parameter tables with physical units.
7. If a promising open-source repository is too large or license-sensitive,
   save source notes and exact links first. Ask the user to crawl the full
   repository only when the implementation genuinely needs it.
8. For obstacle-avoidance work, treat physical deployability as a first-class
   acceptance filter. Before tuning for simulation score, check whether the
   idea keeps bounded commands, slows under risk, uses dwell/hysteresis, and
   can be retuned on a physical UGV. If the answer is unclear, create a small
   `References/research/<topic>_<date>/` research pack before changing the
   controller.

## 5. Full Task Tree

### M0 - Material And Rule Grounding

Goal: turn official material into actionable constraints.

Inputs:

```text
References/official_materials/
Results/tmp/training_pdf_extract/
Docs/Design/赛题.md
Docs/Design/需求.md
```

Outputs:

```text
Docs/Workflows/master_execution_plan.md
Docs/Workflows/initial_race_task_plan.md
Docs/Index/workflow_index.md
```

Acceptance:

- Source materials are identified as usable.
- Submission requirements and scoring rules are known.

### M1 - Static Model Grounding

Goal: understand model topology and scoring before runtime or edits.

Actions:

1. Inspect `Race1.mo`, `Race2.mo`, official track models, controller interface, `ControlAllocate`, `CountPoint`, and `distanceSensor1`.
2. Update `Docs/Index/model_index.md` with exact entry points, signal paths, and score variables.
3. If there are hidden track variants or example limitations, record them.
4. Update `Docs/Workflows/long_task_status_board.md` only when M1 moves to
   `in_progress`, `blocked`, or `completed`.

Outputs:

```text
Docs/Index/model_index.md
Results/evidence/static_model_grounding_<timestamp>.md
```

Acceptance:

- The agent can map sensor inputs to controller outputs and scoring outputs.
- The static evidence note follows `Docs/Workflows/experiment_gate.md` and marks
  unknown facts explicitly instead of guessing.

### M2 - Baseline Runtime Gate

Goal: run the unmodified official model.

Actions:

1. Load `Models/UGV/package.mo` in MWORKS.Sysplorer.
2. Open official examples.
3. Translate/simulate one baseline example first.
4. Capture screenshots/logs/metrics.
5. Resolve login/activation/license issues autonomously when credentials and safe UI route are available; email a short notice after recovery.

Outputs:

```text
Results/simulations/baseline_<timestamp>/MANIFEST.md
Results/simulations/baseline_<timestamp>/metrics.json or metrics_notes.md
Results/simulations/baseline_<timestamp>/screenshots/
```

Acceptance:

- Baseline has load/translate/simulate status.
- If blocked, blocker contains screenshot/log/source and attempted recovery notes.

### M3 - Controller Design

Goal: design a Sysblock/code-generation-friendly obstacle controller.

Initial design direction:

1. State-machine shell: cruise, front-risk, side-risk, emergency, recovery.
2. Rule/PID-like continuous output inside states.
3. Speed and steering limits.
4. Smoothing/hysteresis to avoid rapid switching.
5. Parameters exposed for tuning.

Outputs:

```text
Docs/Design/避障算法设计.md
Results/evidence/controller_design_review_<timestamp>.md
```

Acceptance:

- Design states, thresholds, inputs, outputs, and tuning parameters are documented before broad tuning.

### M4 - Controller Implementation

Goal: implement controller v1 only inside the allowed controller target.

Actions:

1. Modify `ObsAvoidController_Sysblock2.mo` or equivalent Sysblock-controlled content within the obstacle controller boundary.
2. Keep implementation explainable and compatible with generated-code direction.
3. Add comments only where they clarify state logic or non-obvious thresholds.

Outputs:

```text
Results/evidence/controller_v1_source_notes_<timestamp>.md
```

Acceptance:

- Source changes are limited to allowed scope.
- Model can attempt translate/simulate.

### M5 - One-Track Tuning

Goal: obtain one credible track run before expanding.

Actions:

1. Pick one official track.
2. Run baseline and controller v1 if baseline is available.
3. Tune controller thresholds/parameters.
4. Record every meaningful run.

Outputs:

```text
Results/simulations/controller_v1_track_<name>_<timestamp>/
Results/metrics/one_track_tuning_<timestamp>.md
```

Acceptance:

- One track has reproducible metrics, or a clear blocker explains why not.

### M6 - Four-Track Evaluation

Goal: evaluate the same controller across all official tracks.

Actions:

1. Run four official tracks without track/scoring modifications.
2. Summarize pass/fail honestly.
3. Identify whether failures are controller-design failures, runtime failures, or evidence-extraction failures.

Outputs:

```text
Results/metrics/four_track_summary_<timestamp>.md
Results/simulations/<per_track_run_folders>/
```

Acceptance:

- Every row links to evidence.
- Time, road collisions, obstacle collisions, and score are recorded or explicitly marked unavailable.

### M7 - Evidence Automation

Goal: reduce manual visual checking and repeated bookkeeping.

Actions:

1. Create scripts only when repeated extraction/copy/check tasks appear.
2. Prefer small scripts under `Scripts/analysis/`, `Scripts/mworks/`, or `Scripts/quality/`.
3. Automate manifest creation, metrics table generation, screenshot organization, and final package checks.

Outputs:

```text
Scripts/analysis/
Scripts/quality/
Results/evidence/automation_notes_<timestamp>.md
```

Acceptance:

- Repeated evidence tasks are scriptable and reproducible.

### M8 - Report Draft And Figures

Goal: convert evidence into the official report structure.

Actions:

1. Use the official report template as structure reference.
2. Generate figures/tables from run evidence.
3. Explain algorithm assumptions, state logic, parameters, tuning, and limitations.
4. Keep every claim tied to a run folder or source document.

Outputs:

```text
Results/reports/initial_race_report_draft_<timestamp>.md or .docx
Results/figures/
```

Acceptance:

- Report draft is reviewable without rerunning the model.

### M9 - Submission Candidate Package

Goal: produce a local package candidate, not send it yet.

Actions:

1. Copy complete model library into a packaging staging area.
2. Include final report.
3. Exclude `Results/tmp/`, extracted PDFs text, scratch logs, caches, and unrelated research.
4. Write package manifest.
5. Run `Scripts/quality/check_submission_readiness.py` and store JSON/Markdown dry-run output under `Results/deliverables/submission_dry_runs/`.

Outputs:

```text
Results/reports/submission_manifest_<timestamp>.md
Results/reports/<报名单位-团队名称>_candidate.zip
```

Acceptance:

- Candidate archive contains complete model library and report.
- Final email is not sent without user approval.

### M10 - Final Race Preparation Notes

Goal: keep initial-race choices compatible with physical UGV/code generation.

Actions:

1. Record code-generation assumptions.
2. Avoid nonportable dependencies.
3. Keep parameters explainable for physical tuning.
4. Track what must be retested when final-race materials arrive.
5. Maintain a lightweight mapping from external algorithms to the official
   four-distance controller boundary, including what cannot be reused without a
   different sensor/interface.

Outputs:

```text
Docs/Design/final_race_migration_notes.md
```

Acceptance:

- Initial-race design does not knowingly block generated-code deployment.

## 6. Evidence And Notification Rules

Every non-trivial run should produce a manifest with:

```text
request_id or run_id
timestamp
model_root
example_or_track
controller_version
runtime_status
completion
time_s
road_collisions
obstacle_collisions
avoidance_score
artifacts
blockers
notes
```

Email notifications:

1. Send a short Chinese email after recovering MWORKS login/license/activation.
2. Send a short Chinese email when a long autonomous phase reaches completion, blocker, review-ready state, or is delayed by a non-trivial issue that the user may want to inspect asynchronously.
3. Do not email every small observation.
4. Do not send final competition submission email without explicit user approval.
5. Treat SMTP `ok=true` as send evidence only, not proof that the user saw the message. If the user reports no email, record the email evidence JSON path, `to`, `recipient_explicit`, `recipient_warning`, and cooldown fields, then keep the same terminal notice in `Results/evidence/` or the relevant phase manifest so progress remains auditable.
6. Use a task-specific cooldown key and `--cooldown-minutes 0` for explicit
   terminal notices so separate completions/blockers are not suppressed by an
   earlier status email.
7. If the user reports that no notice arrived, immediately send one concise
   current-status notice again, record the gateway JSON path, and write the same
   content into `Results/evidence/notification_delivery_note_<timestamp>.md`.
   Treat delivery visibility as an operations risk, not as proof that project
   work failed.

Board updates:

1. `Docs/Workflows/long_task_status_board.md` is a short operational board, not
   a history ledger.
2. Update it at phase start, phase completion, blocker, and user-review-ready
   points.
3. Keep detailed attempts, logs, screenshots, metrics, research notes, and
   notices in `Results/` or `References/research/`, then link only the durable
   evidence path from the board.

Git closeout:

1. When a task reaches completion, blocker, or review-ready state, inspect the
   changed paths, run the smallest relevant checks, then commit the completed
   task promptly.
2. Use path-limited staging for the exact files changed by the task. Do not
   stage the whole working tree with a broad command.
3. Commit messages should name the task or phase, for example
   `docs: record git closeout policy` or `m1: static model grounding`.
4. Push to `origin` after the commit when authentication works. If push fails
   because credentials are unavailable, report the local commit hash and the
   push blocker instead of retrying blindly.
5. Final competition submission/package email still requires explicit user
   approval even when code and docs have been committed.

## 7. Review Package For User

When the plan reaches review-ready state, provide:

1. Files changed.
2. Task phase completed.
3. Evidence paths.
4. Known blockers.
5. Whether MWORKS was opened.
6. Whether login/activation was recovered.
7. Whether official hard no-edit zones were touched.
8. Next autonomous phase.

## 8. Current Phase Cursor

The cursor points to the next phase in the long autonomous task. It is not a
terminal stop condition. After a phase reaches completion, blocker, or
review-ready state, commit/push the phase evidence and continue to the next
safe phase unless the user explicitly pauses or final submission approval is
required.

Current cursor: v80 sharp curve speed cap is the score-leading local wrapper
candidate with a Track3 runtime caveat after v79/v81/v82/v83/v84/v85/v86/v87/v88 follow-ups
were rejected as accepted baselines. M1 source grounding, M2 bounded baseline,
M3 controller design, M4 bounded controller implementation gate, M5 one-track
Race1 tuning review, M6 wrapper-based four-track metric extraction, historical
M8 report refreshes, and M9 local review-only dry run are complete or
review-ready:

```text
M1: Results/evidence/static_model_grounding_20260708_210142.md
M2: Results/simulations/baseline_20260708_213448/
M3: Docs/Design/避障算法设计.md; Results/evidence/controller_design_review_20260708_215659.md
M4: Results/simulations/controller_refsysblock_20260708_221000/
M5: Results/metrics/one_track_tuning_20260708_231430.md
M6 baseline: Results/metrics/four_track_summary_20260709_120547.md
v13 historical accepted: Results/metrics/four_track_summary_v13_side_trigger045_20260709_1535.md
v45 superseded accepted: Results/metrics/four_track_candidate_review_v45_curvature_speed_regulation_scaled_20260710_0045.md
v48 superseded accepted: Results/metrics/four_track_candidate_review_v48_opposing_steer_guard_20260710.md
v74 superseded accepted: Results/metrics/four_track_candidate_review_v74_guarded_curve_short_lookahead_20260710.md
v80 current accepted: Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
v86 rejected: Results/metrics/track3_candidate_review_v86_conditional_lateral_release_20260710.md
v87 rejected: Results/metrics/track2_candidate_review_v87_front_clear_sustained_side_steer_20260710.md
v88 latest rejected: Results/metrics/track2_candidate_review_v88_side_squeeze_speed_hold_20260710.md
v80 Track3 diagnostic: Results/metrics/trajectory_event_review_diagnostic_v80_track3_pose_20260710.md
```

M2 and M4 verified `UGV.Example.Race1` load/check/simulate and score-variable
access with bounded `stopTime=12`. M6 uses generated `UGV.Test.Saidao*Eval`
wrappers because direct `UGV.saidao.saidao*` source entries omit the
obstacle-controller wiring needed for current API controller evaluation. The
latest 120 s wrapper runs may return `simulate_failed` with `exit_state=2`, but
the enhanced probe reads `T/cR/cO/P` and exports score timeseries after the
model terminal state. v80 currently totals `38.0` and improves Track4 versus
v74, while Track3 remains `P=9.2,cR=1,cO=1` with `simulate_failed/T=59.4`.
v84 initial-lane `y` bias was rejected because it early-stopped Track3 at
`T=1.2,cO=1`; v85 short lateral initial hold was rejected because it
early-stopped Track3 at `T=2.55,cO=1`; v86 conditional lateral release was
rejected because it reached `T=120` but regressed Track3 to `P=8.0,cR=4,cO=1`;
v87 front-clear sustained side steer was rejected because Track2 stayed equal
to v80 at `T=120,cR=1,cO=0,P=9.6`; v88 side-squeeze speed hold was rejected
because Track2 score stayed equal while runtime regressed to
`simulate_failed/T=85.15`.
The source was restored to v80 semantics before the next candidate. Next safe controller work must start from fresh failure-window,
source-level, trajectory evidence, four-direction-only research, or a new
unified mechanism hypothesis. Do not repeat broad speed clamps, accepted
baseline scalar scans, final-steer clipping, simple planner suppression,
negative initial bypass, abrupt lane bias, direct early steer feedforward, simple lateral-initial-dwell shortening, conditional lateral-release threshold scans, the same front-clear sustained side-steer boost, side-squeeze speed escalation, the
same `df < 0.15` road-edge recovery branch, or official wrapper/input changes
as accepted score routes without new evidence. Final package approval remains
a separate user gate.
