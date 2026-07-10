# Track1 Candidate Review: v77 v70 Speed Clamp On v74

Status: rejected_early_stop_artifact, 2026-07-10 CST

## Candidate

v77 started from accepted v74 and retested the earlier v70 active-avoid
path-speed clamp as a combination candidate:

```modelica
gain2.u = if speed_oa < 0 and unitDelay3.y > 0.55 then 0.55 else unitDelay3.y;
```

Intent: check whether clamping path speed during active obstacle avoidance
could improve v74's Track1 early-terminal caveat or road-edge behavior.

## Evidence

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v77_plan_20260710.md
```

Additional v74 geometry diagnosis:

```text
Results/metrics/trajectory_geometry_review_v74_all_tracks_20260710.md
Results/metrics/trajectory_geometry_review_v74_all_tracks_20260710.json
Results/figures/trajectory_geometry_review_v74_all_tracks_20260710/
```

Static gate before runtime:

```text
Results/evidence/controller_deployability_static_check_v77_v70_speed_clamp_on_v74_20260710.md
```

Target run:

```text
Results/simulations/controller_v77_v70_speed_clamp_on_v74_saidao1_120s_20260710/
```

Restored gate:

```text
Results/evidence/controller_deployability_static_check_v74_restored_after_v77_20260710.md
```

## Result

| Candidate | Track | Runtime | Exit | T/s | cR | cO | P |
|---|---|---|---:|---:|---:|---:|---:|
| v74 | Saidao1Eval | `simulate_failed` with result variables | 2 | 17.4 | 1 | 0 | 9.6 |
| v77 | Saidao1Eval | `simulate_failed` with result variables | 2 | 5.3 | 0 | 0 | 10.0 |

## Decision

Reject v77. The apparent `P=10.0` is not accepted because the run terminates
after only `5.3 s` with `simulate_failed / exit_state=2`, shorter than v74's
already-known Track1 early-terminal caveat. This is the same evidence class as
previous rejected early-stop artifacts: score variables are readable, but the
run is not comparable to the 120 s review target.

Do not expand v77 to Track2/3/4. Source semantics were restored to accepted
v74.

## Non-Claims

- No final 80/80 score is claimed.
- No physical UGV success is claimed.
- No report/package readiness change is claimed.
