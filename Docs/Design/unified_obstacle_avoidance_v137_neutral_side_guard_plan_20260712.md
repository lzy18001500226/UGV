# v137 Neutral Side-Guard Plan

Status: rejected after the Track2 120 s gate; v80 semantics restored.

## Evidence Basis

The reproducible v80 Track2 completion request does not finish. It terminates
at `T=305.15 s`, path index 30, position `(28.0947, 14.6752)`, with
`cR=1`, `cO=0`, `P=9.6`, and `distanceSensor1.d=1004.6703`.

From about 61 s to termination, the controller remains in obstacle avoidance:

```text
front distance about 2.0 m (clear)
one side distance below 0.45 m
speed_oa = -1
steer_oa = +0.6
allocated speed about 0.059 m/s
closest_index remains 30
```

The probe cannot recover an assertion message from MWORKS, so `exit_state=2`
remains an unclassified early termination. The official finish assertion is
ruled out by the large finish distance.

Rejected v132-v135 already test forward side-hold, reverse steering-sign swap,
shorter reverse dwell, and motion-consistent forward recovery. None completes
a track. v137 must not repeat those mechanisms or scan their thresholds.

## Unified Candidate

Separate longitudinal risk ownership without changing the existing physical
thresholds or lateral steering law:

1. Front risk keeps the existing full reverse command `speed=-1`.
2. Side-only risk keeps `flag=true` and the existing lateral avoidance law,
   but contributes neutral longitudinal command `speed=0`.
3. Fully clear space returns to cruise `speed=1`.
4. Front risk has priority over the neutral side state.

The neutral contribution differs from v132/v135 forward recovery: it does not
add forward obstacle-controller acceleration. It allows the path planner's
speed contribution to remain active while avoiding repeated full reverse.

Implement the longitudinal contribution with Sysblock-supported bounded
arithmetic in the existing `avoid` state:

```modelica
speed := min(0, max(-1, df - mindis));
```

This is `-1` when the front clearance is zero, increases continuously as front
clearance recovers, and is exactly `0` for side-only risk with `df>=mindis`.
Do not use unsupported inline `if` actions, local helper functions, copied
state blocks, or edits outside the obstacle controller.

## Gates

1. Source deployability checker and all project tests pass.
2. Native Track2 1 s load/check/simulate passes.
3. Track2 120 s reaches the horizon, keeps `cR<=1`, `cO=0`, `P>=9.6`, and
   materially advances beyond v80's index 26 at 120 s.
4. Only after gate 3, run Track2 700 s. Acceptance requires the official finish
   assertion: `SimulateModel=false`, `T>10`, and `distanceSensor1.d<0.02`.
5. Only after a Track2 finish, run Track1 collision regression and then Tracks
   3-4. One algorithm and one parameter set must serve all four tracks.
6. Any early stop, collision regression, or absent progress rejects v137 and
   restores exact v80 source semantics.

This plan does not claim an official finish, an 80-point score, or physical
vehicle readiness.

## Result

The candidate passed the source checker (`high=0`, `medium=0`), all 11 tests,
and the native Track2 1 s gate. At 120 s it reached path index 112 rather than
v80's index 26 and reduced finish-distance squared from `813.7304` to
`329.7867`. The mechanism therefore removed the persistent reverse stall.

It failed the collision gate: `cR` increased from 1 to 2 and `P` fell from
9.6 to 9.2. No official finish occurred. v137 is rejected without a 700 s run
or cross-track expansion, and the controller is restored to v80 semantics.

The exported extra signals become constant before the second collision event,
so they cannot support a precise 100 s collision-window claim. A follow-up may
retain the neutral longitudinal insight only if it introduces a separately
justified lateral safety mechanism and re-runs the full comparable gate.
