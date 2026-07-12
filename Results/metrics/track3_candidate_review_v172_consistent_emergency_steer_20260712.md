# Track3 v172 Consistent Emergency Steer Review

Status: rejected as runtime no-op; exact v148 source restored.

v172 raised only the `df<0.15` direction-correction cap from `0.6` to `0.8`,
matching the normal bypass-state limit. The source checker returned
`high=0,medium=0`, all 14 tests passed, and the Track3 1 s native gate passed.

The strict request produced exactly the v162 result:

```text
T=286.55,cR=2,cO=1,P=8.8
official finish distance squared=295.9073
runtime_status=simulate_failed
```

The cap was not active on the saved trajectory, so this candidate is a no-op.
Reject it, do not expand to other tracks, and do not scan additional values for
the same cap.

Evidence:

- `Docs/Design/unified_obstacle_avoidance_v172_consistent_emergency_steer_plan_20260712.md`
- `Results/evidence/controller_deployability_static_check_v172_consistent_emergency_steer_20260712.md`
- `Results/simulations/candidate_v172_consistent_emergency_steer_track3_1s_20260712/`
- `Results/simulations/candidate_v172_consistent_emergency_steer_track3_700s_20260712/`

No Track3 finish, 80/80, physical, package, or submission claim is made.
