# v194 Lateral Release Continuity Plan

Status: candidate under validation

## Rationale

The current Track3 diagnosis shows that the longitudinal avoidance state can
produce a one-sample `flag=false` pulse while a side trigger is still active.
The outer lateral state interprets that pulse as a complete release and
restarts its fixed initial-turn state. That repeats a positive obstacle offset
against the negative path-recovery heading and causes the early road departure.

This candidate changes only the lateral release condition. It retains the
current front/side trigger, initial turn, dwell, speed, and allocator behavior;
it does not branch by track, time, score, or absolute position.

## Change

Replace the lateral transition condition:

```modelica
not flag
```

with:

```modelica
not flag and df > mindis and dl > 0.45 and dr > 0.45
```

The lateral state can release only when both the longitudinal flag and all
three clearance conditions indicate that the encounter is actually clear.

## Acceptance

1. Deployability checker has no high/medium findings.
2. All existing project tests pass.
3. Plain `SimulateModel` Track3 1 s probe passes.
4. Plain `SimulateModel` Track3 120 s run must either finish officially or
   show repeatable progress beyond the exact baseline without an earlier
   failure. Otherwise reject and restore the exact pre-candidate bytes.
5. Only a positive Track3 result may justify four-track screening.

## Evidence boundary

No result from this candidate may be treated as four-track completion, 80/80,
physical UGV success, or final submission readiness until the corresponding
official gates pass.
