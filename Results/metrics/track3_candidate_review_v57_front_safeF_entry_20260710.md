# Track3 Candidate Review - v57 Front SafeF Entry

timestamp: 2026-07-10 CST
baseline: v48 opposing-steer guard
candidate: v57 front-risk entry with `safeF`
decision: rejected

## Candidate Change

File changed:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Change tested:

```modelica
transition(cruise, avoid, df <= mindis or dl <= 0.45 or dr <= 0.45, reset = false)
  -> transition(cruise, avoid, df <= safeF or dl <= 0.45 or dr <= 0.45, reset = false)
```

This retested earlier front-risk entry under the current v48 allocator, without
changing official tracks, scoring, path planner, reverse speed, filters, or
path-authority weighting.

## Static Gate

```text
Results/evidence/controller_deployability_static_check_v57_front_safeF_entry_20260710.md
ready_for_physical_claim=true
high=0
medium=0
```

## Runtime Evidence

Track3 target run:

```text
Results/simulations/controller_v57_front_safeF_entry_saidao3_120s_20260710/
```

Recorded result variables:

| Candidate | Track | T | cR | cO | P | Runtime |
|---|---|---:|---:|---:|---:|---|
| v48 baseline | Saidao3Eval | 112.45 | 1 | 1 | 9.2 | simulate_failed with result variables |
| v57 | Saidao3Eval | 55.35 | 1 | 1 | 9.2 | simulate_failed with result variables |

## Decision

Reject v57. It did not improve Track3 collision count or score and shortened
the readable run versus v48. Because target evidence regressed, v57 should not
be expanded to Track1 or four-track regression.

## Follow-Up Direction

Restore v48 semantics. The v55-v57 sequence rules out three simple mechanisms
for the current Track3 weakness:

- low-speed path lookahead floor;
- speed-channel-only faster obstacle deceleration;
- simple front-threshold pretrigger under v48 allocation.

The next direction should use a fresh mechanism, likely a more explicit
front-risk/side-risk state or trajectory-level analysis, rather than another
single-threshold or single-filter scan.
