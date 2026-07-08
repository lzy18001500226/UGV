# UGV Initial Race Simulation Report Draft - Blocker Aware

Status: draft scaffold, not final submission material.
Date: 2026-07-09

## 1. 赛题目标与模型说明

本项目面向 2026 智能无人应用挑战赛算法赛道的无人车避障任务。当前工作基于官方 UGV MWORKS/Sysplorer 模型，在不修改官方车辆、道路、传感器、计分或赛道模型的前提下，实现并验证避障控制器。

当前工程目标：

```text
official UGV model
  -> obstacle-avoidance controller
  -> official-track simulation
  -> time/collision/score evidence
  -> report and submission candidate package
```

## 2. 无人车系统结构与控制接口

正常实现边界：

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

控制器输入输出：

```text
inputs:  front_dist, rear_dist, left_dist, right_dist
outputs: speed, steer
```

官方路径规划和控制分配仍是主线，避障控制器输出作为增量进入控制分配，不替代官方路径规划。

Source grounding evidence:

```text
Results/evidence/static_model_grounding_20260708_210142.md
Docs/Index/model_index.md
```

## 3. 避障控制算法原理

当前候选控制器为 `controller_v5_front_dwell_2s`。

设计原则：

1. 保持官方路径规划为 cruise 状态主导。
2. 前方风险时先降速，再向左右更大安全间隙侧转向。
3. 侧向风险时向更大侧向间隙偏置。
4. 用 dwell/hysteresis 思路减少避障后过快释放导致的重复碰撞。
5. 输出速度和转角增量保持饱和，避免为仿真分数引入不可部署的尖锐控制。

Design evidence:

```text
Docs/Design/避障算法设计.md
Results/evidence/controller_design_review_20260708_215659.md
Docs/Design/final_race_migration_notes.md
References/research/physical_ugv_obstacle_avoidance_20260708/
```

## 4. 参数设置与调参依据

已完成一赛道候选调参：

```text
Results/metrics/one_track_tuning_20260708_231430.md
```

当前结论：

| Candidate | Key change | Evidence | Result summary |
|---|---|---|---|
| v1 | base runnable Sysblock structure | `Results/simulations/controller_refsysblock_20260708_221000/` | bounded 12s gate passes |
| v5 | front-risk dwell 1s -> 2s | `Results/simulations/controller_v5_front_dwell_2s_race1_120s_20260708_230305/` | Race1 120s score improved versus v1 candidate |
| v6 | front-risk dwell 3s | recorded in tuning evidence | rejected: dwell too long, road collisions increase |

## 5. 四条赛道仿真结果

Current status: blocked before official four-track scoring.

Evidence:

```text
Results/metrics/four_track_summary_20260708_231430.md
Results/evidence/official_track_api_simulation_blocker_20260708_231430.md
Results/evidence/m6_mworks_activation_blocker_20260708_235918.md
```

Current blocker classification:

```text
MWORKS activation/license blocks loading installed TADynamics dependency.
```

Latest observed error:

```text
错误(9308): (v2.2.3.27)软件尚未激活，请前往菜单栏“帮助”>“使用许可”窗口激活软件后重试，错误码：L5104-B0。
```

This occurred before official-track `CheckModel`/`SimulateModelEx` could be completed in the fresh diagnostic session. It is not a controller-score failure.

Four-track result table must remain unavailable until MWORKS activation is restored and official track runs complete.

| Track | Status | Time | Road collisions | Obstacle collisions | Score | Evidence |
|---|---|---:|---:|---:|---:|---|
| saidao1 | blocked_before_run | n/a | n/a | n/a | n/a | `Results/evidence/m6_mworks_activation_blocker_20260708_235918.md` |
| saidao2 | blocked_before_run | n/a | n/a | n/a | n/a | same blocker |
| saidao3 | blocked_before_run | n/a | n/a | n/a | n/a | same blocker |
| saidao4 | blocked_before_run | n/a | n/a | n/a | n/a | same blocker |

## 6. 结果分析

What is already supported by evidence:

- Source/interface mapping is complete enough for controller work.
- Baseline bounded runtime and controller bounded runtime gates were previously achieved.
- Race1 tuning has a review-ready candidate.
- Current official-track evaluation is blocked by MWORKS activation/license while loading TADynamics, before controller score can be judged.

What must not be claimed yet:

- No four-track completion.
- No final contest score.
- No final submission readiness.
- No physical UGV readiness.

## 7. 不足与改进方向

Immediate recovery:

1. Restore MWORKS activation/license.
2. Rerun `UGV.saidao.saidao1` dependency-load diagnostic.
3. If dependency loading and `CheckModel` pass, continue `SimulateModelEx` option matrix.
4. If one official track runs, expand to all four tracks.

Controller improvement after M6 resumes:

1. Export first-collision windows with distance inputs and speed/steer outputs.
2. Tune speed-turn coupling for physical plausibility, not only one-track score.
3. Preserve explainable bounded state logic for later generated-code/physical UGV use.

## 8. 复现说明

Known good bounded evidence and current blocker paths are listed above. After activation recovery, use the command in:

```text
Results/evidence/m6_mworks_activation_blocker_20260708_235918.md
```

Then update this draft with real four-track metrics.
