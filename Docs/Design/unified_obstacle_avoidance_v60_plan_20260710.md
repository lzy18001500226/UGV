# Unified Obstacle Avoidance v60 Plan

Status: planned from v48 trajectory, official-track geometry, and signal-window evidence. Not yet accepted.

## Goal

Keep one unified controller for all four official tracks, starting from the v48 accepted semantics, and test whether faster obstacle-steering command establishment reduces early obstacle/road events without per-track branches.

## Evidence Basis

Geometry and signal evidence:

- `Results/metrics/trajectory_geometry_review_v48_20260710.md`
- `Results/metrics/signal_geometry_window_summary_v48_20260710.md`
- Track1 v48 score events occur near the road boundary, about `0.46 m` from road center, with no near-obstacle contact.
- Track3 v48 first event is an obstacle collision near start: nearest obstacle distance about `0.106 m`.
- At Track3 event 1, the obstacle controller has already requested reverse and `steer_oa=0.6`, but final `ctrlAlloc.steer` is only about `0.162`.
- The slow build-up is consistent with the obstacle-steering `FirstOrder(T=1)` inside `ControlAllocate.CtrlAlloc`.

## Change

Minimal source change:

```modelica
Modelica.Blocks.Continuous.FirstOrder firstOrder(T=0.35)
```

Only the obstacle-steering filter is changed. The speed filter remains `T=1`.

## Rationale

This is not another scalar scan of distance thresholds or path speed. It targets a measured mechanism: obstacle steering exists but reaches the actuator too slowly near the first high-risk obstacle.

Expected effect:

- Track3: stronger early lateral response before first obstacle contact.
- Track1: possible risk of extra road-boundary oscillation, so Track1 must be checked before acceptance.
- Four-track acceptance remains required because the algorithm is shared.

## Acceptance

Accept v60 only if it improves total four-track evidence or clearly improves Track3 without unacceptable Track1/Track4 regression.

Reject v60 if:

- Track1 regresses below v48 `P=9.2`.
- Track3 keeps `P=9.2` with no collision improvement.
- A new early-stop non-comparable score appears.
- The deployability static checker reports high/medium source risk.

## Scope Boundary

No official road, vehicle, sensor, scoring, or example files may be modified.
This plan does not claim final competition or physical UGV readiness.
