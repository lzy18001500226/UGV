# Track3 Candidate Review: v51 Straight Brake Arbitration

Status: rejected_target_track_early_stop, 2026-07-10 CST

## Candidate

v51 continued from v48 and tested a narrow `ControlAllocate` speed-arbitration
guard:

```modelica
gain2.u = if speed_oa < 0 and abs(unitDelay1.y) < 0.10
  then 0.4 * unitDelay3.y
  else unitDelay3.y;
```

The goal was to target the straight-line early Track3 obstacle window without
repeating v49's broad path-speed attenuation during all reverse avoidance.

## Evidence

Static gate:

```text
Results/evidence/controller_deployability_static_check_v51_straight_brake_arbitration_20260710.md
```

Target run:

```text
Results/simulations/controller_v51_straight_brake_arbitration_saidao3_120s_20260710/
```

Post-run analysis:

```text
Results/metrics/collision_window_analysis_v51_straight_brake_arbitration_track3_20260710.md
Results/metrics/signal_window_summary_v51_straight_brake_arbitration_track3_20260710.md
```

## Result

| Candidate | Runtime | Exit | T/s | cR | cO | P |
|---|---|---:|---:|---:|---:|---:|
| v48 Track3 recorded metrics | simulate_failed with result variables | 2 | 112.45 | 1 | 1 | 9.2 |
| v51 Track3 | simulate_failed with result variables | 2 | 2.25 | 0 | 0 | 10.0 |

`P=10.0` is not valid improvement evidence because the run exits at only
`2.25 s`, before the comparable 120 s review window. This matches the rejected
class of early-stop score inflation seen in v28 and v49.

## Decision

Reject v51 and restore v48 source semantics.

Reason:

```text
The narrow straight-brake arbitration suppresses forward path-speed authority
too early and causes a non-comparable Track3 terminal state.
```

Do not continue this route as a path-speed attenuation scan. The next useful
route should either improve evidence automation/diagnostics or use a different
deployable mechanism that does not create early-stop score inflation.
