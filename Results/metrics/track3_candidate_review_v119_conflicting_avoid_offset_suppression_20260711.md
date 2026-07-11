# Track3 Candidate Review: v119 Conflicting Avoid Offset Suppression

Status: rejected; v80 source semantics restored, 2026-07-11 CST.

## Candidate

v119 preserved the path command but suppressed the obstacle-steering offset
when reverse avoidance and delayed path heading had opposite signs:

```modelica
firstOrder.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0
  then 0
  else gain.y;
```

The candidate was track-agnostic and changed only
`Models/UGV/Control/ControlAllocate/package.mo`.

## Gates

- Source/deployability gate before runtime: `high=0`, `medium=0`.
- Track3 1 s load/check/translation/simulation gate: passed, `exit_state=0`.
- Track3 120 s request: returned an abnormal early stop.

Evidence:

```text
Results/simulations/controller_v119_conflicting_avoid_offset_suppression_saidao3_1s_retry_20260711/
Results/simulations/controller_v119_conflicting_avoid_offset_suppression_saidao3_120s_20260711/
```

Observed target result:

```text
runtime_status=simulate_failed
exit_state=2
T=2.4
cR=0
cO=1
P=9.6
finish_distance_squared=4.2264988920222155
```

The readable `P=9.6` is not a gain: the run stopped after the first obstacle
event and is far shorter than the v80 Track3 reference
`T=59.4,cR=1,cO=1,P=9.2`.

## Decision

Reject v119 and do not expand it to the other tracks. Suppressing the full
avoidance offset during the initial conflict removes required collision
avoidance authority. This also confirms the earlier v94 attenuation family is
not a useful scalar-search direction. The source was restored to the direct
`connect(gain.y, firstOrder.u)` v80 semantics.

Restore evidence:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v119_20260711.md
Results/evidence/controller_deployability_static_check_v80_restored_after_v119_20260711.json
```

Restore checks: `high=0`, `medium=0`; `test_ugv_baseline_probe.py`: 5 passed.

## Next Direction

Do not continue scalar attenuation, sign reversal, dwell, or speed-cap scans.
The next candidate must be a planned structural controller mechanism with
bounded output, hysteresis/state continuity, and a target-track completion or
material path-progress gate before four-track expansion.
