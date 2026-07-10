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

## 5. DOCX Page Render QA

Before treating a report draft as final-review material, run a page-level render
check in addition to DOCX structure checks:

```powershell
python Scripts\report\render_docx_pages_qa.py `
  --docx Results\deliverables\report_drafts\initial_race_report_draft_v48_metrics_20260710.docx `
  --out-dir Results\deliverables\report_drafts\render_check_v48_post_v67_20260710\word_com_export_qa `
  --min-pages 1 `
  --json-out Results\deliverables\report_drafts\render_check_v48_post_v67_20260710\word_com_export_qa\page_render_qa.json `
  --md-out Results\deliverables\report_drafts\render_check_v48_post_v67_20260710\word_com_export_qa\page_render_qa.md `
  --fail-on-not-passed
```

The helper exports DOCX to PDF through Word COM when available, falls back to
LibreOffice when available, renders PDF pages to PNG through Poppler, builds a
contact sheet, and flags blank-looking pages. This still does not approve final
competition submission; it only upgrades report QA from structure-only to
page-render evidence.
