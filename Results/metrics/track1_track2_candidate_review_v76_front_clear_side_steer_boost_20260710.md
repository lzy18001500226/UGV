# Track1/Track2 Candidate Review: v76 Front-Clear Side Steer Boost

Status: rejected, 2026-07-10 CST

## Candidate

v76 started from accepted v74 and tested a narrow obstacle-controller branch in
the active avoid lateral initialization window:

```modelica
if df > safeF and dl < 0.14 and dl < dr then
  steer := 0.75;
else
  steer := 0.6;
end if;
```

Intent: give a small extra right steering command only when the front is clear
and the left side is extremely close, matching the shared early road-edge
windows in v74.

## Evidence

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v76_plan_20260710.md
```

Static gate before runtime:

```text
Results/evidence/controller_deployability_static_check_v76_front_clear_side_steer_boost_20260710.md
```

Target and regression runs:

```text
Results/simulations/controller_v76_front_clear_side_steer_boost_saidao2_120s_20260710/
Results/simulations/controller_v76_front_clear_side_steer_boost_saidao1_120s_20260710/
```

Restored gate:

```text
Results/evidence/controller_deployability_static_check_v74_restored_after_v76_20260710.md
```

## Result

| Candidate | Track | Runtime | Exit | T/s | cR | cO | P |
|---|---|---|---:|---:|---:|---:|---:|
| v74 | Saidao2Eval | `simulate_returned_true` | 0 | 120.0 | 1 | 0 | 9.6 |
| v76 | Saidao2Eval | `simulate_returned_true` | 0 | 120.0 | 1 | 0 | 9.6 |
| v74 | Saidao1Eval | `simulate_failed` with result variables | 2 | 17.4 | 1 | 0 | 9.6 |
| v76 | Saidao1Eval | `simulate_failed` with result variables | 2 | 5.3 | 1 | 0 | 9.6 |

## Decision

Reject v76. Track2 remained non-regressive and clean, but it did not improve
score or collisions. The first regression run then made Track1's existing early
terminal caveat worse, reducing recorded `T` from v74's `17.4` to `5.3` while
keeping the same `P/cR/cO`.

Do not expand v76 to Track3/4. Source semantics were restored to accepted v74:

```text
v13 obstacle-controller side trigger
v45/v74 PathPlanner curvature and guarded short-lookahead semantics
v48 ControlAllocate opposing-steer guard
```

## Non-Claims

- No final competition score is claimed.
- No physical UGV success is claimed.
- No report/package readiness change is claimed.
