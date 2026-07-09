# Unified Obstacle Avoidance v57 Plan

timestamp: 2026-07-10 CST
baseline: v48 opposing-steer guard
scope: one unified obstacle-controller mechanism for all four tracks

## Problem

v48, v55, and v56 all leave Track3 at:

```text
cR=1, cO=1, P=9.2
```

v56 shows that accelerating only the longitudinal obstacle speed filter delays
the first obstacle collision slightly (`1.05 s -> 1.15 s`) but does not remove
it. Therefore the next mechanism should not continue filter-time scans.

## Candidate Mechanism

Make front-risk entry earlier by using the existing `safeF` threshold:

```text
transition(cruise, avoid, df <= mindis or dl <= 0.45 or dr <= 0.45)
  -> transition(cruise, avoid, df <= safeF or dl <= 0.45 or dr <= 0.45)
```

This is deliberately narrow:

- It uses an already declared controller variable: `safeF(start=1.5)`.
- It keeps the v48 `ControlAllocate` opposing-steer guard unchanged.
- It does not change reverse speed, steering gain, filter time constants, or
  path planner.
- It remains one unified algorithm for all tracks.

Earlier v16 tested a similar front threshold before the v48 allocator fix. v57
retests the front-risk entry under the current v48 allocator because the
control-allocation interaction has changed since v16.

## Validation Plan

1. Run static deployability check.
2. Run Track3 target validation first.
3. Accept for Track1 regression only if Track3 improves collision count, score,
   or terminal quality versus v48.
4. If rejected, restore v48 semantics and do not continue simple front-threshold
   scans without a new mechanism reason.

## Non-Goals

- Do not edit official track, road, vehicle, sensor, scoring, or example
  models.
- Do not create per-track branches.
- Do not change `ControlAllocate` or `PathPlanner` in this candidate.
- Do not claim final competition or physical UGV success from this candidate.
