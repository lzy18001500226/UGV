# Track3 Candidate Review - v123 Predictive Front Entry

Status: rejected before target run

## Candidate

v123 attempted to estimate front closing rate from a one-sample delay of the
existing front-distance signal, then enter the unchanged v80 avoid state when
the projected distance at a `0.60 s` horizon crossed `mindis`.

## Static Gate

The source checker passed with `high=0` and `medium=0`, and the targeted Python
tests passed (`7 passed`). These checks did not prove Sysplorer translation.

## Runtime Gate

Both Track3 1 s attempts failed during model checking, before simulation:

- `Results/simulations/controller_v123_predictive_front_entry_saidao3_1s_20260711/`
- `Results/simulations/controller_v123_predictive_front_entry_saidao3_1s_20260711_retry2/`

The first implementation used explicit delay, subtract, gain, and limiter
blocks. The second reduced this to the same `UnitDelay` type already used by
`ControlAllocate`, an annotated connection, and one bounded equation. In both
cases Sysplorer reported the new block and the new state-machine input as
unconnected, then terminated model checking with compiler internal error 100.

## Decision

Reject v123 as non-deployable in the generated Sysblock representation. No
Track3 score, completion, or performance claim exists for this candidate. The
controller source is restored to exact v80 semantics. Do not scan prediction
horizons or add more external ports to this Sysblock.
