# v120 Lateral State Continuity Plan

Status: planned candidate, not accepted

## Evidence

The restored v80 Track3 diagnostic shows that the longitudinal state leaves
`avoid` every two seconds and re-enters it one 0.01 s sample later while a side
distance is still below `0.45` m.  The outer lateral state currently treats
that one-sample `flag=false` pulse as a real obstacle-clear event.

Consequently, the lateral controller repeatedly restarts its fixed `+0.6`
initial-turn state instead of remaining in the gap-directed state after the
first two seconds.  In the saved Track3 run, `steer_oa` has no sign changes and
the vehicle advances through path segments while its negative path-heading
command is repeatedly cancelled by the positive obstacle command.

This mechanism is distinct from rejected candidates:

- v41 held the longitudinal reverse state until every distance was clear;
- v85 shortened the fixed initial-turn duration;
- v91 changed the first-turn direction;
- v94/v118/v119 changed obstacle/path steering arbitration.

## Candidate

Keep the v80 longitudinal state, first-turn value, dwell durations, gap rules,
speed rules, and control allocation unchanged.  Change only the outer lateral
release condition so a one-sample `flag=false` pulse does not reset the lateral
state while an obstacle-side trigger remains active:

```modelica
not flag and df > mindis and dl > 0.45 and dr > 0.45
```

This preserves the initial fixed turn for a new encounter, but lets the
existing gap-directed lateral substate continue across the longitudinal
two-second pulse.

## Gates

1. Controller deployability checker and targeted tests pass.
2. A 1 s Track3 load/check/simulate probe succeeds.
3. A 120 s Track3 run must avoid a new early stop and show either official
   completion or material repeatable progress beyond the restored v80 result.
4. Only after Gate 3 improves may the candidate expand to the other tracks.
5. On failure, restore the exact v80 transition and retain only review evidence.
