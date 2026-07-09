# Unified Obstacle Avoidance v69 Lateral Hysteresis Screening

Status: rejected before source edit
Baseline: v48 opposing-steer guard

## Candidate Idea

External wall-following and reactive obstacle-avoidance references often use
bands or hysteresis to avoid noisy left/right switching. A possible post-v67
candidate was therefore:

```text
when obstacle avoidance is active, add a small hysteresis margin before
switching between left-turn and right-turn lateral avoidance.
```

This would stay inside the official four-distance controller boundary and
would be physically deployable if the local evidence showed left/right
comparison chatter.

## Local Screening Evidence

The saved v48 four-track CSV exports were checked without opening MWORKS:

```text
Results/metrics/lateral_hysteresis_screening_v48_20260710.md
```

Result:

```text
chart.steer sign flips = 0 on Track1, Track2, Track3, and Track4
```

Track3 first obstacle and early road-event windows both keep
`obsAvoidController_Sysblock.chart.steer = 0.6`. The controller is not
oscillating between left and right in the event windows.

## Decision

Reject v69 lateral hysteresis before editing source. It is a plausible
physical-robot pattern, but it does not match the current v48 failure evidence.

Do not patch this as another blind mechanism. Continue with:

1. v48 as the current review-ready best controller;
2. report/readiness and physical-transfer deliverables;
3. targeted research or offline analysis only when it identifies a genuinely
   different four-distance mechanism not already covered by v49-v67 or this
   screening.

## Boundary

No source files were changed for this screening. The official no-edit zones
remain untouched.
