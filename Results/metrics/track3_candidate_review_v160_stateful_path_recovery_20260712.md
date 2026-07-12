# Track3 v160 Candidate Review

Status: rejected.

v160 added a one-second first-order recovery weight to smooth v158/v159's
stateless OA cancellation. A front-obstacle command bypassed cancellation
immediately, preserving nominal OA authority.

The 1 s native gate passed. The strict run exported
`ctrlAlloc.pathRecoveryWeight.y` but stopped at `T=18.75`, `cR=1`, `cO=1`,
`P=9.2`, and finish-distance squared `298.1579`. This is earlier than v148
`T=21.10` and does not reproduce the route progress of v158/v159.

Evidence:

- `Results/simulations/candidate_v160_stateful_path_recovery_track3_1s_20260712/`
- `Results/simulations/candidate_v160_stateful_path_recovery_track3_700s_20260712/`
- `Results/evidence/controller_deployability_static_check_v160_stateful_path_recovery_20260712.md`

Decision: reject v160, remove the added state block, and restore v148. Do not
scan recovery-filter time constants. The next stateful mechanism must use
side-clearance geometry in the avoidance state machine or first justify a
bounded interface extension.
