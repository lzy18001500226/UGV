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

## First Gate

The first useful engineering action is M1 static model grounding. Do this before
opening MWORKS runtime or editing the controller:

```text
inspect Race1/Race2, tracks, controller, ControlAllocate, CountPoint, sensors
update Docs/Index/model_index.md
write Results/evidence/static_model_grounding_<timestamp>.md
```

After M1, follow `Docs/Workflows/master_execution_plan.md` for the M2 baseline
MWORKS/Sysplorer runtime gate and save runtime evidence under
`Results/simulations/`.

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
