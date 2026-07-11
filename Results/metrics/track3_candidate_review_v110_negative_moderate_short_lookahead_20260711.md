# Track3 Candidate Review - v110 Negative Moderate Short Lookahead

Status: rejected; source restored to v80 semantics, 2026-07-11 CST.

## Baseline

Accepted local wrapper baseline remains:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper score: 38.0 / 40
Track3 caveat: simulate_failed/T=59.4,cR=1,cO=1,P=9.2
```

## Candidate

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v110_plan_20260711.md
```

v110 modified only `Models/UGV/Control/PathPlanning/PathPlanner.mo` during the
candidate run. It added a guarded short-lookahead trial for negative moderate
path curvature:

```text
base_steering_angle < -0.18 and base_steering_angle > -0.28
```

This was a unified path-planning rule, not a track-id branch.

Static gate:

```text
Results/evidence/controller_deployability_static_check_v110_negative_moderate_short_lookahead_20260711.md
ready_for_physical_claim=true
high=0
medium=0
```

## Runtime Result

Target run:

```text
Results/simulations/controller_v110_negative_moderate_short_lookahead_saidao3_120s_20260711/
```

| Track | Runtime | Exit | T/s | cR | cO | P | Decision |
|---|---|---:|---:|---:|---:|---:|---|
| Saidao3Eval | `simulate_failed` | 2 | 4.8 | 0 | 1 | 9.6 | Reject as short-run artifact. |

Although the exported score shows `P=9.6`, the run ends at `T=4.8` during a
120 s request. This is not comparable to v80 Track3 evidence and cannot be
used as an accepted score improvement.

## Decision

Reject v110 and keep v80 as the current accepted local wrapper baseline.

Source was restored to v80 `PathPlanner` semantics after the failed target
gate, and the restore gate passed:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v110_20260711.md
ready_for_physical_claim=true
high=0
medium=0
```

Do not continue negative moderate-curvature short-lookahead scans without a
new diagnostic reason. This route creates the same short-run artifact pattern
that the long task is trying to avoid.

## Non-Claims

- No final 80/80 score claim.
- No physical UGV success claim.
- No report/package readiness claim.
- No official vehicle, road, sensor, scoring, example, or official material
  edits.
