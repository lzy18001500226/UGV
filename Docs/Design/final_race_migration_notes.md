# Final Race / Physical UGV Migration Notes

> Keep initial-race simulation decisions compatible with later generated-code and physical UGV deployment. This file is not a claim that physical testing has happened.

Status: initial migration constraints, 2026-07-08 CST.

## 1. Deployment Goal

The initial race uses MWORKS simulation, but the controller should be designed as if it may later be generated and tuned on a physical UGV. The goal is robust obstacle avoidance, not only a high score in one simulated track.

## 2. Current Controller Boundary

Normal editable controller target:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Current usable inputs and outputs:

```text
inputs:  front_dist, rear_dist, left_dist, right_dist
outputs: speed, steer
```

This is a reactive safety-layer interface. It cannot directly host a full LiDAR, SLAM, global-planning, DWA, TEB, or MPC stack unless the competition interface changes.

## 3. Physical Transfer Principles

1. Keep the official path planner primary in cruise; obstacle avoidance should add bounded increments, not replace the driving task.
2. Keep outputs saturated and explainable.
3. Prefer finite-state logic, thresholds, dwell, hysteresis, and speed caps over fragile score-specific constants.
4. Avoid reciprocal distance terms or discontinuous sign flips unless runtime evidence proves they are stable.
5. Record every change with the sensor window that motivated it.
6. Do not edit official vehicle, road, track, scoring, or example systems to hide a controller weakness.

## 4. Algorithm References To Reuse As Patterns

Reference notes are stored at:

```text
References/research/physical_ugv_obstacle_avoidance_20260708/
```

Use them as patterns only:

| Reference Pattern | Useful Part | Current Adaptation |
|---|---|---|
| Follow-the-Gap | steer toward free gap and keep safety bubble | choose larger of left/right clearance under front risk |
| Dynamic Window Approach | feasible command limits and short-horizon obstacle cost | speed/steer saturation, dwell, and speed-turn coupling |
| Potential Field | bounded repulsion from obstacles | linear side/front repulsion with saturation |
| Pure Pursuit | smooth recovery to path-following | release avoidance gradually back to official planner |

## 5. Evidence Needed Before Real-Car Claims

Before any statement like "physical UGV ready", collect at least:

```text
generated-code or deployable controller artifact
parameter table with units and tuning range
simulation run evidence on all required official tracks or an honest blocker
collision/score metrics linked to run folders
first-collision diagnostic windows for failed cases
manual notes for physical safety limits and emergency stop behavior
```

If generated-code or real-car deployment material is unavailable, say so. Do not turn simulation-only evidence into a physical-deployment claim.

## 6. Current Practical Next Step

Resolve the M6 official-track simulation-entry blocker first. While blocked, safe progress is limited to:

1. blocker-aware report drafting;
2. research notes and physical-transfer constraints;
3. evidence automation that does not alter official no-edit zones;
4. support/documentation lookup for the exact MWORKS parameter-evaluation API.
