# Unified Obstacle Avoidance v74 Plan

Status: accepted_review_ready_new_best_with_track1_runtime_caveat, 2026-07-10 CST

## Goal

Continue from accepted v48 after rejecting v73. Test a guarded pure-pursuit
geometry mechanism that keeps v73's local Track1 benefit while avoiding the
Track3 late-road-edge regression.

This is not a short-lookahead scalar scan. It adds two guardrails around the
same mechanism:

- only shorten lookahead for moderate curve steering;
- reject the shortened lookahead result if it creates an extreme steering
  command, then fall back to the original pursuit point.

## Evidence Basis

Current accepted best:

```text
v48 total wrapper score: 37.2
```

v73 review:

```text
Results/metrics/track1_track4_track3_candidate_review_v73_curve_short_lookahead_20260710.md
```

New v48/v73 signal window comparison:

```text
Results/metrics/signal_window_summary_v48_v73_track1_track3_pathplanner_20260710.md
```

Key observations:

- Track1 v48 second road event at `30.35 s` has
  `pathPlanner.steering_angle=-0.6906`, inside a moderate curve range.
- Track3 v73 added a late road event at `116.7 s` where the shortened-lookahead
  output became extreme: `pathPlanner.steering_angle=1.974`,
  `pathPlanner.lookahead_dist=1.316`, `target_v=0.75`.
- Track3's original early obstacle and road events at `1.05 s` and `4.85 s`
  were unchanged by v73; the regression was the new late high-steering event.

## Hypothesis

Shortening lookahead helps some medium-curvature road-edge cases, but applying
it through extreme curvature can over-rotate the path-following command and
create a new late road hit. A bounded accept/reject rule should keep the
medium-curvature benefit and prevent extreme-output regressions.

## Planned Source Change

Allowed scope:

```text
Models/UGV/Control/PathPlanning/PathPlanner.mo
```

Add temporary algorithm variables:

```modelica
Real base_steering_angle;
Real base_lookahead_dist;
Real[2] base_pursuit_point;
```

Add bounded parameters:

```modelica
parameter Real curve_short_lookahead_steer = 0.35;
parameter Real curve_short_lookahead_steer_max = 1.0;
parameter Real curve_short_lookahead_factor = 0.65;
parameter SIunits.Length curve_short_lookahead_min = 1.2;
parameter Real curve_short_lookahead_output_max = 1.0;
```

Mechanism:

1. Compute the normal v48 pursuit point and steering.
2. Save the normal steering, lookahead, and pursuit point.
3. Only try short lookahead when `abs(base_steering_angle)` is in
   `[0.35, 1.0]`.
4. If the shortened-lookahead steering exceeds `1.0 rad`, restore the normal
   v48 steering/lookahead/pursuit point.
5. Keep the existing v45/v48 curvature speed cap after the accepted steering.

## Validation Gate

1. Run the source-only deployability checker.
2. Run Track1 first. Accept continuing only if Track1 improves or remains
   non-regressive compared with v48 `P=9.2`.
3. Run Track3 next. Reject immediately if Track3 remains below v48 `P=9.2` or
   repeats the v73 added road collision behavior.
4. If Track1 and Track3 are acceptable, run Track2 and Track4 for regression.
5. Accept v74 as new review-ready best only if total score exceeds v48 `37.2`
   without introducing a worse runtime caveat.

## Result

v74 passed the planned validation gate and is accepted as the current
review-ready best candidate:

```text
Track1: T=17.4, cR=1, cO=0, P=9.6, simulate_failed / exit_state=2
Track2: T=120.0, cR=1, cO=0, P=9.6, simulate_returned_true / exit_state=0
Track3: T=120.0, cR=1, cO=1, P=9.2, simulate_returned_true / exit_state=0
Track4: T=120.0, cR=2, cO=0, P=9.2, simulate_returned_true / exit_state=0
Total: 37.6
```

Review:

```text
Results/metrics/four_track_candidate_review_v74_guarded_curve_short_lookahead_20260710.md
```

Decision: accept v74 over v48 because total wrapper score improves from `37.2`
to `37.6`, Track2/3/4 scores are non-regressive with cleaner runtime states,
and the rejected v73 Track3 score regression does not repeat. Keep Track1's
early-terminal caveat visible.

## Non-Goals

- No final package.
- No report polish.
- No physical UGV claim.
- No edits to official vehicle, road, sensor, scoring, example, or track files.
- No per-track logic.
