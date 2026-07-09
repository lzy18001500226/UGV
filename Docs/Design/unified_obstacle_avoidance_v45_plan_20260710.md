# Unified Obstacle Avoidance v45 Plan

Status: review_ready_new_best_candidate, 2026-07-10 CST

## Hypothesis

Repeat v44's Regulated Pure Pursuit style mechanism with the observed runtime
speed scale. When path steering demand is large, cap normalized path target
speed to reduce road-edge exposure without suppressing steering authority.

## Edit Scope

Allowed source edit:

```text
Models/UGV/Control/PathPlanning/PathPlanner.mo
```

No official model, vehicle, road, scoring, sensor, or track geometry edits.
No per-track branch.

## Implemented Mechanism

```text
curve_slowdown_steer = 0.35
curve_slowdown_speed = 0.75
if abs(steering_angle) > curve_slowdown_steer
   and target_v > curve_slowdown_speed then
  target_v := curve_slowdown_speed;
end if;
```

## Evidence Plan

1. Static deployability checker for the obstacle controller source remains
   green, confirming the accepted Sysblock obstacle controller did not gain new
   high/medium source risks.
2. Runtime evidence is required because the accepted source change is in
   `PathPlanner.mo`, outside the obstacle-controller-only static checker.
3. Accept only if the same unified mechanism improves total four-track score
   and does not create a per-track branch.

## Result

Evidence:

```text
Results/evidence/controller_deployability_static_check_v45_curvature_speed_regulation_scaled_20260710_0035.md
Results/simulations/controller_v45_curvature_speed_regulation_scaled_saidao1_120s_20260710_0040/
Results/simulations/controller_v45_curvature_speed_regulation_scaled_saidao2_120s_20260710_0040/
Results/simulations/controller_v45_curvature_speed_regulation_scaled_saidao3_120s_20260710_0040/
Results/simulations/controller_v45_curvature_speed_regulation_scaled_saidao4_120s_20260710_0035/
Results/metrics/four_track_candidate_review_v45_curvature_speed_regulation_scaled_20260710_0045.md
```

Four-track wrapper score:

| Track | Runtime | Exit | T/s | cR | cO | P |
|---|---|---:|---:|---:|---:|---:|
| Saidao1Eval | `simulate_returned_true` | 0 | 120.0 | 3 | 0 | 8.8 |
| Saidao2Eval | `simulate_returned_true` | 0 | 120.0 | 1 | 0 | 9.6 |
| Saidao3Eval | `simulate_returned_true` | 0 | 120.0 | 1 | 1 | 9.2 |
| Saidao4Eval | `simulate_returned_true` | 0 | 120.0 | 2 | 0 | 9.2 |

Total wrapper score: `36.8`, improving the accepted v13 total `36.4` by
`+0.4`. v45 is the current review-ready best candidate. It is not a final
competition submission claim and does not prove physical UGV performance.
