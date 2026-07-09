# Track1 Candidate Review - v59 Close-Side Initial Direction Guard

timestamp: 2026-07-10 CST
baseline: v48 opposing-steer guard
decision: rejected, source restored to v48 semantics

## Scope

v59 tested a narrow close-side direction guard in the avoid-lateral initial
state:

```text
Docs/Design/unified_obstacle_avoidance_v59_plan_20260710.md
References/research/reactive_gap_obstacle_avoidance_20260710/source_notes.md
```

The intent was to avoid repeating v58's broad side-gap bypass. v59 changed
initial steering direction only when one side was very close and did not
increase the magnitude beyond v48's `0.6`.

No official vehicle, road, sensor, scoring, example, or official material files
were intentionally modified.

## Static Gate

v59 source-only deployability gate:

```text
Results/evidence/controller_deployability_static_check_v59_close_side_initial_direction_20260710.md
Results/evidence/controller_deployability_static_check_v59_close_side_initial_direction_20260710.json
```

Result:

```text
ready_for_physical_claim=true
high=0
medium=0
```

Restored v48 source-only deployability gate:

```text
Results/evidence/controller_deployability_static_check_v48_restored_after_v59_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v59_20260710.json
```

Result:

```text
ready_for_physical_claim=true
high=0
medium=0
```

## Runtime Result

Track1 wrapper run:

```text
Results/simulations/controller_v59_close_side_initial_direction_saidao1_120s_20260710/
```

Comparison:

| Candidate | Track | Runtime | Exit | T/s | cR | cO | P | Decision |
|---|---|---|---:|---:|---:|---:|---:|---|
| v48 | 1 | `simulate_returned_true` | 0 | 120.0 | 2 | 0 | 9.2 | Keep as current best baseline. |
| v59 | 1 | `simulate_failed` with result variables | 2 | 3.85 | 0 | 0 | 10.0 | Reject: non-comparable early stop artifact. |

Analysis artifacts:

```text
Results/metrics/collision_window_analysis_v48_v59_track1_20260710.md
Results/metrics/signal_window_summary_v48_v59_track1_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_v59_track1_20260710.md
```

## Findings

- v59 did not produce a comparable Track1 completion run.
- The exported `P=10.0` is not accepted because the run stopped at `T=3.85`
  with `simulate_failed` / `exit_state=2`.
- This is another sign that changing the avoid-lateral initial direction can
  destabilize the wrapper rather than improve a full-track score.

## Decision

Reject v59. Restore v48 semantics and continue from v48.

Do not continue close-side initial-direction scans without a new mechanism
reason. The next productive work should either:

1. produce visual/trajectory evidence for the early road/obstacle contacts
   before another controller edit; or
2. shift to report/physical-transfer hardening while keeping v48 as current
   review-ready best.

No final submission package was created or sent.
