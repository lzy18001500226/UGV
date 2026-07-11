# Track2 Candidate Review - v136 Path-Curvature Speed Regulation

Decision: rejected; restored v80 source semantics.

## Results

| Run | Runtime | T/s | Index | cR | cO | P | Finish distance squared |
|---|---|---:|---:|---:|---:|---:|---:|
| v80 extended | abnormal stop | 305.15 | 30 | 1 | 0 | 9.6 | 1004.6703 |
| v136 120 s | horizon reached | 120.00 | 28 | 1 | 0 | 9.6 | 975.9766 |
| v136 extended | abnormal stop | 159.95 | 64 | 1 | 0 | 9.6 | 551.2135 |

v136 corrected a real semantic mismatch: the prior limiter used desired
world-frame heading as local curvature. The candidate materially increased
path throughput without adding a collision, reaching index 64 in 159.95 s.
However, it terminated abnormally far from the finish and therefore failed the
completion-first acceptance gate.

## Durable Evidence

```text
Results/simulations/candidate_v136_path_curvature_speed_regulation_track2_1s_20260712/
Results/simulations/candidate_v136_path_curvature_speed_regulation_track2_120s_20260712/
Results/simulations/candidate_v136_path_curvature_speed_regulation_track2_completion_gate_700s_20260712/
Results/evidence/controller_deployability_static_check_v136_path_curvature_speed_regulation_20260712.md
```

## Follow-up Boundary

Do not scan the v136 curvature thresholds. The next candidate must preserve
the demonstrated throughput gain while addressing the numerical/runtime
failure near path index 64, or isolate that failure from saved geometry before
changing control behavior. No evidence here proves a finish or an 80-point
score.
