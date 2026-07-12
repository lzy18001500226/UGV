# Track3 v173 Progress-Continuous Planner Review

Status: rejected; superseded by v174 before final source restoration.

v173 combined v162 with a sampled nearest-segment search limited to two
segments behind and eight ahead of the previous index. Static checks and all
14 tests passed; the 1 s native gate also passed.

The strict Track3 request ended at:

```text
T=49.3,cR=1,cO=1,P=9.2
closest_index=48
official finish distance squared=385.5061
```

The small bidirectional window prevented reliable mid-route reacquisition and
still permitted index regression. Reject this window policy. The saved
geometry review confirms a mid-route departure rather than a finish approach.

Evidence:

- `Docs/Design/unified_obstacle_avoidance_v173_progress_continuous_planner_plan_20260712.md`
- `Results/simulations/candidate_v173_progress_continuous_planner_track3_1s_20260712/`
- `Results/simulations/candidate_v173_progress_continuous_planner_track3_700s_20260712/`
- `Results/metrics/v173_progress_continuity_geometry_review_20260712.md`

No finish, 80/80, physical, package, or submission claim is made.
