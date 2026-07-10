# Unified Obstacle Avoidance v101 Plan - Narrow Conflict Handoff

Status: planned for verification, 2026-07-11 CST.

## Baseline

Current accepted candidate:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
local wrapper total: 38.0 / 40, equivalent target 76 / 80
```

Known v80 weak points:

```text
Track1: cR=1, cO=0, P=9.6, T=17.4, simulate_failed
Track2: cR=1, cO=0, P=9.6, T=120.0, simulate_returned_true
Track3: cR=1, cO=1, P=9.2, T=59.4, simulate_failed
Track4: cR=1, cO=0, P=9.6, T=120.0, simulate_returned_true
```

## Evidence Behind This Candidate

The v80 early road events share the same obstacle-avoidance state:

```text
df ~= 2.05
dl ~= 0.10
speed_oa = -1
steer_oa = 0.6
```

The difference is path-steer conflict:

```text
Track1: steer_pp is positive, final steer ~= 0.57
Track2/3/4: steer_pp is negative, final steer ~= 0.18
```

v96 showed that changing the initial obstacle steer can remove Track3's road
event, but it created a Track1 early-stop artifact. v100 showed that reducing
the initial steer to `0.2` is too weak and introduces later road collisions.

v101 therefore does not change the lateral state-machine initial steer. It
changes only the path/avoidance arbitration when the path planner is steering
against a severe left-side obstacle-avoidance command.

## Candidate Mechanism

File:

```text
Models/UGV/Control/ControlAllocate/package.mo
```

Replace the current v80/v48 conflict handoff:

```modelica
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0
  then 0.5 * unitDelay1.y
  else unitDelay1.y;
```

with:

```modelica
gain3.u = if speed_oa < 0 and steer_oa > 0 and unitDelay1.y < 0
  and steer_oa * unitDelay1.y < 0
  and abs(steer_oa) > 0.55
  then 0.25 * unitDelay1.y
  else if speed_oa < 0 and steer_oa * unitDelay1.y < 0
  then 0.5 * unitDelay1.y
  else unitDelay1.y;
```

This is a unified rule. It does not branch on track name, wrapper name, score
variables, time, or run id.

## Verification Gate

1. Run source-only deployability check after the edit.
2. Run Track3 first because it has the largest remaining score deficit.
3. If Track3 improves without early-stop artifact, run Track1 regression.
4. If Track1 is not worse, expand to Track2 and Track4.

Acceptance:

```text
Accept only if the four-track local wrapper total exceeds v80 38.0 / 40,
or if the candidate removes Track3 road collision without worsening Track1
runtime comparability and score.
```

Reject immediately if:

```text
Track3 P drops below 9.2
Track3 cR increases
Track1 shows a short early-stop artifact comparable to rejected v96
static deployability checker reports high or medium risk
```

## Non-Claims

This plan does not claim final competition score, report readiness, generated
code success, physical UGV success, or final submission approval.
