# Reactive Obstacle-Avoidance Research Manifest

date: 2026-07-08
scope: M5 one-track tuning and real-car-friendly controller design
project: UGV obstacle-avoidance challenge

## Purpose

The first Race1 tuning attempt showed that direct score-chasing can make the
controller worse. This reference note records small, implementable ideas from
known reactive local-planning algorithms and maps them to the current
Sysblock/Modelica controller boundary.

## Sources

| Source | URL | Why Used | Reused Code |
|---|---|---|---|
| F1TENTH / RoboRacer Follow-the-Gap lab | https://f1tenth-coursekit.readthedocs.io/en/latest/assignments/labs/lab4.html | Reactive obstacle-avoidance framing for race-like Ackermann vehicles. | No |
| f1tenth_lab4_template README | https://github.com/f1tenth/f1tenth_lab4_template | Concrete Follow-the-Gap steps: closest point, safety bubble, max gap, best goal point, Ackermann output. | No |
| PythonRobotics Dynamic Window Approach docs | https://atsushisakai.github.io/PythonRobotics/modules/5_path_planning/dynamic_window_approach/dynamic_window_approach.html | Speed/steering command should be chosen inside dynamic limits, not as unconstrained jumps. | No |
| PythonRobotics DWA source location | https://github.com/AtsushiSakai/PythonRobotics/tree/master/PathPlanning/DynamicWindowApproach | Confirms the reference implementation exists as a local-planner example; not imported. | No |
| Vector Field Histogram overview | https://en.wikipedia.org/wiki/Vector_Field_Histogram | Candidate-valley, hysteresis, body-size and speed-reduction ideas for noisy range sensors. | No |
| F1TENTH Disparity Extender notes | https://www.nathanotterness.com/2019/04/the-disparity-extender-algorithm-and.html | Safety extension around range discontinuities for robust real-car obstacle avoidance. | No |

## Local Adaptation Decision

Do not import an open-source planner into the official MWORKS model. The current
controller has only four distance inputs:

```text
front_dist, rear_dist, left_dist, right_dist
```

Therefore the practical controller should be a simplified reactive gap follower:

```text
front clear  -> follow path planner with small or zero OA correction
front risky  -> slow/reverse and steer toward the larger side gap
side close   -> bias away from the closer side
recovery     -> keep avoidance for a short dwell time, then release with hysteresis
```

This is closer to real-car deployment than tuning arbitrary constants for one
simulation score because it is explainable, bounded, and parameter-light.

## 2026-07-08 Update

Runtime tuning confirmed the value of the dwell/hysteresis idea:

- `controller_v5_front_dwell_2s` improved `UGV.Example.Race1` at 120 s from
  v1 `cR=1, cO=3, P=8.4` to `cR=1, cO=2, P=8.8`.
- Extending dwell further to 3 s over-corrected the vehicle and regressed to
  `cR=17, cO=0, P=3.2`, so v6 was rejected.
- Removing the lateral cruise bias removed the early road collision but caused
  obstacle collisions in the first 35 s, so v4 was rejected.
