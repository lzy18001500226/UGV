# v145 Directional Immediate Lateral Avoidance Plan

Status: rejected after Track2 120 s; exact v80 source semantics restored.

## Goal

Preserve the immediate lateral steering authority that v144 proved necessary,
while removing the fixed positive-direction bias exposed by the reproducible
v137 Track2 termination at `T=28.55 s`.

## Evidence-Grounded Defect

On every entry into lateral avoidance, `ini_state` holds `steer=+0.6` for two
seconds. The left/right sensor-driven states are not reachable until that hold
ends. At the reproduced Track2 road-boundary event, `dl=0.02353`, `dr=0.18837`,
yet the obstacle controller still requested `steer_oa=+0.6`. The planner request
had the same sign and the allocated heading request reached about `1.35 rad`.

The downstream controller already wraps heading error through `angle_diff`, and
the path index remained continuous at 20. This candidate therefore does not edit
PathPlanner or add another heading clamp.

## Unified Mechanism

Use the existing side-clearance comparison during the immediate two-second
state, with unchanged magnitude:

```modelica
steer := 0.6 * sign(dl - dr);
```

This branch-free form is required because the Sysblock state-machine compiler
rejects inline `if` expressions in state actions. It is equivalent for unequal
side distances and returns zero when the distances are equal.

The current v137 diagnostic longitudinal rule remains paired with this candidate
so Track2 can progress instead of stalling under side-only avoidance. The same
source and parameters apply to all tracks.

## Gates

1. Static deployability check and project tests must pass.
2. Track2 1 s must pass load/check/simulation with no collision.
3. Track2 120 s must materially improve on the reproducible v137 failure at
   `T=28.55`, without exceeding v80's `cR=1,cO=0` collision envelope.
4. Only a repeatable comparable gain permits an extended completion run and
   later four-track regression.
5. Failure restores exact v80 longitudinal and lateral semantics.

No fixed-horizon run is an official finish. This plan does not claim 80 points,
physical-vehicle validation, or submission readiness.

## Result

The source gate reported `high=0, medium=0`, all 11 project tests passed, and
the corrected branch-free form passed the Track2 1 s runtime gate. The 120 s
request stopped at `T=101.65` with `cR=0,cO=4,P=8.4`. Directional immediate
steering removed the reproduced road collision but introduced four obstacle
collisions, so it is not retained or expanded to other tracks.
