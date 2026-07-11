# Track2 Candidate Review - v127 Transient Steering

Status: rejected and v80 source restored, 2026-07-11 CST.

## Candidate

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v127_plan_20260711.md
```

v127 replaced the persistent low-pass obstacle-heading offset with a 2 s
washout contribution:

```text
avoid_transient = factor_oa * steer_oa - lowpass(factor_oa * steer_oa)
```

The intent was to retain initial obstacle correction while allowing the path
heading to recover after a sustained avoidance request.

## Gates

Static and targeted test gates passed before runtime:

```text
ready_for_physical_claim=true, high=0, medium=0
pytest: 7 passed
```

The first 120 s retry exposed a zero-filled working-copy corruption in
`ObsAvoidController_Sysblock2.mo`. The file contained 59,365 NUL bytes and
could not define the referenced controller type. Its valid committed v80 blob
was restored and verified by Git hash before rerunning the gates.

Recovered Track2 1 s translation gate:

```text
Results/simulations/controller_v127_transient_steer_saidao2_1s_recovered_20260711/
simulate_returned_true, exit_state=0
T=1.0, cR=0, cO=0, P=10.0
distanceSensor1.d=1.7698060828732471
```

Recovered Track2 120 s completion gate:

```text
Results/simulations/controller_v127_transient_steer_saidao2_120s_recovered_20260711/
simulate_returned_true, exit_state=0
T=120.0, cR=0, cO=3, P=8.8
distanceSensor1.d=859.937808638337
completion=simulation_horizon_reached_finish_not_observed
```

Comparison with v80 Track2:

```text
T=120.0, cR=1, cO=0, P=9.6
distanceSensor1.d=813.7304349381575
completion=simulation_horizon_reached_finish_not_observed
```

## Decision

Reject v127. It produced no official finish, introduced three obstacle
collisions, reduced `P` by 0.8, and ended farther from the finish than v80.
Do not expand it to the other tracks. The result rejects a simple washout of
the avoidance heading as the next completion mechanism; path/heading recovery
needs state-aware arbitration or a reviewed path interface rather than decay
of the only obstacle correction.

Sysplorer also added trailing spaces to the restored controller source during
the runtime probe. That formatting-only drift was removed after the run, and
both candidate-touched source files were restored to their committed hashes.

## Restored Gate

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v127_20260711.md
ready_for_physical_claim=true, high=0, medium=0
pytest: 7 passed
```

## Non-Claims

- No official finish or 80/80 score.
- No physical UGV success.
- No report, package, or submission readiness claim.
- No official no-edit-zone changes.
