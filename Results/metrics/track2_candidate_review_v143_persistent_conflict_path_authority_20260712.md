# Track2 Candidate Review: v143 Persistent-Conflict Path Authority

## Decision

Rejected. Restore v80 control-allocation semantics. Do not run the 700 s
completion gate or expand v143 to other tracks.

## Candidate

v143 added a discrete path-authority state to `ControlAllocate.CtrlAlloc`.
During continuous reverse-avoidance/path-steering conflict, path authority
decreased from 1.0 to 0.2; after conflict release it recovered toward 1.0.
The mechanism used one source and one parameter set and did not modify an
official track, vehicle, road, wrapper, or scoring model.

## Gates

- Static deployability: `high=0`, `medium=0`.
- Tests: `11 passed`.
- Track2 1 s: load/check/simulate passed, `T=1,cR=0,cO=0,P=10`.
- Track2 120 s request: early termination at
  `T=33.85,cR=1,cO=0,P=9.6`, `distanceSensor1.d=176.26296613586933`.
- Path progress: `pathPlanner.closest_index` reached only 4.
- Arbitration state: `conflictPathAuthority.y` reached 0.2 and ended at 0.2.

## Comparison

The v80 comparable Track2 run reaches the full 120 s horizon with
`cR=1,cO=0,P=9.6`, path index 26, and
`distanceSensor1.d=813.7304349381575`. v143 did not reduce collisions and
terminated much earlier with less path progress. Its smaller terminal distance
is a different crash location, not evidence of route completion.

## Evidence

- Design: `Docs/Design/unified_obstacle_avoidance_v143_persistent_conflict_path_authority_plan_20260712.md`
- Static gate: `Results/evidence/controller_deployability_static_check_v143_persistent_conflict_path_authority_20260712.md`
- 1 s run: `Results/simulations/candidate_v143_persistent_conflict_path_authority_track2_1s_20260712/`
- 120 s run: `Results/simulations/candidate_v143_persistent_conflict_path_authority_track2_120s_20260712/`

This review does not claim an official finish, an 80/80 score, physical UGV
success, or submission readiness.
