# Track3 Candidate Review: v52 Brake-Turn Coupling

Status: rejected_target_track_no_improvement, 2026-07-10 CST

## Candidate

v52 continued from v48 and tested a narrow `ControlAllocate` brake-turn
coupling rule. The goal was to reduce the straight-line Track3 obstacle
collision without repeating the broad speed suppression and early-stop behavior
seen in v49 and v51.

Temporary v52 source hypothesis:

```modelica
gain2.u = if speed_oa < 0 and abs(unitDelay1.y) < 0.10 and steer_oa * unitDelay1.y < 0 then 0.75 * unitDelay3.y else unitDelay3.y;
gain3.u = if speed_oa < 0 and abs(unitDelay1.y) < 0.10 and steer_oa * unitDelay1.y < 0 then -0.5 * unitDelay1.y else if speed_oa < 0 and steer_oa * unitDelay1.y < 0 then 0.5 * unitDelay1.y else unitDelay1.y;
```

## Evidence

Static gate:

```text
Results/evidence/controller_deployability_static_check_v52_brake_turn_coupling_20260710.md
```

Target run:

```text
Results/simulations/controller_v52_brake_turn_coupling_saidao3_120s_20260710/
```

Post-run analysis:

```text
Results/metrics/collision_window_analysis_v52_brake_turn_coupling_track3_20260710.md
Results/metrics/signal_window_summary_v52_brake_turn_coupling_track3_20260710.md
```

Restored-source gate:

```text
Results/evidence/controller_deployability_static_check_v48_restored_after_v52_20260710.md
```

## Result

| Candidate | Runtime | Exit | T/s | cR | cO | P |
|---|---|---:|---:|---:|---:|---:|
| v48 Track3 recorded metrics | simulate_failed with result variables | 2 | 112.45 | 1 | 1 | 9.2 |
| v52 Track3 | simulate_failed with result variables | 2 | 8.35 | 1 | 1 | 9.2 |

v52 did not improve Track3 score or collision count, and it terminates much
earlier than v48. The first obstacle collision remains visible at about
`1.1 s`; later road contact appears at about `5.9 s`.

## Decision

Reject v52 and keep v48 as the current review-ready best candidate.

Reason:

```text
The brake-turn coupling did not remove the first Track3 obstacle collision and
introduced an earlier non-comparable terminal state without improving P/cR/cO.
```

The source was restored to v48 semantics and passed the static deployability
gate. The next useful route should be diagnostic or mechanism-driven, not
another brake/path-speed scalar scan.

## Non-Claims

- This review does not claim final competition score.
- This review does not claim physical UGV success.
- This review does not authorize final package creation or submission.
