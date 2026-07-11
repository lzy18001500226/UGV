# Unified Obstacle Avoidance v117 Plan

Status: runtime evaluation blocked; source restored to v80 path semantics

## Problem

The official finish gate requires the vehicle to return to the origin after
10 seconds. The current path planner searches only segments `1..n-1` and its
pursuit-point traversal stops at the last point. It never traverses the closing
segment from the final point back to the first point.

This conflicts with the official closed-track semantics. In particular,
Track1 contains a point after its return to the origin, and Track3 ends about
`1.43 m` from the origin. Scalar speed or collision-window tuning cannot repair
that topology mismatch.

Source geometry evidence:

```text
Results/metrics/track_geometry_v80_20260711.json
Results/metrics/four_track_completion_gate_v80_20260711.md
```

## Unified Mechanism

v117 adds closed-loop variants of the path primitives:

1. nearest-segment search includes the final-to-first segment;
2. pursuit-point traversal wraps from the final point to the first point;
3. speed interpolation wraps across the closing segment;
4. `PathPlanner.is_closed` defaults to `true` for the official closed tracks.

No track identity, obstacle location, official vehicle, road, sensor, scoring,
example, or training-material source is changed.

## Acceptance Order

1. source tests and controller deployability gate pass;
2. Track3 or Track4 shows official finish or material repeatable progress;
3. no new abnormal early stop;
4. collision variables do not materially regress;
5. only then expand to all four tracks with horizons derived from path length.

Reject and restore v80 path semantics if the candidate fails these gates.

## 2026-07-11 Outcome

The source tests and obstacle-controller deployability check passed, but the
first 1 s MWORKS gate stopped before model translation with `L5104-B0` while
loading the TADynamics dependency. The visible recovery route then became
unsafe to continue because window capture returned `window crop is outside
captured monitor` after the recovery dialog changed state.

This does not accept or reject the closed-loop mechanism. The v117 source edit
was removed and v80 path semantics were restored so an unverified candidate
does not remain active. Detailed evidence:

```text
Results/simulations/controller_v117_closed_loop_path_saidao3_1s_20260711/
Results/metrics/track3_candidate_review_v117_closed_loop_path_blocked_20260711.md
Results/evidence/controller_deployability_static_check_v80_restored_after_v117_20260711.md
```
