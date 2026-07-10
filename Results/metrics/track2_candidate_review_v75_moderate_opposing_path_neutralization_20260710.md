# Track2 Candidate Review: v75 Moderate Opposing Path Neutralization

Status: rejected, 2026-07-10 CST

## Candidate

v75 started from accepted v74 and tested a narrow `ControlAllocate` branch:

```modelica
gain3.u = if speed_oa < 0 and steer_oa > 0
  and unitDelay1.y < -0.15 and unitDelay1.y > -0.35
then 0
else if speed_oa < 0 and steer_oa * unitDelay1.y < 0
then 0.5 * unitDelay1.y
else unitDelay1.y;
```

Intent: remove the small negative path-planner contribution that partially
cancels active right obstacle steering in the v74 early road-edge windows.

## Evidence

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v75_plan_20260710.md
```

Static gate:

```text
Results/evidence/controller_deployability_static_check_v75_moderate_opposing_path_neutralization_20260710.md
```

Target run:

```text
Results/simulations/controller_v75_moderate_opposing_path_neutralization_saidao2_120s_20260710/
```

Restored gate:

```text
Results/evidence/controller_deployability_static_check_v74_restored_after_v75_20260710.md
```

## Result

| Candidate | Track | Runtime | Exit | T/s | cR | cO | P |
|---|---|---|---:|---:|---:|---:|---:|
| v74 | Saidao2Eval | `simulate_returned_true` | 0 | 120.0 | 1 | 0 | 9.6 |
| v75 | Saidao2Eval | `simulate_failed` with result variables | 2 | 8.7 | 1 | 0 | 9.6 |

## Decision

Reject v75. It did not improve the target Track2 road-collision count or
score, and it worsened the runtime caveat from v74's clean 120 s run to an
early `simulate_failed` result at `T=8.7`.

Do not expand v75 to Track1/3/4. Source semantics were restored to v74:

```text
v13 obstacle-controller side trigger
v45/v74 PathPlanner curvature and guarded short-lookahead semantics
v48 ControlAllocate opposing-steer guard
```

## Non-Claims

- No final competition score is claimed.
- No physical UGV success is claimed.
- No report/package readiness change is claimed.
