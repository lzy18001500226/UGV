# Track3 Candidate Review: v92 Front Emergency Straight Hold

Status: rejected_target_track_no_score_gain, 2026-07-10 CST

## Scope

Candidate: `v92_front_emergency_straight_hold`

Baseline: accepted local high-score `v80_sharp_curve_speed_cap`

Target track: `UGV.Test.Saidao3Eval`

Edited source during the test:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

No official vehicle, road, sensor, scoring, example, or official material files
were modified.

## Mechanism Tested

v92 tested a narrow front-emergency gate:

```modelica
df <= 0.25 and dl > 0.3 and dr > 0.3
```

Under that gate:

- longitudinal avoid state used `speed := -3` instead of `-1`;
- avoid-lateral initial state used `steer := 0` instead of `0.6`.

The intent was to target only the Track3 early front-obstacle event while
leaving the later side-road events unchanged.

## Evidence

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v92_plan_20260710.md
```

Static source gate:

```text
Results/evidence/controller_deployability_static_check_v92_front_emergency_straight_hold_20260710.md
Results/evidence/controller_deployability_static_check_v92_front_emergency_straight_hold_20260710.json
```

Runtime target run:

```text
Results/simulations/controller_v92_front_emergency_straight_hold_saidao3_120s_20260710/
```

Comparison analysis:

```text
Results/metrics/collision_window_analysis_v80_v92_track3_20260710.md
Results/metrics/collision_window_analysis_v80_v92_track3_20260710.json
Results/metrics/signal_window_summary_v80_v92_track3_20260710.md
Results/metrics/signal_window_summary_v80_v92_track3_20260710.json
```

Restored baseline gate:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v92_20260710.md
Results/evidence/controller_deployability_static_check_v80_restored_after_v92_20260710.json
```

## Result

| Candidate | Track | Runtime | Exit | T/s | cR | cO | P |
|---|---|---|---:|---:|---:|---:|---:|
| v80 | Track3 | `simulate_failed` | 2 | 59.4 | 1 | 1 | 9.2 |
| v92 | Track3 | `simulate_failed` | 2 | 43.9 | 1 | 1 | 9.2 |

Event comparison:

| Event | v80 | v92 |
|---|---:|---:|
| first obstacle event | 1.05 s | 1.10 s |
| first road event | 4.85 s | 6.15 s |

v92 delayed both score events, but did not remove either event and shortened
the target run. The score remained `P=9.2`, so this is not a valid improvement
toward the 80-point goal.

## Decision

Reject v92 and keep v80 as the current accepted high-score baseline.

Do not continue this exact direction as a scalar scan:

- do not widen the `df <= 0.25` band;
- do not increase reverse speed further;
- do not keep combining front emergency reverse with fixed/zero/negative
  initial steering without a new mechanism and evidence.

The useful lesson is that the early front-obstacle event can be delayed but not
removed by a local emergency hold. The next candidate should either:

1. change the approach before the obstacle controller enters emergency mode; or
2. use a more structural local-planning behavior rather than another immediate
   speed/steer authority patch.

No final competition score, physical UGV success, or submission readiness is
claimed.
