# Track3 Candidate Review: v54 Path Authority 0.35

Status: rejected_target_track_runtime_regression, 2026-07-10 CST

## Candidate

v54 continued from the current accepted v48 candidate and tested a narrower
path-authority handoff in `ControlAllocate`:

```modelica
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0
  then 0.35 * unitDelay1.y
  else unitDelay1.y;
```

The change was one unified mechanism. It did not branch on track name, wrapper
name, run id, score variables, or official model internals.

## Evidence

Design plan:

```text
Docs/Design/unified_obstacle_avoidance_v54_plan_20260710.md
```

Pre-change static gate:

```text
Results/evidence/controller_deployability_static_check_v48_pre_v54_20260710.md
```

Candidate static gate:

```text
Results/evidence/controller_deployability_static_check_v54_path_authority_035_20260710.md
```

Target run:

```text
Results/simulations/controller_v54_path_authority_035_saidao3_120s_20260710/
```

Post-run analysis:

```text
Results/metrics/collision_window_analysis_v48_v54_track3_20260710.md
Results/metrics/signal_window_summary_v48_v54_track3_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_v54_track3_20260710.md
```

Restored-source gate:

```text
Results/evidence/controller_deployability_static_check_v48_restored_after_v54_20260710.md
```

## Result

| Candidate | Runtime | Exit | T/s | cR | cO | P |
|---|---|---:|---:|---:|---:|---:|
| v48 Track3 | simulate_failed with result variables | 2 | 112.45 | 1 | 1 | 9.2 |
| v54 Track3 | simulate_failed with result variables | 2 | 7.3 | 1 | 1 | 9.2 |

v54 does not improve Track3 score or collision count and produces a much
earlier terminal state. It therefore does not qualify for Track1 regression or
four-track expansion.

## Interpretation

The target Track3 events remain:

- first obstacle event near `1.05 s`
- road event near `5.1 s`

The v54 control-allocation change slightly increases final steer at the early
events, but it does not remove the obstacle collision and severely shortens the
run. This suggests the remaining weakness is not solved by further lowering the
path contribution between v48's `0.5` and v53's `0`.

## Decision

Reject v54 and keep v48 as the current review-ready best candidate.

Do not continue this path-authority scalar between `0.5` and `0` without a new
mechanism reason. The next work should inspect the obstacle-controller
initial/avoid-state structure and front-risk geometry rather than tuning the
same ControlAllocate scalar again.

## Non-Claims

- This review does not claim final competition score.
- This review does not claim physical UGV success.
- This review does not authorize final package creation or submission.
