# v194 lateral release continuity review

- Candidate: v194 lateral release continuity
- API lane: plain `SimulateModel` (official comparison lane)
- Static deployability: passed, `high=0`, `medium=0`
- Tests: `14 passed`
- Track3 1 s gate: passed
- Track3 120 s screen: `simulate_failed`, `T=16.6 s`, `cR=1`, `cO=2`, `P=8.8`
- Finish-distance squared: `295.055560351749`
- Evidence directory: `Results/simulations/controller_v194_lateral_release_continuity_saidao3_120s_20260712/`

## Decision

Reject v194 and restore the exact pre-candidate controller semantics. The
clearance-gated lateral release did not preserve the baseline trajectory and
terminated earlier with two obstacle collisions. The zero collision values in
the final diagnostic sample are not a success signal because the run did not
finish. Do not expand v194 to the other tracks.

The design hypothesis remains useful: the one-sample release pulse may be a
real mechanism, but this particular release gate is not a viable correction.
The next candidate must use a different state-continuity mechanism and must
not be another scalar clearance threshold.

## Evidence boundary

This result does not claim four-track completion, 80/80, physical UGV
success, or final submission readiness.
