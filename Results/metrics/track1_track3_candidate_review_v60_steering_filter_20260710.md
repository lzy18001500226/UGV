# v60 Steering Filter Candidate Review

Status: rejected, 2026-07-10 CST.

## Candidate

Starting point: v48 opposing-steer guard.

Change tested:

```modelica
Modelica.Blocks.Continuous.FirstOrder firstOrder(T=0.35)
```

This changed only the obstacle-steering first-order filter in
`Models/UGV/Control/ControlAllocate/package.mo`.

## Reason For Test

The v48 geometry and signal evidence showed Track3's first obstacle collision
occurred after the obstacle controller had requested `steer_oa=0.6`, but
`ctrlAlloc.steer` was still only about `0.162`. The hypothesis was that the
obstacle-steering command was being established too slowly by `FirstOrder(T=1)`.

Evidence basis:

- `Results/metrics/trajectory_geometry_review_v48_20260710.md`
- `Results/metrics/signal_geometry_window_summary_v48_20260710.md`
- `Docs/Design/unified_obstacle_avoidance_v60_plan_20260710.md`

## Runtime Evidence

| Track | Run | Runtime status | T | cR | cO | P | Interpretation |
|---|---|---|---:|---:|---:|---:|---|
| Track3 | `Results/simulations/controller_v60_steering_filter_saidao3_120s_20260710/` | service communication failed after simulate; no result variables |  |  |  |  | Not accepted; no score evidence. |
| Track3 retry | `Results/simulations/controller_v60_steering_filter_saidao3_120s_20260710_retry1/` | service communication failed after simulate; no result variables |  |  |  |  | Same failure on bounded retry. |
| Track1 | `Results/simulations/controller_v60_steering_filter_saidao1_120s_20260710/` | `simulate_failed` with result variables | 5.3 | 1 | 0 | 9.6 | Early-stop/non-comparable result; worse than v48 as accepted evidence. |

Static deployability before the run passed:

- `Results/evidence/controller_deployability_static_check_v60_steering_filter_20260710.md`

After rejection, the source was restored to v48 semantics and static check passed:

- `Results/evidence/controller_deployability_static_check_v48_restored_after_v60_20260710.md`

## Decision

Reject v60.

Reasons:

1. Track1 produced an early-stop/non-comparable result, so it cannot supersede
   v48's `T=120.0`, `cR=2`, `cO=0`, `P=9.2` evidence.
2. Track3 did not produce readable score variables after two bounded attempts.
3. Directly shortening the obstacle-steering first-order filter is too risky as
   a shared four-track mechanism.

## Next Direction

Do not continue scanning `firstOrder(T=...)` values without a new mechanism.
The next candidate should still be evidence-driven, but should avoid broad
actuator response changes. Safer directions:

- event-window trajectory interpretation around v48 Track3 first obstacle;
- obstacle-side initial steering arbitration that preserves Track1 road margin;
- controller-local state logic that changes only the first high-risk obstacle
  phase, without per-track names or official model edits.

This review does not claim final competition or physical UGV readiness.
