# Physical UGV Obstacle-Avoidance Research Manifest

date: 2026-07-08
scope: robust obstacle-avoidance ideas for simulation and later physical UGV deployment
project: 2026 UGV obstacle-avoidance challenge

## Purpose

The current controller candidate should not only chase one simulation score. It also needs to remain explainable, bounded, and tunable when the initial-race MWORKS model is later used as the basis for generated code or a physical UGV controller. This note records external references that are useful for that goal, while keeping official model files unchanged.

## Stored Upstream Snippets

Small, reviewable reference files were saved under:

```text
References/research/physical_ugv_obstacle_avoidance_20260708/upstream_snippets/
```

| Source | Stored File | URL | License / Reuse |
|---|---|---|---|
| PythonRobotics Dynamic Window Approach | `pythonrobotics_dynamic_window_approach.py` | https://github.com/AtsushiSakai/PythonRobotics/tree/master/PathPlanning/DynamicWindowApproach | MIT license stored as `pythonrobotics_LICENSE`; reference only, no code imported. |
| PythonRobotics Potential Field Planning | `pythonrobotics_potential_field_planning.py` | https://github.com/AtsushiSakai/PythonRobotics/tree/master/PathPlanning/PotentialFieldPlanning | MIT license stored as `pythonrobotics_LICENSE`; reference only, no code imported. |
| PythonRobotics Pure Pursuit | `pythonrobotics_pure_pursuit.py` | https://github.com/AtsushiSakai/PythonRobotics/tree/master/PathTracking/pure_pursuit | MIT license stored as `pythonrobotics_LICENSE`; reference only, no code imported. |
| F1TENTH Follow-the-Gap lab | `f1tenth_lab4_template_README.md` | https://github.com/f1tenth/f1tenth_lab4_template | README/reference only; no ROS package imported. |

## Why These References

The official controller boundary currently exposes only four range-like inputs:

```text
front_dist, rear_dist, left_dist, right_dist
```

That is not enough to directly import full LiDAR-based Follow-the-Gap, DWA, TEB, or MPC planners. The useful transfer is the design pattern:

1. keep commands inside speed and steering-rate limits;
2. slow down before front-risk turns instead of steering at full speed;
3. use hysteresis or dwell so noisy range changes do not flip the controller;
4. preserve a safety buffer around the closest obstacle or blocked side;
5. keep parameters simple enough to tune on a physical vehicle.

## Immediate Project Consequence

For the current MWORKS controller, do not replace the official path planner or hard-code a large external planner. The next safe controller family is a bounded reactive safety layer:

```text
path planner remains primary
  -> obstacle controller adds bounded speed/steer increments
  -> front-risk slows first, then turns toward larger side clearance
  -> side-risk biases away from the closer side
  -> dwell/hysteresis prevents rapid release after near misses
  -> saturation and rate-like limits keep commands physical
```

This keeps the simulation work aligned with later physical deployment instead of producing a high-score but fragile track-specific trick.

## Non-Goals

- Do not copy ROS/F1TENTH package code into the official MWORKS model.
- Do not edit official road, vehicle, score, or track files.
- Do not claim real-car readiness until generated code or physical deployment evidence exists.
- Do not tune only for one track without preserving the bounded safety-layer interpretation in the design notes.
