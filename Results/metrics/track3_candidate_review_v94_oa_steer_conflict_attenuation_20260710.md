# Track3 Candidate Review - v94 OA Steer Conflict Attenuation

Status: rejected, 2026-07-10 CST.

## Baseline

Accepted baseline remains:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper total: 38.0 / 40
Track3: simulate_failed, T=59.4, cR=1, cO=1, P=9.2
```

## Candidate

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v94_plan_20260710.md
```

Mechanism tested:

```modelica
firstOrder.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0 and abs(unitDelay1.y) > 0.15
  then 0.35 * gain.y
  else gain.y;
```

The candidate attenuated obstacle steering only when obstacle-avoidance steer
conflicted with path steer during active braking.

## Static Gate

```text
Results/evidence/controller_deployability_static_check_v94_oa_steer_conflict_attenuation_20260710.md
high=0, medium=0
```

## Runtime Result

Track3 run:

```text
Results/simulations/controller_v94_oa_steer_conflict_attenuation_saidao3_120s_20260710/
simulate_failed, exit_state=2
T=2.4, cR=0, cO=1, P=9.6
```

This is not an accepted improvement. Although the end score variable is higher
than v80 because the run stops early, the run is non-comparable and much shorter
than the current v80 Track3 evidence.

## Diagnostics

```text
Results/metrics/collision_window_analysis_v94_track3_20260710.md
Results/metrics/signal_window_summary_v94_track3_20260710.md
```

At the first obstacle event:

```text
time=1.05s
cO: 0 -> 1
ctrlAlloc.speed=0.7196
ctrlAlloc.steer=0.1623
ctrlAlloc.speed_oa=-1
ctrlAlloc.steer_oa=0.6
ctrlAlloc.steer_pp=-0.03857
ctrlAlloc.firstOrder.u=0.3
df=0.01324, dl=0.4876, dr=0.6474
```

The v94 guard did not activate there because the path steer magnitude was too
small. The candidate therefore did not address the first obstacle event and
also shortened Track3 runtime.

## Decision

Reject v94 as an accepted baseline. Restore v80 semantics and continue the
long score sprint with a different evidence-backed mechanism.

Restore gate:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v94_20260710.md
high=0, medium=0
```

## Do Not Repeat Without New Evidence

- Do not repeat obstacle-steer attenuation gated only by opposing path steer.
- Do not accept early-stopped `P=9.6` as a score gain when the run is
  non-comparable.
- Do not move to report/package work because the score sprint remains active.
