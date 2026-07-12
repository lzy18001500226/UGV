# v195 Stanley path-heading review

- Candidate: segment-tangent plus bounded cross-track desired-heading control
- Changed file: `Models/UGV/Control/PathPlanning/PathPlanner.mo`
- API lane: plain `SimulateModel`
- Project tests: `14 passed`
- MWORKS Track2 1 s gate: passed (`exit_state=0`)
- MWORKS Track2 120 s screen: horizon reached, no official finish
- Result: `T=120.0`, `cR=1`, `cO=3`, `P=8.4`
- Finish-distance squared: `359.0037114403009`
- Evidence directory: `Results/simulations/controller_v195_stanley_heading_saidao2_120s_20260712/`

## Decision

Reject v195. Replacing the pursuit-point bearing with segment-tangent and
cross-track heading increased obstacle collisions from the comparison
baseline and did not produce an official finish. The PathPlanner source was
restored exactly before closeout. Do not expand this candidate to other tracks
or scan its gain/limit values as a scalar family.

The Stanley reference remains relevant for a future richer path-tracking
interface, but this four-distance contest controller does not accept it as a
drop-in replacement for the current desired-heading semantics.

## Evidence boundary

This result does not claim four-track completion, 80/80, physical UGV success,
or final submission readiness.
