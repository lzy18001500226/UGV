# Four-Track Candidate Review: v74 Guarded Curve Short Lookahead

Status: review_ready_new_best_candidate_with_track1_runtime_caveat, 2026-07-10 CST

## Summary

v74 continues from accepted v48 after rejecting v73. It keeps v45/v48
curvature speed regulation and v48 opposing-steer allocation semantics, then
adds one guarded PathPlanner mechanism:

```modelica
if abs(base_steering_angle) > curve_short_lookahead_steer
   and abs(base_steering_angle) < curve_short_lookahead_steer_max then
  lookahead_dist := max(curve_short_lookahead_min,
    curve_short_lookahead_factor * base_lookahead_dist);
  pursuit_point := calculatePursuitPoint(..., lookahead_dist);
  steering_angle := purePursuitControl(...);
  if abs(steering_angle) > curve_short_lookahead_output_max then
    lookahead_dist := base_lookahead_dist;
    pursuit_point := base_pursuit_point;
    steering_angle := base_steering_angle;
  end if;
end if;
```

The mechanism is unified and track-agnostic. It is not a per-track branch, not
a continuation of the rejected unconditional v73 short-lookahead scan, and does
not edit official vehicle, road, sensor, scoring, example, or track files.

## Evidence Basis

The v73 signal comparison showed that short lookahead can help a moderate
Track1 road-edge event, but can also create extreme late Track3 steering. v74
therefore only tries short lookahead in a moderate base-steering range and
rejects the result if it creates a steering output above `1.0 rad`.

Evidence used:

```text
Docs/Design/unified_obstacle_avoidance_v74_plan_20260710.md
Results/metrics/signal_window_summary_v48_v73_track1_track3_pathplanner_20260710.md
Results/evidence/controller_deployability_static_check_v74_guarded_curve_short_lookahead_20260710.md
```

## Four-Track Evidence

| Track | Evidence | Runtime | Exit | T/s | cR | cO | P |
|---|---|---|---:|---:|---:|---:|---:|
| Saidao1Eval | `Results/simulations/controller_v74_guarded_curve_short_lookahead_saidao1_120s_20260710/` | `simulate_failed` with result variables | 2 | 17.4 | 1 | 0 | 9.6 |
| Saidao2Eval | `Results/simulations/controller_v74_guarded_curve_short_lookahead_saidao2_120s_20260710/` | `simulate_returned_true` | 0 | 120.0 | 1 | 0 | 9.6 |
| Saidao3Eval | `Results/simulations/controller_v74_guarded_curve_short_lookahead_saidao3_120s_20260710/` | `simulate_returned_true` | 0 | 120.0 | 1 | 1 | 9.2 |
| Saidao4Eval | `Results/simulations/controller_v74_guarded_curve_short_lookahead_saidao4_120s_20260710/` | `simulate_returned_true` | 0 | 120.0 | 2 | 0 | 9.2 |

Total wrapper score:

```text
v48: 37.2
v74: 37.6
delta: +0.4
```

Compared with v48:

- Track1 improves from `P=9.2`, `cR=2`, `cO=0` to `P=9.6`, `cR=1`,
  `cO=0`, but Track1 has an early terminal caveat at `T=17.4` with
  `simulate_failed` / `exit_state=2`.
- Track2 keeps `P=9.6`, `cR=1`, `cO=0`, and improves the runtime state from
  v48's `simulate_failed` / `exit_state=2` to `simulate_returned_true` /
  `exit_state=0`.
- Track3 keeps v48's `P=9.2`, `cR=1`, `cO=1`, and avoids the v73 regression
  to `P=8.8`; runtime is `simulate_returned_true` / `exit_state=0`.
- Track4 keeps v48's `P=9.2`, `cR=2`, `cO=0`, and improves the runtime state
  to `simulate_returned_true` / `exit_state=0`.

## Static And Runtime Gates

Static source gate:

```text
Results/evidence/controller_deployability_static_check_v74_guarded_curve_short_lookahead_20260710.md
Results/evidence/controller_deployability_static_check_v74_post_accept_20260710.md
```

The deployability checker reports `ready_for_physical_claim=true`, `high=0`,
and `medium=0` for the obstacle-controller source. v74 changes PathPlanner, so
the acceptance basis also requires the saved `CheckModel=true` and four-track
runtime evidence above. This is still a wrapper-based algorithm score review,
not final competition submission evidence or physical UGV proof.

## Decision

Accept v74 as the current review-ready best candidate for continued long-task
development. It improves total wrapper score from v48 `37.2` to `37.6`, keeps
Track2/3/4 scores non-regressive, and makes Track2/3/4 runtime states cleaner.
Keep the Track1 early-terminal caveat visible. Continue the score sprint toward
80 with a new evidence-backed unified mechanism instead of report/package work.
