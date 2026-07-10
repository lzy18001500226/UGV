# Track2 Candidate Review - v91 Gap-Directed Initial Steer

Status: rejected, source restored to v80 semantics, 2026-07-10 CST.

## Baseline

Current accepted local wrapper candidate:

```text
v80 sharp curve speed cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
total wrapper score: 38.0
```

v80 Track2 reference:

```text
T=120.0
cR=1
cO=0
P=9.6
simulate_returned_true / exit_state=0
```

## Candidate

v91 tested whether the `avoid_lateral` initial state should use the same
gap-directed sign and bounded magnitude as the later dynamic lateral states,
instead of the fixed positive initial command:

```modelica
if dl > dr then
  steer := -min(0.8, 2 * abs(dl - dr));
else
  steer := min(0.8, 2 * abs(dl - dr));
end if;
```

This was a unified four-sensor mechanism. It did not branch on track name,
wrapper name, run id, score variables, or official model internals.

## Target Result

Evidence:

```text
Results/simulations/controller_v91_gap_directed_initial_steer_saidao2_120s_20260710/
Results/evidence/controller_deployability_static_check_v91_gap_directed_initial_steer_20260710.md
```

Observed score variables:

```text
T=104.55
cR=2
cO=1
P=8.8
runtime_status=simulate_failed
simulation_exit_state=2
```

## Decision

Reject v91. It regresses the clean Track2 target gate from v80
`T=120.0,cR=1,cO=0,P=9.6` to `T=104.55,cR=2,cO=1,P=8.8`. Because the target
track regressed, v91 must not be expanded to Track1, Track3, Track4, or
four-track evaluation.

The source was restored to v80 semantics:

```modelica
steer := 0.6;
```

Restore static gate:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v91_20260710.md
```

## Next Direction

Continue from v80, but treat the fixed initial lateral steer as risky to alter
without stronger source-level evidence. The remaining route likely needs
better structure than scalar scans or simple initial-state replacement.
