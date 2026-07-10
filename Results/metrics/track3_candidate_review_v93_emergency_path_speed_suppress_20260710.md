# Track3 Candidate Review - v93 Emergency Path-Speed Suppression

Date: 2026-07-10 CST

## Scope

This review closes `v93_emergency_path_speed_suppress`.

The accepted baseline remains:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
```

## Candidate

v93 tested a front-emergency marker plus control-allocation path-speed
suppression:

```text
ObsAvoidController_Sysblock2.mo:
  if df <= 0.25 and dl > 0.3 and dr > 0.3 then speed := -3 else speed := -1

ControlAllocate/package.mo:
  gain2.u = if speed_oa < -2 then 0 else unitDelay3.y
```

The intent was to make the v92 emergency speed marker affect the final
allocated speed instead of being dominated by path speed.

## Runtime Result

Target run:

```text
Results/simulations/controller_v93_emergency_path_speed_suppress_saidao3_120s_20260710/
simulate_failed / exit_state=2
T=10.7
cR=1
cO=2
P=8.8
```

Baseline comparison:

```text
v80 Track3:
T=59.4
cR=1
cO=1
P=9.2
```

## Event Evidence

Supporting evidence:

```text
Results/metrics/collision_window_analysis_v80_v93_track3_20260710.md
Results/metrics/signal_window_summary_v80_v93_track3_20260710.md
```

v93 moved the first obstacle event later but created an additional obstacle
event:

```text
4.40s: cO 0 -> 1, P 10.0 -> 9.6
5.00s: cO 1 -> 2, P 9.6 -> 9.2
9.35s: cR 0 -> 1, P 9.2 -> 8.8
```

At 5.00s the emergency marker did suppress final speed strongly:

```text
speed_oa=-3
ctrlAlloc.speed=-0.8934
```

The negative final speed did not solve the obstacle interaction; it caused a
worse local behavior with a second obstacle penalty.

## Decision

Reject v93.

Do not continue the route of emergency path-speed suppression or front-emergency
reverse dominance. It improves neither Track3 score nor runtime stability and
regresses from `P=9.2` to `P=8.8`.

Source was restored to v80 semantics after the run. Restore gate:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v93_20260710.md
```

## Next Direction

Avoid another scalar speed/reverse candidate. The next candidate should inspect
geometry/path behavior before contact, or introduce a structurally different
local path/clearance rule that does not create reverse-dominant behavior.

## Non-Claims

- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No final 80/80 claim.
- No physical UGV success claim.
- No report/package work.
