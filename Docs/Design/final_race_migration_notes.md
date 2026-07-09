# Final Race / Physical UGV Migration Notes

> Keep initial-race simulation decisions compatible with later generated-code and physical UGV deployment. This file is not a claim that physical testing has happened.

Status: initial migration constraints plus deployable-algorithm research and v48/post-v67 attribution, 2026-07-10 CST.

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
References/research/robust_physical_ugv_navigation_20260709/
References/research/deployable_ugv_avoidance_algorithms_20260709/
```

Use them as patterns only:

| Reference Pattern | Useful Part | Current Adaptation |
|---|---|---|
| Follow-the-Gap | steer toward free gap and keep safety bubble | choose larger of left/right clearance under front risk |
| Dynamic Window Approach | feasible command limits and short-horizon obstacle cost | speed/steer saturation, dwell, and speed-turn coupling |
| Potential Field | bounded repulsion from obstacles | linear side/front repulsion with saturation |
| Pure Pursuit | smooth recovery to path-following | release avoidance gradually back to official planner |
| Regulated Pure Pursuit | reduce speed by curvature, proximity, and collision risk | lower speed cap under high steering demand or front risk |
| DWA / dynamic window | enforce feasible speed/steer windows and short-horizon obstacle cost | preserve saturation, avoid abrupt sign flips, and penalize speed under risk |
| Stanley / Pure Pursuit | smooth path tracking with steering saturation | smooth return-to-cruise after avoidance; do not replace official path authority |
| TEB local planner | respect obstacle separation and kinodynamic constraints | keep avoidance commands within physical limits; do not direct-import the planner |

The current controller boundary is too narrow for direct TEB/DWA/Nav2/F1TENTH
imports. Treat these projects as algorithm references. The deployable pattern is
a bounded reactive safety layer with explicit speed caps, steering saturation,
hysteresis/dwell, and parameter ranges that a physical UGV team can tune.

## 5. Simulation-To-Real Algorithm Filter

Before accepting a new tuning or algorithm change, check it against this filter:

1. Can the rule be explained using the four official distance inputs and two controller outputs?
2. Are speed and steering bounded under near-zero distance readings?
3. Does the rule slow down when collision risk, steering demand, or implied curvature increases?
4. Is release from avoidance protected by dwell or hysteresis rather than a single noisy sample?
5. Can the parameter be retuned on a physical car without knowing the hidden race track internals?

Reject a change that only improves one simulation run by exploiting a fragile
track-specific constant, discontinuous sign flip, or unbounded gain. If a large
open-source stack looks promising, first save a research note and map the idea
to the current interface; do not import the stack into the official model tree.

## 6. Evidence Needed Before Real-Car Claims

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

## 7. Current Practical Next Step

The earlier M6 direct-official-track API blocker is historical evidence. Current
repeatable controller evaluation uses generated `UGV.Test.Saidao*Eval`
wrappers, which preserve the official track geometry while adding the
controller wiring needed by the API evaluation route.

Current controller candidate:

```text
controller_v48_opposing_steer_guard
Results/metrics/four_track_candidate_review_v48_opposing_steer_guard_20260710.md
```

Important caveat:

```text
Track2/3/4 v48 metrics have readable score variables after simulate_failed /
exit_state=2. They are review evidence, not final clean runtime proof.
```

Post-v67 decision:

```text
Results/metrics/post_v67_v68_attribution_decision_20260710.md
```

The current four-distance interface has shown diminishing returns for blind
controller tuning. v67 made Track3 runtime clean by changing a diagnostic input
route, but did not improve Track3 score. The direct allocation-speed
arbitration route was already tested as v51 and rejected due to early-stop
artifact. Therefore the next safe work is:

1. keep v48 as the current review-ready controller candidate unless stronger
   evidence supersedes it;
2. refresh report/readiness artifacts so the deliverable is honest about
   v48 strengths, v67 limitations, and terminal-state caveats;
3. preserve the no-edit boundary for official vehicle, road, sensor, scoring,
   example, and `saidao` source files;
4. apply the deployability filter before accepting any new tuning: bounded
   commands, speed reduction under risk, dwell/hysteresis, and parameter ranges
   that can be retuned on the physical UGV;
5. only reopen source changes when research or source attribution identifies a
   genuinely different four-scalar reactive mechanism, not another
   threshold/gain/dwell scan.

## 8. Current Static Deployability Gate

The current controller has an automated source-only deployability check:

```powershell
python Scripts\quality\check_controller_deployability.py
```

Latest evidence:

```text
Results/evidence/controller_deployability_static_check_v48_opposing_steer_guard_20260710.md
Results/evidence/controller_deployability_static_check_v48_reconfirmed_after_v67_20260710.md
```

Current result: v48 and the post-v67 reconfirmed source pass the static
deployability checker.

Meaning: the source-only deployability gate no longer detects the earlier
reciprocal-distance spike risk. This is not a physical UGV success claim and
does not prove generated code, real-car tuning, or official final submission
readiness. It only clears the current static source-level high/medium risk gate
for the v48 controller candidate.
