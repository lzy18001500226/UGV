# Unified Obstacle Avoidance v50 Plan

Status: rejected_after_target_track_validation, 2026-07-10 CST

## Goal

Continue from v48, the current review-ready best candidate, with one unified
four-track mechanism. Do not branch by track name, wrapper name, run id, or
scoring variables.

## Evidence Basis

Current accepted candidate:

```text
v48 total wrapper score: 37.2
Track1: P=9.2, cR=2, cO=0
Track2: P=9.6, cR=1, cO=0, simulate_failed with result variables
Track3: P=9.2, cR=1, cO=1, simulate_failed with result variables
Track4: P=9.2, cR=2, cO=0, simulate_failed with result variables
```

Fresh v48 path/control event evidence:

```text
Results/metrics/signal_window_summary_v48_path_ctrl_20260710.md
Results/metrics/signal_window_summary_v48_path_ctrl_20260710.json
```

Observed pattern:

- Several remaining road contacts happen while the obstacle controller is
  already active (`flag=1`), so this is not only a trigger problem.
- At Track1 6.55 s, Track2 4.70 s, Track3 4.85 s, and Track4 4.35 s the path
  planner still commands `target_v=1` with moderate steering demand around
  `0.22` to `0.30` rad.
- The existing v45/v48 curve speed cap only triggers above `0.35` rad, so it
  misses those moderate-turn road-contact windows.
- v47 showed that a simple two-second startup speed cap at `0.75` does not
  remove Track3's first obstacle contact, but it also did not regress runtime
  comparability.
- v49 showed that broad path-speed attenuation during all reverse avoidance is
  too disruptive, so v50 must be narrower than "attenuate whenever
  `speed_oa < 0`".

## Hypothesis

Extend the accepted curvature speed regulation from large turns to moderate
turns:

```modelica
parameter Real curve_slowdown_steer = 0.20;
parameter Real curve_slowdown_speed = 0.75;
```

This keeps the same path-following mechanism and same target-speed cap, but
applies it when the saved v48 evidence shows road-contact risk. It is still one
track-agnostic algorithm and remains deployable as a conservative speed limit
under steering demand.

## Source Scope

Allowed edit:

```text
Models/UGV/Control/PathPlanning/PathPlanner.mo
```

Do not edit:

```text
Models/UGV/Vehicle/
Models/UGV/Road/
Models/UGV/saidao/
Models/UGV/CountPoint/
Models/UGV/Example/
References/official_materials/
```

## Validation Gate

1. Run the static deployability gate.
2. Run Track3 first because v48 still has both obstacle and road collisions.
3. Accept target-track continuation only if Track3 removes a collision or
   improves `P` without a worse non-comparable early terminal state.
4. If Track3 does not improve, reject v50, restore v48 source semantics, record
   the evidence, send a sparse Chinese notice, and continue with another
   evidence-backed mechanism or research path.
5. If Track3 improves, run all four tracks before accepting v50.

## Closeout

v50 ran Track3 and is rejected. Runtime comparability improved to
`simulate_returned_true`, but score and collision counts stayed unchanged:

```text
Track3: T=120.0, cR=1, cO=1, P=9.2
```

Evidence:

```text
Results/simulations/controller_v50_moderate_curve_speed_saidao3_120s_20260710/
Results/metrics/track3_candidate_review_v50_moderate_curve_speed_20260710.md
Results/metrics/collision_window_analysis_v50_moderate_curve_speed_track3_20260710.md
Results/metrics/signal_window_summary_v50_moderate_curve_speed_track3_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v50_20260710.md
```

Source was restored to v48 semantics:

```modelica
curve_slowdown_steer = 0.35
curve_slowdown_speed = 0.75
```

## Non-Claims

- This plan does not claim final competition score.
- This plan does not claim physical UGV success.
- This plan does not authorize final submission packaging or sending.
