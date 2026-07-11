# v133 Reverse-Motion Escape Direction Plan

Status: rejected after native Track2 gates; v80 controller semantics restored.

## New Evidence

The v80 Track2 baseline was reproduced with position exports through its
repeatable early termination:

```text
T=305.15 s, cR=1, cO=0, P=9.6, exit_state=2
distanceSensor1.d=1004.6703
end position=(28.0947, 14.6752)
```

The official road overlay shows a long, slow traversal of the right-hand
vertical segment after the first road collision at 4.70 s.  During the final
120--305 s window, `chart.speed=-1`, while the right clearance stays near
0.14 m and the lateral chart outputs `chart.steer=+0.6`.  The path planner
also requests a positive steering angle, so the final allocator input remains
positive even though the vehicle is commanded to reverse.

Evidence:

```text
Results/simulations/diagnostic_v80_track2_completion_geometry_310s_20260712/
Results/metrics/trajectory_event_review_v80_track2_completion_20260712.md
Results/figures/trajectory_event_review_v80_track2_completion_20260712/
```

## Hypothesis

The existing side-clearance state machine chooses its steering sign as though
the vehicle were moving forward.  However, the longitudinal state is in full
reverse whenever `flag=true`.  Applying a forward escape steering sign while
reversing reverses the lateral travel direction and can maintain the vehicle
against the near-side boundary.

This is not a speed-floor, side-hold, steering-magnitude, or path-steer
attenuation scan.  It preserves all thresholds, the two-second reverse action,
and the path planner.  It changes only the direction mapping of the two
existing `avoid_lateral` states while reverse avoidance is active.

## Scoped Change

Only modify:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

In `avoid_lateral`, swap the signs of the left/right escape outputs:

```text
turn_left:  +min(0.8, 2 * abs(dl - dr)) -> -min(...)
turn_right: -min(0.8, 2 * abs(dl - dr)) -> +min(...)
```

The parallel `curise_lateral` state machine remains unchanged, so forward
cruise behavior is deliberately preserved.

## Gates And Decision

1. Run `check_controller_deployability.py` and `python -m pytest Scripts/tests -q`.
2. Run Track2 for 1 s with the native `-gui` MWORKS API route.
3. Run Track2 for 120 s.  Reject immediately on early abnormal termination,
   any new collision, or score below v80 (`P=9.6`).
4. Only if the 120 s result is comparable and shows material progress, run the
   310 s completion diagnostic.  A finish is required before widening to the
   other official tracks.
5. On any failed gate, restore exactly the v80 controller semantics, re-run
   the static checks, and record the rejection.  Do not treat a shorter
   terminal distance as a finish.

No result from this plan claims official completion, an 80-point score,
physical-car performance, or submission readiness.

## Result And Decision

The final v133 source passed the static deployability gate and the native
one-second Track2 gate.  The latter reached `T=1.0` with `cR=0`, `cO=0`, and
`P=10.0`; it establishes only that the edited Sysblock model loads, checks,
and simulates.

The comparable 120-second Track2 gate rejected the hypothesis:

```text
v133: SimulateModel=false, exit_state=2, T=91.0, cR=1, cO=0, P=9.6
v80:  SimulateModel=true,  exit_state=0, T=120.0, cR=1, cO=0, P=9.6
```

Thus the reversed lateral mapping causes an early terminal state and provides
no score gain.  It is rejected before the 310-second diagnostic or any
cross-track run.  The two `avoid_lateral` output signs were restored to the
v80 mapping; `curise_lateral` was not changed.

Final evidence:

```text
Results/simulations/candidate_v133_reverse_motion_escape_final_track2_1s_20260712/
Results/simulations/candidate_v133_reverse_motion_escape_final_track2_120s_20260712/
Results/evidence/controller_deployability_static_check_v133_reverse_motion_escape_final_20260712.md
Results/evidence/controller_deployability_static_check_v80_restored_after_v133_20260712.md
Results/evidence/pytest_v80_restored_after_v133_20260712.console.txt
```
