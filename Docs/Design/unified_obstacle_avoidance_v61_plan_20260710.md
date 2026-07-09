# Unified Obstacle Avoidance v61 Plan - Early Risk Arbitration

## Goal

Improve the current v48 unified controller on the early Track3 obstacle event
without adding per-track branches or editing official vehicle, road, sensor,
scoring, example, or official material files.

## Evidence Basis

Current accepted candidate:

- `Docs/Design/unified_obstacle_avoidance_v48_plan_20260710.md`
- `Results/metrics/four_track_candidate_review_v48_opposing_steer_guard_20260710.md`
- `Results/metrics/trajectory_geometry_review_v48_20260710.md`
- `Results/metrics/signal_geometry_window_summary_v48_20260710.md`

Key v48 observation:

- Track3 first obstacle event occurs around `1.05 s` at `x ~= 1.2`,
  `y ~= 0.08`, with nearest obstacle distance about `0.106 m`.
- At that moment the obstacle controller already outputs `steer_oa = 0.6` and
  `speed_oa = -1`, but final `ctrlAlloc.steer` is only about `0.162`.
- The path planner is slightly opposing the avoidance turn
  (`steer_pp ~= -0.039`), so v48's half path attenuation still leaves a small
  negative path component during the first obstacle contact.
- v60 direct steering-filter acceleration was rejected, so v61 must not change
  the global filter time constant.

## Candidate Mechanism

Modify only `Models/UGV/Control/ControlAllocate/package.mo`.

Add a narrow dynamic arbitration rule inside `CtrlAlloc`:

```modelica
pathSmallOpposingAvoid =
  speed_oa < 0 and steer_oa * unitDelay1.y < 0 and
  abs(unitDelay1.y) < 0.12 and abs(steer_oa) >= 0.55;
```

When this condition is true:

1. Suppress the small opposing path-steering term instead of keeping v48's
   half path contribution.
2. Raise the obstacle-steering filter input modestly from `gain.y` to
   `1.2 * gain.y`.

Otherwise keep v48 behavior unchanged:

```modelica
gain3.u = if pathSmallOpposingAvoid then 0
  else if speed_oa < 0 and steer_oa * unitDelay1.y < 0
  then 0.5 * unitDelay1.y
  else unitDelay1.y;

firstOrder.u = if pathSmallOpposingAvoid then 1.2 * gain.y else gain.y;
```

This is not a track-specific rule. It uses only existing controller allocation
signals and targets the control situation where obstacle avoidance is active,
strong, and being opposed by only a small path-steering term.

## Why This Is Not Another Rejected Scan

- It does not change `firstOrder(T=1)`, avoiding the rejected v60 direction.
- It does not globally increase `factor_oa`; wrapper `factor_oa=0.5` remains
  unchanged.
- It does not change fixed initial lateral steering strength, avoiding the
  rejected v17/v18 direction.
- It does not reduce speed globally or add path-speed attenuation, avoiding the
  rejected v49/v51/v52 families.

## Risk

Offline v48 CSV screening shows this condition can also appear on Track2,
Track4, and later on Track1. Therefore v61 must be validated as a four-track
unified candidate and may be rejected if it creates early stops or worsens
road-collision behavior.

## Validation Order

1. Run static deployability check.
2. Run Track3 first because it contains the target early obstacle event.
3. If Track3 improves or remains comparable, run Track1 regression because
   Track1 is the strongest road-edge sensitivity check.
4. If still acceptable, run all four official evaluation wrappers.
5. If rejected, restore v48 semantics and record restoration evidence before
   trying another mechanism.

## Acceptance

Accept v61 only if it improves total four-track wrapper score or removes a
critical Track3 obstacle event without causing worse Track1 road behavior.

This plan does not create a final submission package and does not claim
physical UGV success.
