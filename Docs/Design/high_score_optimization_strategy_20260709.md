# High-Score Optimization Strategy

> Research-driven strategy for improving the UGV obstacle-avoidance score after
> v14-v29 scalar/controller attempts were rejected.

Status: active strategy, 2026-07-09 CST.

## 1. Current Baseline

Current accepted controller:

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

v13 records `36.4` total wrapper score in the current four-track evaluation
set. Treat this as local wrapper evidence, not a final official `80`-point
competition claim. The official score formula must be confirmed from official
materials before final reporting.

## 2. Rejected Attempt Lessons

Do not continue v14-v29 style blind scalar scanning.

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

Route A was tested as v29 and rejected because it did not improve Track1 or
Track4 against v13. The remaining routes are hypotheses only; do not implement
one until a fresh failure-window diagnosis explains why it should help.

| Route | Mechanism | Edit scope | First gate |
|---|---|---|---|
| A | Side-danger speed regulation: when either side clearance is extremely low, reduce avoid-mode speed further while keeping v13 trigger semantics. | `ObsAvoidController_Sysblock2.mo` only. | Tested as v29 and rejected. |
| B | Side-danger steering floor: near a wall, require a minimum steer-away magnitude instead of only proportional `2 * abs(dl - dr)`. | `ObsAvoidController_Sysblock2.mo` only. | Track1/Track4, but higher risk of planner fighting. |
| C | Two-bin gap state with release hysteresis: keep avoid lateral behavior until side clearances recover above a release threshold. | `ObsAvoidController_Sysblock2.mo` only. | Higher Sysblock state-machine risk; defer until A/B evidence. |

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

Non-goals:

- Do not create a submission package.
- Do not edit official track, vehicle, road, sensor, scoring, or example code.
- Do not claim physical UGV success from simulation score.
- Do not accept a readable `P=10` when `T` is early/non-comparable.
