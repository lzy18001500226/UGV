# Track3 Candidate Review - v112 Early Conflict Speed Window

Status: rejected, 2026-07-11 CST

## Candidate

v112 tested a bounded variant of the v103 conflict path-speed gate. The goal
was to preserve v103's Track3 road-collision reduction while avoiding the later
Track1 regressions seen in the full four-track v103 review.

Temporary source change:

```modelica
gain2.u = if time < 20 and speed_oa < 0 and steer_oa * unitDelay1.y < 0 and abs(unitDelay1.y) > 0.15 and unitDelay3.y > 0.35 then 0.35 else unitDelay3.y;
```

The candidate remained a unified control-allocation mechanism, not a per-track
branch.

## Runtime Recovery

The first v112 runtime attempt hit a MWORKS/Sysplorer license blocker
(`L5104-B0`). License recovery was verified before retrying the algorithm run:

```text
Results/evidence/mworks_license_recovery_v112_20260711.md
Results/simulations/license_recovery_probe_1s_20260711_1440/
```

That recovery proves only the runtime channel; it is not score evidence.

## Track3 Result

| Candidate | Runtime | Exit | T/s | cR | cO | P | Evidence |
|---|---|---:|---:|---:|---:|---:|---|
| v80 baseline | `simulate_failed` | 2 | 59.4 | 1 | 1 | 9.2 | `Results/simulations/controller_v80_sharp_curve_speed_cap_saidao3_120s_20260710/` |
| v112 | `simulate_failed` | 2 | 26.3 | 1 | 1 | 9.2 | `Results/simulations/controller_v112_early_conflict_speed_window_saidao3_120s_20260711_retry_after_license/` |

v112 did not improve Track3 score or collision counts and shortened the
runtime window relative to v80.

## Decision

Reject v112. Do not expand to Track1/Track2/Track4 regression because the
target weak-track evidence did not improve.

The source was restored to v80 control-allocation semantics. Restore gate:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v112_20260711.md
```

Sparse terminal email notice:

```text
C:\Users\HP\Desktop\MoSim\Results\coagent_gateway\email\email_alert_20260711_145419.json
```

Do not repeat the same early conflict speed-window cap without a new mechanism
or diagnostic showing why it would avoid v112's Track3 shortening.
