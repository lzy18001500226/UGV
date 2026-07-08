# UGV Obstacle Challenge 2026

This is an independent project for the 2026 Intelligent Unmanned Systems Application Challenge, algorithm track: UGV obstacle avoidance 3.0.

The project reuses MoSim's MWORKS/Sysplorer working habits only as reference. It does not share MoSim's UAV/Sunray/Factory mainline, operating board, or runtime evidence.

## Start Here

```text
1. AGENTS.md
2. Docs/Workflows/new_conversation_context.md
3. Docs/Index/workflow_index.md
4. Docs/Workflows/master_execution_plan.md
5. Docs/Workflows/long_task_status_board.md when running or resuming long work
6. Topic workflow/design docs as needed
```

## Current Layout

| Path | Purpose |
|---|---|
| `Models/UGV/` | Editable working copy of the official UGV model. |
| `References/official_materials/` | Read-only copied official PDFs and report template. |
| `Docs/Design/` | Competition task, requirements, and architecture. |
| `Docs/Workflows/` | MWORKS simulation, experiment, and report procedures. |
| `Docs/Index/` | Model and workflow indexes. |
| `Scripts/` | Future automation, metric extraction, and quality checks. |
| `Results/` | Simulation evidence, metrics, figures, reports, and temp files. |

## Current Gate

M1 static model grounding and the M2 bounded baseline runtime gate are complete:

```text
M1: Results/evidence/static_model_grounding_20260708_210142.md
M2: Results/simulations/baseline_20260708_213448/
```

The current next engineering action is M3 controller design. The M2 baseline
evidence confirms bounded MWORKS load/check/simulate and score-variable access
for `UGV.Example.Race1`; it does not claim full-track completion or final
competition score.

## Main Implementation Target

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Default controller interface:

```text
inputs:  front_dist, rear_dist, left_dist, right_dist
outputs: speed, steer
```

Do not modify official track, vehicle, sensor, scoring, or example systems unless a later task explicitly authorizes that scope.
