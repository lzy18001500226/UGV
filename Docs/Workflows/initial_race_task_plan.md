# Initial Race Task Plan

> Auxiliary planning document for the 2026 UGV obstacle-avoidance initial race. Current execution authority is `Docs/Workflows/master_execution_plan.md`; use this file only for extra detail.

Status: planning-only. No MWORKS live run has been started by this document task.

## 1. Source Materials

| Material | Path | Status | Planning Impact |
|---|---|---|---|
| Training 1 | `References/official_materials/4-赛前培训材料/01-无人车避障赛道专项培训（一）.pdf` | usable | Confirms race structure, four initial tracks, model/report deliverables, MoHub support, and final physical-car relevance. |
| Training 2 | `References/official_materials/4-赛前培训材料/02-无人车避障赛道专项培训（二）.pdf` | usable after user fix | Confirms Sysblock/PID/state-machine/mixed-simulation development route and submission requirements. Extracted text is in `Results/tmp/training_pdf_extract/02-无人车避障赛道专项培训（二）.txt`. |
| Rules | `References/official_materials/3-比赛规则/2026比赛规则—算法赛道—无人车避障3.0（第三版）.pdf` | usable | Scoring and deliverable authority. |
| Deployment | `References/official_materials/2-仿真模型部署说明/2026 算法赛道 仿真模型部署说明.pdf` | usable | MWORKS 2026a / Sysplorer 26.3, package loading, simulation, and animation route. |
| Report template | `References/official_materials/5-仿真报告模板（仅供参考）/仿真报告模板.docx` | usable | Report structure reference. |

## 2. Competition Target

The initial race requires the official UGV model to complete one lap on each official ring track while staying inside lane boundaries and avoiding obstacles. The project must produce:

1. A complete simulation model library.
2. A simulation report.

Training 2 makes the final-race direction clear: the controller should be built as a Sysblock-friendly model because generated code will later be deployed to the physical UGV. The first implementation should avoid black-box tricks that are hard to explain or hard to generate.

## 3. Scope Boundary

Default implementation target:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Default source-inspection targets:

```text
Models/UGV/Example/Race1.mo
Models/UGV/Example/Race2.mo
Models/UGV/saidao/saidao5.mo
Models/UGV/saidao/saidao7.mo
Models/UGV/saidao/saidao8.mo
Models/UGV/saidao/saidao9.mo
Models/UGV/CountPoint/package.mo
Models/UGV/Control/ControlAllocate/package.mo
Models/UGV/Vehicle/Sensors/distanceSensor1.mo
```

Hard no-edit areas during normal development:

```text
Models/UGV/Vehicle/
Models/UGV/Road/
Models/UGV/saidao/
Models/UGV/CountPoint/
Models/UGV/Example/
References/official_materials/
```

## 4. Task Phases

### P0 - Material Grounding

Goal: avoid building on invalid or stale competition material.

Actions:

1. Keep the extracted Training 1 and Training 2 text under `Results/tmp/training_pdf_extract/` as temporary reading aids.
2. Treat PDFs/docx in `References/official_materials/` as the source of truth.
3. Do not copy MoSim UAV/Sunray/UE workflows into this project.
4. Keep this UGV project independent from MoSim runtime evidence.

Outputs:

- `Docs/Workflows/initial_race_task_plan.md`
- Updated workflow index.

Acceptance:

- Agent can name valid source materials and the next executable gates.

### P1 - Static Model Grounding

Goal: understand official model structure before live runtime or edits.

Actions:

1. Inspect `Race1.mo` and `Race2.mo` top-level components and connections.
2. Map the four official track files to actual race entry points.
3. Confirm how `ControlAllocate` combines path-planning and obstacle-avoidance outputs.
4. Confirm score variables and collision counters from `CountPoint` and example displays.
5. Confirm sensor meanings and edge cases from `distanceSensor1.mo`.

Outputs:

- Update `Docs/Index/model_index.md` if mapping changes.
- Static evidence note under `Results/evidence/static_model_grounding_<timestamp>.md`
  using `Docs/Workflows/experiment_gate.md`.

Acceptance:

- We know where to read or observe time, road collisions, obstacle collisions, and avoidance score.
- We know the exact controller input/output contract.

### P2 - Baseline Runtime Gate

Goal: run the unmodified official model before controller edits.

Preconditions:

1. Runtime execution is not explicitly paused by the user or master execution plan.
2. MWORKS.Sysplorer 2026a / 26.3 is available.
3. Login/license/activation recovery follows `Docs/Workflows/master_execution_plan.md`; unknown or repeatedly failed credential states become blockers with email notice.

Actions:

1. Load `Models/UGV/package.mo`.
2. Open `UGV.Example.Race1` and `UGV.Example.Race2`.
3. Translate/simulate one baseline example first.
4. Capture load, translate, simulation, and visible score evidence.
5. Apply bounded recovery and research from `master_execution_plan.md`; write a blocker only after recovery paths are exhausted or continuation would violate scope.

Outputs:

```text
Results/simulations/baseline_<timestamp>/MANIFEST.md
Results/simulations/baseline_<timestamp>/metrics.json or metrics_notes.md
Results/simulations/baseline_<timestamp>/screenshot_or_log.*
```

Acceptance:

- At least one official example has recorded load/translate/simulate status.
- No algorithm edit precedes baseline status.

### P3 - Controller Design

Goal: design a conservative, explainable controller that matches Training 2's Sysblock/state-machine direction.

Recommended first controller structure:

1. Cruise state: maintain positive speed and near-zero avoidance steering.
2. Front-risk state: reduce speed and steer toward the side with more clearance.
3. Side-risk state: steer away from the closer side while keeping forward motion.
4. Emergency state: apply strong steering and low or reverse speed when distances are below hard thresholds.
5. Recovery state: return smoothly to cruise after distances recover.

Design constraints:

1. Use parameters already present in `ObsAvoidController_Sysblock2.mo` where reasonable.
2. Keep the logic expressible as Sysblock blocks/state machine and compatible with generated code.
3. Avoid large black-box external Python/C dependencies for the first competition version.
4. Add output limits and smoothing to reduce oscillation.

Outputs:

- `Docs/Design/避障算法设计.md` before or with first implementation.
- Source diff only in the controller target during normal development.

Acceptance:

- The design explains inputs, states, thresholds, outputs, and tuning parameters.

### P4 - One-Track Implementation And Tuning

Goal: get one official track working before expanding to all tracks.

Actions:

1. Implement controller v1 in the target controller model.
2. Run one selected official track.
3. Record completion, time, road collisions, obstacle collisions, and score.
4. Tune only controller logic/parameters unless user approves broader changes.
5. Keep each meaningful run in a separate folder.

Outputs:

```text
Results/simulations/controller_v1_track_<name>_<timestamp>/MANIFEST.md
Results/metrics/one_track_tuning_<timestamp>.md
```

Acceptance:

- One official track has reproducible metrics, or a blocker explains the failure.

### P5 - Four-Track Evaluation

Goal: evaluate the same controller on all four official tracks.

Actions:

1. Run all four official tracks without editing track/scoring files.
2. Save one folder per run.
3. Summarize good and bad results honestly.
4. Do not hide failed tracks behind successful tracks.

Output:

```text
Results/metrics/four_track_summary_<timestamp>.md
```

Minimum table columns:

```text
track, controller_version, completion, time_s, road_collisions,
obstacle_collisions, avoidance_score, evidence_path, notes
```

Acceptance:

- Four-track table exists and every row links to evidence.

### P6 - Report Draft

Goal: turn reproducible evidence into a report that matches the official template.

Actions:

1. Use the official report template as structure reference.
2. Explain model assumptions, controller states/logic, parameters, and tuning process.
3. Include per-track metrics and figures.
4. Clearly state limitations and improvement directions.

Outputs:

```text
Results/reports/initial_race_report_draft_<timestamp>.docx or .md
Results/figures/<report_figures>
```

Acceptance:

- Every report claim cites a run folder, metric table, or figure source.

### P7 - Submission Package

Goal: prepare the exact initial-race submission package.

Official Training 2 submission notes:

```text
deadline: July 15 18:00
content: complete simulation model library + simulation report
archive name: 报名单位-团队名称
email: kongdecai@tongyuan.cc
email subject: 算法赛道—无人车避障初赛作品提交
```

Actions:

1. Package the complete model library, not just a single controller file.
2. Package the final simulation report.
3. Add a local manifest listing files, model version, report version, and evidence basis.
4. Do not include temp extraction files or unrelated project caches in the submission archive.

Output:

```text
Results/reports/submission_manifest_<timestamp>.md
Results/reports/<报名单位-团队名称>.zip
```

Acceptance:

- Archive contains the complete model library and report only, plus any explicitly allowed supplemental material.

## 5. Near-Term Execution Order

Use this order unless the user explicitly changes priority:

1. P1 static model grounding.
2. P2 baseline runtime gate.
3. P3 controller design document.
4. P4 one-track controller implementation and tuning.
5. P5 four-track evaluation.
6. P6 report draft.
7. P7 submission package.

## 6. Do Not Do Yet

1. Do not start MWORKS/Sysplorer just because this planning doc exists; start it when executing the runtime phase in `master_execution_plan.md`.
2. Do not modify controller code before P1 static grounding and P2 baseline status.
3. Do not modify official track, scoring, vehicle, or sensor files as a shortcut.
4. Do not claim lap completion or score from source inspection.
5. Do not build the report from screenshots alone; metrics are required.
6. Do not include `Results/tmp/` extraction files in the final submission package.

## 7. Current Blockers / Open Items

1. Need valid approved credential path for autonomous login/license/activation recovery if MWORKS requests it and no current path is available.
2. Need exact team/archive name before P7 packaging.
3. Need decide whether the first implementation will be graphical Sysblock-only, text-level Modelica edit, or a mixed path that is later reconciled in Sysblock. For competition/code-generation direction, graphical Sysblock/state-machine parity remains the preferred target.
