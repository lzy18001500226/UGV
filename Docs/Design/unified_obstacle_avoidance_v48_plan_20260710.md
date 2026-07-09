# Unified Obstacle Avoidance v48 Plan

Status: review_ready_new_best_candidate_with_runtime_caveat, 2026-07-10 CST

## Goal

Continue from accepted v45 after rejecting v46-v47. Test a narrow
steering-authority mechanism that prevents path following from cancelling
active obstacle-avoidance steering under low-clearance events.

## Evidence Basis

Current accepted best:

```text
v45 total wrapper score: 36.8
```

Relevant v45 weak-event signal evidence:

- Track1 early road event near `6.55 s`:
  - `speed_oa=-1`
  - `steer_oa=0.6`
  - `steer_pp ~= -0.63`
  - final `ctrlAlloc.steer ~= -0.33`
  - interpretation: obstacle avoidance and path following oppose each other.
- Track3 early obstacle event near `1.05 s`:
  - `speed_oa=-1`
  - `steer_oa=0.6`
  - `steer_pp ~= -0.17`
  - final steering is weak positive.
- Track4 early road event near `6.40 s`:
  - `steer_oa` and `steer_pp` are aligned, consistent with v45 improving
    Track4.

Rejected evidence:

- v39 broadly attenuated path-planner steering and regressed Track4.
- v42/v43 changed side/path interaction in the obstacle state machine and
  regressed Track1.
- v46/v47 show simple speed-side mechanisms do not improve Track3.

## Hypothesis

When obstacle avoidance is active and path steering opposes obstacle steering,
attenuating only the opposing path-steering contribution can reduce controller
cancellation while preserving normal path tracking in aligned or non-obstacle
conditions.

## Planned Source Change

Allowed scope:

```text
Models/UGV/Control/ControlAllocate/package.mo
```

Replace the direct `unitDelay1.y -> gain3.u` path-steering feed with a
conditional expression:

```modelica
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0
  then 0.5 * unitDelay1.y
  else unitDelay1.y;
```

This keeps one unified mechanism, uses existing inputs, and does not introduce
per-track branches.

## Validation Gate

1. Run Track1 first because the v45 Track1 early event has the clearest
   opposing-steer cancellation.
2. If Track1 improves without non-comparable runtime failure, run Track3.
3. If either target track improves comparably, run all four tracks.
4. If Track1 regresses or the model fails CheckModel/SimulateModel in a way
   that invalidates the run, reject v48, restore v45 semantics, and continue
   with a different mechanism.

## Result

Saved review:

```text
Results/metrics/four_track_candidate_review_v48_opposing_steer_guard_20260710.md
```

v48 is accepted as the current review-ready best candidate with a runtime
caveat. It improves total wrapper score from v45 `36.8` to `37.2` by improving
Track1 from `P=8.8` to `P=9.2`. Track2, Track3, and Track4 keep the same
recorded `P/cR/cO` score variables as v45 but return `simulate_failed` with
result variables, so v48 is not final competition or physical UGV proof.

## Non-Goals

- No final package.
- No physical UGV claim.
- No edits to official vehicle, road, sensor, scoring, example, or track files.
- No per-track logic.
