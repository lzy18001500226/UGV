# Track3 v161 Candidate Review

Status: rejected; exact v148 allocator semantics restored.

## Candidate

v161 continuously reduced only the conflicting filtered OA heading as the
existing normalized longitudinal command recovered from `speed_oa=-1` to
`speed_oa=0`. It added no threshold, time constant, track branch, or edit to
official models.

## Gates

| Gate | Result |
|---|---|
| Deployability | pass, `high=0, medium=0` |
| Project tests | pass, `14 passed` |
| Track3 1 s | pass, `T=1.0,cR=0,cO=1,P=9.6` |
| Strict Track3 request | reject, early terminal state |

The strict request ended at `T=72.7,cR=2,cO=3,P=8.0`; the official finish
distance variable was `132.7676`, so Track3 did not finish. The candidate
advanced substantially longer than v148 but reproduced the v158/v159 collision
regression. Continuous longitudinal weighting therefore removes the abrupt
boolean handoff but does not make allocator-level path recovery safe.

Evidence:

- `Results/simulations/candidate_v161_longitudinal_authority_blend_track3_1s_20260712_retry1/`
- `Results/simulations/candidate_v161_longitudinal_authority_blend_track3_700s_20260712/`
- `Results/evidence/controller_deployability_static_check_v161_longitudinal_authority_blend_20260712.md`

Decision: reject v161, restore v148, and close allocator-level stateless or
fixed-filter recovery for the next candidate. Do not expand to other tracks.
No official completion, 80/80 score, physical result, or submission readiness
is claimed.
