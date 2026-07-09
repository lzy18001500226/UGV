# Unified Obstacle Avoidance v31 Plan

generated_at: 2026-07-09 21:53 CST

## Scope

One unified controller for all four official tracks. No branch on track name,
wrapper name, run id, score variable, or simulation time table.

Allowed implementation target:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
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

## Evidence Basis

Accepted baseline:

```text
Results/metrics/four_track_summary_v13_side_trigger045_20260709_1535.md
```

Fresh pre-collision attribution:

```text
Results/metrics/v13_pre_collision_control_attribution_20260709_2140.md
```

The new attribution shows that remaining v13 failures are mostly road contacts
while avoid mode is already active or recently toggled. Side margin shrinks
before Track1 and Track4 road contacts, and in several windows the final steer
is dominated by path-planner steer rather than the filtered obstacle-avoidance
contribution.

## Hypothesis

v13 releases avoid mode after 2 seconds. At road-boundary collision windows,
this can return the controller to cruise/path tracking too early, allowing the
path-planner command to dominate while side margin is still shrinking.

v31 extends the avoid-to-cruise release dwell:

```modelica
transition(avoid, cruise, after(3,sec), reset = false)
```

This is not a per-track patch. It is a small hysteresis-style safety mechanism:
hold obstacle-avoidance authority longer after a front or side risk trigger.

## Acceptance Gate

1. Static deployability checker reports `high=0`.
2. Target weak tracks Track1 and Track4 are run first.
3. Accept only if either Track1 or Track4 improves road collision count or score
   against v13 without a non-comparable early stop.
4. If target tracks do not improve, restore v13 and record v31 as rejected.
5. Only expand to Track2/Track3 regression when target evidence improves.

## Non-Claims

- This plan does not claim final competition score.
- This plan does not claim physical UGV readiness.
- This plan does not authorize final submission packaging or sending.
