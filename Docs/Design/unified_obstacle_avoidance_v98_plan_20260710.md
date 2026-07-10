# Unified Obstacle Avoidance v98 Plan

Status: planned, 2026-07-10 CST.

## Baseline

Accepted local wrapper baseline:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper score: 38.0 / 40
effective contest target: about 76 / 80
```

Latest rejected candidates:

```text
v96_severe_side_initial_steer_override
v97_narrow_left_squeeze_initial_override
```

v96 showed that a severe-left initial negative steer can remove the Track3 road
collision (`cR=1 -> 0`) but it also made Track1 stop at `T=4.5` with a
non-comparable `P=10.0` artifact. v97 narrowed the side-distance gate but
regressed Track3 to `cR=13`, so another direct side-distance initial-steer gate
is not justified.

## Evidence Basis

The current v80 Track3 failure has two stages:

```text
1.05 s: front obstacle event, df ~= 0.013, cO 0 -> 1
4.85 s: road event, dl ~= 0.108, cR 0 -> 1
```

Track1 has the later side-road geometry but does not have the same near-front
obstacle precondition. Therefore the new candidate tests a stateful gate: only
after the same avoid episode has observed a near-front obstacle may the
controller use the left-side recovery behavior that helped Track3.

## Candidate Mechanism

Modify only:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Add an internal boolean memory in the chart:

```modelica
front_close_seen(start=false)
```

Longitudinal state behavior:

```modelica
cruise: front_close_seen := false
avoid:  if df < 0.2 then front_close_seen := true; end if
```

Lateral avoid initial state behavior:

```modelica
if front_close_seen and dl < 0.2 and dr > dl then
  steer := -0.6;
else
  steer := 0.6;
end if;
```

The rule remains one unified four-distance controller. It does not branch on
track name, wrapper, time, score variables, official geometry, or result files.

## Difference From Rejected Routes

- Not v96: v96 allowed the negative initial steer on side geometry alone; v98
  requires a prior near-front obstacle in the same avoid episode.
- Not v97: v97 only narrowed the side threshold; v98 changes the state
  precondition and avoids repeating the same side-only gate.
- Not v92-v95: v98 does not change speed, path-speed suppression, or obstacle
  steer filtering.
- Not a per-track patch: the trigger uses only `df`, `dl`, `dr`, and internal
  avoid-state memory.

## Validation Gate

1. Run the source deployability checker with `--fail-on-high`.
2. Run `UGV.Test.Saidao3Eval` first for 120 s.
3. If Track3 does not improve `P`, `cR`, `cO`, or comparable runtime versus
   v80, reject and restore v80 semantics.
4. If Track3 improves, run Track1 regression immediately because v96 failed
   there.
5. Expand to Track2/Track4 only if Track1 remains comparable.

## Non-Claims

- No official vehicle, road, sensor, scoring, example, or official material
  edits.
- No final 80/80 claim.
- No physical UGV success claim.
- No report/package work.
