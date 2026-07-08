# Robust Physical UGV Navigation Research Manifest

date: 2026-07-09
scope: robust obstacle-avoidance and local-control references for simulation-to-real UGV transfer
project: 2026 UGV obstacle-avoidance challenge
trigger_phase: M6 blocked; offline work should improve real-car robustness, not only simulation score

## Purpose

The user clarified that the project goal is good deployable obstacle avoidance on a physical UGV, not only high MWORKS simulation score. This package records targeted external references and how they map to the official controller boundary.

## Sources Checked

| Source | URL / Path | License If Visible | Local Evidence | Relevance |
|---|---|---|---|---|
| TEB local planner | https://github.com/rst-tu-dortmund/teb_local_planner | BSD noted in README | `upstream_notes/teb_local_planner_README.md` | Runtime trajectory optimization with kinodynamic constraints; useful as design vocabulary, not directly importable. |
| Nav2 Regulated Pure Pursuit | https://github.com/ros-navigation/navigation2/tree/main/nav2_regulated_pure_pursuit_controller | Apache-2.0 project context; README citation info | `upstream_notes/nav2_regulated_pure_pursuit_README.md` | Speed regulation by collision risk, curvature, and lookahead; highly relevant to real-car tunability. |
| F1TENTH Follow-the-Gap lab | https://github.com/f1tenth/f1tenth_lab4_template | README/reference only | `upstream_notes/f1tenth_follow_the_gap_README.md` | Reactive safety-bubble and free-gap logic; closest match to four-distance obstacle layer after simplification. |
| PythonRobotics | https://github.com/AtsushiSakai/PythonRobotics | MIT license saved | `upstream_notes/pythonrobotics_LICENSE`; prior snippets in `../physical_ugv_obstacle_avoidance_20260708/` | DWA, potential field, pure pursuit examples; use as algorithm reference only. |
| ROS1 DWA local planner | https://github.com/ros-planning/navigation/tree/noetic-devel/dwa_local_planner | BSD-style ROS navigation context | README fetch returned 404 for the attempted path | Useful conceptually for dynamic-window feasibility, but no local README evidence was saved in this package. |

## What Was Learned

1. Real-car robustness usually comes from command feasibility, speed regulation, collision horizon checks, and conservative behavior near high curvature or obstacles.
2. The official UGV controller boundary currently has only `front_dist`, `rear_dist`, `left_dist`, and `right_dist`; it cannot directly host full TEB/DWA/SLAM/costmap planners.
3. The transferable part is a bounded safety layer: front-risk slows first, side imbalance steers away, release uses dwell/hysteresis, and speed is reduced when steering demand is high.
4. Strong score-only tricks such as discontinuous sign flips, reciprocal-distance spikes, or track-specific constants are risky for generated code and physical tuning.

## What Was Reused

No upstream code was copied into `Models/UGV/`. The saved upstream files are documentation evidence only. Existing controller changes remain limited to the allowed obstacle-controller boundary.

## What Was Not Reused

- Full ROS navigation stacks, action servers, costmaps, and message interfaces.
- Any changes to official vehicle, road, track, scoring, or example files.
- Any direct import of TEB/DWA/RPP code into Modelica/Sysblock.

## Next Action

When MWORKS activation is restored and official-track simulation can run again, evaluate candidate improvements in this order:

1. preserve current v5 front-risk dwell baseline;
2. add first-collision/sensor-window extraction before changing gains;
3. test speed reduction coupled to steering magnitude;
4. test exit hysteresis around front-risk release;
5. only then consider more complex planner-like logic if the official interface exposes more state.