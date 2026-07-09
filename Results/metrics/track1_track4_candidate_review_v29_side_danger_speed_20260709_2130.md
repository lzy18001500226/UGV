# Track1 / Track4 Candidate Review - v29 Side-Danger Speed Regulation

Generated: 2026-07-09 CST

## Scope

Candidate:

```text
v29_side_danger_speed_regulation
```

Strategy source:

```text
Docs/Design/high_score_optimization_strategy_20260709.md
```

Allowed edit target:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

No official no-edit zone was modified.

## Mechanism Hypothesis

v13 already detects side risk through:

```modelica
df <= mindis or dl <= 0.45 or dr <= 0.45
```

The v29 hypothesis was that, once avoid mode is active and either side distance
is in a severe danger band, reducing avoid-mode speed could lower road-contact
exposure without adding more steering fight. This was tested as a mechanism
candidate after v14-v28 scalar and allocator routes failed to improve the weak
tracks reliably.

## Static Gate

Static deployability check passed before runtime testing:

```text
Results/evidence/controller_deployability_static_check_v29_side_danger_speed_20260709_2105.md
```

Checker summary:

```text
ready_for_physical_claim=true
high=0
medium=0
```

This only proves the source-level gate; it does not prove race score or
physical UGV readiness.

## Runtime Evidence

| Track | Model | Runtime status | Exit state | T/s | Road cR | Obstacle cO | Score P | Evidence |
|---|---|---|---:|---:|---:|---:|---:|---|
| 1 | `UGV.Test.Saidao1Eval` | `simulate_returned_true` | 0 | 120.0 | 3 | 0 | 8.8 | `Results/simulations/controller_v29_side_danger_speed_saidao1_120s_20260709_2105/` |
| 4 | `UGV.Test.Saidao4Eval` | `simulate_returned_true` | 0 | 120.0 | 3 | 0 | 8.8 | `Results/simulations/controller_v29_side_danger_speed_saidao4_120s_20260709_2115/` |

The evidence folders contain `metrics.json`, score timeseries, extra timeseries,
probe steps, result-variable summaries, and manifests.

## Comparison Against Accepted v13

Accepted v13 reference:

```text
Results/metrics/four_track_summary_v13_side_trigger045_20260709_1535.md
```

| Track | v13 P | v13 collisions | v29 P | v29 collisions | Decision |
|---|---:|---|---:|---|---|
| Track1 | 8.8 | `cR=3`, `cO=0` | 8.8 | `cR=3`, `cO=0` | No improvement. |
| Track4 | 8.8 | `cR=3`, `cO=0` | 8.8 | `cR=3`, `cO=0` | No improvement. |

v29 did not improve either target weak-track score or collision count. Because
it adds behavior without measurable benefit on the intended tracks, it is not
accepted.

## Restore Gate

After rejecting v29, the controller source was restored to v13 semantics and
the deployability static checker passed again:

```text
Results/evidence/controller_deployability_static_check_v13_restored_after_v29_20260709_2130.md
```

Restore checker summary:

```text
ready_for_physical_claim=true
high=0
medium=0
```

`git diff -w -- Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`
was empty after restoration, so the v29 semantic change is not retained. Any
remaining source diff in that file should be treated as formatting/noise unless
a later semantic diff proves otherwise.

## Decision

Reject v29.

Current accepted controller remains:

```text
v13 side-trigger 0.45
```

Do not create another scalar candidate without a fresh failure-window diagnosis
and a mechanism hypothesis. The next candidate should focus on a different
explainable mechanism, such as side-danger steering floor or a limited release
hysteresis test, only after reading the saved collision and signal windows.

## Non-Claims

- This is MWORKS/Sysplorer wrapper evidence, not physical UGV evidence.
- This does not claim final competition score or submission readiness.
- This does not authorize edits to official vehicle, road, track, scoring, or
  example packages.
