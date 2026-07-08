# UGV Submission Readiness Dry Run

generated_at: 2026-07-09T01:41:11+08:00
ready: false
final_approval: false

## Summary

- tracked_model_files: 67
- tracked_metric_or_evidence_files: 22
- tracked_report_or_workflow_files: 18

## Blockers

- four_track_metrics_blocked_or_unavailable
- final_submission_approval_missing

## Required Paths

- model_root: Models/UGV -> exists=true
- model_package: Models/UGV/package.mo -> exists=true
- controller: Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo -> exists=true
- official_report_template: References/official_materials/5-仿真报告模板（仅供参考）/仿真报告模板.docx -> exists=true
- report_draft: Results/deliverables/report_drafts/initial_race_report_draft_blocker_aware_20260709.md -> exists=true
- report_docx_draft: Results/deliverables/report_drafts/initial_race_report_draft_blocker_aware_20260709.docx -> exists=true
- report_render_qa_note: Results/deliverables/report_drafts/render_check_20260709_0118/QA_NOTE.md -> exists=true
- one_track_metrics: Results/metrics/one_track_tuning_20260708_231430.md -> exists=true
- four_track_summary: Results/metrics/four_track_summary_20260708_231430.md -> exists=true
- activation_blocker: Results/evidence/m6_mworks_activation_blocker_20260708_235918.md -> exists=true

## Four Track Gate

ready: false
- UGV.saidao.saidao1: present=true, blocked_or_unavailable=true
- UGV.saidao.saidao2: present=true, blocked_or_unavailable=true
- UGV.saidao.saidao3: present=true, blocked_or_unavailable=true
- UGV.saidao.saidao4: present=true, blocked_or_unavailable=true

## Package Plan

### Include

- `Models/UGV/`
- `Results/deliverables/report_drafts/initial_race_report_draft_blocker_aware_20260709.md`
- `Results/deliverables/report_drafts/initial_race_report_draft_blocker_aware_20260709.docx`
- `Results/metrics/four_track_summary_<final_timestamp>.md once available`
- `Results/metrics/one_track_tuning_20260708_231430.md`
- `Results/evidence/static_model_grounding_20260708_210142.md`
- `Results/evidence/controller_design_review_20260708_215659.md`
- `Results/evidence/controller_v1_source_notes_20260708_220257.md`

### Exclude

- `Results/tmp/`
- `Scripts/mworks/__pycache__/`
- `untracked scratch simulation folders unless promoted by manifest`
- `References/research/ large upstream sources unless cited in report appendix`
- `final competition email/send action until user approval`

## Non-Claims

- Does not run MWORKS.
- Does not create final zip.
- Does not send final competition submission email.
- Does not convert blocked four-track evidence into score claims.
