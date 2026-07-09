# Reactive Four-Sensor UGV Notes

timestamp: 2026-07-10 CST

## Web Sources Checked

| Source | URL | Relevance |
|---|---|---|
| Reactive Obstacle-Avoidance Systems for Wheeled Mobile Robots | https://www.mdpi.com/2076-3417/11/14/6468 | Confirms reactive systems map sensor readings directly to avoidance decisions; useful for keeping UGV controller simple and low-latency. |
| Wall Follower Autonomous Robot Development Applying Fuzzy Control | https://www.scirp.org/journal/paperinformation?paperid=27701 | Uses distance sensors for wall following; supports treating side distance as a control signal rather than only a collision trigger. |
| Obstacle Avoidance with Ultrasonic Sensors | https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated1/borenstein_obstacle_avoidance.pdf | Classic ultrasonic obstacle-avoidance reference; useful for range-sensor failure awareness and conservative filtering ideas. |
| Wall Following and Obstacle Avoidance project note | https://hackaday.io/project/28646-wall-following-and-obstacle-avoidance | Practical three/five-sensor wall-following pattern; useful as a lightweight implementation analogy, not as source code. |

## Project Takeaways

1. With only front/rear/left/right distances, full VFH/DWA/gap navigation is
   over-parameterized for the official controller boundary.
2. v58 confirmed that stronger side-gap bypass can trade road collisions for
   additional obstacle collisions. Do not keep scanning stronger initial
   bypass steering.
3. A more plausible next mechanism is side-distance centering or wall/edge
   following: when obstacle avoidance is active and a side distance is small,
   bias steering away from the nearer side without flipping into a large
   obstacle-seeking side arc.
4. Any side-distance centering must be bounded and must not override the
   current v48 opposing-steer guard without evidence.

## Non-Reuse

No external code was copied. These notes are design guidance only.
