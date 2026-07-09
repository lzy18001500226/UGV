# Track3 Candidate Review: v66 Road-Edge Initial Steering Boost

timestamp: 2026-07-10 06:25 CST
baseline: v48 opposing-steer guard
decision: rejected, source restored to v48 semantics

## Scope

v66 tested a narrow road-edge boost in the `avoid_lateral` initial state:

```modelica
if dl < 0.16 or dr < 0.16 then
  steer := 0.8;
else
  steer := 0.6;
end if;
```

This kept v48's initial steering direction, did not branch on track name, and
did not edit official vehicle, road, sensor, scoring, example, or official
material files.

Plan and attribution:

```text
Docs/Design/unified_obstacle_avoidance_v66_plan_20260710.md
Results/evidence/track3_v48_event_source_attribution_20260710.md
Results/metrics/track3_v48_countpoint_source_attribution_20260710.md
```

## Static Gates

v66 gate:

```text
Results/evidence/controller_deployability_static_check_v66_road_edge_initial_steer_boost_20260710.md
Results/evidence/controller_deployability_static_check_v66_road_edge_initial_steer_boost_20260710.json
```

Restored v48 gate:

```text
Results/evidence/controller_deployability_static_check_v48_restored_after_v66_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v66_20260710.json
```

Both reported:

```text
ready_for_physical_claim=true
high=0
medium=0
```

## Runtime Result

Track3 wrapper run:

```text
Results/simulations/controller_v66_road_edge_initial_steer_boost_saidao3_120s_20260710/
```

Comparison:

| Candidate | Track | Runtime | Exit | T/s | cR | cO | P | Decision |
|---|---|---|---:|---:|---:|---:|---:|---|
| v48 | Track3 | `simulate_failed` with result variables | 2 | 112.45 | 1 | 1 | 9.2 | Keep current best baseline. |
| v66 | Track3 | `simulate_failed` with result variables | 2 | 2.65 | 0 | 1 | 9.6 | Reject: non-comparable early stop artifact. |

Offline comparison:

```text
Results/metrics/signal_window_summary_v48_v66_track3_20260710.md
Results/metrics/signal_window_summary_v48_v66_track3_20260710.json
```

## Findings

- v66 did not remove the first Track3 obstacle collision. The `cO: 0 -> 1`
  event remained at `1.05 s`.
- The apparent score increase to `P=9.6` is not accepted because the run ended
  at `T=2.65`, before the comparable road-event window where v48 loses the
  second `0.4` point.
- Since Track3 target evidence did not produce a comparable improvement,
  Track1 regression and four-track expansion were not run.

## Decision

Reject v66 and continue from v48.

Do not continue road-edge initial-steering magnitude scans without a different
mechanism reason. The remaining useful directions are:

1. deeper source/runtime attribution for why Track3 early obstacle collision
   occurs despite `flag=1` and fixed positive initial steer; or
2. research into four-distance, code-generation-friendly local avoidance that
   changes the trajectory before the first obstacle event without relying on
   per-track branches or final-score artifacts; or
3. report/physical-transfer hardening while keeping v48 as the current
   review-ready controller.

No final submission package was created or sent.
