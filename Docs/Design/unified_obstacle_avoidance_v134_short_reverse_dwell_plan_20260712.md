# v134 Short Reverse-Dwell Plan

Status: rejected after the target Track1 gate; v80 semantics restored.

## Evidence Basis

The restored v80 Track1 diagnostic reached the 25 s horizon but accumulated two
road collisions.  At both score changes, the front sensor was already clear
while the controller was still in its fixed reverse action:

| Time/s | cR | df/m | dl/m | dr/m | speed_oa | steer_oa |
|---:|---:|---:|---:|---:|---:|---:|
| 8.05 | 1 | 2.587 | 0.1045 | 0.2665 | -1 | +0.6 |
| 11.85 | 2 | 2.050 | 0.1002 | 0.2639 | -1 | +0.6 |

Evidence: `Results/simulations/diagnostic_v80_track1_allocator_state_25s_20260712/`,
`Results/metrics/v80_track1_allocator_contribution_25s_20260712.md`, and
`Results/metrics/v80_track1_signal_windows_25s_20260712.md`.

## Candidate

Change only the existing longitudinal transition from `avoid` to `cruise`:

```modelica
after(2, sec) -> after(1, sec)
```

This retains the existing entry trigger, reverse command magnitude, lateral
steering sign, path planner, and control allocator.  It tests whether the
fixed two-second reverse dwell itself carries the vehicle into a side boundary
after a side-triggered avoidance event.

This is not a retry of reverse-speed magnitude, side-hold forward release,
lateral-sign swap, or allocator handoff candidates.  The earlier 3 s release
dwell rejection does not test the opposite, shorter-dwell hypothesis.

## Scope And Gates

Only edit:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

1. Run deployability and unit tests.
2. Run native MWORKS Track1 for 1 s.
3. Run native MWORKS Track1 for 25 s with the same signals as the v80
   diagnostic.
4. Accept only if the run reaches the full 25 s horizon, has fewer than two
   road collisions, no obstacle collision, and no new runtime failure.
5. If accepted, run a 120 s Track1 comparison before any other track.
6. On any failure or no material improvement, restore v80 immediately and
   record the rejection.  No run below the official origin-return gate is an
   official finish or an 80-point score.

## Result

The candidate passed the source deployability checker (`high=0`, `medium=0`),
all eight unit tests, and the native one-second Track1 load/check/simulation
gate.  The decisive 25-second comparison rejected it:

| Controller | Runtime | T/s | cR | cO | P | Finish distance squared |
|---|---|---:|---:|---:|---:|---:|
| v80 | horizon reached | 25.00 | 2 | 0 | 9.2 | 171.4798 |
| v134 | failed, exit state 2 | 20.55 | 2 | 0 | 9.2 | 146.2652 |

Shortening the reverse dwell did not remove either collision and introduced an
earlier abnormal stop.  A smaller terminal distance is not accepted because
the official finish condition was not reached.  The source is restored to the
v80 two-second dwell; no 120-second or cross-track expansion is justified.

Evidence:

```text
Results/evidence/controller_deployability_static_check_v134_short_reverse_dwell_20260712.md
Results/simulations/candidate_v134_short_reverse_dwell_track1_1s_20260712/
Results/simulations/candidate_v134_short_reverse_dwell_track1_25s_20260712/
```
