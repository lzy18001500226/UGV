# Track3 v165 Candidate Review

Status: rejected; exact v148 source semantics restored.

v165 retained v162's narrow front-obstacle recovery and added a stateless
geometric capture of the closure segment `path[end-2] -> path[end-1]`. The
official road representation repeats the origin at `path[end-1]` and appends
the first outgoing point at `path[end]`, so this corrected the initial v165
draft's segment selection.

Static deployability checks passed with `high=0, medium=0`; all 14 script tests
passed. The corrected 1 s native gate passed, with closure-segment projection
progress equal to `1` at startup, proving the capture condition was inactive
during departure.

The strict Track3 run nevertheless stopped at
`T=18.1,cR=1,cO=1,P=9.2`, official finish-distance squared `295.2941`.
Exported samples contain no point satisfying the capture predicate before the
stop. Adding the continuous closure-segment calculation alone changed the
translated equation evaluation enough to perturb this numerically sensitive
trajectory before the intended finish area.

Evidence:

- `Docs/Design/unified_obstacle_avoidance_v165_final_segment_capture_plan_20260712.md`
- `Results/evidence/controller_deployability_static_check_v165_final_segment_capture_20260712.md`
- `Results/simulations/candidate_v165_final_segment_capture_track3_1s_20260712/`
- `Results/simulations/candidate_v165_final_segment_capture_corrected_track3_1s_20260712/`
- `Results/simulations/candidate_v165_final_segment_capture_track3_700s_20260712/`

Decision: reject v165 and close direct `PathPlanner` endpoint-helper additions
for this tuning pass. Preserve v162 as diagnostic evidence only. Next work
should use offline trajectory analysis or an existing controller state surface
without adding planner equations.

No Track3 finish, 80/80, physical-vehicle, package, or submission claim is
made.
