# Four-Track Candidate Review: v45 Curvature Speed Regulation Scaled

Status: review_ready_new_best_candidate, 2026-07-10 CST

## Summary

v45 applies one unified path-speed mechanism across all four tracks:

```text
if abs(pathPlanner.steering_angle) > 0.35
   and pathPlanner.target_v > 0.75 then
  pathPlanner.target_v := 0.75;
end if;
```

It is a Regulated Pure Pursuit style speed cap for high steering demand. It is
not a per-track branch and does not touch official vehicle, road, sensor,
scoring, or track geometry.

## v44 Scale Lesson

v44 used the same mechanism with `curve_slowdown_speed = 7.5`. Saved Track4
analysis showed v44 matched v13 exactly:

```text
T=113.1, cR=3, cO=0, P=8.8
```

Evidence:

```text
Results/simulations/controller_v44_curvature_speed_regulation_saidao4_120s_20260710_0029/
Results/metrics/collision_window_analysis_v13_v44_track4_20260710_0032.md
Results/metrics/signal_window_summary_v13_v44_track4_20260710_0032.md
```

Reason: exported `pathPlanner.target_v` and `ctrlAlloc.speed_pp` are normalized
around `1.0`, so `7.5` did not cap runtime speed. v44 is rejected as a no-op.

## v45 Four-Track Evidence

| Track | Evidence | Runtime | Exit | T/s | cR | cO | P |
|---|---|---|---:|---:|---:|---:|---:|
| Saidao1Eval | `Results/simulations/controller_v45_curvature_speed_regulation_scaled_saidao1_120s_20260710_0040/` | `simulate_returned_true` | 0 | 120.0 | 3 | 0 | 8.8 |
| Saidao2Eval | `Results/simulations/controller_v45_curvature_speed_regulation_scaled_saidao2_120s_20260710_0040/` | `simulate_returned_true` | 0 | 120.0 | 1 | 0 | 9.6 |
| Saidao3Eval | `Results/simulations/controller_v45_curvature_speed_regulation_scaled_saidao3_120s_20260710_0040/` | `simulate_returned_true` | 0 | 120.0 | 1 | 1 | 9.2 |
| Saidao4Eval | `Results/simulations/controller_v45_curvature_speed_regulation_scaled_saidao4_120s_20260710_0035/` | `simulate_returned_true` | 0 | 120.0 | 2 | 0 | 9.2 |

Total wrapper score:

```text
v13: 36.4
v45: 36.8
delta: +0.4
```

Track4 improves from `P=8.8`, `cR=3`, `cO=0` to `P=9.2`, `cR=2`, `cO=0`.
Track1, Track2, and Track3 stay at the accepted v13 score levels.

## Static Gate Boundary

The saved checker result is:

```text
Results/evidence/controller_deployability_static_check_v45_curvature_speed_regulation_scaled_20260710_0035.md
```

It reports `ready_for_physical_claim=true`, `high=0`, `medium=0`. This checker
only inspects the obstacle-controller source. Because v45 changes
`PathPlanner.mo`, the acceptance basis is the combination of:

1. source diff limited to the path planner speed cap,
2. four-track wrapper runtime evidence,
3. no per-track branching,
4. no edits to official hard no-edit zones.

## Decision

Accept v45 as the current review-ready best candidate for the long task.
Do not build or send a final competition package without explicit user
approval. Continue optimization from v45 rather than reverting to v13 unless a
later regression check or user review rejects it.
