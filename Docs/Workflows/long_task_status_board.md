# Long Task Status Board

> Short operational board for the UGV initial-race long task. Keep this file concise; detailed evidence belongs in `Results/`.

Status: ready_for_M1_static_grounding, 2026-07-08 CST.

## Current Long Task

```text
UGV initial-race M1-M6 autonomous loop:
M1 static model grounding
M2 baseline runtime
M3 controller design
M4 controller implementation
M5 one-track tuning
M6 four-track evaluation
```

## Phase Board

| Phase | State | Owner | Evidence | Next Action |
|---|---|---|---|---|
| M1 Static model grounding | ready | Codex | pending | Inspect Race1/Race2, tracks, controller, ControlAllocate, CountPoint, sensors. |
| M2 Baseline runtime | waiting_on_M1 | Codex | pending | Load official model in MWORKS after M1. |
| M3 Controller design | waiting_on_M2 | Codex | pending | Draft `Docs/Design/避障算法设计.md`. |
| M4 Controller implementation | waiting_on_M3 | Codex | pending | Implement only controller boundary. |
| M5 One-track tuning | waiting_on_M4 | Codex | pending | Tune one official track with evidence. |
| M6 Four-track evaluation | waiting_on_M5 | Codex | pending | Run all official tracks and summarize metrics. |
| M7-M9 Report/package | deferred | Codex + user final approval | pending | Start after M6 review. |

## Blockers

None currently recorded.

## Review Notes

- Do not use this board as a history ledger.
- Update only when phase state changes or a review/blocker appears.
- Long details, logs, screenshots, and metrics must stay under `Results/`.
