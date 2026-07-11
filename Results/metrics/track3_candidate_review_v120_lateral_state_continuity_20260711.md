# Track3 Candidate Review: v120 Lateral State Continuity

Status: rejected and restored to v80

## Hypothesis

v80 emits a one-sample `flag=false` pulse every two seconds while a side
distance is still below the obstacle trigger.  The pulse resets the outer
lateral state and repeatedly restarts the fixed `+0.6` initial turn.  v120
required obstacle-clear distances before allowing that outer lateral reset,
while leaving the longitudinal state and all controller gains unchanged.

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v120_lateral_state_continuity_plan_20260711.md
```

## Gates

- deployability checker: `high=0`, `medium=0`
- targeted tests: `7 passed`
- Track3 1 s load/check/simulate: passed, `exit_state=0`
- Track3 120 s request: abnormal early stop, `exit_state=2`

Evidence:

```text
Results/simulations/controller_v120_lateral_state_continuity_saidao3_1s_20260711/
Results/simulations/controller_v120_lateral_state_continuity_saidao3_120s_20260711/
Results/metrics/v120_track3_signal_windows_20260711.md
Results/metrics/v120_track3_signal_windows_20260711.json
```

## Comparison

| Candidate | T/s | cR | cO | P | terminal path segment | completion |
|---|---:|---:|---:|---:|---:|---|
| restored v80 | 59.4 | 1 | 1 | 9.2 | 29 | not finished |
| v120 | 52.95 | 1 | 2 | 8.8 | 16 | not finished |

v120 changed the mechanism as intended: saved `steer_oa` now changes sign
instead of remaining fixed positive.  However, the candidate added an obstacle
collision, stopped earlier, and reached much less of the path.  Keeping the
gap-directed substate active across the longitudinal pulse exposes noisy
left/right decisions and is not a completion or score gain.

## Decision

Reject v120, do not expand it to Tracks 1, 2, or 4, and restore the exact v80
controller source.  Do not repeat this outer-lateral release condition without
a separate bounded direction-latching or hysteresis mechanism supported by new
evidence.
