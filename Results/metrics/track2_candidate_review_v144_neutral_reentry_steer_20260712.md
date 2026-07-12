# Track2 Candidate Review - v144 Neutral Re-entry Steering

## Decision

Reject v144 and restore exact v80 controller semantics.

| Gate | Result | Decision |
|---|---|---|
| Completion-chain audit | official/wrapper paths identical and closed | pass |
| Static deployability | `high=0, medium=0` | pass |
| Project tests | `11 passed` | pass |
| Native Track2 1 s | `T=1,cR=0,cO=0,P=10.0` | pass |
| Track2 120 s | `T=120,cR=3,cO=7,P=6.0` | reject |
| Official finish | `distanceSensor1.d=379.7594` | not reached |

v144 retained v137's neutral side-only longitudinal authority and changed the
nested lateral avoid-state re-entry output from fixed `+0.6` to `0`. The
candidate reached the configured horizon but introduced two additional road
collisions and seven obstacle collisions relative to v137. The fixed re-entry
steering therefore supplies necessary early obstacle authority; removing it is
not a safe correction for v137's later road collision.

The failed 105 s v137 diagnostic ended non-comparably at `T=28.55` and is kept
only as runtime instability evidence. It is not used to attribute the second
collision.

Evidence:

```text
Results/metrics/track2_completion_chain_static_audit_20260712.md
Results/simulations/diagnostic_v137_track2_second_collision_105s_20260712/
Results/simulations/candidate_v144_neutral_reentry_steer_track2_1s_20260712/
Results/simulations/candidate_v144_neutral_reentry_steer_track2_120s_20260712/
Results/evidence/controller_deployability_static_check_v144_neutral_reentry_steer_20260712.md
```

Do not repeat neutral/attenuated lateral re-entry as the next candidate. A
follow-up must retain immediate obstacle steering authority and target the
later road-boundary event with an independent observable.

This result does not claim a finish, an official score, physical validation,
or submission readiness.
