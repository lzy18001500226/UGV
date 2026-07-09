# Unified Obstacle Avoidance v62 Plan - Front-Centered Initial Bypass

## Goal

Try a small, sensor-gated initial bypass correction for the v48 Track3 early
obstacle event, without per-track logic and without touching official no-edit
zones.

## Evidence Basis

Current best remains v48:

- `Results/metrics/four_track_candidate_review_v48_opposing_steer_guard_20260710.md`
- `Results/metrics/trajectory_geometry_review_v48_20260710.md`
- `Results/metrics/signal_geometry_window_summary_v48_20260710.md`
- `Results/metrics/track3_candidate_review_v61_early_risk_arbitration_20260710.md`

v61 proved that a modest allocation-side steering boost is not enough: Track3
still has the same `1.05 s` obstacle event.

Additional geometry/source observation:

- Track3 first obstacle is at approximately `(1.2698, 0)`.
- v48 reaches the collision at about `(1.2, 0.08)`.
- The current `avoid_lateral` initial state always commands `steer := 0.6` for
  the first 2 seconds of avoidance before side-distance steering takes over.
- Track3 early sensor values show front distance falling below about `1.2`
  while left/right distances are almost equal.
- Track4 starts with a near obstacle at negative `y`, but its early front
  clearance is much larger, so a front-close gate should avoid changing its
  initial behavior at `t ~= 1 s`.

## Candidate Mechanism

Modify only:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Inside the `avoid_lateral` `ini_state` action, replace the fixed:

```modelica
steer := 0.6;
```

with a normal Sysblock-supported algorithm `if` statement:

```modelica
if df < 1.2 and abs(dl - dr) < 0.02 then
  steer := -0.45;
else
  steer := 0.6;
end if;
```

This is a unified sensor condition, not a track branch. It means: when the
obstacle is front-centered and close while side evidence is symmetric, take a
small negative initial bypass instead of the default positive initial bypass.
All other avoidance cases keep v48 behavior.

## Why This Is Different From Rejected Candidates

- It does not change allocation filter time constants, avoiding v60.
- It does not globally increase steering magnitude, avoiding v17.
- It does not use side-clearance-only steering, avoiding v19.
- It does not add speed attenuation or braking, avoiding v49/v51/v52.
- It is explicitly gated by front-close and left/right symmetry evidence.

## Risk

The condition may also trigger on another track when a centered close obstacle
appears. Therefore v62 must be tested as a unified algorithm:

1. Track3 first.
2. If Track3 improves or is comparable, Track4 and Track2 startup regression.
3. Track1 road-edge regression.
4. Four-track review only if the target and regressions are acceptable.

## Acceptance

Accept only if v62 improves Track3 or total four-track wrapper score without
introducing worse Track1/Track4 behavior. Otherwise restore v48 semantics and
record rejection evidence.

This plan does not create final competition submission material and does not
claim physical UGV success.
