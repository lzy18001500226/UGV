# Track3 v159 Candidate Review

Status: rejected.

v159 removed v158's path-heading magnitude gate so any opposite path command
immediately cancelled the filtered OA offset while `speed_oa=0`. Initial
front-obstacle authority remained unchanged.

The 1 s native gate passed. The strict run stopped at `T=78.7`, `cR=3`,
`cO=3`, `P=7.6`, and finish-distance squared `96.9383`. This is substantial
route progress versus v148, but it is not an official finish and materially
regresses both collision categories and score.

Evidence:

- `Results/simulations/candidate_v159_immediate_neutral_path_recovery_track3_1s_20260712/`
- `Results/simulations/candidate_v159_immediate_neutral_path_recovery_track3_700s_20260712/`
- `Results/evidence/controller_deployability_static_check_v159_immediate_neutral_path_recovery_20260712.md`

Decision: reject v159 and restore exact v148 allocator semantics. v158/v159
together prove that path recovery improves route progress but stateless
switching adds collisions. Do not scan heading thresholds or cancellation
gains. The next mechanism needs bounded state continuity between avoidance and
path recovery.
