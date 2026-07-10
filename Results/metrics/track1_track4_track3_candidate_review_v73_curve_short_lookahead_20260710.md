# v73 Curve-Short-Lookahead Candidate Review

Status: rejected_as_accepted_baseline, 2026-07-10 CST

## Candidate

v73 tested a unified path-planner geometry mechanism from v48:

```text
Models/UGV/Control/PathPlanning/PathPlanner.mo
```

Mechanism:

- keep v48 obstacle-controller and allocation semantics;
- keep v45/v48 curvature speed cap;
- add a temporary short-lookahead recomputation when the first pure-pursuit
  steering angle is above `0.35 rad`;
- use `curve_short_lookahead_factor=0.65` and
  `curve_short_lookahead_min=1.2`.

The source was restored to v48 semantics after this review.

## Evidence Basis

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v73_plan_20260710.md
```

Geometry diagnosis:

```text
Results/metrics/trajectory_geometry_review_v48_all_tracks_20260710.md
Results/figures/trajectory_geometry_review_v48_all_tracks_20260710/
```

Static gates:

```text
Results/evidence/controller_deployability_static_check_v73_curve_short_lookahead_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v73_20260710.md
```

Simulation runs:

```text
Results/simulations/controller_v73_curve_short_lookahead_saidao1_120s_20260710/
Results/simulations/controller_v73_curve_short_lookahead_saidao2_120s_20260710/
Results/simulations/controller_v73_curve_short_lookahead_saidao3_120s_20260710/
Results/simulations/controller_v73_curve_short_lookahead_saidao4_120s_20260710/
```

## Score Summary

| Track | v48 T | v48 cR | v48 cO | v48 P | v73 T | v73 cR | v73 cO | v73 P | Decision |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Saidao1Eval | 120.00 | 2 | 0 | 9.2 | 17.40 | 1 | 0 | 9.6 | Local score improved, but early terminal caveat remains. |
| Saidao2Eval | 60.15 | 1 | 0 | 9.6 | 120.00 | 1 | 0 | 9.6 | Non-regressive. |
| Saidao3Eval | 112.45 | 1 | 1 | 9.2 | 120.00 | 2 | 1 | 8.8 | Regressed. |
| Saidao4Eval | 112.40 | 2 | 0 | 9.2 | 120.00 | 2 | 0 | 9.2 | Non-regressive and cleaner runtime. |
| Total | - | - | - | 37.2 | - | - | - | 37.2 | No total gain. |

## Interpretation

v73 confirms that changing pursuit geometry can affect the road-edge weak
events: Track1 improved from `P=9.2` to `P=9.6`, and Track4 remained at
`P=9.2` with a clean `simulate_model=true` run.

The same unconditional short-lookahead mechanism is not safe enough as a
four-track baseline because Track3 regressed from `P=9.2` to `P=8.8` and
increased road collision count from `cR=1` to `cR=2`.

## Decision

Reject v73 as the accepted baseline.

Current accepted baseline remains:

```text
v48 opposing-steer guard, total wrapper score 37.2
```

Do not continue unconditional short-lookahead scans. If revisiting this family,
the next mechanism needs a guard that separates road-edge curve cutting from
Track3's obstacle/startup geometry, rather than applying the same shortened
pursuit distance to every large-steering state.

## Non-Claims

- This does not improve the accepted total score.
- This does not prove final competition score.
- This does not prove physical UGV behavior.
- This did not edit official road, vehicle, sensor, scoring, example, or track
  files.
