# Track3 Candidate Review: v49 Path-Speed Attenuation

Status: rejected_target_track_early_stop, 2026-07-10 CST

## Candidate

v49 continued from v48 and tested one unified `ControlAllocate` arbitration
mechanism:

```modelica
gain2.u = if speed_oa < 0 then 0.6 * unitDelay3.y else unitDelay3.y;
```

The goal was to reduce the path-planner forward-speed contribution when the
obstacle-avoidance controller is already asking for reverse/braking, without
increasing obstacle speed-channel gain or reverse speed.

## Gate

Static source gate:

```text
Results/evidence/controller_deployability_static_check_v49_path_speed_attenuation_20260710.md
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
Results/simulations/controller_v49_path_speed_attenuation_saidao3_120s_20260710/
```

Track3 result:

| Candidate | Runtime | Exit | T/s | cR | cO | P |
|---|---|---:|---:|---:|---:|---:|
| v48 | `simulate_failed` | 2 | 112.45 | 1 | 1 | 9.2 |
| v49 | `simulate_failed` | 2 | 5.75 | 0 | 1 | 9.6 |

Although the exported score variable `P` is higher, the run ends at only
`5.75 s`. This is an early, non-comparable terminal result and cannot be
accepted as a controller improvement.

## Decision

Reject v49. Do not continue this candidate to four-track regression.

Reason:

```text
The mechanism suppresses forward path-speed authority too aggressively during
early avoidance and produces a very early terminal run. It does not provide a
credible four-track competition improvement over v48.
```

Restored source gate:

```text
Results/evidence/controller_deployability_static_check_v48_restored_after_v49_20260710.md
```

## Lessons

- The Track3 early obstacle contact is real, but bluntly reducing path speed
  during all reverse avoidance is too disruptive.
- Continue from v48, not v49.
- The next candidate should use a narrower condition or a different mechanism,
  and it must avoid early-stop score inflation.

## Non-Claims

- This is not a final competition score claim.
- This does not claim physical UGV readiness.
- This does not authorize final submission packaging or sending.
