# Long Task Status Board

> Short operational board for the UGV initial-race long task. Keep this file concise; detailed evidence belongs in `Results/`.

Status: M5_one_track_tuning_in_progress, 2026-07-08 CST.

## Current Long Task

```text
UGV initial-race M1-M9 autonomous loop:
M1 static model grounding
M2 baseline runtime
M3 controller design
M4 controller implementation
M5 one-track tuning
M6 four-track evaluation
M7 evidence automation as needed
M8 report draft
M9 submission candidate package, without final send
```

## Phase Board

| Phase | State | Owner | Evidence | Next Action |
|---|---|---|---|---|
| M1 Static model grounding | completed | Codex | `Results/evidence/static_model_grounding_20260708_210142.md` | Done; use source mapping for M2. |
| M2 Baseline runtime | completed_bounded_gate | Codex | `Results/simulations/baseline_20260708_213448/` | Done; load/check/simulate and score variables verified for bounded stopTime=12. |
| M3 Controller design | completed | Codex | `Docs/Design/避障算法设计.md`; `Results/evidence/controller_design_review_20260708_215659.md` | Done; use conservative reactive increment design for M4. |
| M4 Controller implementation | completed_bounded_gate | Codex | `Results/evidence/controller_v1_source_notes_20260708_220257.md`; `Results/simulations/controller_refsysblock_20260708_221000/` | Done; recovered from failed plain algorithm by using valid Sysblock reference structure. |
| M5 One-track tuning | in_progress | Codex | pending | Run longer Race1/first official track, compare against bounded baseline, then tune controller logic if needed. |
| M6 Four-track evaluation | waiting_on_M5 | Codex | pending | Run all official tracks and summarize metrics. |
| M7 Evidence automation | waiting_on_repetition | Codex | pending | Add only scripts that reduce repeated run/metric/package work. |
| M8 Report draft | waiting_on_M6 | Codex | pending | Draft after credible run evidence exists. |
| M9 Submission candidate package | waiting_on_M8 | Codex + user final approval | pending | Build local candidate only; do not send final submission without user approval. |

## Blockers

None currently recorded.

## Review Notes

- M1 is source/static only. It does not claim MWORKS load, translate, simulate, lap completion, score, or GUI health.
- M2 confirms bounded runtime load/check/simulate for `UGV.Example.Race1`; it does not claim full-track completion or final competition score.
- M4 confirms a first runnable Sysblock controller structure with bounded `stopTime=12` metrics `T=12`, `cR=0`, `cO=0`, `P=10`; it does not claim full-track completion.
- Do not use this board as a history ledger.
- Update only when phase state changes or a review/blocker appears.
- Long details, logs, screenshots, and metrics must stay under `Results/`.
