# Track3 Candidate Review: v46 Speed Channel 120 Percent

Status: rejected_target_track_regression, 2026-07-10 CST

## Candidate

v46 keeps the accepted v45 path curvature speed cap and changes only the
obstacle-avoidance speed contribution in `ControlAllocate`:

```modelica
gain1(k=1.2*factor_oa)
```

This is one unified mechanism. It does not add per-track logic and does not
modify official vehicle, road, sensor, scoring, example, or track files.

## Gate

Static source gate:

```text
Results/evidence/controller_deployability_static_check_v46_speed_channel_120pct_20260710.md
```

Result:

```text
ready_for_physical_claim=true
high=0
medium=0
```

## Target Track Evidence

Target run:

```text
Results/simulations/controller_v46_speed_channel_120pct_saidao3_120s_20260710/
```

Track3 result:

| Candidate | Runtime | Exit | T/s | cR | cO | P |
|---|---|---:|---:|---:|---:|---:|
| v45 | `simulate_returned_true` | 0 | 120.0 | 1 | 1 | 9.2 |
| v46 | `simulate_failed` | 2 | 45.2 | 1 | 1 | 9.2 |

Collision-window analysis:

```text
Results/metrics/collision_window_analysis_v46_speed_channel_120pct_track3_20260710.md
```

## Decision

Reject v46. It did not improve the target Track3 score and regressed runtime
comparability from the v45 120 s run to a `simulate_failed` result ending at
`T=45.2`.

Do not continue this candidate to four-track regression. Restore accepted v45
source semantics before the next candidate.

## Lesson

The v45 remaining Track3 issue is not safely fixed by increasing the
obstacle-avoidance speed-channel contribution. v28 showed that a 2x change is
too aggressive; v46 shows that even a mild 1.2x change can shorten the run
without improving score. The next mechanism should not continue speed-channel
gain escalation.
