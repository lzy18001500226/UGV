# Unified obstacle avoidance v131 plan

Status: runtime candidate superseding v130.

## Goal

Retain v130's evidence-backed same-direction sharp-turn authority handoff while
preventing the `1.0 rad` threshold from creating expensive continuous-solver
events.

## Candidate

```modelica
firstOrder.u = noEvent(if speed_oa < 0 and steer_oa * unitDelay1.y > 0
  and abs(unitDelay1.y) > 1.0 then 0 else gain.y);
```

`noEvent` changes solver event handling, not the requested control values. All
v80 behavior outside the same-direction sharp-turn state remains unchanged.

## Gates

1. Static checker and targeted tests.
2. Track2 1 s translation/runtime gate.
3. Track2 180 s fixed-solver gate must complete within a comparable bounded
   wall-clock window and export completion/collision/path/steering evidence.
4. Expand unchanged to all tracks only for a finish or material comparable
   gain without collision regression.
5. Restore committed v80 source exactly on rejection.

## Current result

The static checker passed with `high=0`, `medium=0`, and the targeted test suite
passed (`7 passed`). Runtime validation is inconclusive: three bounded 1 s
attempts stopped making progress inside `StartSysplorer` before model open,
check, or translation. Restarting only the stale Sysplorer client did not
restore the API channel. This is not evidence that v131 translates or fails to
translate.

The candidate source was removed and committed v80 was restored exactly while
the design remains pending runtime validation. Do not accept v131 or expand it
to other tracks until a fresh 1 s probe crosses the model-check gate.
