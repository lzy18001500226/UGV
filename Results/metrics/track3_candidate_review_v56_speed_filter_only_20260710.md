# Track3 Candidate Review - v56 Speed Filter Only

timestamp: 2026-07-10 CST
baseline: v48 opposing-steer guard
candidate: v56 obstacle-avoidance speed-filter-only acceleration
decision: rejected

## Candidate Change

File changed:

```text
Models/UGV/Control/ControlAllocate/package.mo
```

Change tested:

```modelica
firstOrder1(T=1) -> firstOrder1(T=0.5)
```

Only the obstacle-avoidance speed channel was changed. The obstacle-avoidance
steering filter, v48 opposing-steer guard, path planner, official tracks, and
scoring models remained unchanged.

## Static Gate

```text
Results/evidence/controller_deployability_static_check_v56_speed_filter_only_20260710.md
ready_for_physical_claim=true
high=0
medium=0
```

## Runtime Evidence

Track3 target run:

```text
Results/simulations/controller_v56_speed_filter_only_saidao3_120s_20260710/
```

Recorded result variables:

| Candidate | Track | T | cR | cO | P | Runtime |
|---|---|---:|---:|---:|---:|---|
| v48 baseline | Saidao3Eval | 112.45 | 1 | 1 | 9.2 | simulate_failed with result variables |
| v56 | Saidao3Eval | 54.45 | 1 | 1 | 9.2 | simulate_failed with result variables |

## Decision

Reject v56. It did not improve Track3 collision count or score and shortened
the readable run versus v48. Because target evidence regressed, v56 should not
be expanded to Track1 or four-track regression.

## Follow-Up Direction

Restore v48 semantics. Do not continue filter-time scans unless a fresh
mechanism explains why a different filter structure would address both the
early obstacle collision and later road collision without creating early stop.
