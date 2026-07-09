# UGV Initial Race Simulation Report Draft - M6 Metrics Refresh

Status: 四赛道指标已刷新 / M6 metrics refreshed review draft, not final submission material.
Date: 2026-07-09

## 1. 赛题目标与模型说明

本项目面向 2026 智能无人应用挑战赛算法赛道的无人车避障任务。当前工作基于官方 UGV MWORKS/Sysplorer 模型，在不修改官方车辆、道路、传感器、计分或赛道模型的前提下，实现并验证避障控制器。

当前工程目标是从官方 UGV 模型出发，完成避障控制器、官方赛道仿真、时间/碰撞/得分证据、报告和提交候选包。

## 2. 无人车系统结构与控制接口

正常实现边界：`Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`。

控制器输入为 `front_dist`、`rear_dist`、`left_dist`、`right_dist`，输出为 `speed` 和 `steer`。

官方路径规划和控制分配仍是主线，避障控制器输出作为增量进入控制分配，不替代官方路径规划。

Source grounding evidence: `Results/evidence/static_model_grounding_20260708_210142.md` and `Docs/Index/model_index.md`.

## 3. 避障控制算法原理

当前候选控制器为 `controller_v5_front_dwell_2s`。

设计原则：

1. 保持官方路径规划为 cruise 状态主导。
2. 前方风险时先降速，再向左右更大安全间隙侧转向。
3. 侧向风险时向更大侧向间隙偏置。
4. 用 dwell/hysteresis 思路减少避障后过快释放导致的重复碰撞。
5. 输出速度和转角增量保持饱和，避免为仿真分数引入不可部署的尖锐控制。

Design evidence: `Docs/Design/避障算法设计.md`, `Results/evidence/controller_design_review_20260708_215659.md`, `Docs/Design/final_race_migration_notes.md`, and the research packs under `References/research/`.

## 4. 参数设置与调参依据

已完成一赛道候选调参，证据为 `Results/metrics/one_track_tuning_20260708_231430.md`。

当前结论：

| Candidate | Key change | Evidence | Result summary |
|---|---|---|---|
| v1 | base runnable Sysblock structure | `Results/simulations/controller_refsysblock_20260708_221000/` | bounded 12s gate passes |
| v5 | front-risk dwell 1s -> 2s | `Results/simulations/controller_v5_front_dwell_2s_race1_120s_20260708_230305/` | Race1 120s score improved versus v1 candidate |
| v6 | front-risk dwell 3s | recorded in tuning evidence | rejected: dwell too long, road collisions increase |

## 5. 四条赛道仿真结果

Current status: four-track wrapper metrics are available.

Primary evidence: `Results/metrics/four_track_summary_20260709_120547.md`.

Evaluation entry models:

```text
UGV.Test.Saidao1Eval
UGV.Test.Saidao2Eval
UGV.Test.Saidao3Eval
UGV.Test.Saidao4Eval
```

These wrappers preserve the official `Models/UGV/saidao/` source geometry and add the obstacle-controller wiring required by the current API evaluation route. The official vehicle, road, sensor, scoring, example, and `saidao` source files were not edited.

Runtime note: all final 120 s runs returned `simulate_failed` with `exit_state=2`, but the enhanced probe read final `T/cR/cO/P` variables and exported score timeseries after the model terminal state. Therefore the table below is usable review evidence, but it should not be described as an ordinary clean `SimulateModelEx=true` return.

| Track | Model | Terminal time T/s | Road collisions cR | Obstacle collisions cO | Score P | Evidence |
|---|---|---:|---:|---:|---:|---|
| saidao1 / LOGO | `UGV.Test.Saidao1Eval` | 86.9 | 4 | 3 | 7.2 | `Results/simulations/eval_saidao1_connected_120s_final_20260709_120547/` |
| saidao2 / 综合环形 | `UGV.Test.Saidao2Eval` | 101.8 | 3 | 1 | 8.4 | `Results/simulations/eval_saidao2_connected_120s_final_20260709_120547/` |
| saidao3 / 三角形 | `UGV.Test.Saidao3Eval` | 50.4 | 2 | 5 | 7.2 | `Results/simulations/eval_saidao3_connected_120s_final_20260709_120547/` |
| saidao4 / 云型 | `UGV.Test.Saidao4Eval` | 47.2 | 2 | 0 | 9.2 | `Results/simulations/eval_saidao4_connected_120s_final_20260709_120547/` |

## 6. 结果分析

What is already supported by evidence:

- Source/interface mapping is complete enough for controller work.
- Baseline bounded runtime and controller bounded runtime gates were previously achieved.
- Race1 tuning has a review-ready candidate.
- MWORKS login/license recovery was completed through the real Sysplorer login and license activation flow, then verified by a 1 s API probe.
- Four-track wrapper evaluation now has terminal time, road-collision, obstacle-collision, and score evidence for all four tracks.

What must not be claimed yet:

- No optimized final contest score.
- No final submission readiness.
- No physical UGV readiness.

Current result quality:

- Best current track: saidao4, `P=9.2`.
- Weakest current tracks: saidao1 and saidao3, both `P=7.2`.
- Track3 is mainly limited by obstacle collisions (`cO=5`).
- Track1 is limited by both road and obstacle collisions (`cR=4`, `cO=3`).

## 7. 不足与改进方向

Controller improvement:

1. Prioritize Track3 obstacle-collision reduction and Track1 mixed road/obstacle collision reduction.
2. Export first-collision windows with distance inputs and speed/steer outputs.
3. Tune speed-turn coupling for physical plausibility, not only one-track score.
4. Preserve explainable bounded state logic for later generated-code/physical UGV use.
5. Apply the deployability filter from `References/research/deployable_ugv_avoidance_algorithms_20260709/source_notes.md` before accepting any simulation-score tuning.

Evidence/package improvement:

1. Keep `UGV.Test.Saidao*Eval` as the current repeatable M6 API evaluation route.
2. Keep direct `UGV.saidao.saidao*` entries as official source geometry references, not editable controller-integration targets.
3. Submission readiness dry run has been refreshed with the M6 metrics.
4. A local review-only candidate archive can be built for user audit; final competition package/send still requires explicit user approval.

## 8. 复现说明

Known good M6 final evidence is listed above. The current repeatable command shape is:

```powershell
& 'D:\Program Files\MWORKS\Sysplorer 2026a\External\python64\python.exe' `
  Scripts\mworks\ugv_baseline_probe.py `
  --project-root C:\Users\HP\Desktop\UGV `
  --out-dir Results\simulations\eval_saidao<track>_connected_120s_final_<timestamp> `
  --model-name UGV.Test.Saidao<track>Eval `
  --stop-time 120 `
  --request-id M6-wrapper-120s-final-track-<track> `
  --run-label m6_wrapper_120s_final_track_<track> `
  --controller-version controller_v5_bounded_linear_deployability `
  --use-simulate-ex `
  --relax-translation-checks `
  --option compileOptions=0
```

If `L5104-B0` reappears, recover through the documented real Sysplorer login and `帮助 -> 使用许可` activation workflow, then verify with `Results/simulations/license_gui_confirm_1s_20260709_after_real_login/`-style 1 s API probe.

Submission readiness dry run was refreshed at `Results/deliverables/submission_dry_runs/submission_readiness_20260709_122252.md`; current blocker is final submission approval only. Local review candidate package generation must remain review-only and must not send the final competition submission email.
