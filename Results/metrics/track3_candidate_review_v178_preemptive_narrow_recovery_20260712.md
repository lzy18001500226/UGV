# Track3 v178 Preemptive Narrow Recovery Review

Status: rejected; exact v148 source restored.

v178 moved v162's direction-aware close-front branch from `df<0.15` to
`df<0.20`, based on the saved timing between branch activation and the first
Track3 road event.

The deployability checker passed with `high=0,medium=0`, all 14 tests passed,
and the Track3 1 s native gate passed. The strict request produced:

```text
T=228.15,cR=2,cO=1,P=8.8
official finish distance squared=385.5204
runtime_status=simulate_failed
```

The candidate ran substantially longer than v148 but did not finish, ended far
from the origin, and regressed v162's `T=286.55` near-loop diagnostic. Reject
without four-track expansion, restore exact v148, and do not scan nearby
front-distance thresholds.

Evidence:

- `Docs/Design/unified_obstacle_avoidance_v178_preemptive_narrow_recovery_plan_20260712.md`
- `Results/evidence/controller_deployability_static_check_v178_preemptive_narrow_recovery_20260712.md`
- `Results/simulations/candidate_v178_preemptive_narrow_recovery_track3_1s_20260712/`
- `Results/simulations/candidate_v178_preemptive_narrow_recovery_track3_700s_20260712/`

No Track3 finish, 80/80, physical-car, package, or submission claim is made.
