# Track3 Candidate Review: v198 Heading Equivalent-Angle Unwrap

Status: rejected; exact v148 allocator semantics restored.

v198 selected the `2*pi`-equivalent final heading nearest to the previous
sample. The intent was to remove a possible `atan2` wrap discontinuity without
changing the physical heading, obstacle state machine, speed, official model,
or any track-specific behavior.

## Gates

- Static deployability: `high=0`, `medium=0`.
- Project tests: `14 passed`.
- Track3 1 s plain `SimulateModel`: passed, `exit_state=0`.
- Track3 700 s plain `SimulateModel`: early termination.

Observed long-run result:

```text
T=21.1
cR=1
cO=1
P=9.2
exit_state=2
distanceSensor1.d=301.43126761991095
```

Evidence:

- `Results/simulations/candidate_v198_heading_unwrap_track3_1s_20260712/`
- `Results/simulations/candidate_v198_heading_unwrap_track3_700s_20260712/`
- `Results/evidence/controller_deployability_static_check_v198_heading_unwrap_20260712.md`

## Decision

Reject v198. Its Track3 result is identical to the current plain v148 baseline,
so the equivalent-angle branch did not alter the relevant failure trajectory.
Do not expand it to the other tracks and do not scan unwrap or slew constants.
The candidate statements were removed and exact v148 allocator semantics were
restored.

This evidence does not claim Track3 completion, four-track completion, 80/80,
physical-vehicle success, or submission readiness.
