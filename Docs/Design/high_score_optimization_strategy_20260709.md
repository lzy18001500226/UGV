# High-Score Optimization Strategy

> Research-driven strategy for improving the UGV obstacle-avoidance score after
> v14-v41 scalar/controller/allocation/timing attempts were rejected.

Status: active strategy after v45 review-ready improvement, 2026-07-10 CST.

## 1. Current Baseline

Previous accepted controller:

```text
v13 side-trigger 0.45
transition(cruise, avoid, df <= mindis or dl <= 0.45 or dr <= 0.45, reset = false)
```

Current review evidence:

```text
Results/metrics/four_track_summary_v13_side_trigger045_20260709_1535.md
```

Wrapper score evidence:

| Track | T/s | cR | cO | P |
|---|---:|---:|---:|---:|
| Saidao1Eval | 120.0 | 3 | 0 | 8.8 |
| Saidao2Eval | 91.9 | 1 | 0 | 9.6 |
| Saidao3Eval | 120.0 | 1 | 1 | 9.2 |
| Saidao4Eval | 113.1 | 3 | 0 | 8.8 |

v13 recorded `36.4` total wrapper score in the current four-track evaluation
set. v45 is now the review-ready best candidate with `36.8` total wrapper
score. Treat both as local wrapper evidence, not final official `80`-point
competition claims. The official score formula must be confirmed from official
materials before final reporting.

Current review-ready best candidate:

```text
v45 curvature-speed regulation scaled
PathPlanner cap: abs(steering_angle) > 0.35 -> target_v <= 0.75
Results/metrics/four_track_candidate_review_v45_curvature_speed_regulation_scaled_20260710_0045.md
```

## 2. Rejected Attempt Lessons

Do not continue v14-v41 style blind scalar/timing scanning.

Rejected route summary:

| Route | Lesson |
|---|---|
| Fixed initial steer changes | Worsened Track1/Track3 or failed to improve Track4. |
| Front threshold widening | Did not solve the relevant collision windows. |
| Side-clearance direction tricks | Removed some road collisions but increased obstacle collisions. |
| Global speed changes | Produced early-stop or non-comparable runs. |
| ControlAllocate defaults | Can be a no-op because generated wrappers instantiate `ctrlAlloc(factor_oa=0.5)`. |
| Speed-channel gain changes | Can produce high-looking but non-comparable early-stop scores. |
| Side-danger speed regulation | Passed the static gate but did not improve Track1/Track4 against v13. |
| Steering floor / longer avoid dwell | Steering floor did not improve Track1/Track4; longer avoid release regressed Track1 badly. |

Accepted operating rule:

```text
new candidate = failure-window diagnosis -> mechanism hypothesis -> static gate -> target-track run -> regression
```

## 3. Failure Attribution

Key saved analyses:

```text
Results/metrics/collision_window_analysis_v13_track1_track3_20260709_1705.md
Results/metrics/signal_window_summary_v13_track1_track3_20260709_1705.md
Results/metrics/collision_window_analysis_v13_track4_20260709_1910.md
Results/metrics/signal_window_summary_v13_track4_20260709_1910.md
Results/metrics/ctrlalloc_contribution_analysis_v13_track1_track3_track4_20260709_1915.md
```

Observed pattern:

| Track | Main failure pattern | Implication |
|---|---|---|
| Track1 | Road contacts with `flag=1`, side distance often very small. | Existing avoid mode recognizes risk but does not recover enough lateral margin. |
| Track3 | One early obstacle contact plus one road contact. | Needs early front/side safety behavior without destabilizing path following. |
| Track4 | Road contacts with `flag=1`, sometimes high steering near very small side distance. | More steering alone is not reliable; reduce risk exposure and avoid abrupt planner fighting. |

Therefore the next useful candidate should not be another isolated scalar tweak.
It should introduce a small safety mechanism that is explainable from the
signals and deployable on a physical UGV.

## 4. Research Mapping

Local reference packs:

```text
References/research/physical_ugv_obstacle_avoidance_20260708/
References/research/robust_physical_ugv_navigation_20260709/
References/research/deployable_ugv_avoidance_algorithms_20260709/
```

Reusable ideas under the current four-distance controller boundary:

| External pattern | Direct stack reuse? | Usable mechanism here |
|---|---|---|
| Follow-the-Gap / F1TENTH | No; full scan array is unavailable. | Treat left/right as a two-bin gap proxy; steer toward larger clearance. |
| Regulated Pure Pursuit | No; no pose/path/costmap inside this controller. | Reduce speed when obstacle risk or steering demand is high. |
| DWA | No; no pose, velocity, obstacle coordinates, or motion model. | Keep commands bounded; avoid abrupt sign/large-speed changes. |
| TEB | No; optimizer/costmap stack is out of scope. | Use physical feasibility as an acceptance filter. |

The controller must remain a reactive safety overlay. It must not pretend to be
a full local planner unless the official interface changes.

## 5. Candidate Mechanism Routes

Routes A, B, and the long-release variant of C were tested and rejected. The
remaining routes are hypotheses only; do not implement one until a fresh
failure-window diagnosis explains why it should help.

| Route | Mechanism | Edit scope | First gate |
|---|---|---|---|
| A | Side-danger speed regulation: when either side clearance is extremely low, reduce avoid-mode speed further while keeping v13 trigger semantics. | `ObsAvoidController_Sysblock2.mo` only. | Tested as v29 and rejected. |
| B | Side-danger steering floor: near a wall, require a minimum steer-away magnitude instead of only proportional `2 * abs(dl - dr)`. | `ObsAvoidController_Sysblock2.mo` only. | Tested as v30 and rejected. |
| C | Longer avoid release hysteresis: keep avoid mode active longer after trigger. | `ObsAvoidController_Sysblock2.mo` only. | Tested as v31 and rejected; avoid longer reverse dwell. |
| D | Planner-fighting mitigation: inspect whether path-planner steer dominates near road contacts and find a bounded safety overlay that does not edit official path/road/scoring files. | Prefer `ObsAvoidController_Sysblock2.mo`; touch allocation/planner only with explicit design reason and source gate. | Needs a fresh source-boundary decision before implementation. |

Candidate acceptance:

1. Static deployability checker has `high=0`.
2. Target weak track does not early-stop with non-comparable `T`.
3. Target weak track improves `P` or collision count against v13.
4. Regression on Track1/Track3/Track4 does not reduce total wrapper evidence.
5. If it fails, restore v13 and record the reason.

## 6. Completed v29 Check

Completed candidate:

```text
candidate: v29_side_danger_speed_regulation
starting point: v13 source semantics
primary change: avoid longitudinal speed becomes slightly more conservative only
                when min(dl, dr) is in the severe side-danger band.
```

Result:

```text
Results/metrics/track1_track4_candidate_review_v29_side_danger_speed_20260709_2130.md
```

v29 passed the source-level deployability checker and completed Track1/Track4
target runs, but both target tracks stayed at `P=8.8`, `cR=3`, `cO=0`, matching
v13 instead of improving it. It is rejected, and the source has been restored to
v13 semantics.

## 7. Next Execution Plan

Before another controller edit:

1. Re-read the saved collision-window and signal-window evidence.
2. Pick one mechanism that explains a specific failure window.
3. Run the source deployability checker before runtime.
4. Run the target weak track first.
5. Run regression on Track1/Track3/Track4 only if the target track improves.

## 8. Completed v30 / v31 Checks

v30 side-danger steering floor:

```text
Docs/Design/unified_obstacle_avoidance_v30_plan_20260709.md
Results/metrics/track1_track4_candidate_review_v30_side_danger_steering_floor_20260709_2116.md
```

v30 passed the static source gate and ran Track1/Track4, but both target
tracks stayed at `P=8.8`, `cR=3`, `cO=0`, matching v13 instead of improving it.
It is rejected.

v31 avoid-release 3s:

```text
Results/metrics/v13_pre_collision_control_attribution_20260709_2140.md
Docs/Design/unified_obstacle_avoidance_v31_plan_20260709.md
Results/metrics/track1_candidate_review_v31_avoid_release3s_20260709_2200.md
```

v31 extended avoid release from 2 seconds to 3 seconds. It passed the static
gate but regressed Track1 to `P=2.0`, `cR=17`, `cO=3`, so it is rejected and
the longer reverse/avoid dwell route should not be continued without a new
mechanism reason.

Non-goals:

- Do not create a submission package.
- Do not edit official track, vehicle, road, sensor, scoring, or example code.
- Do not claim physical UGV success from simulation score.
- Do not accept a readable `P=10` when `T` is early/non-comparable.

## 9. Completed v32-v35 Front-Open Braking Check

Evidence:

```text
Docs/Design/unified_obstacle_avoidance_v32_plan_20260709.md
Docs/Design/unified_obstacle_avoidance_v33_plan_20260709.md
Docs/Design/unified_obstacle_avoidance_v34_plan_20260709.md
Docs/Design/unified_obstacle_avoidance_v35_plan_20260709.md
Results/metrics/track3_candidate_review_v32_v35_front_open_brake_20260709_2230.md
Results/evidence/controller_deployability_static_check_v13_restored_after_v35_20260709_2227.md
```

Result:

```text
v32: rejected, Sysblock state-machine action rejected inline if expression.
v33: rejected, explicit front_open_brake state did not trigger.
v34: rejected, added transition still did not trigger stronger braking.
v35: rejected, normal algorithm if statement triggered speed=-1.6 but Track3
     stopped earlier at T=106.35 with no score improvement.
```

Lesson:

```text
Do not keep increasing reverse braking, avoid dwell, or open-front braking
without a new mechanism reason. The next candidate should address interaction
between obstacle avoidance and path-planner steering, or use fresh failure
window evidence to justify a different mechanism.
```

## 10. Completed v36-v39 Steering-Authority Checks

Evidence:

```text
Docs/Design/unified_obstacle_avoidance_v36_plan_20260709.md
Docs/Design/unified_obstacle_avoidance_v37_plan_20260709.md
Docs/Design/unified_obstacle_avoidance_v38_plan_20260709.md
Docs/Design/unified_obstacle_avoidance_v39_plan_20260709.md
Results/metrics/four_track_candidate_review_v36_final_steer_limiter_20260709_2300.md
Results/metrics/track4_track3_candidate_review_v37_final_steer_limiter_wide_20260709_2330.md
Results/metrics/track4_track3_candidate_review_v38_negative_steer_guard_20260709_2315.md
Results/metrics/track4_candidate_review_v39_planner_steer_attenuation_20260709_2330.md
Results/evidence/controller_deployability_static_check_v13_restored_after_v39_20260709_2330.md
```

Result:

```text
v36: rejected, symmetric final steering limiter improved Track4 but reduced total score.
v37: rejected, wider symmetric limiter still regressed Track3.
v38: rejected, one-sided negative guard improved Track4 to P=9.2 but regressed Track3 to P=7.2.
v39: rejected, simple planner-steering attenuation regressed Track4 to P=7.6.
```

Lesson:

```text
Do not continue final-steer clipping or simple planner-steering suppression as
next routes. The failure pattern is not simply excessive final steering; v39
shows that removing path authority during side risk can create earlier road and
obstacle contacts. The next candidate should stay inside the obstacle
controller boundary and change risk timing or lateral-mode behavior using a
fresh failure-window hypothesis.
```
## 11. Long-Task Continuation Rule

Rejected candidates do not end the long task. The repeatable loop is:

```text
failure evidence
  -> mechanism hypothesis
  -> design note and source-boundary decision
  -> static gate
  -> target-track runtime evidence
  -> accept, reject, or restore v13
  -> sparse email notice
  -> continue with the next evidence-backed mechanism or targeted research
```

## 12. Completed v40-v41 Timing Checks

Evidence:

```text
Docs/Design/unified_obstacle_avoidance_v40_plan_20260709.md
Docs/Design/unified_obstacle_avoidance_v41_plan_20260709.md
Results/metrics/track4_candidate_review_v40_side_safety_bubble_20260709_2350.md
Results/metrics/track4_candidate_review_v41_guarded_release_20260710_0007.md
Results/evidence/controller_deployability_static_check_v13_restored_after_v41_20260710_0007.md
```

Result:

```text
v40: rejected, side-trigger 0.45 -> 0.55 produced identical Track4 P=8.8.
v41: rejected, guarded avoid release regressed Track4 to P=8.0 with cO=2.
```

Lesson:

```text
Do not continue side-trigger threshold scanning or longer/guarded avoid-release
routes as the next mechanism. v40 shows earlier side activation has no effect
on the saved Track4 failure trajectory; v41 shows keeping avoid active while
risk remains can add obstacle collisions. The next route should use a different
mechanism, preferably trajectory/path behavior or a more informed algorithmic
reference, before editing the controller again.
```

## 13. Completed v42-v45 Path-Authority / Speed Checks

Evidence:

```text
Docs/Design/unified_obstacle_avoidance_v42_plan_20260710.md
Docs/Design/unified_obstacle_avoidance_v43_plan_20260710.md
Docs/Design/unified_obstacle_avoidance_v44_plan_20260710.md
Docs/Design/unified_obstacle_avoidance_v45_plan_20260710.md
References/research/curvature_speed_regulation_20260710/MANIFEST.md
Results/metrics/track1_candidate_review_v42_conservative_open_side_20260710_0018.md
Results/metrics/track1_candidate_review_v43_decoupled_side_guard_20260710_0022.md
Results/metrics/collision_window_analysis_v13_v44_track4_20260710_0032.md
Results/metrics/four_track_candidate_review_v45_curvature_speed_regulation_scaled_20260710_0045.md
```

Result:

```text
v42: rejected, open-side steering regressed Track1.
v43: rejected, side-only longitudinal/lateral decoupling regressed Track1.
v44: rejected as no-op, speed cap used the wrong scale.
v45: accepted as a superseded review-ready best, total wrapper score 36.8 vs v13 36.4.
v48: accepted as current review-ready best with runtime caveat, total wrapper score 37.2 vs v45 36.8.
```

Lesson:

```text
Path-authority interaction is useful only when it preserves steering authority
and uses the actual runtime scale. Simple steering suppression regresses, but a
bounded high-curvature speed cap improves Track4 without reducing Track1/2/3.
Continue from v48 and evaluate future mechanisms with one unified algorithm
across all four tracks.
```
