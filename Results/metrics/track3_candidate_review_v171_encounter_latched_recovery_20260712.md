# Track3 v171 Encounter-Latched Recovery Review

Status: rejected; exact v148 source restored.

v171 tested a controller-local encounter latch. It preserved v162's narrow
close-front direction correction and zeroed lateral avoidance only after the
current avoid episode had observed and then cleared a front obstacle.

The source checker reported `high=0,medium=0`, project tests passed, and the
Track3 1 s native gate passed. The strict request ended at:

```text
T=17.75,cR=1,cO=2,P=8.8
official finish distance=292.9712
runtime_status=simulate_failed
```

This is an early non-finish and adds one obstacle collision against v148.
Encounter latching does not provide enough geometric context to select a safe
path-recentering window. Reject v171, do not expand it to other tracks, and do
not continue scans of its clear-distance threshold.

Evidence:

- `Docs/Design/unified_obstacle_avoidance_v171_encounter_latched_recovery_plan_20260712.md`
- `Results/evidence/controller_deployability_static_check_v171_encounter_latched_recovery_20260712.md`
- `Results/simulations/candidate_v171_encounter_latched_recovery_track3_1s_20260712/`
- `Results/simulations/candidate_v171_encounter_latched_recovery_track3_700s_20260712/`

No finish, 80/80, physical, package, or submission claim is made.
