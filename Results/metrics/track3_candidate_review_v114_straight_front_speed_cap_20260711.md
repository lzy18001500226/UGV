# Track3 Candidate Review - v114 Straight Front Speed Cap

Status: rejected, 2026-07-11 CST

## Candidate

v114 tested a narrow control-allocation cap for the fixed Track3 early obstacle
event. It started from the accepted local wrapper baseline
`v80_sharp_curve_speed_cap`.

Temporary source change:

```modelica
gain2.u = if speed_oa < 0 and abs(unitDelay1.y) < 0.05 and unitDelay3.y > 0.35 then 0.35 else unitDelay3.y;
```

The candidate was designed to reduce path-speed dominance when obstacle
avoidance is braking and the path steering is nearly straight.

## Evidence Basis

The fixed Track3 obstacle event in v80/v103/v113 occurs at `t=1.05s` with:

```text
df ~= 0.013
speed_oa = -1
pathPlanner.target_v = 1
ctrlAlloc.speed ~= 0.72
```

Supporting diagnostics:

```text
Results/metrics/track3_event_signal_summary_v80_v103_v113_20260711.md
Results/metrics/track3_event_signal_summary_v80_v103_v113_ctrlalloc_20260711.md
Results/metrics/track3_path_progress_signal_summary_v80_v103_v113_20260711.md
```

## Gates

Static deployability gate passed before runtime:

```text
Results/evidence/controller_deployability_static_check_v114_straight_front_speed_cap_20260711.md
ready_for_physical_claim=true, high=0, medium=0
```

## Track3 Result

| Candidate | Runtime | Exit | T/s | cR | cO | P | Evidence |
|---|---|---:|---:|---:|---:|---:|---|
| v80 baseline | `simulate_failed` | 2 | 59.4 | 1 | 1 | 9.2 | `Results/simulations/controller_v80_sharp_curve_speed_cap_saidao3_120s_20260710/` |
| v114 | `simulate_failed` | 2 | 1.6 | 0 | 0 | 10.0 | `Results/simulations/controller_v114_straight_front_speed_cap_saidao3_120s_20260711/` |

Collision-window analysis:

```text
Results/metrics/collision_window_analysis_v114_track3_20260711.md
```

The apparent `P=10.0` is not accepted because the run stops at `T=1.6`, far
before a comparable 120 s evaluation window and before the normal Track3 road
event window.

## Decision

Reject v114 as a short-run artifact. Do not expand it to Track1/Track2/Track4.

The source was restored to v80 control-allocation semantics. Restore gate:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v114_20260711.md
ready_for_physical_claim=true, high=0, medium=0
```

## Next Direction

Do not repeat a hard low straight-front path-speed cap. The mechanism shows the
early obstacle loss is sensitive to path-speed dominance, but an abrupt cap can
create non-comparable early termination. A future candidate needs a smoother
or state-conditioned start/brake handoff, or a trajectory-level correction that
does not immediately stop the run.

## Non-Claims

- No final `80 / 80` claim.
- No physical UGV success claim.
- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No report/package work.
