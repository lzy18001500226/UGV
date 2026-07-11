# Four-Track Candidate Review - v109 Asymmetric Left Squeeze

Status: rejected; source restored to v80 semantics, 2026-07-11 CST.

## Baseline

Accepted local wrapper baseline remains:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper score: 38.0 / 40
```

v80 remains the evidence-backed score leader despite the known Track3 runtime
caveat:

```text
Saidao3Eval: simulate_failed/T=59.4,cR=1,cO=1,P=9.2
```

## Candidate

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v109_plan_20260711.md
```

v109 tested an asymmetric left-squeeze obstacle-controller change. It was one
unified rule, not a track-id branch.

Static gate:

```text
Results/evidence/controller_deployability_static_check_v109_asymmetric_left_squeeze_20260711.md
ready_for_physical_claim=true
high=0
medium=0
```

Restore gate after rejection:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v109_20260711.md
ready_for_physical_claim=true
high=0
medium=0
```

## Four-Track Result

| Track | Runtime | Exit | T/s | cR | cO | P | Evidence |
|---|---|---:|---:|---:|---:|---:|---|
| Saidao1Eval | `simulate_failed` | 2 | 17.4 | 1 | 0 | 9.6 | `Results/simulations/controller_v109_asymmetric_left_squeeze_saidao1_120s_20260711/` |
| Saidao2Eval | `simulate_failed` | 2 | null | null | null | null | `Results/simulations/controller_v109_asymmetric_left_squeeze_saidao2_120s_20260711/` |
| Saidao3Eval | `simulate_failed` | 2 | 11.6 | 0 | 1 | 9.6 | `Results/simulations/controller_v109_asymmetric_left_squeeze_saidao3_120s_20260711/` |
| Saidao4Eval | `simulate_failed` | 2 | 7.2 | 0 | 0 | 10.0 | `Results/simulations/controller_v109_asymmetric_left_squeeze_saidao4_120s_20260711/` |

Total wrapper score: not accepted and not comparable, because Track2 has no
readable score values and Track3/Track4 are short-run artifacts.

## Rejection Reasons

1. Track2 exported no usable `score_timeseries.csv` and all score values are
   null despite variable names being present.
2. Track3 and Track4 terminate at 11.6 s and 7.2 s, so their apparent `P=9.6`
   and `P=10.0` values are not comparable to the accepted 120 s evidence.
3. Every v109 track reports `simulate_failed` with `exit_state=2`.
4. v109 does not produce a complete four-track improvement over v80.

## Related Analysis

```text
Results/metrics/collision_window_analysis_v109_asymmetric_left_squeeze_20260711.md
```

The collision-window analysis is useful for understanding the short-run score
events, but it does not convert early-stop evidence into an accepted score
candidate.

## Decision

Reject v109 and keep v80 as the current accepted local wrapper baseline.

Do not continue asymmetric initial-squeeze or left/right initial-steer reversal
variants without a new source-level mechanism. The next candidate should avoid:

```text
1. v103/v106-style broad speed gates that regress Track1.
2. v96-v100/v109-style initial-steer reversal or squeeze scans.
3. short-run score artifacts as evidence of high score.
```

## Non-Claims

- No final 80/80 score claim.
- No physical UGV success claim.
- No report/package readiness claim.
- No official vehicle, road, sensor, scoring, example, or official material
  edits.
