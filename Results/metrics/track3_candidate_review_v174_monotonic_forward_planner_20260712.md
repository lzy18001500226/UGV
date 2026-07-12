# Track3 v174 Monotonic-Forward Planner Review

Status: rejected; exact v148 controller and original global planner restored.

v174 kept the v162 obstacle branch and replaced v173's narrow path window with
a search from the previously accepted segment through all remaining forward
segments. This removed backward index movement and wraparound without using a
track identifier, fixed coordinate, score, or race-time branch.

Static checks passed with `high=0`, `medium=0`; all 14 tests passed; the 1 s
native gate passed and exported `progress_index`, `progress_fraction`, and
`closest_index`.

The strict Track3 request reproduced v173's failure:

```text
T=49.30,cR=1,cO=1,P=9.2
closest_index=48
official finish distance squared=385.5061
```

The run stopped mid-route and did not satisfy the official finish assertion.
Searching every forward segment therefore did not fix the planner departure;
the failure is not caused solely by v173's small forward window. Do not extend
this candidate to the other tracks or retain its source changes.

Evidence:

- `Docs/Design/unified_obstacle_avoidance_v174_monotonic_forward_planner_plan_20260712.md`
- `Results/evidence/controller_deployability_static_check_v174_monotonic_forward_planner_20260712.md`
- `Results/simulations/candidate_v174_monotonic_forward_planner_track3_1s_20260712/`
- `Results/simulations/candidate_v174_monotonic_forward_planner_track3_700s_20260712/`

No Track3 finish, four-track completion, 80/80, physical, package, or
submission claim is made.
