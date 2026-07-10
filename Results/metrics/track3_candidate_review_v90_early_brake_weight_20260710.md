# Track3 Candidate Review - v90 Early Brake Weight

Status: rejected, source restored to v80 semantics, 2026-07-10 CST.

## Baseline

Current accepted local wrapper candidate:

```text
v80 sharp curve speed cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
total wrapper score: 38.0
```

v80 Track3 reference:

```text
T=59.4
cR=1
cO=1
P=9.2
simulate_failed / exit_state=2
```

## Candidate

v90 tried to increase only the reverse obstacle-avoidance braking contribution
in `Models/UGV/Control/ControlAllocate/package.mo`:

```modelica
gain1.u = if speed_oa < 0 then 2 * speed_oa else speed_oa;
```

The intent was to address the v80 Track3 diagnosis where obstacle avoidance
already requested reverse motion before the first collision, but the allocated
speed was still positive near the obstacle-collision window.

## Target Result

Evidence:

```text
Results/simulations/controller_v90_early_brake_weight_saidao3_120s_20260710/
```

Observed score variables:

```text
T=4.60
cR=0
cO=0
P=10.0
runtime_status=simulate_failed
simulation_exit_state=2
```

The run stopped at `T=4.60 s`, far before the requested `120 s` horizon and
earlier than v80 Track3 (`T=59.4 s`). Its manifest explicitly records
`status: blocked` and says not to treat the run as controller, track, score, or
completion evidence.

## Decision

Reject v90. The apparent `P=10.0` is a non-comparable early-stop artifact, not
a proven score improvement. Do not promote this mechanism to the accepted
baseline and do not widen it to four-track evaluation.

The source was restored to v80 semantics:

```modelica
connect(speed_oa, gain1.u)
```

Restore static gate:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v90_20260710.md
```

## Next Direction

Continue from v80. The next candidate should use new source-level evidence
rather than repeating broad path-speed clamps, accepted-baseline scalar scans,
initial-lane bias/dwell changes, side-squeeze steering/speed/marker edits, or
this early-brake-weight mechanism.
