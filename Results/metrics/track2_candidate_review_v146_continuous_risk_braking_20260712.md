# Track2 Candidate Review: v146 Continuous Risk Braking

## Decision

Rejected. Exact v80 semantics are restored. No extended completion run or
cross-track expansion is justified.

## Candidate

v146 replaced v80's fixed `speed=-1` during avoidance with a bounded maximum of
normalized front intrusion and extreme side-clearance risk. It retained the
existing lateral state machine and used the same source for every track.

## Evidence

| Gate | Result |
|---|---|
| Static deployability | pass, `high=0,medium=0` |
| Tests | `11 passed` |
| Track2 1 s | pass, `T=1,cR=0,cO=0,P=10` |
| Track2 120 s request | early stop at `T=39.3` |
| Score variables | `cR=1,cO=0,P=9.6` |
| Finish distance squared | `788.8770693400352` |

The candidate runs longer than both current v137 repetitions at `T=28.55`, but
still exits on a road collision and is not comparable to v80's full 120 s
horizon. The evidence rules out another threshold scan within this purely
longitudinal family: progress release needs a stable lateral/path-preservation
mechanism, not only a different reverse-speed magnitude.

Artifacts:

- `Results/evidence/controller_deployability_static_check_v146_continuous_risk_braking_20260712.md`
- `Results/simulations/candidate_v146_continuous_risk_braking_track2_1s_20260712/`
- `Results/simulations/candidate_v146_continuous_risk_braking_track2_120s_20260712/`

No finish, 80-point score, physical validation, or submission readiness is
claimed.
