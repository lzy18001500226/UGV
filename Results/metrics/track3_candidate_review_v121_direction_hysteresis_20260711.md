# Track3 Candidate Review: v121 Direction Hysteresis

Status: rejected; do not expand to other tracks

## Candidate

v121 combined v120's actual-clear lateral-state release with a `0.08 m`
left/right gap hysteresis in the four `avoid_lateral` direction transitions.
Cruise lateral logic, longitudinal timing, speed commands, path planning, and
control allocation remained unchanged.

## Gates

- deployability checker: `high=0`, `medium=0`
- targeted tests: `7 passed`
- Track3 1 s gate: passed, `exit_state=0`, `T=1.0`, `cR=0`, `cO=0`, `P=10.0`
- Track3 120 s target run: rejected, `exit_state=2`

## Comparable Result

| Candidate | T | cR | cO | P | terminal path segment |
|---|---:|---:|---:|---:|---:|
| restored v80 | 59.4 | 1 | 1 | 9.2 | 29 |
| v120 continuity | 52.95 | 1 | 2 | 8.8 | 16 |
| v121 continuity + hysteresis | 11.8 | 1 | 2 | 8.8 | 6 |

The v121 run retained five positive/negative `ctrlAlloc.steer_oa` sign changes,
so the `0.08 m` dead band did not stabilize direction enough to offset the
regression introduced by persistent lateral-state continuity.  It terminated
much earlier than both v80 and v120 and added one obstacle collision relative
to v80.  This is neither completion nor a comparable score/progress gain.

## Evidence

- plan:
  `Docs/Design/unified_obstacle_avoidance_v121_direction_hysteresis_plan_20260711.md`
- static gate:
  `Results/evidence/controller_deployability_static_check_v121_direction_hysteresis_20260711.md`
- 1 s runtime:
  `Results/simulations/controller_v121_direction_hysteresis_saidao3_1s_20260711/`
- interrupted outer-timeout attempt, not an algorithm result:
  `Results/simulations/controller_v121_direction_hysteresis_saidao3_120s_20260711/`
- valid 120 s target attempt:
  `Results/simulations/controller_v121_direction_hysteresis_saidao3_120s_20260711_retry1/`

## Decision

Reject v121 and restore the exact committed v80 controller source.  Do not
apply v120-style persistent lateral continuity or this direction hysteresis to
the other tracks.  The next candidate must address completion using a
different structural mechanism, not another hysteresis-width scan.

This evidence does not claim official completion, an 80-point score, physical
UGV success, report readiness, or submission readiness.
