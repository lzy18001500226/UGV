# Track3 Candidate Review - v95 Early Front Brake Marker

Status: rejected, 2026-07-10 CST.

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
Docs/Design/unified_obstacle_avoidance_v95_plan_20260710.md
```

Mechanism tested in the longitudinal avoid state:

```modelica
if df < 1.1 and dl > 0.5 and dr > 0.5 then
  speed := -2;
else
  speed := -1;
end if;
```

The intent was to mark early front risk before the very-close collision window,
without modifying path planning, control allocation, official tracks, or
scoring.

## Static Gate

```text
Results/evidence/controller_deployability_static_check_v95_early_front_brake_marker_20260710.md
high=0, medium=0
```

## Runtime Result

Track3 run:

```text
Results/simulations/controller_v95_early_front_brake_marker_saidao3_120s_20260710/
simulate_failed, exit_state=2
T=2.45, cR=0, cO=0, P=10.0
```

This is not an accepted improvement. The apparent `P=10.0` comes from a very
short early stop and is not comparable with the current 120 s review target or
the v80 Track3 run.

## Diagnostics

```text
Results/metrics/collision_window_analysis_v95_track3_20260710.md
Results/metrics/signal_window_summary_v95_track3_20260710.md
```

The candidate avoided readable collision increments before termination, but it
created an early-stop artifact. This is the same evidence class as earlier
rejected short-run candidates: readable score variables do not count as a
baseline gain when the simulation terminates before a comparable run window.

## Decision

Reject v95 as an accepted baseline. Restore v80 semantics and continue the
long score sprint with a different evidence-backed mechanism.

Restore gate:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v95_20260710.md
high=0, medium=0
```

## Do Not Repeat Without New Evidence

- Do not accept early-front braking if it produces short-run `P=10.0` artifacts.
- Do not repeat stronger early reverse/braking markers without a separate
  mechanism that preserves comparable runtime.
- Do not move to report/package work because the score sprint remains active.
