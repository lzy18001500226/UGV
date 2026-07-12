# Track3 v164 Candidate Review

Status: rejected; exact v148 source semantics restored.

v164 combined v162's narrow front-obstacle recovery with a stateful endpoint
capture in `PathPlanner`. After the vehicle left a 3 m radius around the path
endpoint, returning inside that radius would force the pursuit point to the
exact endpoint. The mechanism was unified and contained no track identifier.

Static deployability checks passed with `high=0, medium=0`; all 14 script tests
passed; the 1 s native MWORKS gate passed and exported `pathPlanner.lap_departed`.

The strict Track3 request failed early at
`T=20.15,cR=1,cO=1,P=9.2`, with official finish-distance squared
`302.2936`. This is a clear regression from v162's near-complete loop and no
improvement over v148. The new discrete departure event occurs near the start
of the run and perturbs the numerical trajectory before endpoint capture is
needed, so this implementation is not safe to retain.

Evidence:

- `Docs/Design/unified_obstacle_avoidance_v164_endpoint_capture_plan_20260712.md`
- `Results/evidence/controller_deployability_static_check_v164_endpoint_capture_20260712.md`
- `Results/simulations/candidate_v164_endpoint_capture_track3_1s_20260712/`
- `Results/simulations/candidate_v164_endpoint_capture_track3_700s_20260712/`

Decision: reject v164 and restore v148. Do not expand this candidate to Tracks
1, 2, or 4. A future endpoint solution must avoid introducing a start-of-run
state event into the continuous path-planning loop; first diagnose official
finish assertion semantics and the shared start/end segment selection.

No Track3 finish, 80/80, physical-vehicle, package, or submission claim is
made.
