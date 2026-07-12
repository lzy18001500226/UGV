# Track3 Candidate Review v202 Terminal Approach Envelope

## Decision

Reject v202 and restore v199 source semantics.

## Candidate

The shared allocator received a departure-armed terminal distance-speed
envelope. It was intended to slow the vehicle before the final return heading
error became infeasible.

## Validation

- Static deployability: `high=0`, `medium=0`.
- Project tests: `14 passed`.
- Track3 1 s native gate: passed, `SimulateModel=true`, `T=1`, `cR=0`,
  `cO=0`, `P=10`.
- Track3 700 s decisive run: timed out after more than 6 minutes without
  metrics or a result packet. It therefore cannot prove completion or score.

The candidate is rejected for a runtime-efficiency regression. Its source was
rolled back exactly. This timeout is not interpreted as a finish or as an
official score.

## Evidence

- `Docs/Design/unified_obstacle_avoidance_v202_terminal_approach_envelope_plan_20260712.md`
- `Results/evidence/controller_deployability_static_check_v202_terminal_approach_envelope_20260712.md`
- `Results/simulations/controller_v202_terminal_approach_envelope_saidao3_1s_20260712/`
- `Results/simulations/controller_v202_terminal_approach_envelope_saidao3_700s_20260712/`
