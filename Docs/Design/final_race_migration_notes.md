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

## 9. Current v48 Parameter Table

This table is the current transfer baseline. If final-race or physical-UGV
materials arrive, start from these values and retune in the order below instead
of restarting from rejected candidates.

| Area | Parameter / rule | Current value | Source / evidence | Physical-transfer note |
|---|---|---:|---|---|
| Obstacle trigger | front distance trigger | `df <= mindis`, `mindis = 1.0` | `ObsAvoidController_Sysblock2.mo` | Retune only after checking sensor scale and stopping distance. |
| Obstacle trigger | side distance trigger | `dl <= 0.45 or dr <= 0.45` | v13/v48 accepted chain | Useful for side grazing; do not scan blindly without collision-window evidence. |
| Longitudinal command | cruise speed | `1.0` | controller cruise state | Keep as nominal low-speed baseline for simulation and physical safety. |
| Longitudinal command | avoid speed | `-1.0` | controller avoid state | Reverse/brake command is bounded; stronger reverse was already risky in rejected routes. |
| Longitudinal dwell | avoid release dwell | `2 s` | `transition(avoid, cruise, after(2,sec))` | Longer dwell regressed v31; do not increase without new evidence. |
| Lateral command | initial avoid steer | `0.6` | controller avoid-lateral initial state | Magnitude scans were mostly rejected; treat as baseline, not a free tuning knob. |
| Lateral command | side-distance steer | `min(0.8, 2 * abs(dl - dr))` | controller turn states | Bounded linear rule; avoids the earlier reciprocal-distance spike risk. |
| Lateral dwell | avoid-lateral initialization | `2 s` | `transition(ini_state, state, after(2,sec))` | Shorter dwell regressed prior attempts; keep unless new timing evidence appears. |
| Path tracking | path planner instance | `lookahead_base = 2`, `lookahead_gain = 0.1` in official/eval wrappers | wrapper/source inspection | Do not edit official wrappers for scoring; adapt only if final-race interface changes. |
| Path speed | curvature speed trigger | `abs(steering_angle) > 0.35` | v45/v48 accepted chain | Accepted because it improved wrapper score; further threshold scans were exhausted. |
| Path speed | curvature speed cap | `0.75` | v45/v48 accepted chain | Physical retune can lower only with runtime stability evidence. |
| Allocation | obstacle influence factor | wrapper uses `factor_oa = 0.5` | wrapper/source inspection | Changing class default alone is a no-op because wrappers instantiate this value. |
| Allocation | path influence factor | wrapper uses `factor_pp = 1.0` | wrapper/source inspection | Full path suppression regressed v53. |
| Allocation | opposing-steer guard | `0.5 * path steer` only when reverse OA steer opposes path steer | v48 review | Current best unified mechanism; keep unless superseded by four-track evidence. |
| Filtering | OA speed / steer first-order filters | `T = 1` | `ControlAllocate/package.mo` | Direct filter-time scans regressed or produced unstable evidence. |

## 10. Exhausted Mechanism Families

The following routes have enough local evidence to avoid repeating them under
new names:

| Mechanism family | Local evidence | Decision |
|---|---|---|
| Blind side-threshold, initial-steer, dwell, and reverse-speed scans | v14-v23, v31-v35 | Do not retry without a new collision-window reason. |
| Steering filter and direct early steer feedforward | v24, v60, v63 | Not a justified next route; produced no comparable improvement. |
| Path-speed attenuation, straight brake arbitration, and brake-turn coupling | v49, v51, v52 | Rejected due to early stops or unchanged Track3 score. |
| Complete path-steer neutralization or path-authority scalar scans | v53, v54 | Regressed or shortened runs; v48 half attenuation is safer. |
| Low-speed lookahead floor, speed-filter-only acceleration, simple front-threshold changes | v55-v57 | Did not improve Track3 score and shortened runs. |
| Stronger initial side-gap bypass or close-side initial direction | v58, v59, v62, v66 | Produced obstacle collisions or non-comparable early stops. |
| Front-clear side reentry and emergency-front reverse hold | v64, v65 | Did not remove current score-loss pattern. |
| Nearest-distance wrapper input change | v67 | Cleaned runtime state but did not improve Track3 score; not an accepted score route. |
| Lateral left/right hysteresis | v69 offline screening | Saved signals show zero `chart.steer` sign flips; no source edit justified. |

If a future idea resembles one of these families, first write a short
attribution note showing what is materially different before changing source.

## 11. Final-Race / Physical Retuning Order

When final-race material or physical UGV access becomes available, use this
order:

1. Confirm sensor units and saturation: front/rear/left/right distance scale,
   sign, update rate, dropout behavior, and minimum reliable value.
2. Confirm actuator units and limits: commanded speed unit, steer unit/range,
   rate limit, and emergency stop behavior.
3. Re-run the static deployability checker and record generated-code warnings
   before physical tests.
4. Start with v48 baseline parameters and reduce only speed-related risk first:
   nominal speed, curvature speed cap, and avoid release timing.
5. Tune distance thresholds only after a physical or final-race diagnostic
   window shows which sensor boundary is late.
6. Tune steering authority last; it is the most likely to create oscillation or
   road-edge regressions under this four-distance interface.
7. Preserve one unified controller across all tracks. Do not create per-track
   constants or edit official vehicle, road, sensor, scoring, example, or
   `saidao` files.

Review checkpoint before claiming transfer readiness:

```text
generated-code artifact exists
parameter table updated with physical units/ranges
four official tracks or final-race equivalents have saved evidence
known caveats are still visible
final submission / physical success is explicitly approved or separately proven
```
