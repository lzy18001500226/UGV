# Unified obstacle avoidance v131 plan

Status: rejected after bounded Track2 long-run gate.

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

## Result

The recovery state was cleared without restoring the old backup. An unchanged
v80 Track2 1 s probe then passed load, check, and simulation. v131 subsequently
passed its static gate (`high=0`, `medium=0`), targeted tests (`7 passed`), and
the Track2 1 s translation/runtime gate with `simulate_returned_true` and
`exit_state=0`.

The decisive Track2 180 s fixed-solver gate did not finish within the bounded
eight-minute wall-clock budget and produced no `metrics.json` or score export.
Its dedicated Sysplorer process tree was stopped after the timeout. Therefore
`noEvent` did not remove the long-run runtime-efficiency regression observed in
v130. v131 is rejected, is not expanded to other tracks, and
`Models/UGV/Control/ControlAllocate/package.mo` is restored exactly to committed
v80.

See `Results/metrics/track2_candidate_review_v131_noevent_handoff_20260712.md`.
