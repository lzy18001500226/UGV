# Unified Obstacle Avoidance v80 Plan

Status: accepted_as_current_high_score_candidate_with_runtime_caveat, 2026-07-10 CST

## Goal

Continue from accepted v74 after rejecting v79. Test a narrow PathPlanner
speed-shaping mechanism for extreme path curvature only.

This is not a broad speed clamp, not a per-track branch, and not another
initial-steering or avoid-dwell scan.

## Evidence Basis

Accepted v74 still has a late Track4 road collision:

```text
Track4 t=104 s:
pathPlanner.steering_angle = 1.638
pathPlanner.target_v = 0.75
ctrlAlloc.steer = 1.937
cR: 1 -> 2
```

v50 already showed that lowering the moderate-curvature threshold with the
same `0.75` speed cap does not solve Track3. v70 showed that a broad
active-avoid speed clamp can produce non-comparable early-stop behavior.

v80 therefore targets only extreme path curvature:

```text
abs(steering_angle) > 1.0
```

## Planned Source Change

Allowed source:

```text
Models/UGV/Control/PathPlanning/PathPlanner.mo
```

Add parameters:

```modelica
parameter Real sharp_curve_slowdown_steer = 1.0;
parameter Real sharp_curve_slowdown_speed = 0.55;
```

Add a second speed cap after the existing v74 moderate-curve cap:

```modelica
if abs(steering_angle) > sharp_curve_slowdown_steer
   and target_v > sharp_curve_slowdown_speed then
  target_v := sharp_curve_slowdown_speed;
end if;
```

## Validation Gate

1. Run source deployability checker.
2. Run Track4 first because the target event is the only v74 event with
   `abs(steering_angle) > 1.0`.
3. Continue to regression only if Track4 improves without early-stop artifact.
4. Reject and restore v74 if Track4 stays at `P=9.2` or gets worse.

## Non-Goals

- No final competition score claim.
- No physical UGV success claim.
- No report/package work.
- No official material or scoring edits.

## Result

v80 is accepted as the current high-score local wrapper candidate:

```text
Track1: T=17.4, cR=1, cO=0, P=9.6, simulate_failed / exit_state=2
Track2: T=120.0, cR=1, cO=0, P=9.6, simulate_returned_true / exit_state=0
Track3: T=59.4, cR=1, cO=1, P=9.2, simulate_failed / exit_state=2
Track4: T=120.0, cR=1, cO=0, P=9.6, simulate_returned_true / exit_state=0
Total wrapper score: 38.0
```

Compared with v74, Track4 improves from `P=9.2,cR=2` to `P=9.6,cR=1`.
Track3 keeps `P=9.2,cR=1,cO=1` but regresses from clean `T=120.0` runtime to
`simulate_failed/T=59.4`, so this remains a high-score candidate with a visible
runtime caveat.

Review: `Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md`.
