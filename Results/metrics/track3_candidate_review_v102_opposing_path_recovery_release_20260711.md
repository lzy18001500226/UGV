# Track3 Candidate Review - v102 Opposing Path Recovery Release

Status: rejected, 2026-07-11 CST.

## Baseline

Accepted baseline remains:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper total: 38.0 / 40
Track3: simulate_failed, T=59.4, cR=1, cO=1, P=9.2
```

## Candidate

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v102_plan_20260711.md
```

Mechanism tested in `Models/UGV/Control/ControlAllocate/package.mo`:

```modelica
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0 and abs(unitDelay1.y) <= 0.2
  then 0.5 * unitDelay1.y
  else unitDelay1.y;
```

The intent was to keep v80/v48's opposing path-steer attenuation for weak path
signals, but release full path recovery authority when active reverse obstacle
avoidance and a material opposing path signal are present.

## Static Gate

```text
Results/evidence/controller_deployability_static_check_v102_opposing_path_recovery_release_20260711.md
ready_for_physical_claim=true
high=0
medium=0
```

## Runtime Result

Track3 runtime evidence:

```text
Results/simulations/controller_v102_opposing_path_recovery_release_saidao3_120s_20260711/
simulate_failed
exit_state=2
T=32.3
cR=1
cO=1
P=9.2
```

Comparison:

```text
v80 Track3:  T=59.4, cR=1, cO=1, P=9.2
v102 Track3: T=32.3, cR=1, cO=1, P=9.2
```

v102 does not improve score variables and shortens runtime versus v80, so it is
not accepted and is not expanded to Track1/2/4.

## Diagnostics

Collision windows:

```text
Results/metrics/collision_window_analysis_v102_opposing_path_recovery_release_track3_20260711.md
```

Events:

```text
1.05s: cO 0 -> 1
4.85s: cR 0 -> 1
```

Signal summary:

```text
Results/metrics/signal_window_summary_v102_opposing_path_recovery_release_track3_20260711.md
```

Key observation:

```text
4.85s: steer_pp=-0.2213, gain3.u=-0.2213, steer_oa=0.6, final steer=0.07439
```

Releasing full path-steer recovery reduced final steering substantially versus
v80, but the road event still occurred at the same event time. This rules out
simple opposing-path recovery release as a sufficient fix.

## Decision

Reject v102. Source was restored to the accepted v80/v48 control-allocation
semantics after this review and rechecked:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v102_20260711.md
ready_for_physical_claim=true
high=0
medium=0
```

## Reusable Learning

- Full release of opposing path recovery can lower the final Track3 road-window
  steering to about `0.074`, but that still does not remove the road collision.
- Do not continue with small scalar changes around the `abs(unitDelay1.y)`
  release threshold.
- The next useful candidate should address the vehicle's side exposure before
  the 4.85s road event or use a different diagnostic surface, not only final
  steering authority at the event sample.

No final 80/80 claim, physical UGV success claim, report readiness claim, or
submission claim is made from v102.
