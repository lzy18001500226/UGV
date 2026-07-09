# UGV Initial Race Simulation Report Draft - v48 Metrics Refresh

Status: v48 opposing-steer guard review draft with post-v67 attribution, not final submission material.
Date: 2026-07-10

## 1. 赛题目标与模型说明

本项目面向 2026 智能无人应用挑战赛算法赛道的无人车避障任务。当前工作基于官方 UGV MWORKS/Sysplorer 模型，在不修改官方车辆、道路、传感器、计分或赛道模型的前提下，实现并验证一套统一避障控制算法。

当前工程目标是完成避障控制器、四条官方赛道仿真、时间/碰撞/得分证据和仿真报告。最终比赛提交包和提交邮件仍需要用户明确批准，本报告不是最终提交声明。

## 2. 无人车系统结构与控制接口

正常实现边界：

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
Models/UGV/Control/ControlAllocate/package.mo
Models/UGV/Control/PathPlanning/PathPlanner.mo
```

控制器输入为 `front_dist`、`rear_dist`、`left_dist`、`right_dist`，输出为 `speed` 和 `steer`。官方路径规划和控制分配仍是主线，避障控制器与控制分配改动只作为安全叠加层，不替代官方车辆、道路、传感器、计分或赛道模型。

Source grounding evidence:

```text
Results/evidence/static_model_grounding_20260708_210142.md
Docs/Index/model_index.md
```

## 3. 避障控制算法原理

当前最好候选为 `controller_v48_opposing_steer_guard`。

核心思路：

1. 保留 v13 的侧向触发阈值，让侧边接近障碍时也进入避障。
2. 保留 v45 的曲率速度限制，让大转角路径跟踪时降低目标速度。
3. 在控制分配中增加 v48 opposing-steer guard：当避障正在要求倒车/制动，且避障转向与路径转向相互抵消时，减弱路径转向贡献，避免路径规划与避障转向直接打架。
4. 所有机制均为赛道无关规则，不按赛道名、wrapper 名、运行编号或计分变量分支。

v48 的核心控制分配逻辑：

```modelica
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0 then
  0.5 * unitDelay1.y
else
  unitDelay1.y;
```

Design and diagnostic evidence:

```text
Docs/Design/避障算法设计.md
Docs/Design/unified_obstacle_avoidance_v48_plan_20260710.md
Docs/Design/unified_obstacle_avoidance_v68_planning_note_20260710.md
Docs/Design/final_race_migration_notes.md
Results/metrics/four_track_candidate_review_v48_opposing_steer_guard_20260710.md
Results/metrics/signal_window_summary_v48_path_ctrl_20260710.md
Results/metrics/post_v67_v68_attribution_decision_20260710.md
```

## 4. 参数设置与调参依据

Current v48 transfer baseline:

| Parameter group | Current value | Transfer / tuning note |
|---|---|---|
| Front trigger | `df <= mindis`, `mindis = 1.0` | Retune only after checking final-race or physical sensor scale and stopping distance. |
| Side trigger | `dl <= 0.45 or dr <= 0.45` | Accepted through v13/v48 evidence; do not scan blindly. |
| Cruise speed | `1.0` | Nominal low-speed baseline. |
| Avoid speed | `-1.0` | Bounded reverse/brake command; stronger reverse routes were risky. |
| Avoid release dwell | `2 s` | Longer dwell regressed v31. |
| Initial avoid steer | `0.6` | Keep as baseline; magnitude scans were mostly rejected. |
| Side-distance steer | `min(0.8, 2 * abs(dl - dr))` | Bounded linear rule replacing reciprocal spike risk. |
| Avoid-lateral initialization | `2 s` | Shorter dwell regressed prior attempts. |
| Curvature speed cap | `abs(steering_angle) > 0.35 -> target_v <= 0.75` | v45/v48 accepted mechanism; further threshold scans were exhausted. |
| Wrapper allocation | `factor_pp = 1.0`, `factor_oa = 0.5` | Wrapper instances override class defaults; default-only edits are no-ops. |
| Opposing-steer guard | `0.5 * path steer` when reverse obstacle steering opposes path steering | v48 current best unified mechanism. |

The complete physical-transfer table and retuning order are maintained in:

```text
Docs/Design/final_race_migration_notes.md
```

当前调参路径：

| Candidate | Key change | Evidence | Result summary |
|---|---|---|---|
| v13 | side trigger threshold raised to 0.45 | `Results/metrics/four_track_summary_v13_side_trigger045_20260709_1535.md` | total wrapper score 36.4 |
| v45 | path curvature speed cap, `abs(steering_angle) > 0.35 -> target_v <= 0.75` | `Results/metrics/four_track_candidate_review_v45_curvature_speed_regulation_scaled_20260710_0045.md` | total wrapper score 36.8 |
| v48 | opposing-steer guard in `ControlAllocate` | `Results/metrics/four_track_candidate_review_v48_opposing_steer_guard_20260710.md` | total wrapper score 37.2 |

Rejected follow-ups v49-v67 show why v48 remains current best and why the next
step is not blind controller tuning:

| Candidate | Key change | Decision |
|---|---|---|
| v49 | broad path-speed attenuation during reverse avoidance | rejected: Track3 early stop at `T=5.75` |
| v50 | lower curvature-speed threshold from `0.35` to `0.20` | rejected: Track3 stayed `P=9.2`, `cR=1`, `cO=1` |
| v51 | narrow straight-line path-speed attenuation | rejected: Track3 early stop at `T=2.25` |
| v52-v57 | brake-turn coupling, path-authority, low-speed lookahead, filter/front-threshold variants | rejected: Track3 score stayed `P=9.2` or runs shortened |
| v58-v66 | reactive gap, close-side direction, steering/filter/feedforward/emergency/road-edge variants | rejected: no comparable score improvement or early-stop artifacts |
| v67 | nearest-obstacle distance diagnostic input | rejected as a score route: clean Track3 runtime but unchanged `P=9.2`, `cR=1`, `cO=1` |

Additional post-v67 screening:

| Screening | Decision |
|---|---|
| v69 lateral left/right hysteresis | rejected before source edit; saved v48 signals show zero `chart.steer` sign flips on all four tracks |

## 5. 四条赛道仿真结果

Primary evidence:

```text
Results/metrics/four_track_candidate_review_v48_opposing_steer_guard_20260710.md
```

Evaluation entry models:

```text
UGV.Test.Saidao1Eval
UGV.Test.Saidao2Eval
UGV.Test.Saidao3Eval
UGV.Test.Saidao4Eval
```

These wrappers preserve the official `Models/UGV/saidao/` source geometry and add the obstacle-controller wiring required by the current API evaluation route. The official vehicle, road, sensor, scoring, example, and `saidao` source files were not edited.

Runtime caveat: Track2, Track3, and Track4 returned `simulate_failed` with `exit_state=2`, but the enhanced probe read final `T/cR/cO/P` variables and exported score timeseries after the model terminal state. Therefore the table below is usable review evidence, but it is not final competition evidence and must not be described as a clean runtime success on every track.

| Track | Model | Runtime status | Terminal time T/s | Road collisions cR | Obstacle collisions cO | Score P | Evidence |
|---|---|---|---:|---:|---:|---:|---|
| saidao1 / LOGO | `UGV.Test.Saidao1Eval` | `simulate_returned_true` | 120.0 | 2 | 0 | 9.2 | `Results/simulations/controller_v48_opposing_steer_guard_saidao1_120s_20260710/` |
| saidao2 / 综合环形 | `UGV.Test.Saidao2Eval` | `simulate_failed` with readable variables | 60.15 | 1 | 0 | 9.6 | `Results/simulations/controller_v48_opposing_steer_guard_saidao2_120s_20260710/` |
| saidao3 / 三角形 | `UGV.Test.Saidao3Eval` | `simulate_failed` with readable variables | 112.45 | 1 | 1 | 9.2 | `Results/simulations/controller_v48_opposing_steer_guard_saidao3_120s_20260710/` |
| saidao4 / 云型 | `UGV.Test.Saidao4Eval` | `simulate_failed` with readable variables | 112.4 | 2 | 0 | 9.2 | `Results/simulations/controller_v48_opposing_steer_guard_saidao4_120s_20260710/` |

Total score comparison:

| Candidate | Total score | Notes |
|---|---:|---|
| v13 side trigger 0.45 | 36.4 | historical accepted controller candidate |
| v45 curvature speed regulation | 36.8 | superseded by v48 |
| v48 opposing-steer guard | 37.2 | current review-ready best candidate with runtime caveat |

## 6. 结果分析

What is supported by evidence:

1. Source/interface mapping is complete enough for controller work.
2. Baseline bounded runtime and controller bounded runtime gates were previously achieved.
3. v48 improves total wrapper score by `+0.4` over v45 and `+0.8` over v13.
4. v48 reduces Track1 road collisions from v45 `cR=3` to `cR=2`, with no obstacle collision on Track1.
5. Static deployability checker reports `ready_for_physical_claim=true`, `high=0`, and `medium=0` for the source-level checks.
6. MWORKS login/license recovery was completed through the real Sysplorer login and license activation flow, then verified by a 1 s API probe.

What must not be claimed yet:

1. No final optimized contest score.
2. No final competition submission readiness.
3. No physical UGV readiness.
4. No claim that Track2, Track3, and Track4 returned clean runtime success.

Current result quality:

1. Best current track: saidao2, `P=9.6`, but with terminal-state caveat.
2. Track1 is the cleanest 120 s runtime in v48, `P=9.2`, `cR=2`, `cO=0`.
3. Track3 remains the most important weak track because it still has both one road collision and one obstacle collision.
4. Track2/3/4 terminal-state caveats must be addressed before final competition claims.

Post-v67 attribution:

```text
Results/metrics/signal_window_summary_v48_all_tracks_v67_track3_post_research_20260710.md
Results/metrics/ctrlalloc_contribution_analysis_v48_all_tracks_v67_track3_post_research_20260710.md
Results/metrics/post_v67_v68_attribution_decision_20260710.md
```

The new offline attribution shows that the remaining score-loss windows are
not simple trigger-missing failures. At v48 score-loss events, avoidance is
already active and requests reverse/braking plus obstacle steering. Track3's
first obstacle event still has high final forward speed (`~0.72`) because the
path forward-speed contribution dominates early in the filtered allocation
window. However, the direct straight-line arbitration mechanism was already
tested as v51 and rejected due to non-comparable early stop. Therefore the
current engineering decision is to avoid another blind source patch and move
the long task forward through report/readiness and physical-transfer
consolidation until a genuinely different deployable four-scalar mechanism is
identified.

## 7. 不足与改进方向

Controller improvement:

1. Do not continue blind scalar scans, global speed attenuation, stronger reverse-speed scalar changes, or path-speed attenuation scans.
2. The next algorithmic improvement should start from fresh failure-window evidence and a mechanism that does not create early-stop score inflation.
3. Track3 early obstacle contact needs a better obstacle-horizon or path-authority interaction design; v49/v51 show that simply suppressing forward path speed is too disruptive.
4. Preserve explainable bounded logic for later generated-code/physical UGV tuning.
5. Apply the deployability filter from `References/research/deployable_ugv_avoidance_algorithms_20260709/source_notes.md` before accepting any simulation-score tuning.
6. Treat post-v67 analysis as the current stop line for blind controller churn:
   no v68 source edit should be made until it has a materially different
   mechanism from v49-v67.

Evidence/package improvement:

1. Keep `UGV.Test.Saidao*Eval` as the current repeatable API evaluation route.
2. Keep direct `UGV.saidao.saidao*` entries as official source geometry references, not editable controller-integration targets.
3. Keep old M6/v13 report and old local review package as historical audit evidence only.
4. Do not build or send a new final competition package without explicit user approval.
5. Continue current long task by improving the report, final-race migration
   notes, readiness checks, and reproducibility evidence instead of stopping
   after rejected candidates.
6. Use `Docs/Design/final_race_migration_notes.md` as the current M10 review
   surface for physical-transfer assumptions, exhausted mechanism families,
   and final-race retuning order.

## 8. 复现说明

Known v48 review evidence is listed above. The current repeatable command shape is:

```powershell
& 'D:\Program Files\MWORKS\Sysplorer 2026a\External\python64\python.exe' `
  Scripts\mworks\ugv_baseline_probe.py `
  --project-root C:\Users\HP\Desktop\UGV `
  --out-dir Results\simulations\controller_v48_opposing_steer_guard_saidao<track>_120s_<timestamp> `
  --model-name UGV.Test.Saidao<track>Eval `
  --stop-time 120 `
  --request-id controller_v48_opposing_steer_guard_saidao<track>_120s_<timestamp> `
  --run-label controller_v48_track<track>_opposing_steer_guard `
  --controller-version v48_opposing_steer_guard `
  --use-simulate-ex `
  --relax-translation-checks `
  --option compileOptions=0 `
  --save-variable-names `
  --extra-var-substring obsAvoidController_Sysblock.chart `
  --extra-var-substring ctrlAlloc `
  --extra-var-substring pathPlanner
```

If `L5104-B0` reappears, recover through the documented real Sysplorer login and `帮助 -> 使用许可` activation workflow, then verify with a `license_gui_confirm_1s_*` 1 s API probe before resuming runtime claims.
