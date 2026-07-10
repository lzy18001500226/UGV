# Unified Obstacle Avoidance v84 Plan

Status: rejected_after_target_gate, 2026-07-10 CST

## Goal

Continue from accepted v80 and test one unified trajectory-level mechanism:
an initial-lane safety bias in `PathPlanner` that keeps the early trajectory
slightly farther from the bottom road edge and the first Track3 obstacle.

This is not a report/package task. It is a score-sprint candidate.

## Baseline

Accepted local wrapper best remains v80:

```text
total wrapper score: 38.0
Track1: P=9.6, cR=1, cO=0, simulate_failed/T=17.4
Track2: P=9.6, cR=1, cO=0, clean T=120
Track3: P=9.2, cR=1, cO=1, simulate_failed/T=59.4
Track4: P=9.6, cR=1, cO=0, clean T=120
```

## Evidence Basis

Trajectory and event evidence:

```text
Results/metrics/collision_window_analysis_v80_all_tracks_20260710.md
Results/metrics/signal_window_summary_v80_all_tracks_radius025_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v80_all_tracks_radius025_20260710.md
Results/metrics/trajectory_geometry_review_v74_all_tracks_20260710.md
Results/metrics/trajectory_geometry_review_v80_track2_diagnostic_20260710.md
```

Observed early events are close to the lower road boundary:

```text
Track1 road event: x ~= 3.007, y ~= 1.851, dRoadCenter ~= 0.5009
Track2 road event: x ~= 3.644, y ~= 0.4601, dRoadCenter ~= 0.4601
Track3 obstacle event: x ~= 1.200, y ~= 0.0799, dNearestObs ~= 0.1061
Track3 road event: x ~= 3.364, y ~= 0.4616, dRoadCenter ~= 0.4616
Track4 road event: x ~= 3.656, y ~= 0.4637, dRoadCenter ~= 0.4637
```

The repeated local-control attempts have mostly failed because the obstacle
overlay is already active when the score events happen. v84 tests whether a
small trajectory reference bias before the event can change the approach path
instead of reacting after the threshold is crossed.

## Rejected Routes Not Repeated

- v47 startup speed cap.
- v63 direct early obstacle-steer feedforward.
- v65 stronger front emergency braking.
- v75 opposing path neutralization.
- v76 front-clear side steer boost.
- v82 small-angle road-edge short lookahead.
- v83 `df < 0.15` road-edge recovery.

## Candidate Mechanism

Allowed scope:

```text
Models/UGV/Control/PathPlanning/PathPlanner.mo
```

Add an effective y-coordinate for path tracking only:

```modelica
parameter Real initial_lane_bias_time = 6.0;
parameter Real initial_lane_bias_y_min = 0.0;
parameter Real initial_lane_bias_y_max = 1.0;
parameter Real initial_lane_safety_y_bias = 0.20;
Real effective_y;

if time < initial_lane_bias_time
   and y >= initial_lane_bias_y_min
   and y < initial_lane_bias_y_max then
  effective_y := y - initial_lane_safety_y_bias;
else
  effective_y := y;
end if;
```

Use `effective_y` for the pure-pursuit closest-segment and steering
calculation. This is a unified start-lane safety offset, not a track-id branch.
It does not edit official road, obstacle, vehicle, sensor, scoring, or example
files.

## Validation Gate

1. Apply the minimal `PathPlanner` edit.
2. Run `Scripts/quality/check_controller_deployability.py`.
3. Run Track3 first because it has both the first obstacle event and the road
   event.
4. Continue to four-track regression only if Track3 improves `P/cR/cO` or at
   least removes one collision without a worse early terminal artifact.
5. Reject and restore v80 semantics if Track3 is unchanged, regresses, or
   produces a non-comparable early stop.

## Non-Goals

- No official material/model no-edit-zone changes.
- No per-track algorithm.
- No final 80/80, physical UGV, or submission claim.

## Review Outcome

v84 passed the static gate but failed the Track3 target gate with an early,
non-comparable terminal state:

```text
Track3 v84: T=1.2, cR=0, cO=1, P=9.6, simulate_failed / exit_state=2
```

The apparent score is rejected because the run ended at 1.2 s. Source semantics
were restored to v80 and the restore static gate passed:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v84_20260710.md
```

Review:

```text
Results/metrics/track3_candidate_review_v84_initial_lane_y_bias_20260710.md
```
