# Track3 v177 Offset-Correction Review

Status: rejected; exact v148 source restored.

v177 retained v162's narrow `df<0.15` correction and reduced only the fixed
lateral entry steering from `+0.60` to `+0.55`, based on v162's repeatable
positive return-line offset.

Static deployability passed with `high=0,medium=0`, all 14 tests passed, and
the Track3 1 s native gate passed. The strict request produced:

```text
T=18.50,cR=1,cO=0,P=9.6
official finish distance squared=293.7713
runtime_status=simulate_failed
```

This is an early non-finish, not a score gain. The candidate removed the first
obstacle collision but lost the long route traversal established by v162.
Reject it without four-track expansion, restore exact v148, and do not scan
more fixed-entry steering magnitudes.

Evidence:

- `Docs/Design/unified_obstacle_avoidance_v177_offset_correction_plan_20260712.md`
- `Results/evidence/controller_deployability_static_check_v177_offset_correction_20260712.md`
- `Results/simulations/candidate_v177_offset_correction_track3_1s_20260712/`
- `Results/simulations/candidate_v177_offset_correction_track3_700s_20260712/`

No Track3 finish, 80/80, physical-car, package, or submission claim is made.
