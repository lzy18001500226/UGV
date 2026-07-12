# Track2 v190 Signed-Front Release Review

## Verdict

Rejected and rolled back. The candidate did not complete Track2 and did not
preserve the accepted baseline behavior.

## Candidate

- Controller: `ObsAvoidController_Sysblock2.mo`
- Changes: raw signed `front_dist`, `mindis=1.5`, positive-front entry gate,
  clearance-aware release.
- Allocator: unchanged.
- Official model/sensor/scoring: unchanged.

## Gates

- Static deployability: passed, `high=0`, `medium=0`.
- Repository tests: passed, `14 passed`.
- Track2 1 s native gate: passed, `T=1,cR=0,cO=0,P=10`.
- Track2 strict 700 s: failed.

## Runtime Evidence

Run directory:
`Results/simulations/controller_v190_signed_front_release_saidao2_700s_20260712/`

Observed result:

```text
simulate_model=False
termination=unclassified_early_termination
T=28.95
cR=4
cO=1
P=8.0
finish_distance_squared=794.011650829773
```

The official completion predicate was not satisfied. The candidate is not a
four-track candidate and must not be scored as an improvement.

## Rollback

The controller is restored to the exact `HEAD` semantics after this review.
