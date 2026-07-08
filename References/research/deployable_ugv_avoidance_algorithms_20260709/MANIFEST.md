# Deployable UGV Avoidance Algorithms Research Manifest

date: 2026-07-09
scope: deployable obstacle-avoidance algorithms for simulation-to-physical UGV transfer
project: 2026 UGV obstacle-avoidance challenge
trigger: user clarified that the target is strong real-car obstacle avoidance, not only simulation score

## Purpose

This package records targeted upstream references that can improve the UGV controller while staying inside the current contest boundary. The current editable controller receives only four scalar distances and outputs speed/steer increments, so full planner stacks are reference patterns, not direct implementation targets.

## Saved Sources

| Source | Local Evidence | Role In This Project |
|---|---|---|
| F1TENTH Follow-the-Gap | `upstream_notes/f1tenth_follow_the_gap_README.md` | Reactive gap selection and safety bubble pattern. |
| Nav2 Regulated Pure Pursuit | `upstream_notes/nav2_regulated_pure_pursuit_README.md` | Speed regulation by curvature, proximity, and collision horizon. |
| TEB local planner | `upstream_notes/teb_local_planner_README.md`; `upstream_notes/teb_local_planner_LICENSE` | Obstacle separation and kinodynamic constraint vocabulary. |
| ROS1 DWA local planner | `upstream_notes/ros1_dwa_local_planner_package.xml` | Dynamic-window command feasibility and local obstacle cost pattern. |
| PythonRobotics DWA | `upstream_notes/pythonrobotics_dynamic_window_approach.py`; `upstream_notes/pythonrobotics_LICENSE` | Readable velocity-window, obstacle-cost, and prediction-horizon reference. |
| PythonRobotics Pure Pursuit | `upstream_notes/pythonrobotics_pure_pursuit.py`; `upstream_notes/pythonrobotics_LICENSE` | Path following and steering saturation pattern. |
| PythonRobotics Stanley control | `upstream_notes/pythonrobotics_stanley_control.py`; `upstream_notes/pythonrobotics_LICENSE` | Cross-track/path-heading control vocabulary for later richer interfaces. |

The raw fetch log is stored in `fetch_manifest.json`. It includes failed URL attempts instead of hiding them.

## What Was Learned

1. Real-car performance depends on command feasibility and conservative release behavior as much as obstacle clearance.
2. The current four-distance interface cannot host full LiDAR gap arrays, costmaps, global plans, TEB optimization, or DWA sampling directly.
3. The transferable layer is a small safety controller: front risk slows first, side imbalance steers toward clearance, high steering demand lowers speed, and release uses dwell/hysteresis.
4. The next controller changes should be diagnostic-driven: first-collision windows and distance/speed/steer traces should come before more gain tuning.
5. Any score improvement that relies on unbounded gains, one-track constants, or discontinuous steering flips should be rejected unless it also passes the physical-transfer filter.

## What Was Not Reused

- No upstream code was copied into `Models/UGV/`.
- No official vehicle, road, sensor, scoring, or example files were modified.
- No ROS stack, costmap, action server, or external planner dependency was introduced.
- No live MWORKS run or real-car readiness claim is made by this research pack.

## Implementation Consequence

When M6 runtime is unblocked, keep `controller_v5_front_dwell_2s` as the baseline and test only one deployability-improving idea at a time:

1. speed reduction proportional to absolute steering demand;
2. front-risk exit hysteresis separate from entry threshold;
3. explicit minimum forward speed/stop behavior near front emergency;
4. parameter table with physical meaning and tuning range.

If the official final-race interface exposes richer sensing or pose/path state, then revisit full Follow-the-Gap, DWA, RPP, TEB, or Stanley/Pure-Pursuit integration as a separate design step.
