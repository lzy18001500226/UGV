# UGV Submission Readiness Dry Run

generated_at: 2026-07-10T08:47:33+08:00
ready: false
final_approval: false

## Summary

- tracked_model_files: 72
- tracked_metric_or_evidence_files: 364
- tracked_report_or_workflow_files: 106

## Blockers

- final_submission_approval_missing

## Required Paths

- model_root: Models/UGV -> exists=true
- model_package: Models/UGV/package.mo -> exists=true
- controller: Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo -> exists=true
- official_report_template: References/official_materials/5-仿真报告模板（仅供参考）/仿真报告模板.docx -> exists=true
- report_draft: Results/deliverables/report_drafts/initial_race_report_draft_v48_metrics_20260710.md -> exists=true
- report_docx_draft: Results/deliverables/report_drafts/initial_race_report_draft_v48_metrics_20260710.docx -> exists=true
- report_render_qa_note: Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/QA_NOTE.md -> exists=true
- report_page_render_qa_note: Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/word_com_export_qa/page_render_qa.md -> exists=true
- report_page_render_qa_json: Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/word_com_export_qa/page_render_qa.json -> exists=true
- report_page_render_contact_sheet: Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/word_com_export_qa/contact_sheet.png -> exists=true
- report_page_render_pdf: Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/word_com_export_qa/initial_race_report_draft_v48_metrics_20260710_word_export.pdf -> exists=true
- report_trajectory_figure_track1: Results/figures/trajectory_event_review_v48_20260710/v48_track1_trajectory_events.png -> exists=true
- report_trajectory_figure_track3: Results/figures/trajectory_event_review_v48_20260710/v48_track3_trajectory_events.png -> exists=true
- report_trajectory_overlay_track3: Results/figures/trajectory_event_review_v48_20260710/v48_track3_road_obstacle_overlay.png -> exists=true
- controller_deployability_static_check: Results/evidence/controller_deployability_static_check_v48_reconfirmed_after_v67_20260710.md -> exists=true
- one_track_metrics: Results/metrics/one_track_tuning_20260708_231430.md -> exists=true
- four_track_summary: Results/metrics/four_track_candidate_review_v48_opposing_steer_guard_20260710.md -> exists=true
- post_v67_attribution_decision: Results/metrics/post_v67_v68_attribution_decision_20260710.md -> exists=true
- login_license_recovery_evidence: Results/evidence/mworks_login_license_recovery_gui_api_confirmed_20260709.md -> exists=true

## Four Track Gate

ready: true
- UGV.Test.Saidao1Eval: present=true, blocked_or_unavailable=false
- UGV.Test.Saidao2Eval: present=true, blocked_or_unavailable=false
- UGV.Test.Saidao3Eval: present=true, blocked_or_unavailable=false
- UGV.Test.Saidao4Eval: present=true, blocked_or_unavailable=false

## Package Plan

### Include

- `Models/UGV/`
- `Results/deliverables/report_drafts/initial_race_report_draft_v48_metrics_20260710.md`
- `Results/deliverables/report_drafts/initial_race_report_draft_v48_metrics_20260710.docx`
- `Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/QA_NOTE.md`
- `Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/word_com_export_qa/page_render_qa.md`
- `Results/deliverables/report_drafts/render_check_v48_post_v67_20260710/word_com_export_qa/contact_sheet.png`
- `Results/figures/trajectory_event_review_v48_20260710/`
- `Results/metrics/four_track_candidate_review_v48_opposing_steer_guard_20260710.md`
- `Results/metrics/post_v67_v68_attribution_decision_20260710.md`
- `Results/metrics/one_track_tuning_20260708_231430.md`
- `Results/evidence/static_model_grounding_20260708_210142.md`
- `Results/evidence/controller_design_review_20260708_215659.md`
- `Results/evidence/controller_v1_source_notes_20260708_220257.md`
- `Results/evidence/controller_deployability_static_check_v48_reconfirmed_after_v67_20260710.md`

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
- Does not treat final submission as approved by the user.
