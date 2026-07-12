# v140 Neutral Side-Risk With Proportional Steering Plan

## Status

Candidate design only. v80 remains the accepted rollback baseline until the
Track2 comparable gate passes.

## Evidence Basis

- v80 reaches a side-only risk condition with the front clear, keeps
  `speed_oa=-1`, and stalls near path index 30.
- v137 changed only the longitudinal side-risk ownership and reached path
  index 112 at 120 s, but its fixed `steer_oa=+0.6` produced an additional
  road collision.
- v138 changed only lateral magnitude and did not materially improve v80
  because the v80 reverse-speed stall remained.

Evidence:

```text
Results/metrics/track2_v80_termination_classification_20260712.md
Results/metrics/track2_candidate_review_v137_neutral_side_guard_20260712.md
Results/metrics/track2_candidate_review_v138_adaptive_lateral_magnitude_20260712.md
```

## Unified Mechanism

Use one controller and one parameter set for every track:

1. Preserve full reverse authority when the front is inside `mindis`.
2. When only a side is close and the front is clear, give the obstacle
   controller neutral longitudinal authority (`speed=0`) so path following
   can continue instead of repeatedly reversing.
3. Keep the existing side choice, but scale the lateral command by measured
   clearance asymmetry: `min(0.6, 2*abs(dl-dr))`. This retains strong action
   when one side is clearly safer and avoids the fixed full turn when the two
   side distances are nearly equal.
4. Leave cruise, front-risk transitions, path planner, vehicle, road, sensor,
   scoring, and example models unchanged.

The intended state-machine assignments are:

```modelica
// longitudinal avoid state
speed := min(0, max(-1, df - mindis));

// lateral avoid state, preserving the existing selected direction
steer := min(0.6, 2 * abs(dl - dr));
steer := -min(0.6, 2 * abs(dl - dr));
```

The two lines are placed in their existing directional states; no new ports,
external signals, timers, or per-track parameters are introduced.

## Scope and Rollback

- Editable source: `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`.
- Do not modify official vehicle, road, sensor, score, example, or reference
  files.
- If any gate fails, restore the exact v80 source semantics and retain the
  candidate evidence and review decision.

## Gates

1. Run the deployability checker and `python -m pytest Scripts/tests -q`.
2. Run Track2 for 1 s; this proves load/check/simulate only.
3. Run Track2 for 120 s. Require a comparable runtime, `cO=0`, no increase
   over v80's `cR=1`, and material progress beyond the v80 index 26 result.
4. Only after gate 3 passes, run the 700 s official completion gate. A finish
   requires `SimulateModel=false`, `T>10`, and `distanceSensor1.d<0.02`.
5. Only after a Track2 finish, run Track1 collision regression, then Tracks 3
   and 4 using the same source and parameters.

This plan does not claim an 80/80 score, official completion, physical UGV
performance, or submission readiness.
