# Track3 Candidate Review: v117 Closed-Loop Path

generated_at: 2026-07-11T19:15:52+08:00
decision: blocked_not_evaluated
active_source_after_review: v80 path semantics restored

## Candidate

v117 proposed one unified path-topology change: include the final-to-first
segment in nearest-segment search, pursuit traversal, and speed interpolation.
It did not branch by track and did not edit an official no-edit zone.

## Checks

- `test_analyze_track_geometry.py`: 2 tests passed.
- `test_ugv_baseline_probe.py`: 5 tests passed.
- v117 obstacle-controller deployability check: high=0, medium=0.
- `git diff --check` on candidate paths: no whitespace error.

## Runtime Gate

The bounded Track3 `stopTime=1` gate did not reach model translation:

```text
runtime_status: dependency_model_file_load_failed
MWORKS error: L5104-B0, software not activated
```

The Sysplorer login/activation recovery window was opened, but subsequent
capture failed with `window crop is outside captured monitor`. Continuing with
stale coordinates would be unsafe, so no further GUI input or long simulation
was attempted.

Runtime evidence:

```text
Results/simulations/controller_v117_closed_loop_path_saidao3_1s_20260711/
```

## Decision

v117 is neither accepted nor algorithmically rejected. Its source changes were
removed because no MWORKS translation or track evidence exists. Retry the same
mechanism only after license recovery and a fresh targetable Sysplorer window,
starting with the 1 s gate before any full-track run.

## Non-Claims

- No Track3 completion was observed.
- No score improvement was observed.
- No four-track result was produced.
- This blocker does not prove a v117 algorithm defect.
