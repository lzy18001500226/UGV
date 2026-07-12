# Track3 v162 Candidate Review

Status: rejected; exact v148 source restored.

v162 combined v148 with the old v83 narrow `df<0.15` lateral recovery. Static
checks and the 1 s MWORKS gate passed. The strict Track3 request reached
`T=286.55,cR=2,cO=1,P=8.8`, with official finish distance `295.9073`.

The saved trajectory traverses the main loop but returns along the start/finish
straight near `y=0.5`, missing the origin assertion. Compared with v148, v162
preserves the single obstacle collision and extends runtime dramatically, but
adds one road collision and does not finish. It is therefore not retained.

Evidence:

- `Results/simulations/candidate_v162_v148_narrow_recovery_track3_1s_20260712/`
- `Results/simulations/candidate_v162_v148_narrow_recovery_track3_700s_20260712/`
- `Results/metrics/v162_track3_geometry_review_20260712.md`
- `Results/evidence/controller_deployability_static_check_v162_v148_narrow_recovery_20260712.md`

Reusable result: narrow state-machine recovery is the first mechanism to
produce a near-complete Track3 loop. A follow-up needs stateful centerline
recovery after obstacle clearance; it must not globally remove OA authority.

No finish, 80/80, physical, package, or submission claim is made.
