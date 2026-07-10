# Track2 Candidate Review v88 Side-Squeeze Speed Hold

Status: rejected as accepted baseline. This review records the target-track
gate result only; it does not claim final score, report readiness, submission
readiness, or physical UGV behavior.

## Candidate

Baseline:

```text
v80 sharp curve speed cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
```

Candidate:

```text
v88 side-squeeze speed hold
Docs/Design/unified_obstacle_avoidance_v88_plan_20260710.md
```

Mechanism:

```text
When the controller is already in avoid mode, the front is clear, and either
side distance is <= 0.12, change the longitudinal avoid speed command from -1
to -1.3.
```

The target gate was Track2 because v80 Track2 is runtime-clean but still has
one early side road collision.

## Evidence

Run:

```text
Results/simulations/controller_v88_side_squeeze_speed_hold_saidao2_120s_20260710/
```

Static source gate:

```text
Results/evidence/controller_deployability_static_check_v88_side_squeeze_speed_hold_20260710.md
```

Measured target-track result:

| Candidate | Track | Runtime | T | cR | cO | P |
|---|---|---|---:|---:|---:|---:|
| v80 baseline | Saidao2Eval | simulate_returned_true / exit_state=0 | 120.0 | 1 | 0 | 9.6 |
| v88 | Saidao2Eval | simulate_failed / exit_state=2 | 85.15 | 1 | 0 | 9.6 |

## Decision

Reject v88. The target-track gate did not improve `cR`, `cO`, or `P`, and it
introduced a worse runtime caveat by ending Track2 at `T=85.15` instead of the
v80 clean 120 s run.

Do not expand v88 to Track1/Track3/Track4. Restore v80 source semantics and
run the restored static source gate before the next candidate.

## Next Action

Continue the score sprint from v80 with a different evidence-backed unified
mechanism. Do not repeat side-squeeze speed escalation unless new evidence
shows a softer or structurally different longitudinal behavior is needed.
