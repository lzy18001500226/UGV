# Unified Obstacle Avoidance v73 Plan

Status: rejected_as_accepted_baseline, 2026-07-10 CST

## Goal

Continue from accepted v48 and test one unified path-tracking geometry
mechanism: shorten the pure-pursuit lookahead only when the planned steering
angle is already large.

The goal is to reduce curve cutting and near-road-edge contacts without adding
per-track branches, more obstacle steering authority, or another blind scalar
scan.

## Evidence Basis

Current accepted best:

```text
v48 total wrapper score: 37.2 / 40
```

Latest four-track geometry review:

```text
Results/metrics/trajectory_geometry_review_v48_all_tracks_20260710.md
```

Relevant weak events:

- Track1 road events:
  - `6.55 s`, `(x=2.966, y=1.785)`, `dRoadCenter=0.4648`
  - `30.35 s`, `(x=12.63, y=6.126)`, `dRoadCenter=0.4605`
- Track2 road event:
  - `4.70 s`, `(x=3.644, y=0.4601)`, `dRoadCenter=0.4601`
- Track3:
  - obstacle event `1.05 s`, `(x=1.2, y=0.0799)`, `dNearestObs=0.1061`
  - road event `4.85 s`, `(x=3.364, y=0.4616)`, `dRoadCenter=0.4616`
- Track4 road events:
  - `4.35 s`, `(x=3.656, y=0.4637)`, `dRoadCenter=0.4637`
  - `90.15 s`, `(x=10.5, y=12.17)`, `dRoadCenter=0.4602`

Interpretation:

- Apart from Track3's first obstacle hit, the repeated failure geometry is
  near-road-edge behavior around `dRoadCenter ~= 0.46`.
- v45/v48 already slow the vehicle during large steering, but still use the
  same pursuit point geometry.
- Rejected follow-ups show that more global steering boost, lower path-authority
  scalar scans, allocation-only branches, and speed-only changes are not a good
  next direction.

## Hypothesis

Pure pursuit can cut curves when the lookahead point is too far ahead during
large steering. Shortening lookahead only after detecting a large planned
steering angle should pull the pursuit target closer to the local path segment,
reducing road-edge violations while preserving straight-line behavior.

## Planned Source Change

Allowed scope:

```text
Models/UGV/Control/PathPlanning/PathPlanner.mo
```

Add bounded parameters:

```modelica
parameter Real curve_short_lookahead_steer = 0.35;
parameter Real curve_short_lookahead_factor = 0.65;
parameter SIunits.Length curve_short_lookahead_min = 1.2;
```

After the first pure-pursuit steering calculation, recompute the pursuit point
and steering only when `abs(steering_angle)` is above the curve threshold:

```modelica
if abs(steering_angle) > curve_short_lookahead_steer then
  lookahead_dist := max(curve_short_lookahead_min,
    curve_short_lookahead_factor * lookahead_dist);
  pursuit_point := UGV.Control.PathPlanning.Internal.calculatePursuitPoint(
    path, closest_index, path_progress, lookahead_dist);
  steering_angle := UGV.Control.PathPlanning.Internal.purePursuitControl(
    x, y, pursuit_point[1], pursuit_point[2]);
end if;
```

Keep the existing v45/v48 curvature speed cap after the recomputed steering.

## Validation Gate

1. Run the source-only deployability checker.
2. Run Track1 first because it has two road events and a clean v48 runtime
   comparison.
3. If Track1 improves or is at least non-regressive without non-comparable early
   stop, run Track4 because v71 showed this area is sensitive to regressions.
4. If Track1/Track4 are acceptable, run all four tracks.
5. Reject v73 and restore v48 semantics if:
   - Track1 regresses below v48 `P=9.2`, or
   - Track4 regresses below v48 `P=9.2`, or
   - the change causes a new non-comparable early stop that cannot be explained
     by existing v48 runtime caveats.

## Result

Saved review:

```text
Results/metrics/track1_track4_track3_candidate_review_v73_curve_short_lookahead_20260710.md
```

v73 is rejected as the accepted baseline. It improved Track1 locally from
`P=9.2` to `P=9.6` and kept Track2/Track4 non-regressive, but Track3 regressed
from v48 `P=9.2`, `cR=1`, `cO=1` to `P=8.8`, `cR=2`, `cO=1`. Total score stayed
`37.2`, so v48 remains the current review-ready best. Source semantics were
restored to v48 and passed:

```text
Results/evidence/controller_deployability_static_check_v48_restored_after_v73_20260710.md
```

## Non-Goals

- No final package.
- No report polish.
- No physical UGV claim.
- No edits to official vehicle, road, sensor, scoring, example, or track files.
- No per-track logic.
