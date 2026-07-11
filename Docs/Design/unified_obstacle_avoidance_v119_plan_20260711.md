# Unified Obstacle Avoidance v119 Plan

Status: rejected after target-track regression; v80 source semantics restored,
2026-07-11 CST.

## Goal

Keep four-track completion as the first hard gate. Test one unified allocation
mechanism from restored v80 semantics, without editing official vehicle, road,
sensor, scoring, example, track, or official-material files.

## Evidence Basis

Track3 v80 enters avoidance before both early events. At the obstacle event
(`t=1.05 s`) and road event (`t=4.85 s`), the obstacle heading offset is
positive while the path heading is negative. The blended desired heading is
therefore driven away from the path:

```text
t=1.05: steer_oa=+0.6, steer_pp=-0.0386, final=+0.1623, cO 0->1
t=4.85: steer_oa=+0.6, steer_pp=-0.2204, final=+0.1855, cR 0->1
```

v53/v75 reduced or removed path-heading authority and failed. v118 reversed
the obstacle offset and reached 120 s, but regressed Track3 to `cR=2`, `cO=2`,
`P=8.4`. Neither candidate tested preserving the path heading while suppressing
only the conflicting obstacle offset.

## Candidate

Modify only `Models/UGV/Control/ControlAllocate/package.mo`:

```modelica
firstOrder.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0
  then 0
  else gain.y;
```

This is track-agnostic. It does not change path speed, reverse authority,
sensor thresholds, or the path planner. It only prevents the obstacle heading
offset from overriding the path heading when the two commands disagree.

## Validation

1. Run source tests and deployability static check.
2. Run the Track3 1 s translation/simulation gate.
3. Run Track3 to 120 s with collision, position, finish-distance, and path
   progress evidence.
4. Continue to Track1 regression only if Track3 shows a comparable completion
   or material progress/collision gain without a new abnormal stop.
5. Expand to all four tracks only after target and regression gates pass.
6. Reject and restore v80 immediately if the target gate regresses or merely
   creates a non-comparable early-stop score artifact.

No completion, `80/80`, physical-car, package, or submission claim may be made
without the corresponding saved evidence.

## Outcome

The 1 s translation/simulation gate passed, but the 120 s Track3 request
stopped abnormally at `T=2.4 s` with `cR=0`, `cO=1`, `P=9.6`, and
`exit_state=2`. This is far shorter than v80 Track3 (`T=59.4`) and is not a
score gain. v119 was rejected and the direct obstacle-offset connection was
restored. See
`Results/metrics/track3_candidate_review_v119_conflicting_avoid_offset_suppression_20260711.md`.
