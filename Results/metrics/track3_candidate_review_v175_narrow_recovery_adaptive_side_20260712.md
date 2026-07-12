# Track3 v175 Narrow Recovery and Adaptive Side Review

Status: rejected as runtime no-op; exact v148 semantics restored.

v175 combined v162's narrow front-obstacle direction correction with v138's
`0.6` cap on the existing proportional left/right lateral states. Static
checks passed with `high=0`, `medium=0`; all 14 tests and the 1 s native gate
passed.

The strict Track3 result exactly reproduced v162:

```text
T=286.55,cR=2,cO=1,P=8.8
official finish distance squared=295.90730013110414
```

The identical runtime and finish distance show that the old `0.8` cap did not
activate on this trajectory. Do not scan these lateral magnitude caps further.
The candidate did not satisfy the official origin assertion and is not
expanded to other tracks.

Evidence:

- `Docs/Design/unified_obstacle_avoidance_v175_narrow_recovery_adaptive_side_plan_20260712.md`
- `Results/evidence/controller_deployability_static_check_v175_narrow_recovery_adaptive_side_20260712.md`
- `Results/simulations/candidate_v175_narrow_recovery_adaptive_side_track3_1s_20260712/`
- `Results/simulations/candidate_v175_narrow_recovery_adaptive_side_track3_700s_20260712/`

No Track3 finish, four-track completion, 80/80, physical, package, or
submission claim is made.
