# Track2 Candidate Review v87 Front-Clear Sustained Side Steer

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
v87 front-clear sustained side steer
Docs/Design/unified_obstacle_avoidance_v87_plan_20260710.md
```

Mechanism:

```text
When df > safeF and dl <= 0.12 and dl < dr, increase the positive
avoid-lateral steering command from the v80 value to 0.8.
```

The target gate was Track2 because v80 Track2 still has one road collision
while being runtime-clean.

## Evidence

Run:

```text
Results/simulations/controller_v87_front_clear_sustained_side_steer_saidao2_120s_20260710/
```

Static source gate:

```text
Results/evidence/controller_deployability_static_check_v87_front_clear_sustained_side_steer_20260710.md
```

Restored v80 source gate after rejecting v87:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v87_20260710.md
```

Measured target-track result:

| Candidate | Track | Runtime | T | cR | cO | P |
|---|---|---|---:|---:|---:|---:|
| v80 baseline | Saidao2Eval | simulate_returned_true / exit_state=0 | 120.0 | 1 | 0 | 9.6 |
| v87 | Saidao2Eval | simulate_returned_true / exit_state=0 | 120.0 | 1 | 0 | 9.6 |

## Decision

Reject v87. The target-track gate did not improve `cR`, `cO`, `P`, runtime
status, or completion time versus v80. Because there is no target-track gain,
v87 should not be expanded to Track1/Track3/Track4 regression testing.

## Next Action

Continue the score sprint from v80 with a different evidence-backed unified
mechanism.

Do not repeat this same front-clear sustained side-steer boost without new
failure-window evidence showing a different trigger condition or interaction.
