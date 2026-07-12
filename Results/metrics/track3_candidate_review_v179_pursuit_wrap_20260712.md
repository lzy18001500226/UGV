# Track3 Candidate Review: v179 Pursuit Wrap

Status: rejected; exact v148 source semantics restored.

## Candidate

v179 combined the proven v162 narrow-front recovery with one path-topology
change: `calculatePursuitPoint` continued from the final path point to the
first point. Nearest-segment search and speed interpolation were unchanged.

## Gates

- Controller deployability: high=0, medium=0.
- Project tests: 14 passed.
- Track3 1 s native gate: passed with `SimulateModel=true`.
- Strict Track3 request: `SimulateModel=false`, `exit_state=2`.

## Result

```text
T=110.4
cR=1
cO=1
P=9.2
distanceSensor1.d=301.7618089408252
```

This is not an official finish because the finish distance is not below
`0.02`. It is also materially worse than v162's `T=286.55,cR=2,cO=1,P=8.8`
near-loop traversal. The mechanism changed the trajectory before the desired
return-to-origin event but did not improve completion.

## Decision

Reject v179 and restore exact v148 source semantics. Do not expand it to other
tracks and do not continue pursuit-wrap parameter stacking. The generic
completion blocker remains Track3 trajectory control, not an isolated missing
final-to-first pursuit segment.

Evidence:

- `Docs/Design/unified_obstacle_avoidance_v179_pursuit_wrap_plan_20260712.md`
- `Results/simulations/candidate_v179_pursuit_wrap_track3_1s_20260712/`
- `Results/simulations/candidate_v179_pursuit_wrap_track3_700s_20260712/`
- `Results/evidence/controller_deployability_static_check_v179_pursuit_wrap_20260712.md`

No completion, score gain, physical-car, package, or submission claim is made.
