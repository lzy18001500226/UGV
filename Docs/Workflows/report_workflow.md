# Report Workflow

## 1. Purpose

Produce the initial-race simulation report using the official report template
and project evidence.

## 2. Inputs

1. Official template:

```text
References/official_materials/5-仿真报告模板（仅供参考）/
```

2. Competition and scoring notes:

```text
Docs/Design/赛题.md
Docs/Design/需求.md
Docs/Design/架构.md
```

3. Run evidence:

```text
Results/simulations/
Results/metrics/
Results/figures/
```

## 3. Report Sections

Recommended structure:

1. 赛题目标与模型说明。
2. 无人车系统结构与控制接口。
3. 避障控制算法原理。
4. 参数设置与调参依据。
5. 四条赛道仿真结果。
6. 结果分析：用时、碰撞、得分、失败场景。
7. 不足与改进方向。
8. 复现说明。

## 4. Evidence Requirements

Every result table should name:

```text
track
controller version
run folder
time
collision count
score
```

Every figure should have a caption and point back to the run folder.
