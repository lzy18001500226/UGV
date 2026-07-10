# Track3 Candidate Review - v84 Initial-Lane Y Bias

Status: rejected_target_track_early_stop, 2026-07-10 CST

## Candidate

v84 started from accepted v80 and tested a unified initial-lane safety bias in
`PathPlanner`: during the first 6 seconds and only while the vehicle y position
was in the lower start-lane band, pure-pursuit used `effective_y = y - 0.20`.

The intent was to lift the early trajectory away from the bottom road edge and
the first Track3 obstacle before the obstacle overlay reacts.

## Baseline

Accepted current local wrapper baseline remains v80:

```text
Track3 v80: T=59.4, cR=1, cO=1, P=9.2, simulate_failed / exit_state=2
Total v80 wrapper score: 38.0
```

## Evidence

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v84_plan_20260710.md
```

Static source gate before runtime:

```text
Results/evidence/controller_deployability_static_check_v84_initial_lane_y_bias_20260710.md
ready_for_physical_claim=true, high=0, medium=0
```

Target run:

```text
Results/simulations/controller_v84_initial_lane_y_bias_saidao3_120s_20260710/
```

Recorded result variables:

```text
runtime_status=simulate_failed
simulation_exit_state=2
T=1.2
cR=0
cO=1
P=9.6
```

Restore gate after rejecting v84:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v84_20260710.md
ready_for_physical_claim=true, high=0, medium=0
```

## Decision

Reject v84. The apparent `P=9.6` is not comparable because the run terminated
at `T=1.2 s` after an obstacle event. It does not prove score improvement and
is worse than v80/v83 as a target-track gate.

Source semantics were restored to v80 after this review.

## Lesson

The first-second Track3 obstacle event is sensitive to small initial trajectory
reference changes. Do not continue broad initial-lane y-bias scans from this
form. A future trajectory-level mechanism needs a less abrupt, source-grounded
approach, or should be preceded by offline trajectory simulation showing it
does not cause an immediate obstacle threshold crossing.

## Non-Claims

- No final score improvement is claimed.
- No physical UGV success is claimed.
- No report/package readiness change is claimed.
