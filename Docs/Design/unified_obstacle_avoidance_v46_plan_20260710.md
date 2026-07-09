# Unified Obstacle Avoidance v46 Plan

Status: planned_for_target_track_validation, 2026-07-10 CST

## Goal

Continue from accepted v45. Test one unified, track-agnostic mechanism that
addresses the remaining v45 failures without per-track branches or official
model edits.

## Evidence Basis

v45 is the current review-ready best candidate:

- Track1: `T=120.0`, `cR=3`, `cO=0`, `P=8.8`
- Track2: `T=120.0`, `cR=1`, `cO=0`, `P=9.6`
- Track3: `T=120.0`, `cR=1`, `cO=1`, `P=9.2`
- Track4: `T=120.0`, `cR=2`, `cO=0`, `P=9.2`
- Total: `36.8`

Fresh v45 signal-window evidence shows that the obstacle controller is already
active near weak events, but the final allocated speed remains comparatively
high:

- Track3 obstacle event near `1.05 s`: `speed_oa=-1`, `speed_pp=1`,
  `ctrlAlloc.speed ~= 0.51`.
- Track1 early road event near `6.55 s`: `speed_oa=-1`, `speed_pp=0.75`,
  `ctrlAlloc.speed ~= 0.25`.
- Track4 early road event near `6.40 s`: `speed_oa=-1`, `speed_pp=0.75`,
  `ctrlAlloc.speed ~= 0.25`.

Rejected prior evidence matters:

- v24 made obstacle filters faster and did not improve Track3 score.
- v28 doubled only the obstacle-avoidance speed contribution and produced a
  non-comparable early failure.

Therefore v46 must not repeat a broad filter change or a 2x speed-channel
change.

## Hypothesis

A mild obstacle-speed contribution increase can reduce early obstacle or road
contact during active avoidance while avoiding the v28 overreaction failure.

## Planned Source Change

Allowed scope:

```text
Models/UGV/Control/ControlAllocate/package.mo
```

Change only the obstacle-avoidance speed-channel gain from:

```modelica
gain1(k=factor_oa)
```

to:

```modelica
gain1(k=1.2*factor_oa)
```

Do not change:

- official vehicle, road, sensor, scoring, or example models;
- obstacle-controller state-machine thresholds;
- path data;
- per-track logic.

## Validation Gate

1. Run Track3 first because its v45 obstacle event is the clearest target.
2. Accept target-track continuation only if Track3 remains comparable and
   improves over v45 `P=9.2` or removes the early obstacle collision without a
   worse runtime terminal state.
3. If Track3 improves, run all four tracks and compare total score against
   v45 `36.8`.
4. If Track3 regresses or produces non-comparable early failure, reject v46,
   restore accepted v45 source semantics, record evidence, email a sparse
   Chinese notice, then continue with a different mechanism.

## Non-Goals

- No final submission package.
- No final physical UGV claim.
- No per-track tuning.
- No broad scalar sweep.
