# Track4 Candidate Review: v79 Max-Steer Clamp

Status: rejected_target_track_no_score_gain, 2026-07-10 CST

## Candidate

v79 started from accepted v74 and tested a PathPlanner physical-output clamp:

```modelica
if steering_angle > max_steer then
  steering_angle := max_steer;
elseif steering_angle < -max_steer then
  steering_angle := -max_steer;
end if;
```

Intent: check whether enforcing the already-declared `max_steer=0.523599`
could remove Track4's late road-edge event where v74 produced a much larger
path steering command.

## Evidence

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v79_plan_20260710.md
```

Static source gate before runtime:

```text
Results/evidence/controller_deployability_static_check_v79_max_steer_clamp_20260710.md
```

Target run:

```text
Results/simulations/controller_v79_max_steer_clamp_saidao4_120s_20260710/
```

Collision-window analysis:

```text
Results/metrics/collision_window_analysis_v74_v79_track4_20260710.md
```

## Result

| Candidate | Track | Runtime | Exit | T/s | cR | cO | P |
|---|---|---:|---:|---:|---:|---:|---:|
| v74 | Saidao4Eval | `simulate_returned_true` | 0 | 120.0 | 2 | 0 | 9.2 |
| v79 | Saidao4Eval | `simulate_returned_true` | 0 | 120.0 | 2 | 0 | 9.2 |

The final score did not improve. The second road-collision event also moved
earlier in the score time series:

```text
v74: 104.0 s
v79: 59.45 s
```

## Decision

Reject v79. Do not expand it to Track1/2/3 because the target weak track did
not improve and the event timing became worse.

Source semantics were restored to accepted v74 after this target-track test.

## Non-Claims

- No final 80/80 score is claimed.
- No physical UGV success is claimed.
- No report/package readiness change is claimed.
