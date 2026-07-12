# v162 Rear-Observability Diagnostic

Status: diagnostic complete; no candidate promoted; v148 restored.

The Track3 v162 reproduction reached the bounded 200 s horizon with
`T=200,cR=2,cO=1,P=8.8`. It exported the previously missing rear sensor `db`
alongside position, path progress, four-direction distances, and control
contributions.

## Findings

| Window | df | db | dl | dr | Interpretation |
|---|---:|---:|---:|---:|---|
| departure near 1 s | 0.847 | 0.957 | 0.568 | 0.567 | rear clear |
| loop near 60 s | front clear | below 0.02 | asymmetric | asymmetric | rear-close state occurs mid-loop |
| return near 179 s | 2.055 | 0.018 | 0.065 | 0.100 | rear close, right gap larger |
| second outbound near 185 s | 2.055 | 0.026 | 0.056 | 0.109 | similar state persists after origin miss |

The rear sensor distinguishes initial departure from later motion, but not the
specific return-to-finish window. Predicates based on `df>1.5`, small `db`, and
side asymmetry recur on the main loop as well as the return straight. Using
them would be a hidden Track3 geometry patch and is not justified.

## Decision

Keep `db` available for future research but do not add a rear-threshold branch.
Close this diagnostic without a runtime candidate and retain exact v148.

Evidence:

- `Docs/Design/v162_rear_observability_diagnostic_plan_20260712.md`
- `Results/simulations/diagnostic_v162_rear_observability_track3_200s_20260712/`

No finish, score gain, physical-car, package, or submission claim is made.
