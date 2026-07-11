# Track2 Candidate Review - v137 Neutral Side Guard

## Decision

Reject v137 and retain restored v80 source semantics.

| Gate | v137 result | Decision |
|---|---|---|
| Static deployability | high=0, medium=0 | pass |
| Project tests | 11 passed | pass |
| Native Track2 1 s | horizon reached, `P=10.0` | pass |
| Track2 120 s | horizon reached, index 112 | progress gain |
| Collision score | `cR=2`, `cO=0`, `P=9.2` | reject |
| Official finish | `distanceSensor1.d=329.7867` | not reached |
| 700 s / other tracks | not run | prerequisite failed |

The restored v80 comparison at 120 s is `cR=1`, `cO=0`, `P=9.6`, path index
26, and finish-distance squared `813.7304`. v137 materially improves traversal
but adds one road collision. The project requires completion first without
retaining a score regression, so the candidate is not accepted.

Evidence:

```text
Results/simulations/candidate_v137_neutral_side_guard_track2_1s_20260712/
Results/simulations/candidate_v137_neutral_side_guard_track2_120s_20260712/
Results/evidence/controller_deployability_static_check_v137_neutral_side_guard_20260712.md
Results/evidence/controller_deployability_static_check_v80_restored_after_v137_20260712.md
Results/metrics/track2_v80_termination_classification_20260712.md
```

The v137 extra-variable export freezes values before the later collision event;
do not infer an exact collision cause from those repeated terminal samples.
The reusable finding is bounded: neutral side-only longitudinal authority
removes the v80 reverse stall, but needs a new lateral safety mechanism before
it can be accepted.
