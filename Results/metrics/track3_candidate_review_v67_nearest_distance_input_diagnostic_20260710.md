# Track3 Diagnostic Review - v67 Nearest-Distance Input

timestamp: 2026-07-10 CST
baseline: v48 opposing-steer guard
decision: rejected as final route; useful diagnostic evidence

## Scope

v67 tested whether the remaining Track3 v48 failure is mainly caused by a
semantic gap between the scorer-facing nearest obstacle distance and the
controller-facing four directional distance inputs.

The test used a generated diagnostic wrapper only:

```text
Models/UGV/Test/Saidao3NearestObstacleDiag.mo
```

No official vehicle, road, sensor, scoring, example, or official material files
were modified. This wrapper is not final competition evidence because it
changes the controller input semantics for diagnosis.

## Runtime Result

Runtime evidence:

```text
Results/simulations/diagnostic_v67_nearest_obstacle_front_saidao3_120s_20260710/
```

Result:

| Candidate | Track | Runtime | Exit | T/s | cR | cO | P | Decision |
|---|---|---:|---:|---:|---:|---:|---:|---|
| v48 | Track3 | simulate_failed with result variables | 2 | 112.45 | 1 | 1 | 9.2 | keep as accepted baseline with runtime caveat |
| v67 diagnostic | Track3 | simulate_returned_true | 0 | 120.0 | 1 | 1 | 9.2 | reject as improvement route |

MWORKS bundled Python was required for this run because the normal Python
environment does not include the `mworks` module.

## Analysis Artifacts

```text
Results/metrics/collision_window_analysis_v48_v67_track3_20260710.md
Results/metrics/collision_window_analysis_v48_v67_track3_20260710.json
Results/metrics/signal_window_summary_v48_v67_track3_20260710.md
Results/metrics/signal_window_summary_v48_v67_track3_20260710.json
Results/evidence/controller_deployability_static_check_v48_reconfirmed_after_v67_20260710.md
Results/evidence/controller_deployability_static_check_v48_reconfirmed_after_v67_20260710.json
```

Key window findings:

- v67 keeps the first obstacle event at `1.05 s`.
- v67 keeps one obstacle collision and one road collision, so `P` remains
  `9.2`.
- v67 changes runtime health from `simulate_failed`/`exit_state=2` to
  `simulate_returned_true`/`exit_state=0`, but this does not improve the
  competition score variables.
- At the relevant early windows, the obstacle controller still outputs the
  fixed startup lateral command `steer := 0.6`; changing `df` semantics alone
  does not change the lateral bypass behavior.

## Decision

Reject the nearest-distance-input route as a score-improvement path. The
diagnostic is still useful because it shows the remaining Track3 issue is not
solved merely by exposing scorer-like obstacle distance to `front_dist`.

Continue from v48. The next route should not be another threshold or initial
steering scan. It should use four-direction-only evidence and external
research to identify a deployable trajectory-level or reactive safety overlay
that can work within the official controller boundary.

This review does not create a submission package and does not claim physical
UGV success.
