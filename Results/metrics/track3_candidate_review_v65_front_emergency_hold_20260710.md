# Track3 Candidate Review - v65 Front Emergency Hold

generated_at: 2026-07-10 CST

## Decision

Reject `v65_front_emergency_hold` and continue from the accepted v48
opposing-steer guard baseline.

The candidate was unified and track-agnostic, passed the static source gate,
and measurably reduced allocated speed near the first Track3 obstacle event.
However, it did not improve collision count or score and shortened the run
substantially, so it is not accepted.

## Candidate

Baseline:

```text
v48 opposing-steer guard
```

Candidate source mechanism inside the existing longitudinal `avoid` state:

```modelica
if df <= 0.25 then
  speed := -3;
else
  speed := -1;
end if;
flag := true;
```

Scope:

- one unified controller for all four official tracks
- no branch on track name, wrapper name, run id, or score variables
- implementation target only:
  `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`
- no edits to official vehicle, road, sensor, scoring, or example packages

## Evidence

Plan and research:

```text
Docs/Design/unified_obstacle_avoidance_v65_plan_20260710.md
References/research/post_v64_limited_sensor_behaviors_20260710/MANIFEST.md
References/research/post_v64_limited_sensor_behaviors_20260710/source_notes.md
```

Static source gate:

```text
Results/evidence/controller_deployability_static_check_v65_front_emergency_hold_20260710.md
Results/evidence/controller_deployability_static_check_v65_front_emergency_hold_20260710.json
```

Runtime evidence:

```text
Results/simulations/controller_v65_front_emergency_hold_saidao3_120s_20260710/
```

Comparison diagnostics:

```text
Results/metrics/collision_window_analysis_v48_v65_track3_20260710.md
Results/metrics/signal_window_summary_v48_v65_track3_20260710.md
```

Restore gate:

```text
Results/evidence/controller_deployability_static_check_v48_restored_after_v65_20260710.md
Results/evidence/controller_deployability_static_check_v48_restored_after_v65_20260710.json
```

## Result Summary

| Candidate | Runtime status | Exit state | T/s | cR | cO | P |
|---|---|---:|---:|---:|---:|---:|
| v48 Track3 | `simulate_failed` with readable score variables | 2 | 112.45 | 1 | 1 | 9.2 |
| v65 Track3 | `simulate_failed` with readable score variables | 2 | 36.55 | 1 | 1 | 9.2 |

Signal comparison around the first obstacle event:

| Candidate | First obstacle event | `ctrlAlloc.speed` | `chart.speed` | `df` |
|---|---:|---:|---:|---:|
| v48 | 1.05 s | 0.7196 | -1 | 0.01324 |
| v65 | 1.15 s | 0.3623 | -3 | 0.0168 |

## Interpretation

v65 proved that a very close-front emergency band can reduce final allocated
speed and slightly delay the first obstacle event. It still does not avoid the
obstacle or the later road event, and the run ends much earlier than v48.

Do not continue this route by increasing reverse speed, widening the emergency
front threshold, or scanning emergency-hold constants. The next candidate needs
a different mechanism or deeper trajectory/source attribution.

## Non-Claims

- This is MWORKS/Sysplorer wrapper evidence, not physical UGV proof.
- This does not claim final competition score or submission readiness.
- This does not authorize final competition packaging or sending.
