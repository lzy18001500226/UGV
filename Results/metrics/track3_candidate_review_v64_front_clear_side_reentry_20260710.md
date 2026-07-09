# Track3 Candidate Review: v64 Front-Clear Side-Reentry Steering

## Scope

- Candidate: `v64_front_clear_side_reentry`
- Plan: `Docs/Design/unified_obstacle_avoidance_v64_plan_20260710.md`
- Source file tested:
  `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`
- Target track: `UGV.Test.Saidao3Eval`

No official vehicle, road, sensor, scoring, example, or official material files
were modified.

## Candidate Mechanism

Inside `avoid_lateral.ini_state`, v64 replaced the fixed initial steer with:

```modelica
if df > mindis and dl < 0.45 and dl < dr then
  steer := -min(0.8, 2 * abs(dl - dr));
elseif df > mindis and dr < 0.45 and dr < dl then
  steer := min(0.8, 2 * abs(dl - dr));
else
  steer := 0.6;
end if;
```

This was intended to avoid repeated fixed-positive side re-entry when front
clearance is safe but a side road edge is close.

## Evidence

Static source gate:

```text
Results/evidence/controller_deployability_static_check_v64_front_clear_side_reentry_20260710.md
Results/evidence/controller_deployability_static_check_v64_front_clear_side_reentry_20260710.json
```

Runtime evidence:

```text
Results/simulations/controller_v64_front_clear_side_reentry_saidao3_120s_20260710/
```

Offline analysis:

```text
Results/metrics/signal_window_summary_v48_v64_track3_20260710.md
Results/metrics/signal_window_summary_v48_v64_track3_20260710.json
```

## Result

| Candidate | Track | Runtime | Exit | T/s | cR | cO | P | Decision |
|---|---|---|---:|---:|---:|---:|---:|---|
| v48 baseline | Track3 | simulate_failed with result variables | 2 | 112.45 | 1 | 1 | 9.2 | keep |
| v64 | Track3 | simulate_failed with result variables | 2 | 3.85 | 0 | 1 | 9.6 | reject |

`P=9.6` is not accepted improvement evidence because v64 terminates at only
`3.85 s`, before the v48 4.85 s road event and far before the 120 s review
window. This is an early-stop score artifact.

The signal-window comparison confirms that v64 did not change the first Track3
obstacle event:

```text
1.05 s: cO 0 -> 1, ctrlAlloc.steer ~= 0.1623, steer_oa = 0.6
```

The front-clear side-reentry rule therefore avoids the intended front-obstacle
window, but it destabilizes the run before a comparable road-edge review can be
made.

## Decision

Reject v64. Do not expand to Track4/Track1/Track2 and do not continue simple
side-reentry steering scans from this mechanism without a new explanation for
the early terminal state.

Restore v48 semantics before the next candidate.

This review does not create a submission package and does not claim physical
UGV success.
