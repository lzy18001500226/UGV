# Track2 candidate review: v130 and v131 steering handoff

## Decision

- v130 is rejected because its 180 s run remained inside the solver for about
  10 minutes without producing result artifacts, a material runtime-efficiency
  regression relative to recent candidates.
- v131 is not accepted or rejected on algorithm behavior. Its static gate
  passed, but runtime remained blocked in `StartSysplorer` before model check.
- The working source is restored exactly to committed v80.

## Gates

| candidate | static | 1 s runtime | 180 s runtime | decision |
|---|---|---|---|---|
| v130 eventful handoff | pass | pass | no result after bounded ~10 min | reject |
| v131 `noEvent` handoff | pass | blocked before model open/check | not run | pending runtime validation |

v130 1 s evidence:

```text
Results/simulations/controller_v130_same_direction_handoff_saidao2_1s_20260712/
simulate_returned_true, exit_state=0
```

v130 bounded long-run evidence:

```text
Results/simulations/controller_v130_same_direction_handoff_saidao2_180s_20260712/
```

v131 connection attempts:

```text
Results/simulations/controller_v131_noevent_handoff_saidao2_1s_20260712/
Results/simulations/controller_v131_noevent_handoff_saidao2_1s_retry2_20260712/
Results/simulations/controller_v131_noevent_handoff_saidao2_1s_retry3_20260712/
```

Each v131 attempt reached Python module import and then remained in
`StartSysplorer`; none reached `open_model_file`, `check_model`, or simulation.

## Recovery cursor

On a healthy Sysplorer API channel, first run an unchanged v80 1 s control
probe. Only if that passes should v131 be reapplied from its design and tested.
Do not diagnose v131 syntax from the current connection blocker.

The follow-up unchanged-v80 control probe identified the concrete blocker as a
Sysplorer `自动恢复` modal rather than login or candidate code. See
`Results/evidence/sysplorer_auto_recovery_blocker_v80_20260712.md`. Discarding
or restoring the listed backup requires a user decision before runtime work
continues.

## Non-claims

- No official finish.
- No score improvement.
- No v131 runtime validation.
- No physical UGV readiness.
