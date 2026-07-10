# Track3 Candidate Review - v101 Narrow Conflict Handoff

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
Docs/Design/unified_obstacle_avoidance_v101_plan_20260711.md
```

Temporary mechanism in `Models/UGV/Control/ControlAllocate/package.mo`:

```modelica
gain3.u = if speed_oa < 0 and steer_oa > 0 and unitDelay1.y < 0
  and steer_oa * unitDelay1.y < 0 and abs(steer_oa) > 0.55
  then 0.25 * unitDelay1.y
  else if speed_oa < 0 and steer_oa * unitDelay1.y < 0
  then 0.5 * unitDelay1.y
  else unitDelay1.y;
```

The intent was to keep the accepted default half attenuation but further reduce
opposing path-steer contribution when obstacle avoidance is strongly steering
positive and braking.

## Static Gate

```text
Results/evidence/controller_deployability_static_check_v101_narrow_conflict_handoff_20260711.md
ready_for_physical_claim=true
high=0
medium=0
```

This is a source-only risk gate and does not replace MWORKS model simulation.

## Runtime Result

Track3 evidence:

```text
Results/simulations/controller_v101_narrow_conflict_handoff_saidao3_120s_20260711/
simulate_failed
exit_state=2
T=40.3
cR=1
cO=1
P=9.2
```

Comparison:

```text
v80 Track3:  T=59.4, cR=1, cO=1, P=9.2
v101 Track3: T=40.3, cR=1, cO=1, P=9.2
```

v101 did not improve Track3 score or collision count and shortened the run.

## Diagnostics

Collision windows:

```text
Results/metrics/collision_window_analysis_v101_narrow_conflict_handoff_track3_20260711.md
```

Events:

```text
1.05s: cO 0 -> 1
4.65s: cR 0 -> 1
```

Signal summary:

```text
Results/metrics/signal_window_summary_v101_narrow_conflict_handoff_track3_20260711.md
```

Key observation:

```text
4.65s: steer_oa=0.6, steer_pp=-0.220, gain3.u=-0.055,
       final steer=0.240, cR still occurs
```

Compared with v80 Track3's road-event final steer near `0.185`, v101 increased
the final steer but the road event still occurred slightly earlier. This means
the remaining Track3 weakness is not solved by a simple stronger
obstacle-side steering arbitration.

## Decision

Reject v101. Do not expand to Track1/2/4 because the target Track3 gate did not
improve beyond v80.

Source was restored to the accepted v80/v48 `ControlAllocate` arbitration
semantics after this review:

```text
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0
  then 0.5 * unitDelay1.y
  else unitDelay1.y;
```

## Reusable Learning

- The v80/v101 Track3 road event persists even when final steering rises from
  roughly `0.185` to `0.240`.
- Further scans of path-conflict attenuation are unlikely to be the next best
  use of time unless paired with a different state or trajectory mechanism.
- A better v102 direction should inspect geometric trajectory/pose evolution,
  speed/reverse timing, or planner path geometry rather than only final steering
  magnitude.

No final 80/80 claim, physical UGV success claim, report readiness claim, or
submission claim is made from v101.
