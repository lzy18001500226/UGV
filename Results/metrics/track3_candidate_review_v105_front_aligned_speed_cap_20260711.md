# Track3 Candidate Review - v105 Front-Aligned Speed Cap

Status: rejected_no_score_gain, 2026-07-11 CST.

## Baseline

Accepted local wrapper baseline remains:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper score: 38.0 / 40
Track3: simulate_failed, T=59.4, cR=1, cO=1, P=9.2
```

## Candidate

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v105_plan_20260711.md
```

Mechanism tested in `ControlAllocate/package.mo`:

```modelica
gain2.u = if speed_oa < 0 and steer_oa > 0.4 and abs(steer_pp) < 0.12 and unitDelay3.y > 0.55
  then 0.55
  else unitDelay3.y;
```

The intent was to reduce the path-speed contribution only during straight,
front-aligned obstacle approach, avoiding v92/v93/v95 reverse dominance and
v103/v104 conflict speed-gate behavior.

## Static Gate

```text
Results/evidence/controller_deployability_static_check_v105_front_aligned_speed_cap_20260711.md
ready_for_physical_claim=true
high=0
medium=0
```

## Runtime Result

Target run:

```text
Results/simulations/controller_v105_front_aligned_speed_cap_saidao3_120s_20260711/
simulate_failed, exit_state=2
T=67.65
cR=1
cO=1
P=9.2
```

Comparison:

```text
v80 Track3:  T=59.4,  cR=1, cO=1, P=9.2
v105 Track3: T=67.65, cR=1, cO=1, P=9.2
```

## Diagnostics

```text
Results/metrics/signal_window_summary_v80_v105_track3_20260711.md
Results/metrics/ctrlalloc_contribution_analysis_v80_v105_track3_20260711.md
```

v105 delayed both Track3 penalties but did not remove them:

```text
First obstacle event:
  v80  t=1.05, final_speed=0.7196, P 10.0 -> 9.6
  v105 t=1.60, final_speed=0.1767, P 10.0 -> 9.6

First road event:
  v80  t=4.85,  P 9.6 -> 9.2
  v105 t=18.75, P 9.6 -> 9.2
```

## Decision

Reject v105 as an accepted baseline. It improves timing margin but not score or
collision counts, so it is not worth expanding to Track1/2/4.

Restore accepted v80 ControlAllocate semantics before the next candidate. The
next mechanism should focus on path geometry or steering behavior, not another
speed-only suppression route.
