# Unified Obstacle Avoidance v100 Plan

Status: planned before source edit, 2026-07-11 CST.

## Goal

Continue the long score sprint from the accepted local wrapper baseline
`v80_sharp_curve_speed_cap` toward the 80-point target. This candidate must
stay one unified controller for all four tracks and must not edit official
vehicle, road, sensor, scoring, example, or official material files.

Immediate target:

```text
Track3 v80 residual: cR=1, cO=1, P=9.2, T=59.4
```

The first runtime gate is Track3. If Track3 improves without an early-stop
artifact, run Track1 regression next because v96 showed Track1 is sensitive to
initial lateral steering changes.

## Evidence Basis

Current accepted baseline:

```text
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper score: 38.0 / 40
```

The shared v80 road-edge events have a severe side-squeeze pattern:

```text
Track1: dl ~= 0.101, dr ~= 0.197, steer_oa=0.6
Track2: dl ~= 0.109, dr ~= 0.271, steer_oa=0.6
Track3: dl ~= 0.106, dr ~= 0.271, steer_oa=0.6
Track4: dl ~= 0.105, dr ~= 0.267, steer_oa=0.6
```

At the Track3 road event, path steering is already trying to recover:

```text
steer_pp ~= -0.221
steer_oa = 0.6
final_steer ~= 0.185
```

So the remaining issue is not that the path layer lacks any recovery intent;
it is that the lateral obstacle initial state still outputs a fixed `0.6`
command during a side-squeeze window and overpowers the recovery.

## Rejected Routes Not To Repeat

- v96 proved severe negative initial steering can remove Track3 road collision,
  but it produced a Track1 short-run artifact.
- v97 showed a narrower direct negative initial-steer threshold can make Track3
  much worse.
- v98 showed adding front-obstacle memory around the same negative override did
  not improve Track3.
- v99 showed path-only centerline damping can delay but not remove the Track3
  road event.

Therefore v100 must not continue the direct initial-steer override family and
must not repeat path-only damping.

## Candidate Mechanism

Modify only:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

In the lateral avoid initial state, keep the original fixed `0.6` steering for
normal front-risk starts, but reduce initial steering authority during severe
left-side squeeze:

```modelica
if dl < 0.2 and dr > dl then
  steer := 0.2;
else
  steer := 0.6;
end if;
```

This is not a sign flip. It only damps the fixed initial lateral steering when
the side gap already says the vehicle is too close to the left side. The goal
is to let the existing negative path-steering recovery participate without
creating v96-style aggressive countersteer.

The first Track3 obstacle event should remain close to v80 because it has:

```text
df ~= 0.013, dl ~= 0.488, dr ~= 0.647
```

That does not satisfy `dl < 0.2`, so v100 should keep the original `0.6`
initial steer for the near-front obstacle case.

## Acceptance Gate

1. Static deployability checker passes with `high=0`, `medium=0`.
2. Run `UGV.Test.Saidao3Eval` first.
3. Accept expansion only if Track3 improves score variables or road event
   count without a short-run artifact.
4. If Track3 improves, immediately run Track1 regression.
5. Only after Track3 and Track1 pass, expand to Track2 and Track4.

## Rejection Rule

Reject and restore v80 semantics if v100:

- keeps Track3 at `P=9.2,cR=1,cO=1` with materially shorter runtime;
- increases Track3 road or obstacle collisions;
- creates a short-run `P=10` artifact;
- regresses Track1 below v80 when regression is run.

## Non-Claims

- No final 80/80 claim.
- No physical UGV success claim.
- No final submission/package claim.
- No report-polish work.
