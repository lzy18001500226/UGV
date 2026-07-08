# M1 Static Model Grounding Evidence

## timestamp

2026-07-08 21:01 CST

## scope

Source/static inspection only. MWORKS/Sysplorer was not opened, no model was
loaded, translated, simulated, or visually reviewed. This note proves
`source_grounded` only.

## files_read

- `AGENTS.md`
- `Docs/Workflows/new_conversation_context.md`
- `Docs/Index/workflow_index.md`
- `Docs/Workflows/master_execution_plan.md`
- `Docs/Workflows/long_task_status_board.md`
- `Docs/Index/model_index.md`
- `Docs/Workflows/experiment_gate.md`
- `Docs/Workflows/mworks_ugv_simulation_workflow.md`
- `Docs/Design/赛题.md`
- `Docs/Design/需求.md`
- `Models/UGV/Example/Race1.mo`
- `Models/UGV/Example/Race2.mo`
- `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`
- `Models/UGV/Control/ControlAllocate/package.mo`
- `Models/UGV/CountPoint/package.mo`
- `Models/UGV/Vehicle/Sensors/distanceSensor1.mo`
- `Models/UGV/saidao/package.mo`
- `Models/UGV/saidao/package.order`
- `Models/UGV/saidao/saidao5.mo`
- `Models/UGV/saidao/saidao7.mo`
- `Models/UGV/saidao/saidao8.mo`
- `Models/UGV/saidao/saidao9.mo`

## entry_models

| Entry | Source File | Internal Model Name | Static Finding |
|---|---|---|---|
| Controller example | `Models/UGV/Example/Race1.mo` | `Race1` | Instantiates `ObsAvoidController_Sysblock2` as `obsAvoidController_Sysblock`. |
| No-controller example | `Models/UGV/Example/Race2.mo` | `Race2` | No `ObsAvoidController_Sysblock2` instance found in inspected source. |
| Official LOGO track | `Models/UGV/saidao/saidao5.mo` | `saidao1` | File name and model name differ. |
| Official comprehensive ring track | `Models/UGV/saidao/saidao7.mo` | `saidao2` | File name and model name differ. |
| Official triangle track | `Models/UGV/saidao/saidao8.mo` | `saidao3` | File name and model name differ. |
| Official cloud track | `Models/UGV/saidao/saidao9.mo` | `saidao4` | File name and model name differ. |

## track_mapping

`Models/UGV/saidao/package.order` lists the files in this order:

```text
saidao5
saidao7
saidao8
saidao9
```

The internal Modelica model names are `saidao1`, `saidao2`, `saidao3`, and
`saidao4`. Runtime loading must verify the package browser/model name after
loading `Models/UGV/package.mo`; do not infer the open command from the file
name alone.

All inspected example/track entries use `Road.TabularRoadObstacle` with
`road.roadMap`, `road.roadWidth`, and `road.obstaclePoint`; inspected obstacle
settings use `obstacleHeight = 0.1` and `obstacleSize = 0.1`.

## controller_interface

`Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`
exposes these ports:

```text
inputs:  front_dist, rear_dist, left_dist, right_dist
outputs: speed, steer
```

The initial `equation` section is empty, so this is the intended first
implementation target after baseline runtime is known.

Relevant existing parameters in `ModelWorkspace`:

```text
speed_Cruise = 1
front_safe = 1
side_safe = 0.3
k_rep_front = 2
k_rep_side = 1
k_steer = 0.6
speed_avoid_front = 0.5
speed_avoid_side = 1.5
speed_error = -0.8
k_steer_side = 3
steer_error = 0.8
error_side = 0.15
eps = 1e-4
```

## control_allocation_path

`Race1` source connection path:

```text
distanceSensor1.front_dist -> obsAvoidController_Sysblock.front_dist
distanceSensor1.rear_dist  -> obsAvoidController_Sysblock.rear_dist
distanceSensor1.left_dist  -> obsAvoidController_Sysblock.left_dist
distanceSensor1.right_dist -> obsAvoidController_Sysblock.right_dist

obsAvoidController_Sysblock.speed -> ctrlAlloc.speed_oa
obsAvoidController_Sysblock.steer -> ctrlAlloc.steer_oa
pathPlanner.target_v             -> ctrlAlloc.speed_pp
pathPlanner.steering_angle       -> ctrlAlloc.steer_pp
ctrlAlloc.speed                  -> pID_Ackermann.v_desired
ctrlAlloc.steer                  -> pID_Ackermann.psi_desired
```

`CtrlAlloc` has inputs `speed_pp`, `speed_oa`, `steer_pp`, and `steer_oa`; outputs
`speed` and `steer`. The package default is `factor_pp = 1`, `factor_oa = 0.3`,
but `Race1`, `Race2`, and inspected official tracks instantiate it with
`factor_pp = 1`, `factor_oa = 0.5`.

## sensor_semantics

`distanceSensor1` outputs:

```text
front_dist, rear_dist, left_dist, right_dist
DisRoad, DisObstacle
```

Static source behavior:

- `left_dist` and `right_dist` use obstacle lateral distances when the nearest
  obstacle vector is within the vehicle longitudinal span; otherwise they use
  road lateral distances.
- `front_dist` and `rear_dist` use obstacle front/rear distances when the
  nearest obstacle vector is within the vehicle lateral span; otherwise
  `front_dist` uses `fdist` and `rear_dist` uses `Bdist`.
- In examples/tracks, `distanceSensor1.fdist = pathPlanner.lookahead_dist`.
- `DisRoad = min(Ldist, Rdist)`.
- `DisObstacle = sqrt(vec_obsB[1]^2 + vec_obsB[2]^2)`.
- Completion is represented by an assertion: `d >= 0.02 or time <= 10` with
  message `已跑完赛道全程，仿真结束`.

## score_variables

`Models/UGV/CountPoint/package.mo` defines:

```text
counterR: road collision count
counterO: obstacle collision count
finalPoints = 10 - (counterR + counterO) * 0.4
```

`Race1`, `Race2`, and inspected official tracks expose:

```text
cR = countPoint.counterR
cO = countPoint.counterO
P  = countPoint.finalPoints
T  = time
```

## hard_no_edit_zones_checked

No files under these hard no-edit zones were modified during M1:

```text
Models/UGV/Vehicle/
Models/UGV/Road/
Models/UGV/saidao/
Models/UGV/CountPoint/
Models/UGV/Example/
References/official_materials/
```

Only documentation/status/evidence files are intended to change in this phase.

## open_questions_or_blockers

- No blocker for M2 from static source inspection.
- Runtime model names for official tracks must be verified inside MWORKS after
  loading the package because file names and internal model names differ.
- M1 does not prove model load, translation, simulation, score, lap completion,
  GUI health, or login/license state.

## next_phase_readiness

Ready for M2 baseline runtime gate.

Recommended M2 first action: load `Models/UGV/package.mo` in MWORKS/Sysplorer,
then open the controller example or official track entry with explicit model-name
verification. Capture manifest and screenshots/logs under
`Results/simulations/baseline_<timestamp>/`.
