# Sysblock Obstacle Controller Reference Notes

Date: 2026-07-08
Purpose: M4 recovery after a direct algorithm body in `ObsAvoidController_Sysblock2.mo` failed MWORKS Sysblock port connection checks.

## Local Reference Used

```text
C:\Users\HP\Desktop\MoSim\References\MWORKS\智能无人系统应用挑战赛培训配套文档及案例\03-2025年智能无人系统应用挑战赛专项培训\00-模型材料\UGV\Control\ObstacleAvoidanceController\ObsAvoidController_Sysblock2.mo
```

## Why This Reference Is Relevant

The current UGV controller file is the same Sysblock controller target but with an empty body in the official copied model. The reference controller shows the expected Sysblock structure:

- root `SysplorerEmbeddedCoder.Port.Inport/Outport` ports,
- internal `Chart` state machine,
- internal `internalShare` ports,
- explicit `connect(...)` equations from external ports to blocks and chart outputs to root outports,
- state-machine action algorithms for `speed` and `steer`.

The failed v1 hand-written algorithm produced unconnected-port diagnostics for all root ports, so the recovery path is to restore a valid Sysblock graphical/control structure rather than keep adding plain Modelica algorithm code at the root.

## Reuse Boundary

This reference is used as a local training/example source for Sysblock structure and a first runnable controller baseline. It is not copied into official material, vehicle, road, sensor, scoring, or example files. The only normal implementation target remains:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

## Follow-up

After a valid MWORKS check/simulation gate, later M5 tuning should adjust only controller parameters/logic inside the allowed controller boundary and record whether the controller behavior improves over the empty-controller bounded baseline.
