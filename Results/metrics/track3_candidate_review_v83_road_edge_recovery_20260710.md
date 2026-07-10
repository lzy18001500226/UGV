# Track3 Candidate Review - v83 Road-Edge Recovery

Status: rejected_as_score_candidate, 2026-07-10 CST

## Candidate

v83 tested a narrow road-edge recovery branch in `avoid_lateral.ini_state`:
when `df < 0.15`, it steered away from the closer side instead of using the
accepted v80 fixed initial lateral steer.

## Baseline

Accepted current local wrapper baseline remains v80 sharp curve speed cap:

```text
Track3 v80: T=59.4, cR=1, cO=1, P=9.2, simulate_failed / exit_state=2
Total v80 wrapper score: 38.0
```

## Evidence

Runtime target gate:

```text
Results/simulations/controller_v83_road_edge_recovery_saidao3_120s_20260710/
```

Recorded score variables:

```text
Track3 v83: T=120.0, cR=1, cO=1, P=9.2
runtime_status=simulate_returned_true
simulation_exit_state=0
```

Static deployability gate for the v83 source:

```text
Results/evidence/controller_deployability_static_check_v83_road_edge_recovery_20260710.md
ready_for_physical_claim=true, high=0, medium=0
```

Restore gate after rejecting v83:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v83_20260710.md
ready_for_physical_claim=true, high=0, medium=0
```

The large diagnostic file
`Results/simulations/controller_v83_road_edge_recovery_saidao3_120s_20260710/extra_timeseries.csv`
is intentionally kept local and exact-ignored because it is larger than the
GitHub file limit. The manifest, metrics, score timeseries, and result-variable
summary remain the portable evidence.

## Decision

v83 is not accepted as a new score baseline. It improves runtime comparability
on Track3 versus v80, but it does not improve `P`, road collisions, or obstacle
collisions:

```text
v80 Track3: P=9.2, cR=1, cO=1
v83 Track3: P=9.2, cR=1, cO=1
```

The source semantics were restored to v80 after this review.

## Next Direction

Continue from v80. Do not retry this same `df < 0.15` road-edge recovery branch
or nearby sign flip without new failure-window evidence showing a score-bearing
road collision that this mechanism can remove without preserving the obstacle
collision.
