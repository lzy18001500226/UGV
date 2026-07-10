# Sparse Reactive Obstacle Avoidance Research Manifest

timestamp: 2026-07-10 CST
purpose: post-v69 research for a genuinely different, deployable four-distance UGV obstacle-avoidance mechanism
status: research notes only, no source edit

## Sources

| Source | URL | Use |
|---|---|---|
| Vector Field Histogram paper copy | `https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated1/borenstein_VFHisto.pdf` | Confirms VFH needs a histogram/grid world model from range data, so it cannot be directly copied into the current four-scalar controller. |
| RoboRacer/F1TENTH Follow-the-Gap lab | `https://f1tenth-coursekit.readthedocs.io/en/latest/assignments/labs/lab4.html` | Confirms FTG is a compact reactive planner but assumes LaserScan-like range samples. |
| RoboRacer/F1TENTH reactive lecture | `https://f1tenth-coursekit.readthedocs.io/en/latest/lectures/ModuleB/lecture05.html` | Confirms related reactive patterns: Follow-the-Gap, Disparity Extender, Bug, artificial potential fields. |
| Braitenberg vehicles robotics review | `https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2020.565963/full` | Confirms sparse sensor-to-actuator coupling can create obstacle-avoidance behavior without a full internal map. |

## Local Outputs

```text
References/research/sparse_reactive_obstacle_avoidance_20260710/source_notes.md
```

## Boundaries

- Do not copy source code from external projects into the official model.
- Do not edit official vehicle, road, sensor, scoring, example, or material files.
- Do not treat scan/grid planners as directly implementable under the current four-distance controller boundary.
- Use these notes to screen future unified controller mechanisms before runtime.
