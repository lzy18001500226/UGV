# Track3 Candidate Review - v99 Centerline Damping

Status: rejected, 2026-07-10 CST.

## Candidate

`v99_centerline_damping` added a path-planner centerline damping term to
`Models/UGV/Control/PathPlanning/PathPlanner.mo`.

The mechanism used signed lateral error from the closest path segment and was
intended to reduce early road-edge drift without changing the obstacle
avoidance controller, official models, score logic, or per-track behavior.

## Static Gate

Static deployability check passed before runtime:

```text
Results/evidence/controller_deployability_static_check_v99_centerline_damping_20260710.md
ready_for_physical_claim=true
high=0
medium=0
```

After rejection, source was restored to the accepted `v80_sharp_curve_speed_cap`
semantics and rechecked:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v99_20260710.md
ready_for_physical_claim=true
high=0
medium=0
```

`git diff --ignore-space-at-eol` confirms no semantic source diff remains in
`PathPlanner.mo` after restoration.

## Runtime Result

Track3 runtime evidence:

```text
Results/simulations/controller_v99_centerline_damping_saidao3_120s_20260710
runtime=simulate_failed
exit_state=2
T=53.4
cR=1
cO=1
P=9.2
```

Comparison baseline:

```text
v80 Track3: T=59.4, cR=1, cO=1, P=9.2
v99 Track3: T=53.4, cR=1, cO=1, P=9.2
```

## Diagnostic Value

v99 did not improve score, but it showed that path-level centerline correction
can delay the road event:

```text
v80 road event: t=4.85 s
v99 road event: t=5.90 s
```

At the v99 road event, the centerline term was active but not sufficient:

```text
centerline_error_signed ~= -0.461
centerline_correction ~= -0.115
pathPlanner.steering_angle ~= -0.336
base_steering_angle ~= -0.221
ctrlAlloc.steer ~= 0.130
steer_oa ~= 0.600
```

The useful lesson is that pure path-level damping alone is too weak against the
active obstacle-avoidance steering authority in the early side-squeeze window.
The next candidate should not repeat broad scalar scans or direct initial-steer
overrides. It should use the v99 insight only if it changes the authority
interaction materially while preserving Track1 and avoiding short-run score
artifacts.

## Decision

Reject v99.

Reasons:

- Track3 score stayed at `P=9.2`.
- Track3 runtime shortened from `59.4 s` to `53.4 s`.
- Both obstacle and road collision counts remained unchanged.
- The candidate did not justify expanding to Track1/2/4 regression.

No final 80/80 claim, no physical UGV claim, and no package/submission claim
are made from this result.
