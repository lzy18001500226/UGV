# Track3 v168 Closure-Progress Capture Review

Status: rejected; exact v148 source semantics restored.

v168 combined v162's narrow obstacle recovery with a closure capture using
only the already-computed `closest_index` and `path_progress`. When the vehicle
was in the final two path segments with progress above `0.5`, the pursuit point
was set to the repeated origin at `path[end-1]`. No state, event, geometry
function, new variable, or track identifier was added.

Static deployability passed with `high=0, medium=0`; all 14 tests passed; the
Track3 1 s native gate passed.

The strict run stopped at `T=18.1,cR=1,cO=1,P=9.2`, official finish-distance
squared `295.2941`. This exactly matches v165's early termination even though
v168's closure predicate was inactive in the early trajectory. Together,
v165/v168 prove that adding an endpoint-helper branch to `PathPlanner` changes
this numerically sensitive translated system before the intended finish area.

Decision: reject v168, restore v148, and close all `PathPlanner` endpoint
capture edits for the current task. Future candidates must not add planner
equations merely to force the finish assertion.

Evidence:

- `Docs/Design/unified_obstacle_avoidance_v168_closure_progress_capture_plan_20260712.md`
- `Results/evidence/controller_deployability_static_check_v168_closure_progress_capture_20260712.md`
- `Results/simulations/candidate_v168_closure_progress_capture_track3_1s_20260712/`
- `Results/simulations/candidate_v168_closure_progress_capture_track3_700s_20260712/`

No Track3 finish, 80/80, physical-vehicle, package, or submission claim is
made.
