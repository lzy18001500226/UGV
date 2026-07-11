# Track3 Candidate Review: v122 Coherent Gap State

Status: rejected; do not expand to other tracks

## Candidate

v122 tested a coherent four-distance Bug/Follow-the-Gap style state rule in the
editable obstacle controller:

- gap-directed bounded initial steering (`0.25..0.6` magnitude);
- actual-clear release across transient `flag=false` pulses;
- `0.08 m` direction hysteresis in the persistent avoid-lateral state.

Longitudinal timing and speed, path planning, control allocation, official
vehicle/road/sensor/scoring/track models, and wrappers were unchanged.

## Gates

- deployability checker: `high=0`, `medium=0`
- targeted tests: `7 passed`
- Track3 1 s gate: passed, `exit_state=0`
- Track3 120 s target gate: rejected, `exit_state=2`

## Comparable Result

| Candidate | T | cR | cO | P | Finish distance squared |
|---|---:|---:|---:|---:|---:|
| restored v80 | 59.4 | 1 | 1 | 9.2 | 296.8655 |
| v120 continuity | 52.95 | 1 | 2 | 8.8 | 294.0036 |
| v121 continuity + hysteresis | 11.8 | 1 | 2 | 8.8 | 52.6946 |
| v122 coherent gap state | 21.7 | 1 | 2 | 8.8 | 290.3339 |

v122 did not finish, terminated much earlier than v80, and retained the extra
obstacle collision introduced by persistent lateral-state continuity.  Its
smaller gap-directed entry command did not make the combined state mechanism
safe or comparable.

## Evidence

- `Docs/Design/unified_obstacle_avoidance_v122_coherent_gap_state_plan_20260711.md`
- `Results/evidence/controller_deployability_static_check_v122_coherent_gap_state_20260711.md`
- `Results/simulations/controller_v122_coherent_gap_state_saidao3_1s_20260711/`
- `Results/simulations/controller_v122_coherent_gap_state_saidao3_120s_20260711/`

## Decision

Reject v122 and restore the exact committed v80 controller source.  Close the
v120-v122 persistent-gap-state family.  Do not continue by scanning entry
magnitude, hysteresis width, or release clearance.  The next batch needs a new
completion mechanism or a better observed-state interface, not more tuning of
this state family.

This result does not prove official completion, an 80-point score, physical
UGV success, report readiness, or submission readiness.
