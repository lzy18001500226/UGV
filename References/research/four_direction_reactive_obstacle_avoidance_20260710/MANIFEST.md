# Four-Direction Reactive Obstacle Avoidance Research Manifest

timestamp: 2026-07-10 CST
purpose: choose the next unified UGV obstacle-avoidance mechanism after v67 rejected the nearest-distance input route

## Scope

This research pack focuses on algorithms that can plausibly be mapped to the
current official controller boundary:

```text
front_dist, rear_dist, left_dist, right_dist -> speed, steer
```

It is not a plan to import a full LiDAR, SLAM, ROS, DWA, TEB, or learning stack.

## Sources

| Source | URL | Use |
|---|---|---|
| RoboRacer/F1TENTH Follow the Gap lab | https://f1tenth-coursekit.readthedocs.io/en/latest/assignments/labs/lab4.html | Reactive obstacle-avoidance workflow: preprocess ranges, remove unsafe bubble, choose gap, steer to best point. |
| RoboRacer lecture on Follow the Gap | https://f1tenth-coursekit.readthedocs.io/en/latest/lectures/ModuleB/lecture05.html | Places FTG, Disparity Extender, Bug, and potential-field methods in the reactive-navigation family. |
| F1TENTH survey, arXiv 2402.18558 | https://arxiv.org/html/2402.18558v1 | Confirms FTG/Disparity Extender as simple mapless autonomous-racing approaches. |
| RoboRacer platform survey, arXiv 2506.15899 | https://arxiv.org/html/2506.15899v1 | Notes FTG is computationally efficient and suitable for real-time navigation. |
| Disparity Extender explanation | https://www.nathanotterness.com/2019/04/the-disparity-extender-algorithm-and.html | Useful idea: enlarge/inflate obstacles around sharp range disparities before choosing the path. |
| CMU Bug Algorithms lecture | https://www.cs.cmu.edu/~motionplanning/lecture/Chap2-Bug-Alg_howie.pdf | Bug-style fallback: go toward goal, follow obstacle boundary, leave when safe. |
| Improved Bug algorithm paper | https://journals.sagepub.com/doi/10.1177/17298806231169186 | Reminder that pure Bug/wall-follow methods can degrade in real environments with odometry drift. |
| Wall-following PID ultrasonic example | https://www.researchgate.net/publication/351315086_Wall_Following_Control_System_with_PID_Control_and_Ultrasonic_Sensor_for_KRAI_2018_Robot | Physical small-robot pattern: PID wall following with ultrasonic distance feedback. |
| Wall-follower open-source example | https://github.com/Rajneesh04/Wall-follower | Simple front + side sensor wall-following/obstacle-avoidance implementation reference. |

## Local Output

```text
References/research/four_direction_reactive_obstacle_avoidance_20260710/source_notes.md
```

## Immediate UGV Conclusion

The next candidate should not try to emulate full FTG from only four scalar
sensors. Instead, use the transferable part:

```text
risk classification
  -> safety bubble / center-of-gap proxy
  -> bounded speed tied to risk and steering demand
  -> hysteresis so obstacle mode does not reset the lateral decision every 2 s
```

The first design target should be a deployable four-direction-only safety
overlay, not another wrapper input change or per-track behavior.
