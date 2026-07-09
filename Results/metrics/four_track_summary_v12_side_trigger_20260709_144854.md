# Four-Track Evaluation Summary - v12 Side Trigger - 20260709_144854

## Scope

Phase: targeted controller tuning after M6 wrapper metrics.

Allowed controller target:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Official no-edit zones were not modified:

```text
Models/UGV/Vehicle/
Models/UGV/Road/
Models/UGV/saidao/
Models/UGV/CountPoint/
Models/UGV/Example/
References/official_materials/
```

Controller version:

```text
controller_v12_side_trigger_0p30
```

Logical change:

```modelica
transition(cruise, avoid, df <= mindis or dl <= 0.30 or dr <= 0.30, reset = false)
```

Rationale: diagnostic exports showed many obstacle-collision windows where
`flag=0` and `df` did not trigger the front avoid state, while side distances
were already small. v12 lets close side proximity enter the existing
longitudinal avoid behavior instead of relying only on front distance.

## Result Table

| Track | Model | Runtime status | Exit state | T/s | Road cR | Obstacle cO | Score P | Evidence |
|---|---|---|---:|---:|---:|---:|---:|---|
| 1 | `UGV.Test.Saidao1Eval` | `simulate_returned_true` | 0 | 120.0 | 3 | 3 | 7.6 | `Results/simulations/controller_v12_side_trigger_saidao1_120s_20260709_144006/` |
| 2 | `UGV.Test.Saidao2Eval` | `simulate_returned_true` | 0 | 120.0 | 1 | 0 | 9.6 | `Results/simulations/controller_v12_side_trigger_saidao2_120s_20260709_144200/` |
| 3 | `UGV.Test.Saidao3Eval` | `simulate_returned_true` | 0 | 120.0 | 2 | 1 | 8.8 | `Results/simulations/controller_v12_side_trigger_saidao3_120s_20260709_143835/` |
| 4 | `UGV.Test.Saidao4Eval` | `simulate_failed` with result variables readable | 2 | 94.95 | 3 | 0 | 8.8 | `Results/simulations/controller_v12_side_trigger_saidao4_120s_20260709_144434/` |

Total score:

```text
v5/M6 baseline: 32.0
v12 side trigger: 34.8
delta: +2.8
```

## Baseline Comparison

| Track | v5/M6 P | v12 P | Delta | Interpretation |
|---|---:|---:|---:|---|
| Track1 | 7.2 | 7.6 | +0.4 | Slight improvement; still collision-heavy. |
| Track2 | 8.4 | 9.6 | +1.2 | Clear improvement. |
| Track3 | 7.2 | 8.8 | +1.6 | Main gain; side trigger reduced obstacle collisions. |
| Track4 | 9.2 | 8.8 | -0.4 | Small regression and still has terminal `simulate_failed` state. |

## Checks

Static deployability checker passed before and after v12 runtime runs:

```text
Results/evidence/controller_deployability_static_check_v12_side_trigger_20260709.md
Results/evidence/controller_deployability_static_check_v12_side_trigger_postrun_20260709.md
```

Checker summary:

```text
ready_for_physical_claim=true
high=0
medium=0
low=2
```

## Decision

v12 is accepted as the current review-ready controller candidate because it
improves four-track total score from `32.0` to `34.8` without touching official
no-edit zones and without introducing high/medium static deployability risks.

This is not a final optimized competition claim:

- Track1 remains collision-heavy.
- Track4 slightly regresses and still reaches a readable-result terminal state.
- The result uses generated `UGV.Test.Saidao*Eval` wrappers for repeatable
  controller evaluation, following the current M6 evidence rule.
- No physical UGV or final-race deployment success is claimed.

## Next Engineering Step

Before another controller rewrite, inspect collision windows or trajectory
behavior for Track1 and Track4:

```text
Track1: determine why cO remains 3 and whether side trigger creates slow-wall behavior.
Track4: determine why v12 loses 0.4 score despite zero obstacle collisions.
```
