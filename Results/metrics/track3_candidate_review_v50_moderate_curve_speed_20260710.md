# Track3 Candidate Review: v50 Moderate Curve Speed

Status: rejected, 2026-07-10 CST

## Candidate

v50 continued from v48 and lowered the path-planner curvature speed-regulation
threshold:

```modelica
curve_slowdown_steer = 0.20
curve_slowdown_speed = 0.75
```

The mechanism was track-agnostic and was intended to slow the vehicle during
moderate steering windows where v48 still had road contacts.

## Evidence

Static gate:

```text
Results/evidence/controller_deployability_static_check_v50_moderate_curve_speed_20260710.md
```

Runtime:

```text
Results/simulations/controller_v50_moderate_curve_speed_saidao3_120s_20260710/
```

Post-run analysis:

```text
Results/metrics/collision_window_analysis_v50_moderate_curve_speed_track3_20260710.md
Results/metrics/signal_window_summary_v50_moderate_curve_speed_track3_20260710.md
```

## Result

| Track | Runtime | T/s | cR | cO | P |
|---|---|---:|---:|---:|---:|
| Saidao3Eval | simulate_returned_true | 120.0 | 1.0 | 1.0 | 9.2 |

Collision events remained:

- `1.05 s`: obstacle collision, `P 10.0 -> 9.6`
- `5.05 s`: road collision, `P 9.6 -> 9.2`

At `5.05 s`, the lower threshold did reduce the path speed target to `0.75`,
but the road collision still occurred. At `1.05 s`, the first obstacle
collision still occurred before this moderate-curve mechanism could address the
failure.

## Decision

Reject v50.

Reason: the v50 validation gate required Track3 to remove a collision or
improve `P` without a worse terminal state. v50 improved runtime comparability
over the v48 Track3 caveat, but it did not improve the Track3 score or
collision counts:

```text
v48 Track3 recorded metrics: T=112.45, cR=1, cO=1, P=9.2, simulate_failed with result variables
v50 Track3 metrics:          T=120.0,  cR=1, cO=1, P=9.2, simulate_returned_true
```

This is useful evidence, but not enough to replace the current v48 best
four-track candidate.

## Restore

Restore v48 source semantics in `Models/UGV/Control/PathPlanning/PathPlanner.mo`:

```modelica
curve_slowdown_steer = 0.35
curve_slowdown_speed = 0.75
```

Do not continue this route as broader path-speed attenuation or another simple
threshold scan. The next candidate should target the actual early Track3
obstacle event or use a new deployable unified mechanism with stronger evidence
than scalar speed-threshold tuning.
