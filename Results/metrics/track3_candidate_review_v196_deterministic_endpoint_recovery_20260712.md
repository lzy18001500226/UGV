# Track3 v196 Deterministic Endpoint Recovery Review

Status: rejected; exact v148 semantics restored.

## Candidate

v196 combined v162's narrow `df < 0.15` direction-aware obstacle entry with a
deterministic final-point fallback in `calculatePursuitPoint`. The intent was
to preserve v162's near-loop traversal while removing the unassigned-output
condition implicated by v180's translation-sensitive endpoint behavior.

## Gates and result

- Static controller gate: `high=0`, `medium=0`.
- Project tests: `14 passed`.
- Track3 1 s native gate: passed.
- Plain `SimulateModel` Track3 completion request: failed to finish.
- Final values: `T=18.1,cR=1,cO=1,P=9.2`.
- Official finish distance squared: `295.2941326655146`.

Evidence:

- `Results/evidence/controller_deployability_static_check_v196_deterministic_endpoint_recovery_20260712.md`
- `Results/simulations/controller_v196_deterministic_endpoint_recovery_saidao3_1s_20260712/`
- `Results/simulations/controller_v196_deterministic_endpoint_recovery_saidao3_700s_20260712/`

## Decision

Reject v196. The fallback changed translated early-route behavior and produced
an earlier non-finish than both v148 and v162. Do not combine endpoint fallback
initialization with v162 or continue endpoint-expression variants. The
controller and pursuit function are restored to exact pre-candidate semantics.

This result does not claim four-track completion, 80/80, physical UGV success,
or submission readiness.
