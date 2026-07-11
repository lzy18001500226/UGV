# Track3 Candidate Review - v113 Conflict Speed Until 25s

Status: rejected, 2026-07-11 CST

## Candidate

v113 tested a wider bounded variant of the v103 conflict path-speed gate. It
started from the current accepted local wrapper baseline `v80_sharp_curve_speed_cap`.

Temporary source change:

```modelica
gain2.u = if time < 25 and speed_oa < 0 and steer_oa * unitDelay1.y < 0 and abs(unitDelay1.y) > 0.15 and unitDelay3.y > 0.35 then 0.35 else unitDelay3.y;
```

The candidate remained a unified control-allocation mechanism. It did not use
track id, official geometry edits, score-variable branches, or per-track
special casing.

## Evidence Basis

v103 proved that the full-run conflict gate can remove the Track3 road
collision, but it regresses Track1 later. v112 then proved that `time < 20`
expires too early, because Track3 still hits a road event after the gate
expires.

v113 extended that bounded window to `time < 25`.

## Gates

Static deployability gate passed before runtime:

```text
Results/evidence/controller_deployability_static_check_v113_conflict_speed_until25_20260711.md
ready_for_physical_claim=true, high=0, medium=0
```

## Track3 Result

| Candidate | Runtime | Exit | T/s | cR | cO | P | Evidence |
|---|---|---:|---:|---:|---:|---:|---|
| v80 baseline | `simulate_failed` | 2 | 59.4 | 1 | 1 | 9.2 | `Results/simulations/controller_v80_sharp_curve_speed_cap_saidao3_120s_20260710/` |
| v112 | `simulate_failed` | 2 | 26.3 | 1 | 1 | 9.2 | `Results/simulations/controller_v112_early_conflict_speed_window_saidao3_120s_20260711_retry_after_license/` |
| v113 | `simulate_failed` | 2 | 76.7 | 1 | 1 | 9.2 | `Results/simulations/controller_v113_conflict_speed_until25_saidao3_120s_20260711/` |

Collision-window analysis:

```text
Results/metrics/collision_window_analysis_v113_track3_20260711.md
```

v113 event times:

```text
t=1.05s:  cO 0 -> 1, P 10.0 -> 9.6
t=25.7s:  cR 0 -> 1, P 9.6 -> 9.2
```

The candidate delayed the road event compared with v112, but did not remove
either Track3 collision and did not improve the score variable.

## Decision

Reject v113. Do not expand it to Track1/Track2/Track4 regression testing
because the target weak-track evidence did not improve over v80.

The source was restored to v80 control-allocation semantics. Restore gate:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v113_20260711.md
ready_for_physical_claim=true, high=0, medium=0
```

## Next Direction

Do not repeat another scalar extension of the same conflict speed-window
candidate. The remaining Track3 losses are:

```text
early obstacle collision at t=1.05s
road event around the post-window exit region
```

Next candidates should inspect the initial obstacle event geometry/control
state or use a non-time-only release condition for the road event, while
preserving v80 as the accepted high-score baseline.

## Non-Claims

- No final `80 / 80` claim.
- No physical UGV success claim.
- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No report/package work.
