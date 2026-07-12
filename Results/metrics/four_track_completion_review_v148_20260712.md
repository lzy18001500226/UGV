# v148 Four-Track Completion Review

## Decision

Retain v148 as the new completion baseline. It uses one controller on all four
tracks and reaches the official origin assertion on Tracks 1, 2, and 4.
Track3 remains the only completion blocker.

| Track | T/s | cR | cO | P | final d | Completion |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 164.25 | 4 | 1 | 8.0 | 0.0296359 | official finish assertion, last pre-event sample |
| 2 | 183.10 | 3 | 0 | 8.8 | 0.0207526 | official finish assertion, last pre-event sample |
| 3 | 21.10 | 1 | 1 | 9.2 | 301.4313 | failed far from finish |
| 4 | 89.75 | 3 | 0 | 8.8 | 0.0229278 | official finish assertion |

The official model terminates a completed run with
`assert(d >= 0.02 or time <= 10, "已跑完赛道全程，仿真结束")`. MWORKS may expose
the last result sample before the zero crossing, so the probe now accepts a
narrow result-sampling bound of `d<=0.03` only when simulation returns false
after 10 s. A normal horizon return never counts as completion.

Track3 diagnostics show the remaining failure at path index 36. In its final
window, side-only avoidance has `speed_oa=0`, `steer_oa=+0.6`, while the path
heading rises to about `1.73 rad`; the allocator combines them to about
`2.03 rad`. The next candidate should target that same-sign side-only heading
addition without changing front-risk authority or using per-track parameters.

Evidence:

```text
Results/simulations/candidate_v148_completion_first_track1_700s_20260712/
Results/simulations/candidate_v148_completion_first_track2_700s_20260712/
Results/simulations/candidate_v148_completion_first_track3_700s_20260712/
Results/simulations/candidate_v148_completion_first_track4_700s_20260712/
Results/simulations/diagnostic_v148_track3_full_signals_120s_20260712/
Results/metrics/track3_v148_signal_windows_20260712.md
```

This is 3/4 verified completion, not four-track completion, 80/80, submission
readiness, or physical-vehicle validation.
