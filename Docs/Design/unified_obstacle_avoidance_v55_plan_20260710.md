# Unified Obstacle Avoidance v55 Plan

timestamp: 2026-07-10 CST
baseline: v48 opposing-steer guard
scope: one unified controller/path-planner mechanism for all four tracks

## Problem

v48 is the current best review-ready candidate, but Track3 still has one
obstacle collision and one road collision:

```text
Track3 v48: T=112.45, cR=1, cO=1, P=9.2, simulate_failed caveat
```

The first Track3 obstacle collision happens at `t=1.05 s` with:

```text
df=0.01324
dl=0.4876
dr=0.6474
obs flag=1
pathPlanner.steering_angle=-0.2717
ctrlAlloc.steer=0.1612
```

This means the obstacle controller is already active, but the path-planner
heading still opposes part of the avoidance steering. v53/v54 showed that
further reducing the path-authority scalar in `ControlAllocate` is unsafe, so
v55 must not continue that scalar scan.

## Candidate Mechanism

Add a low-speed lookahead floor in `PathPlanner`:

```text
lookahead_dist = lookahead_base + lookahead_gain * v
if v < low_speed_lookahead_trigger:
  lookahead_dist = max(lookahead_dist, low_speed_lookahead_floor)
```

Intended effect:

- At low speed or reverse/near-stop avoidance, the path target moves farther
  ahead.
- The path angle becomes less locally aggressive.
- Obstacle avoidance steering is less likely to be cancelled by a short-horizon
  path angle.

This is a unified path-planning mechanism, not a per-track branch and not a
new official-model or scoring edit.

## Implementation

Editable file:

```text
Models/UGV/Control/PathPlanning/PathPlanner.mo
```

Hard no-edit zones remain untouched:

```text
Models/UGV/Vehicle/
Models/UGV/Road/
Models/UGV/saidao/
Models/UGV/CountPoint/
Models/UGV/Example/
References/official_materials/
```

Initial v55 parameters:

```text
low_speed_lookahead_trigger = 0.6
low_speed_lookahead_floor = 4.0
```

These are chosen from v48 Track3 first-collision geometry: increasing the
lookahead from about `2.05` to about `4.0` should reduce the local path angle
opposing the obstacle controller without changing the obstacle-controller state
machine.

## Validation Plan

1. Run static deployability check.
2. Run Track3 first because it is the target weak track.
3. Accept v55 for broader regression only if Track3 improves collision count,
   score, or terminal quality versus v48 without an obvious early-stop
   regression.
4. If Track3 improves, run Track1 regression because previous steering/path
   candidates often harmed Track1.
5. If rejected, restore v48 semantics, save evidence, send sparse terminal
   email, commit the rejection evidence, and continue with the next
   evidence-backed mechanism.

## Non-Goals

- Do not tune a per-track branch.
- Do not edit official road, vehicle, sensor, scoring, or example models.
- Do not continue path-authority scalar scans in `ControlAllocate`.
- Do not claim final competition or physical UGV success from this candidate.
