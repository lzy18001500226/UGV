# Track2 Candidate Review - v126 Severe-Side Guard

Status: rejected and v80 source restored, 2026-07-11 CST.

## Candidate

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v126_plan_20260711.md
```

v126 kept full `-1` obstacle authority for front danger or severe side squeeze
(`dl <= 0.12` or `dr <= 0.12`) and used v125's `-0.4` only for moderate
side-triggered avoidance.

## Gates

Static and targeted test gates passed:

```text
Results/evidence/controller_deployability_static_check_v126_severe_side_guard_20260711.md
ready_for_physical_claim=true, high=0, medium=0
pytest: 7 passed
```

Track2 1 s translation gate passed:

```text
Results/simulations/controller_v126_severe_side_guard_saidao2_1s_20260711/
simulate_returned_true, T=1.0, cR=0, cO=0, P=10.0
```

Track2 completion gate:

```text
Results/simulations/controller_v126_severe_side_guard_saidao2_120s_20260711/
simulate_returned_true / exit_state=0
T=120.0, cR=1, cO=0, P=9.6
distanceSensor1.d=850.20967756104
completion=simulation_horizon_reached_finish_not_observed
```

Comparison with restored v80 Track2:

```text
T=120.0, cR=1, cO=0, P=9.6
distanceSensor1.d=813.7304349381575
completion=simulation_horizon_reached_finish_not_observed
```

## Decision

Reject v126. It produced no official finish, no collision/score improvement,
and a worse end distance than v80. Do not expand it to the other tracks.

v125-v126 jointly reject the current four-distance longitudinal-tier family:
relaxing persistent side-triggered reverse authority can remove the low-speed
symptom, but it does not preserve route direction or produce completion. The
next mechanism should establish path/heading consistency through a separately
reviewed interface or state design rather than continue side-brake scalar or
threshold scans.

## Non-Claims

- No official finish or 80/80 score.
- No physical UGV success.
- No report, package, or submission readiness claim.
- No official no-edit-zone changes.
