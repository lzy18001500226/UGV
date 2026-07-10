# Track1/Track4 Candidate Review: v71/v72 Steering Authority

Status: rejected_mixed_or_regressive, 2026-07-10 CST.

## Decision

Reject v71 and v72 as accepted controller baselines. Keep v48 as the current
review-ready best source semantics.

v71 is still useful evidence: severe-side steering authority can remove one
Track1 road collision. It is not accepted because the same source change
regresses Track4 and lowers total score.

v72 is rejected because a narrower control-allocation-only path-authority
branch did not preserve the Track1 gain and caused an early terminal state.

## Baseline

Current accepted baseline before these tests:

```text
v48 opposing-steer guard
Track1: T=120.0, cR=2, cO=0, P=9.2
Track2: T=60.15, cR=1, cO=0, P=9.6
Track3: T=112.45, cR=1, cO=1, P=9.2
Track4: T=112.4, cR=2, cO=0, P=9.2
Total wrapper P = 37.2 / 40
```

## Candidate Evidence

Plans:

```text
Docs/Design/unified_obstacle_avoidance_v71_plan_20260710.md
Docs/Design/unified_obstacle_avoidance_v72_plan_20260710.md
```

Static gates:

```text
Results/evidence/controller_deployability_static_check_v71_severe_left_steer_authority_20260710.md
Results/evidence/controller_deployability_static_check_v72_narrow_opposing_path_authority_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v71_v72_20260710.md
```

Runs:

```text
Results/simulations/controller_v71_severe_left_steer_authority_saidao1_120s_20260710/
Results/simulations/controller_v71_severe_left_steer_authority_saidao4_120s_20260710/
Results/simulations/controller_v72_narrow_opposing_path_authority_saidao1_120s_20260710/
```

Analysis:

```text
Results/metrics/collision_window_analysis_v48_v71_track1_track4_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_v71_track1_track4_20260710.md
Results/metrics/signal_window_summary_v48_v71_track1_track4_20260710.md
Results/metrics/collision_window_analysis_v48_v72_track1_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_v72_track1_20260710.md
```

## Results

| Candidate | Track | Runtime | Exit | T/s | cR | cO | P | Decision |
|---|---|---|---:|---:|---:|---:|---:|---|
| v48 | Track1 | simulate_returned_true | 0 | 120.0 | 2 | 0 | 9.2 | Baseline |
| v71 | Track1 | simulate_returned_true | 0 | 120.0 | 1 | 0 | 9.6 | Local improvement |
| v48 | Track4 | simulate_failed with result variables | 2 | 112.4 | 2 | 0 | 9.2 | Baseline |
| v71 | Track4 | simulate_returned_true | 0 | 120.0 | 2 | 1 | 8.8 | Reject: obstacle regression |
| v72 | Track1 | simulate_failed with result variables | 2 | 53.55 | 2 | 0 | 9.2 | Reject: no gain, early terminal |

## Interpretation

v71 shows that the second Track1 road collision can be removed by increasing
active obstacle steering in severe left-side clearance windows. However, doing
that inside the obstacle controller changes downstream trajectory on Track4,
introduces an obstacle collision near `94.6 s`, and lowers Track4 from `P=9.2`
to `P=8.8`.

v72 tried to avoid expanding the `ControlAllocate` interface by targeting the
Track1 path/avoidance cancellation window using only existing allocation
signals. That narrower branch did not improve Track1 and shortened the run to
`T=53.55`, so the approach is rejected.

## Current Source State

Source semantics were restored to v48 after v71/v72:

```text
obstacle-controller v13 side trigger
PathPlanner v45 curvature speed cap
ControlAllocate v48 opposing-steer guard
```

Restored static gate:

```text
Results/evidence/controller_deployability_static_check_v48_restored_after_v71_v72_20260710.md
```

## Next Work

Do not retry:

- global obstacle-controller steering boost;
- lower path-authority scalar scans;
- allocation-only branch without side-distance context.

The next evidence-backed route should inspect whether a deployable side-risk
gate can be added without a broad interface expansion, or shift to another
weakness such as Track3 obstacle/front-risk geometry. Any new candidate still
must be one unified algorithm across tracks.

## Non-Claims

- This review does not claim final competition score.
- This review does not claim physical UGV success.
- This review does not authorize package creation or final submission.
