# Physical UGV Obstacle-Avoidance Source Notes

## Follow-the-Gap / F1TENTH

Core idea: find free space from range data, choose a goal inside the largest safe gap, and publish speed/steering commands that drive into that gap.

Transfer to this project:

- With only `left_dist` and `right_dist`, the "largest gap" is approximated by the side with larger clearance.
- The closest-point safety bubble becomes the front/side risk threshold plus a short dwell after risk is detected.
- A real vehicle may need a lower speed during front-risk turns even if the simulation score rewards aggressive motion.

Risk if copied literally:

- Full Follow-the-Gap assumes a LiDAR scan array. The official controller does not expose that interface, so direct import would be a scope mismatch.

## Dynamic Window Approach

Core idea: sample feasible velocity/yaw-rate commands within dynamic limits, predict short trajectories, and score them by goal, speed, and obstacle cost.

Transfer to this project:

- Treat `speed` and `steer` outputs as bounded, physical increments.
- Avoid discontinuous jumps between cruise, avoidance, and recovery.
- Add rate-like or dwell-like behavior where Modelica/Sysblock constraints make explicit rate limiting awkward.
- Keep front-risk speed reduction coupled to steering demand: sharper avoidance should generally mean slower forward motion.

Risk if copied literally:

- DWA needs pose, heading, obstacle coordinates, and a motion model. The current official controller boundary has only distance inputs and increment outputs.

## Potential Field Planning

Core idea: attract toward goal and repel from obstacles.

Transfer to this project:

- The current controller is already a simplified repulsive field: front risk reduces speed and side imbalance drives steering.
- Keep repulsion bounded. Reciprocal-distance gains can explode near zero and are harder to deploy safely on a physical vehicle.

Risk if copied literally:

- Pure potential fields can oscillate or get stuck near local minima. The project should prefer explicit states, thresholds, dwell, and saturation.

## Pure Pursuit

Core idea: follow a geometric look-ahead target smoothly instead of directly chasing instantaneous position error.

Transfer to this project:

- The official path planner remains the path-following authority. The obstacle controller should not override it in cruise.
- Avoidance release should be gradual enough that the path planner can recover the road centerline after an obstacle maneuver.

Risk if copied literally:

- The controller boundary does not expose waypoints or vehicle pose, so pure pursuit belongs to the official planner layer, not this obstacle-increment layer.

## Recommended Next Controller Improvements

Only attempt these after resolving or bypassing the M6 official-track simulation entry blocker with honest evidence:

1. Preserve v5 as the current candidate: 2 s front-risk dwell is useful, 3 s is too long.
2. Add explicit exit hysteresis for front risk if Modelica syntax and runtime behavior stay stable.
3. Couple speed reduction to steering magnitude, so stronger turns are slower.
4. Export first-collision windows with `front_dist`, `left_dist`, `right_dist`, `speed`, `steer`, `cR`, and `cO` before changing more gains.
5. Prefer parameters that can be explained and tuned on a physical car: front-safe distance, side-safe distance, steering gain, speed cap, dwell.

## Current Notification Caveat

An SMTP send can succeed while the user still does not see the email because of recipient mismatch, spam filtering, QQ delivery rules, or mailbox state. Treat `ok=true` as send evidence, not human-read evidence. Keep terminal notices in project evidence paths as well as sending email.
