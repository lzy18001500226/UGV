# Controller v1 Source Notes

timestamp: 2026-07-08 22:02:57 CST
phase: M4 controller implementation
status: first_attempt_failed_recovered_with_reference_sysblock_structure

## Scope

Edited only the allowed controller target:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

No official vehicle, road, sensor, scoring, example, or official-material files
were intentionally changed.

## Implementation Summary

The copied controller body was empty. v1 adds a conservative reactive obstacle
avoidance increment that keeps the official path planner dominant through the
existing `CtrlAlloc` blend.

State priority:

```text
front emergency -> front risk -> side risk -> cruise
```

Core behavior:

- `front_dist < error_side`: use `speed_error` and maximum steer toward the side
  with larger clearance.
- `front_dist < front_safe`: use `speed_avoid_front`, side-clearance steering,
  and a bounded front-risk steer push.
- `left_dist < side_safe` or `right_dist < side_safe`: use
  `speed_avoid_side` and bounded side-clearance steering.
- no risk: output zero speed/steer increments so path planning remains primary.

Outputs are saturated to:

```text
speed in [speed_error, speed_avoid_side]
steer in [-steer_error, steer_error]
```

## Runtime Result

The initial plain root-level Modelica algorithm failed MWORKS `CheckModel` in:

```text
Results/simulations/controller_v1_20260708_220257/
```

MWORKS reported unconnected Sysblock ports, which showed that this controller
target needs a valid Sysblock graph/state-machine structure instead of only root
algorithm assignments.

Recovery used the local Sysblock training reference documented in:

```text
References/research/sysblock_obstacle_controller_20260708/MANIFEST.md
```

The recovered controller structure passed the M4 bounded runtime gate:

```text
Results/simulations/controller_refsysblock_20260708_221000/
```

Observed bounded metrics at `stopTime=12`:

```text
CheckModel=True
SimulateModel=True
T=12.0
cR=0.0
cO=0.0
P=10.0
```

This is still a bounded runtime gate, not a full official track score claim.

## Verification Plan

1. Run Python syntax check for the project MWORKS helper.
2. Run `CheckModel("UGV.Example.Race1")` through the MWORKS Sysplorer API.
3. Run a bounded finite-stop simulation before any tuning.
4. If syntax or runtime fails, inspect MWORKS logs and local source first, then
   either patch within the allowed controller boundary or write a blocker.

## Known Risks

- Steering sign is inferred and must be validated by simulation.
- Bounded simulation proves load/check/sim API and readable metrics only; it is
  not full-track completion evidence.
