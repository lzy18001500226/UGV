# UGV Initial Race Simulation Report Draft - v13 Metrics Refresh

Status: v13 side-trigger 0.45 review draft, not final submission material.
Date: 2026-07-09

## 1. 赛题目标与模型说明

本项目面向 2026 智能无人应用挑战赛算法赛道的无人车避障任务。当前工作基于官方 UGV MWORKS/Sysplorer 模型，在不修改官方车辆、道路、传感器、计分或赛道模型的前提下，实现并验证避障控制器。

当前工程目标是从官方 UGV 模型出发，完成避障控制器、官方赛道仿真、时间/碰撞/得分证据和仿真报告。最终比赛提交包和提交邮件仍需要用户明确批准，本报告不是最终提交声明。

## 2. 无人车系统结构与控制接口

正常实现边界：

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

控制器输入为 `front_dist`、`rear_dist`、`left_dist`、`right_dist`，输出为 `speed` 和 `steer`。官方路径规划和控制分配仍是主线，避障控制器输出作为增量进入控制分配，不替代官方路径规划。

Source grounding evidence:

```text
Results/evidence/static_model_grounding_20260708_210142.md
Docs/Index/model_index.md
```

## 3. 避障控制算法原理

当前候选控制器为 `controller_v13_side_trigger_0p45`。

设计原则：

1. 保持官方路径规划为 cruise 状态主导。
2. 前方风险时先降速，再向左右更大安全间隙侧转向。
3. 侧向风险纳入纵向避障触发，避免车身侧边已经接近障碍但 `front_dist` 尚未触发时继续巡航。
4. 用 dwell/hysteresis 思路减少避障后过快释放导致的重复碰撞。
5. 输出速度和转角增量保持饱和，避免为仿真分数引入不可部署的尖锐控制。

v13 的核心逻辑变化：

```modelica
transition(cruise, avoid, df <= mindis or dl <= 0.45 or dr <= 0.45, reset = false)
```

该改动来自 v12 碰撞窗口分析：Track1 早期障碍物碰撞发生时 `flag=0`，侧向距离约为 `0.46`，说明 v12 的 `0.30` 侧向触发阈值偏晚。v13 采用 `0.45` 作为窄范围试验，不做大状态机重写。

Design and diagnostic evidence:

```text
Docs/Design/避障算法设计.md
Results/evidence/controller_design_review_20260708_215659.md
Results/metrics/v12_collision_window_interpretation_20260709_1520.md
```

## 4. 参数设置与调参依据

当前调参路径：

| Candidate | Key change | Evidence | Result summary |
|---|---|---|---|
| v5 | front-risk dwell 1 s -> 2 s | `Results/metrics/one_track_tuning_20260708_231430.md` | M6 baseline for later comparison, total wrapper score 32.0 |
| v12 | add side trigger `dl <= 0.30 or dr <= 0.30` | `Results/metrics/four_track_summary_v12_side_trigger_20260709_144854.md` | total wrapper score 34.8 |
| v13 | side trigger threshold raised to 0.45 | `Results/metrics/four_track_summary_v13_side_trigger045_20260709_1535.md` | total wrapper score 36.4 |

Rejected path: v7-v11 scalar tuning changes are not accepted as current controller changes. They are retained only as tuning history because they did not provide a better four-track tradeoff or lacked a diagnostic reason.

## 5. 四条赛道仿真结果

Primary evidence:

```text
Results/metrics/four_track_summary_v13_side_trigger045_20260709_1535.md
```

Evaluation entry models:

```text
UGV.Test.Saidao1Eval
UGV.Test.Saidao2Eval
UGV.Test.Saidao3Eval
UGV.Test.Saidao4Eval
```

These wrappers preserve the official `Models/UGV/saidao/` source geometry and add the obstacle-controller wiring required by the current API evaluation route. The official vehicle, road, sensor, scoring, example, and `saidao` source files were not edited.

Runtime note: Track2 and Track4 returned `simulate_failed` with `exit_state=2`, but the enhanced probe read final `T/cR/cO/P` variables and exported score timeseries after the model terminal state. Therefore the table below is usable review evidence, but it should not be described as an ordinary clean `SimulateModelEx=true` return for every track.

| Track | Model | Runtime status | Terminal time T/s | Road collisions cR | Obstacle collisions cO | Score P | Evidence |
|---|---|---|---:|---:|---:|---:|---|
| saidao1 / LOGO | `UGV.Test.Saidao1Eval` | `simulate_returned_true` | 120.0 | 3 | 0 | 8.8 | `Results/simulations/controller_v13_side_trigger045_saidao1_120s_20260709_1524/` |
| saidao2 / 综合环形 | `UGV.Test.Saidao2Eval` | `simulate_failed` with readable variables | 91.9 | 1 | 0 | 9.6 | `Results/simulations/controller_v13_side_trigger045_saidao2_120s_20260709_1528/` |
| saidao3 / 三角形 | `UGV.Test.Saidao3Eval` | `simulate_returned_true` | 120.0 | 1 | 1 | 9.2 | `Results/simulations/controller_v13_side_trigger045_saidao3_120s_20260709_1530/` |
| saidao4 / 云型 | `UGV.Test.Saidao4Eval` | `simulate_failed` with readable variables | 113.1 | 3 | 0 | 8.8 | `Results/simulations/controller_v13_side_trigger045_saidao4_120s_20260709_1526/` |

Total score comparison:

| Candidate | Total score | Notes |
|---|---:|---|
| v5/M6 baseline | 32.0 | Baseline four-track wrapper evidence |
| v12 side trigger 0.30 | 34.8 | Improves Track1/2/3, Track4 regresses vs v5 |
| v13 side trigger 0.45 | 36.4 | Improves total score by +1.6 vs v12 and +4.4 vs v5/M6 |

## 6. 结果分析

What is supported by evidence:

1. Source/interface mapping is complete enough for controller work.
2. Baseline bounded runtime and controller bounded runtime gates were previously achieved.
3. v13 improves Track1 and Track3 compared with v12 while preserving Track2 and not further worsening Track4.
4. Static deployability checker reports `ready_for_physical_claim=true`, `high=0`, and `medium=0` for v13 source-level checks.
5. MWORKS login/license recovery was completed through the real Sysplorer login and license activation flow, then verified by a 1 s API probe.

What must not be claimed yet:

1. No final optimized contest score.
2. No final competition submission readiness.
3. No physical UGV readiness.
4. No claim that every 120 s run returned a clean success status.

Current result quality:

1. Best current track: saidao2, `P=9.6`.
2. Track3 improved to `P=9.2`.
3. Track1 obstacle collisions dropped to zero, but road collisions remain.
4. Track4 remains weaker than the v5/M6 baseline and is the next improvement target.

## 7. 不足与改进方向

Controller improvement:

1. Prioritize Track4 road-boundary recovery before another broad controller rewrite.
2. Inspect Track4 signal windows around late road collisions, especially `flag` state, side distance, speed, and steer behavior.
3. Tune speed-turn coupling for physical plausibility, not only one-track score.
4. Preserve explainable bounded state logic for later generated-code/physical UGV use.
5. Apply the deployability filter from `References/research/deployable_ugv_avoidance_algorithms_20260709/source_notes.md` before accepting any simulation-score tuning.

Evidence/package improvement:

1. Keep `UGV.Test.Saidao*Eval` as the current repeatable API evaluation route.
2. Keep direct `UGV.saidao.saidao*` entries as official source geometry references, not editable controller-integration targets.
3. Keep the old M6 report and old local review package as historical audit evidence only.
4. Do not build or send a new final competition package without explicit user approval.

## 8. 复现说明

Known v13 review evidence is listed above. The current repeatable command shape is:

```powershell
& 'D:\Program Files\MWORKS\Sysplorer 2026a\External\python64\python.exe' `
  Scripts\mworks\ugv_baseline_probe.py `
  --project-root C:\Users\HP\Desktop\UGV `
  --out-dir Results\simulations\controller_v13_side_trigger045_saidao<track>_120s_<timestamp> `
  --model-name UGV.Test.Saidao<track>Eval `
  --stop-time 120 `
  --request-id M7-v13-track<track>-side-trigger045 `
  --run-label controller_v13_track<track>_side_trigger045 `
  --controller-version controller_v13_side_trigger_0p45 `
  --use-simulate-ex `
  --relax-translation-checks `
  --option compileOptions=0
```

If `L5104-B0` reappears, recover through the documented real Sysplorer login and `帮助 -> 使用许可` activation workflow, then verify with a `license_gui_confirm_1s_*` 1 s API probe before resuming runtime claims.
