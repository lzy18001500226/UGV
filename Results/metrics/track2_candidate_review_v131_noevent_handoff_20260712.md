# Track2 Candidate Review: v131 No-Event Same-Direction Handoff

## Decision

Rejected. The candidate translated and completed its one-second runtime gate,
but failed the decisive bounded long-run efficiency gate. No four-track
expansion was run.

## Candidate

`v131` replaces the direct obstacle-steering connection with:

```modelica
firstOrder.u = noEvent(if speed_oa < 0 and steer_oa * unitDelay1.y > 0
  and abs(unitDelay1.y) > 1.0 then 0 else gain.y);
```

The intended change was to preserve v130's same-direction sharp-turn handoff
while preventing repeated threshold events from making the long simulation
unusable.

## Recovery And Gates

| gate | result | evidence |
|---|---|---|
| unchanged v80 Track2 1 s recovery control | pass: load/check/simulate, `exit_state=0` | `Results/simulations/controller_v80_recovery_control_saidao2_1s_20260712_0348/metrics.json` |
| v131 static deployability | pass: `high=0`, `medium=0` | `Results/evidence/controller_deployability_static_check_v131_20260712.md` |
| targeted tests | pass: `7 passed` | command output for `python -m pytest Scripts/tests -q` |
| v131 Track2 1 s | pass: `simulate_returned_true`, `exit_state=0`, score variables present | `Results/simulations/controller_v131_noevent_handoff_saidao2_1s_recovery_20260712_0351/metrics.json` |
| v131 Track2 180 s | reject: no return, metrics, or export before eight-minute wall-clock limit | `Results/simulations/controller_v131_noevent_handoff_saidao2_180s_20260712_0354/` |

The long run was terminated only after verifying that its dedicated process
tree belonged to this request (`v131-track2-180-20260712-0354`). Existing
Sysplorer sessions were not restarted.

## Restore

`Models/UGV/Control/ControlAllocate/package.mo` is restored exactly to the
committed v80 hash `47f679f14b9af888f8565eb91c55d2bdeeac6f77`.

## Non-Claims

- No official Track2 finish.
- No score improvement.
- No four-track validation.
- No physical UGV readiness claim.
