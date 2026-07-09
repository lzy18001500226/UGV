# Four-Track Evaluation Summary - v13 Side Trigger 0.45 - 20260709_1535

## Scope

Phase: narrow v13 controller experiment after v12 collision-window analysis.

Allowed controller target:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Logical change from v12:

```modelica
transition(cruise, avoid, df <= mindis or dl <= 0.45 or dr <= 0.45, reset = false)
```

No official no-edit zone was modified.

## Rationale

v12 collision-window evidence showed Track1's first two obstacle collisions
occurred with `flag=0` and side distance around `0.46`, so the v12 side trigger
threshold `0.30` was too late. v13 tests the smallest direct threshold change
that can cover this window while guarding Track4 for road-boundary regression.

Pre-change evidence:

```text
Results/metrics/v12_collision_window_interpretation_20260709_1520.md
```

## Result Table

| Track | Model | Runtime status | Exit state | T/s | Road cR | Obstacle cO | Score P | Evidence |
|---|---|---|---:|---:|---:|---:|---:|---|
| 1 | `UGV.Test.Saidao1Eval` | `simulate_returned_true` | 0 | 120.0 | 3 | 0 | 8.8 | `Results/simulations/controller_v13_side_trigger045_saidao1_120s_20260709_1524/` |
| 2 | `UGV.Test.Saidao2Eval` | `simulate_failed` with result variables readable | 2 | 91.9 | 1 | 0 | 9.6 | `Results/simulations/controller_v13_side_trigger045_saidao2_120s_20260709_1528/` |
| 3 | `UGV.Test.Saidao3Eval` | `simulate_returned_true` | 0 | 120.0 | 1 | 1 | 9.2 | `Results/simulations/controller_v13_side_trigger045_saidao3_120s_20260709_1530/` |
| 4 | `UGV.Test.Saidao4Eval` | `simulate_failed` with result variables readable | 2 | 113.1 | 3 | 0 | 8.8 | `Results/simulations/controller_v13_side_trigger045_saidao4_120s_20260709_1526/` |

Total score:

```text
v5/M6 baseline: 32.0
v12 side trigger 0.30: 34.8
v13 side trigger 0.45: 36.4
delta vs v12: +1.6
delta vs v5/M6: +4.4
```

## Comparison

| Track | v5/M6 P | v12 P | v13 P | Decision |
|---|---:|---:|---:|---|
| Track1 | 7.2 | 7.6 | 8.8 | v13 improves early obstacle-collision window. |
| Track2 | 8.4 | 9.6 | 9.6 | v13 preserves v12 gain. |
| Track3 | 7.2 | 8.8 | 9.2 | v13 further improves. |
| Track4 | 9.2 | 8.8 | 8.8 | v13 does not recover v5 but does not worsen v12. |

## Checks

Static deployability checker passed before and after v13 runtime runs:

```text
Results/evidence/controller_deployability_static_check_v13_side_trigger_045_20260709.md
Results/evidence/controller_deployability_static_check_v13_side_trigger_045_closeout_20260709.md
```

Checker summary:

```text
ready_for_physical_claim=true
high=0
medium=0
```

## Decision

v13 is accepted as the current review-ready controller candidate.

Non-claims:

- This is wrapper-based MWORKS/Sysplorer evidence, not physical UGV evidence.
- Track4 remains weaker than the v5/M6 baseline.
- `simulate_failed` with readable variables remains a known evidence mode for
  Track2 and Track4, consistent with earlier M6/v12 evidence handling.
- Final competition submission still requires explicit user approval.

## Next Engineering Step

The next useful improvement target is Track4 road-boundary recovery. Avoid a
broad rewrite until Track4 signal windows are inspected in more detail.
