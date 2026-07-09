# Unified Obstacle Avoidance v56 Plan

timestamp: 2026-07-10 CST
baseline: v48 opposing-steer guard
scope: one unified controller/control-allocation mechanism for all four tracks

## Problem

v48 Track3 still records one obstacle collision and one road collision:

```text
Track3 v48: T=112.45, cR=1, cO=1, P=9.2
```

At the first obstacle collision window, the obstacle controller is active but
the final speed remains high:

```text
t=1.05 s
speed_pp=1
speed_oa=-1
oa_speed_filtered=-0.2804
final_speed=0.7196
steer_oa=0.6
final_steer=0.1623
```

v24 reduced both obstacle-avoidance filters from `T=1` to `T=0.5`, but it
still kept Track3 at `P=9.2` and early-stopped. Therefore v56 must not repeat
the broad filter change. It tests only the longitudinal deceleration channel.

## Candidate Mechanism

Change only the obstacle-avoidance speed filter in `ControlAllocate`:

```text
firstOrder1(T=1) -> firstOrder1(T=0.5)
```

Keep unchanged:

```text
firstOrder(T=1)             # steering obstacle channel remains smooth
opposing-steer path guard   # v48 accepted behavior remains
obstacle controller state machine
path-planner speed regulation
```

Expected effect:

- Obstacle speed command reaches the allocator earlier during front-risk
  windows.
- Steering transients remain bounded because the steering filter is unchanged.
- The change remains one unified algorithm and does not branch by track.

## Validation Plan

1. Run static deployability check.
2. Run Track3 first.
3. Accept for broader regression only if Track3 improves collision count,
   score, or terminal quality versus v48.
4. If rejected, restore v48 semantics and do not continue filter-time scans
   without a new mechanism reason.

## Non-Goals

- Do not change official track, road, vehicle, sensor, scoring, or example
  models.
- Do not tune per track.
- Do not modify the steering filter in this candidate.
- Do not claim final competition or physical UGV success from this candidate.
