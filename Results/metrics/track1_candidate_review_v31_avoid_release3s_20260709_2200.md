# Track1 Candidate Review - v31 Avoid Release 3s

generated_at: 2026-07-09 22:00 CST

## Decision

Reject `v31_avoid_release3s`.

The candidate was evidence-backed and track-agnostic, but it badly regressed
the first target weak track. The source was restored to v13 semantics after the
target run.

## Candidate

Baseline:

```text
v13 side-trigger 0.45
transition(avoid, cruise, after(2,sec), reset = false)
```

v31 attempted mechanism:

```text
transition(avoid, cruise, after(3,sec), reset = false)
```

Rationale:

```text
Results/metrics/v13_pre_collision_control_attribution_20260709_2140.md
Docs/Design/unified_obstacle_avoidance_v31_plan_20260709.md
```

The intended mechanism was a small hysteresis-style safety extension: keep
avoid mode active longer after side/front risk because v13 road contacts often
occur while side margin is shrinking and path-planner steering can dominate.

## Evidence

Static gate:

```text
Results/evidence/controller_deployability_static_check_v31_avoid_release3s_20260709_2153.md
```

Target run:

```text
Results/simulations/controller_v31_avoid_release3s_saidao1_120s_20260709_2155/
```

Source restored static gate:

```text
Results/evidence/controller_deployability_static_check_v13_restored_after_v31_20260709_2200.md
```

## Result Summary

| Track | Runtime status | T/s | cR | cO | P | v13 comparison |
|---|---|---:|---:|---:|---:|---|
| Track1 `UGV.Test.Saidao1Eval` | `simulate_returned_true` | 120.0 | 17 | 3 | 2.0 | severe regression |

Accepted v13 target-track comparison:

```text
Track1: T=120.0, cR=3, cO=0, P=8.8
```

## Interpretation

- Extending avoid release from 2 seconds to 3 seconds caused the controller to
  remain in reverse/avoid behavior too long.
- The longer dwell increased road contacts and introduced obstacle contacts.
- This rejects the "longer avoid hold" route for now; do not expand v31 to
  Track4 or regression tracks.
- The next candidate should avoid longer reverse dwell. A more promising route
  is to reduce path-planner fighting only during severe side-risk, or to inspect
  whether the final steering path has an unbounded planner contribution that can
  be safely limited without touching official files.

## Non-Claims

- This is not a final competition score claim.
- This does not claim physical UGV readiness.
- This does not authorize final submission packaging or sending.
