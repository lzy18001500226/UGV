# v144 Neutral Re-entry Steering Plan

Status: runtime candidate from restored v80 comparison semantics.

## Evidence Basis

The Track2 completion-chain audit confirms that the official and wrapper paths
are identical, closed at the origin, and structurally finishable. Existing
v80/v137 trajectories show no path-index discontinuity, so PathPlanner is not
changed without runtime evidence.

v137 provides the strongest current progress result: neutral side-only
longitudinal authority reaches Track2 index 112 at 120 s instead of v80 index
26. It also adds a road collision at `t=100 s`. At that event the front is
clear and the two side clearances are nearly symmetric, while the obstacle
steering output is the fixed `+0.6` re-entry value.

The nested lateral state machine initializes every avoid-state entry with
`steer=+0.6` before measured left/right asymmetry selects a turn state. The
outer avoid state recycles after two seconds, so sustained side risk can
reapply this directional bias repeatedly even when neither side justifies it.

## Unified Candidate

1. Preserve v137's bounded longitudinal contribution:

```modelica
speed := min(0, max(-1, df - mindis));
```

2. Change only the nested lateral re-entry value from fixed left steering to
neutral steering:

```modelica
steer := 0;
```

3. Preserve the existing measured left/right transition rules and turn-state
steering laws. This removes only the unmeasured reset bias; it does not add a
per-track branch, tune a scalar threshold, wash out sustained obstacle
steering, or alter official models.

## Gates

1. Deployability checker reports `high=0, medium=0`; all project tests pass.
2. Track2 1 s load/check/simulate succeeds.
3. Track2 120 s must reach the horizon, retain `cR<=1,cO=0,P>=9.6`, and
   advance materially beyond v80 index 26.
4. Only after gate 3, run the extended Track2 finish gate. Completion requires
   `SimulateModel=false`, `T>10`, and `distanceSensor1.d<0.02`.
5. Only after an official Track2 finish, run Track1 collision regression and
   then Tracks 3-4 with the same source and parameters.
6. Any early termination, collision regression, or absent material progress
   rejects v144 and restores v80 semantics.

This plan does not claim a finish, an official score, physical validation, or
submission readiness.
