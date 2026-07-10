# Unified Obstacle Avoidance v86 Plan

Status: implementation candidate after v85 rejection. This document does not
claim a score, runtime success, physical UGV proof, report readiness, or
submission readiness.

## Baseline And Rejection Lesson

Current accepted local wrapper baseline remains v80:

```text
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
```

v85 shortened the lateral initial hold from `2 s` to `1.2 s`, but Track3
early-stopped at `T=2.55,cO=1,P=9.6`, so v85 is rejected:

```text
Results/metrics/track3_candidate_review_v85_short_lateral_initial_hold_20260710.md
```

The lesson is that the fixed initial lateral hold is carrying short-term
stability. The next candidate must not simply shorten the dwell time as a
scalar scan.

## Hypothesis

Keep the original `2 s` initial lateral hold as the default, but allow an early
handoff to side-gap feedback only when lateral imbalance is already visible.
This attempts to preserve v80/v85 initial obstacle stability while reducing the
late upper-edge squeeze seen in v80 Track3.

## Source Change

Allowed target:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Change only the lateral avoid internal transition:

```text
from:
  after(2,sec)

to:
  after(2,sec) or (after(1.5,sec) and abs(dl - dr) > 0.04)
```

The longitudinal `avoid -> cruise after(2,sec)` transition remains unchanged.

## Acceptance

1. Static deployability checker passes with no high/medium risks.
2. Track3 v86 does not early-stop before v80's `T=59.4` unless it also produces
   clearly better score evidence that is comparable.
3. Accept v86 only if it improves Track3 score/runtime without reducing total
   four-track score below v80 `38.0`.
4. If Track3 is improved or comparable, run all four wrappers.
5. If rejected, restore v80 semantics and record the rejection with evidence.
