# Track3 Candidate Review - v58 Reactive Gap Initial Bypass

timestamp: 2026-07-10 CST
baseline: v48 opposing-steer guard
decision: rejected, source restored to v48 semantics

## Scope

v58 tested a compact reactive-gap idea inspired by:

```text
References/research/reactive_gap_obstacle_avoidance_20260710/MANIFEST.md
Docs/Design/unified_obstacle_avoidance_v58_plan_20260710.md
```

The change was limited to the obstacle controller startup lateral-avoid action:
when one side was clearly more open than the other, use a bounded stronger
initial bypass steering command; otherwise keep v48's default `steer := 0.6`.

No official vehicle, road, sensor, scoring, example, or official material files
were intentionally modified.

## Static Gate

v58 source-only deployability gate:

```text
Results/evidence/controller_deployability_static_check_v58_reactive_gap_initial_bypass_20260710.md
Results/evidence/controller_deployability_static_check_v58_reactive_gap_initial_bypass_20260710.json
```

Result:

```text
ready_for_physical_claim=true
high=0
medium=0
```

Restored v48 source-only deployability gate:

```text
Results/evidence/controller_deployability_static_check_v48_restored_after_v58_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v58_20260710.json
```

Result:

```text
ready_for_physical_claim=true
high=0
medium=0
```

These are source/static checks only. They do not prove MWORKS runtime
completion or physical UGV behavior.

## Runtime Result

Track3 wrapper run:

```text
Results/simulations/controller_v58_reactive_gap_initial_bypass_saidao3_120s_20260710/
```

Comparison:

| Candidate | Track | Runtime | Exit | T/s | cR | cO | P | Decision |
|---|---|---|---:|---:|---:|---:|---:|---|
| v48 | 3 | `simulate_failed` with result variables | 2 | 112.45 | 1 | 1 | 9.2 | Keep as current best baseline. |
| v58 | 3 | `simulate_failed` with result variables | 2 | 38.80 | 0 | 3 | 8.8 | Reject: lower score and more obstacle collisions. |

Analysis artifacts:

```text
Results/metrics/collision_window_analysis_v48_v58_track3_20260710.md
Results/metrics/signal_window_summary_v48_v58_track3_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_v58_track3_20260710.md
```

## Findings

- v58 removed the v48 Track3 road-collision event in the saved score variables.
- It added two later obstacle collisions, raising Track3 obstacle collisions
  from `1` to `3` and lowering score from `9.2` to `8.8`.
- At the first collision, both v48 and v58 still collide at `1.05 s`, so this
  mechanism does not solve the early unavoidable/near-ambiguous obstacle event.
- At later events, stronger side-opening bypass can trade road-edge safety for
  obstacle collisions. This is not acceptable for a unified four-track
  controller.

## Decision

Reject v58. Restore v48 semantics and continue from v48.

Do not continue the same "stronger initial side-gap bypass" route without a
new mechanism reason. A next candidate should inspect whether the problem is
better handled by:

1. a short bounded speed/steer coordination window tied to confirmed obstacle
   collision risk, not a side-gap sign flip;
2. a collision-window-specific controller attribution around Track1/Track4
   road-edge collisions; or
3. a report/physical-transfer task if score tuning returns diminishing gains.

No final submission package was created or sent.
