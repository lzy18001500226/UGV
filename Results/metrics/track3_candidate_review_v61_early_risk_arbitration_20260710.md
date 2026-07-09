# Track3 Candidate Review: v61 Early Risk Arbitration

## Scope

- Candidate: `v61_early_risk_arbitration`
- Plan: `Docs/Design/unified_obstacle_avoidance_v61_plan_20260710.md`
- Source file tested: `Models/UGV/Control/ControlAllocate/package.mo`
- Target track: `UGV.Test.Saidao3Eval`
- Goal: improve the v48 Track3 early obstacle event without per-track logic,
  official-file edits, global steering-filter time changes, or another blind
  scalar scan.

No official vehicle, road, sensor, scoring, example, or official material files
were modified.

## Candidate Mechanism

v61 added a narrow allocation condition for active obstacle avoidance where the
path steering was small and opposed to obstacle steering:

```modelica
pathSmallOpposingAvoid =
  speed_oa < 0 and steer_oa * unitDelay1.y < 0 and
  abs(unitDelay1.y) < 0.12 and abs(steer_oa) >= 0.55;
```

When true, the candidate suppressed the small opposing path-steering term and
raised the obstacle-steering filter input from `gain.y` to `1.2 * gain.y`.

## Evidence

Static source gate:

```text
Results/evidence/controller_deployability_static_check_v61_early_risk_arbitration_20260710.md
Results/evidence/controller_deployability_static_check_v61_early_risk_arbitration_20260710.json
```

Runtime evidence:

```text
Results/simulations/controller_v61_early_risk_arbitration_saidao3_120s_20260710/
```

Offline analysis:

```text
Results/metrics/collision_window_analysis_v48_v61_track3_20260710.md
Results/metrics/collision_window_analysis_v48_v61_track3_20260710.json
Results/metrics/signal_window_summary_v48_v61_track3_20260710.md
Results/metrics/signal_window_summary_v48_v61_track3_20260710.json
```

Restoration evidence:

```text
Results/evidence/controller_deployability_static_check_v48_restored_after_v61_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v61_20260710.json
```

## Result

| Candidate | Track | Runtime | Exit | T/s | cR | cO | P | Decision |
|---|---|---|---:|---:|---:|---:|---:|---|
| v48 baseline | Track3 | simulate_failed with result variables | 2 | 112.45 | 1 | 1 | 9.2 | keep |
| v61 | Track3 | simulate_failed with result variables | 2 | 63.7 | 1 | 1 | 9.2 | reject |

Collision windows:

| Candidate | First obstacle event | Road event |
|---|---|---|
| v48 | `1.05 s`, `cO: 0 -> 1` | `4.85 s`, `cR: 0 -> 1` |
| v61 | `1.05 s`, `cO: 0 -> 1` | `4.25 s`, `cR: 0 -> 1` |

At the target `1.05 s` event, v61 increased the final steering command from
about `0.162` to about `0.193`, but the obstacle collision still occurred.
The road-collision event also moved earlier from `4.85 s` to `4.25 s`.

## Decision

Reject v61. It did not improve Track3 score, did not remove the early obstacle
event, and shortened the run versus v48. Because the target weak-track result
did not improve, Track1 and four-track regression were not run.

Restore v48 semantics and continue from v48 for the next evidence-backed
unified mechanism.

Do not continue this exact dynamic small-opposing-path boost unless new
evidence explains why a different bounded arbitration mechanism would avoid
the same `1.05 s` obstacle event without moving road collisions earlier.

This review does not create a submission package and does not claim physical
UGV success.
