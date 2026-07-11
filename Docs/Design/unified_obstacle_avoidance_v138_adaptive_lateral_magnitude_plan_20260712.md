# v138 Adaptive Lateral-Magnitude Plan

Status: rejected after Track2 120 s; v80 remains the rollback baseline.

## Why This Candidate

v80 can remain in side-only avoidance with `speed_oa=-1`, which leaves very
little forward progress. v137 showed that neutral side-only longitudinal
authority can remove that stall, but its fixed `steer_oa=+0.6` led to an extra
road collision (`cR=2` versus v80 `cR=1`) and was rejected.

v138 isolates the lateral part of that failure. It does not change the
longitudinal controller or path planner. In the existing lateral avoidance
state, the direction still comes from the existing left/right state machine,
but the magnitude is bounded by the measured left/right clearance difference:

```text
avoid_steer_magnitude = min(0.6, 2 * abs(dl - dr))
```

This is not a speed threshold scan, a fixed side bias, a direction-sign swap,
or a reverse-dwell change. It reduces an unnecessarily strong turn when the
two side clearances are close, while retaining the v80 maximum authority when
the gap asymmetry is large.

## Scope

- Change only the two final lateral avoidance assignments in
  `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`.
- Keep v80 longitudinal state transitions and control-allocation semantics.
- Do not edit official track, vehicle, road, sensor, scoring, example, or
  reference files.
- Use the same candidate for all tracks; do not tune per-track parameters.

## Gates

1. Run the deployability checker and project tests.
2. Run native Track2 for 1 s.
3. Run Track2 for 120 s and compare with v80: require a comparable runtime,
   no new road/obstacle collision, and a measurable progress or score gain.
4. Only if gate 3 passes, run the extended Track2 completion gate. Completion
   requires `SimulateModel=false`, `T>10`, and `distanceSensor1.d<0.02`.
5. Only after Track2 finishes, run Track1 regression and then expand to the
   remaining tracks.

Any collision regression, non-comparable early termination, or absent progress
gain rejects v138. Restore exact v80 semantics and record the rejection.
No horizon-only run is a finish, and this plan does not claim an 80-point score
or physical-vehicle readiness.

## Result

The source-only deployability check reported `high=0, medium=0`, and all 11
project tests passed. Track2's native 1 s gate reached the configured horizon
with `cR=0, cO=0, P=10.0`.

The comparable Track2 120 s run was not an improvement: it ended at `T=59.3 s`
with `cR=1, cO=0, P=9.6`, whereas v80's 120 s comparison reaches the horizon
with `cR=1, cO=0, P=9.6`. It therefore has no score/progress gain and is
rejected without a 700 s run or cross-track expansion. The controller is
restored to v80 semantics.

Evidence:

- `Results/evidence/controller_deployability_static_check_v138_adaptive_lateral_magnitude_20260712.md`
- `Results/simulations/candidate_v138_adaptive_lateral_magnitude_track2_1s_20260712/`
- `Results/simulations/candidate_v138_adaptive_lateral_magnitude_track2_120s_20260712/`
- `Results/metrics/track2_candidate_review_v138_adaptive_lateral_magnitude_20260712.md`
