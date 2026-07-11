# Unified Obstacle Avoidance v109 Plan

Status: planned, 2026-07-11 CST.

## Baseline

Accepted local wrapper baseline remains:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper score: 38.0 / 40
Track3 caveat: simulate_failed/T=59.4,cR=1,cO=1,P=9.2
```

Runtime channel recovery before this candidate:

```text
Results/metrics/runtime_channel_recovery_v80_after_v108_20260711.md
```

## Evidence Basis

v96 showed a useful but unsafe direction:

```text
Docs/Design/unified_obstacle_avoidance_v96_plan_20260710.md
Results/metrics/track1_track3_candidate_review_v96_severe_side_initial_steer_override_20260710.md
```

The v96 severe left-side initial steer override removed the Track3 road
collision (`P=9.2 -> 9.6`) but created a Track1 short-run artifact (`T=4.5`,
`P=10.0`, non-comparable). Therefore the next attempt should not repeat v96's
broad `dl < 0.2 and dr > dl` trigger.

The v80 side-squeeze evidence separates Track1 from Track3/2/4 by lateral
asymmetry:

```text
Track1 road event: dl≈0.101, dr≈0.197, dr-dl≈0.096
Track3 road event: dl≈0.106, dr≈0.271, dr-dl≈0.165
Track2/Track4 road events are similar to Track3 at dr-dl≈0.16
```

## Candidate Mechanism

Modify only the lateral avoid initial action in:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Replace the unconditional initial avoid-lateral command:

```modelica
steer := 0.6;
```

with a narrow asymmetric-left-squeeze override:

```modelica
if dl < 0.18 and dr - dl > 0.14 then
  steer := -0.6;
else
  steer := 0.6;
end if;
```

This is intended to preserve v96's Track3 road-collision benefit while avoiding
the Track1 early-stop trigger whose `dr-dl` is much smaller.

## Difference From Rejected Routes

- Not v96 replay: it adds an asymmetry gate derived from the Track1 regression
  evidence instead of using broad `dr > dl`.
- Not a speed-gate family retry: it changes lateral initial steering only.
- Not v85/v86: it does not shorten or conditionally release the lateral dwell.
- Not v91: it does not replace all initial commands with direct gap steering.
- Not per-track: the rule uses only four-distance geometry.

## Target Gate

1. Run static deployability gate.
2. Run Track3 first.
3. If Track3 does not improve over v80 (`P=9.2,cR=1,cO=1`) or creates an early
   non-comparable artifact, reject and restore v80.
4. If Track3 improves comparably, run Track1 regression before any four-track
   acceptance.

## Non-Claims

- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No final 80/80 score claim.
- No physical UGV success claim.
- No package/submission claim.
