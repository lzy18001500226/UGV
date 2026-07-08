# Controller Design Review

## timestamp

2026-07-08 21:56 CST

## phase

M3 controller design.

## scope

Design-only review for the first obstacle-avoidance controller. No model source
was modified by this review. No simulation claim is made here.

## inputs_read

- `AGENTS.md`
- `Docs/Workflows/new_conversation_context.md`
- `Docs/Workflows/master_execution_plan.md`
- `Docs/Workflows/long_task_status_board.md`
- `Docs/Index/model_index.md`
- `Docs/Workflows/experiment_gate.md`
- `Docs/Workflows/mworks_ugv_simulation_workflow.md`
- `Results/evidence/static_model_grounding_20260708_210142.md`
- `Results/simulations/baseline_20260708_213448/metrics.json`
- `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`
- `Models/UGV/Control/ControlAllocate/package.mo`
- `Models/UGV/Control/PathPlanning/PathPlanner.mo`

## design_output

```text
Docs/Design/避障算法设计.md
```

## core_decisions

1. Implement a conservative reactive controller inside
   `ObsAvoidController_Sysblock2.mo` only.
2. Treat controller outputs as avoidance increments blended by
   `ControlAllocate.CtrlAlloc`, not as a replacement for the official path
   planner.
3. Use existing parameters first; avoid adding new tuning variables before the
   first check/simulation pass.
4. Prefer bounded `if` branches and saturation over inverse-distance terms for
   the first implementation.
5. Validate steer sign in M5; if wrong, flip sign as a recorded controlled run.

## hard_no_edit_zones

No edits were made under:

```text
Models/UGV/Vehicle/
Models/UGV/Road/
Models/UGV/saidao/
Models/UGV/CountPoint/
Models/UGV/Example/
References/official_materials/
```

## next_phase

Proceed directly to M4 implementation in:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Then run MWORKS `CheckModel` and a bounded simulation gate before tuning.
