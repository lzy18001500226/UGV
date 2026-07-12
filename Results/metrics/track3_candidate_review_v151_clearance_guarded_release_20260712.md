# Track3 v151 Candidate Review

Status: rejected.

The 1 s native gate passed. The 700 s bounded native run terminated early at
`T=301.3`, `cR=33`, `cO=6`, `P=-5.6`, and finish-distance squared `261.4286`.
This is neither a finish nor a useful score gain. The controller remains in
avoid too long when complete clearance never occurs, causing repeated road and
obstacle collisions.

Evidence:

- `Results/simulations/candidate_v151_clearance_guarded_release_track3_1s_20260712/`
- `Results/simulations/candidate_v151_clearance_guarded_release_track3_700s_20260712/`

Decision: reject permanent clearance-gated release. Keep v148's neutral
side-only longitudinal command and test only bounded persistence with a hard
maximum dwell.
