# Experiment Gate

## 0. Static Evidence Note

M1 source-only grounding should write a static evidence note before any runtime
claim or controller edit:

```text
Results/evidence/static_model_grounding_<timestamp>.md
```

Minimum sections:

```text
timestamp
scope
files_read
entry_models
track_mapping
controller_interface
control_allocation_path
sensor_semantics
score_variables
hard_no_edit_zones_checked
open_questions_or_blockers
next_phase_readiness
```

Rules:

1. `source_grounded` means source/interface inspected only, not model load or simulation.
2. Static notes must cite exact model files and variable/component names.
3. If a score, sensor, or interface detail is not confirmed from source, mark it
   `unconfirmed` instead of guessing.

## 1. Run Manifest

Every meaningful simulation run should include a manifest:

```text
request_id:
timestamp:
model_root:
example_or_track:
controller_file:
controller_version:
runtime:
status:
completion:
time_s:
road_collisions:
obstacle_collisions:
avoidance_score:
artifacts:
blockers:
notes:
```

Use `status=blocked` if the model cannot load, translate, simulate, animate, or
produce readable metrics.

## 2. Acceptance Levels

| Level | Meaning |
|---|---|
| source_grounded | Source/interface inspected only. |
| load_passed | Model/package loaded in MWORKS. |
| translate_passed | Model translated/compiled. |
| simulate_started | Simulation started but no final score yet. |
| bounded_runtime_gate | Bounded finite-stop simulation completed and key variables are readable; not full-track completion. |
| run_completed | One track completed with metrics. |
| four_track_completed | All four official tracks completed with metrics. |
| report_ready | Report draft references reproducible evidence. |

## 3. Evidence Rules

1. A source check is not a simulation pass.
2. A load pass is not a lap completion.
3. A screenshot is review evidence, not enough for scoring by itself.
4. A report claim must cite a run folder or metric artifact.
5. If metrics extraction is manual, record exactly where the number was read.
