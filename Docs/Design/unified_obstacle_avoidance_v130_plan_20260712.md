# Unified obstacle avoidance v130 plan

Status: runtime candidate from the committed v80 baseline.

## Goal

Keep one algorithm for all four tracks and resolve the Track2 late-stage
same-direction steering over-allocation without weakening obstacle steering on
straight approaches or during opposing path/avoidance commands.

## Evidence basis

The corrected v80 Track2 run ends with path steering near `1.25 rad` while the
obstacle controller remains in reverse avoidance. The v129 diagnostic exported
`pathPlanner.steering_angle=1.275`, `ctrlAlloc.steer_oa=0.6`, and final
`ctrlAlloc.steer=1.573`; both steering channels point in the same direction.
The car remains near path index 27 and does not finish. v127 showed that a
global obstacle-steer washout is unsafe because it introduced three obstacle
collisions.

## Candidate

Use the existing `1.0 rad` sharp-turn boundary as a state-aware authority
handoff. When reverse avoidance is active, obstacle steering and path steering
have the same sign, and the path already requests a sharp turn, stop feeding
additional obstacle steering into its existing first-order filter:

```modelica
firstOrder.u = if speed_oa < 0 and steer_oa * unitDelay1.y > 0
  and abs(unitDelay1.y) > 1.0 then 0 else gain.y;
```

This preserves v80 behavior for straight obstacle approaches, moderate turns,
and opposing steering conflicts. It uses no track id, score signal, official
geometry, or new external port.

## Gates

1. Static deployability checker and targeted Python tests.
2. Track2 1 s translation/runtime gate.
3. Track2 fixed-solver 180 s completion gate with path, speed, steering, and
   score variables exported.
4. Expand unchanged to all four tracks only after an official finish or a
   material comparable gain without a collision regression.
5. On rejection, restore both candidate-touched source files exactly to the
   committed v80 hashes and retain negative evidence.

## Non-claims

- No official finish or 80/80 claim before runtime evidence.
- No physical UGV readiness claim.
- No official no-edit-area modification.

## Runtime result

The 1 s translation/runtime gate passed. The 180 s Track2 run remained inside
`SimulateModelEx` for about 10 minutes with no result artifact, while the
MWORKS process made only slow CPU progress. This is a runtime-efficiency
regression relative to v128/v129. The likely cause is repeated solver events
near the sharp-turn threshold. v130 is rejected as written and superseded by
v131, which preserves the same authority rule inside `noEvent(...)`.
