# Unified Obstacle Avoidance v97 Plan

Status: planned, 2026-07-10 CST

## Goal

Improve the current accepted v80 score candidate without creating another
Track1 early-stop artifact. The target is Track3's road-collision event while
preserving Track1 runtime comparability.

## Baseline

Current accepted baseline:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper total: 38.0 / 40
Track1: T=17.4, cR=1, cO=0, P=9.6
Track3: T=59.4, cR=1, cO=1, P=9.2
```

Rejected v96 learning:

```text
if dl < 0.2 and dr > dl then steer := -0.6 else steer := 0.6
```

This removed Track3's road collision but caused a Track1 short-run artifact:

```text
Track1 v96: T=4.5, cR=0, cO=0, P=10.0
```

## Evidence Used

Track3 v80 road event:

```text
t=4.85, df=2.05, dl=0.1083, dr=0.2731, dr-dl=0.1648
```

Track1 v96 early-stop tail:

```text
t=4.50, df=2.05, dl=0.1533, dr=0.2673, dr-dl=0.1140
```

## Candidate Mechanism

Narrow the initial lateral override so it applies only to a severe asymmetric
left-side squeeze:

```modelica
if df > 1.8 and dl < 0.13 and dr - dl > 0.13 then
  steer := -0.6;
else
  steer := 0.6;
end if;
```

This is a unified sensor-geometry rule, not a per-track branch.

## Acceptance Gate

1. Static deployability checker passes with `high=0, medium=0`.
2. Track3 improves versus v80 or at least removes the v80 road collision.
3. Track1 does not regress into a short-run artifact like v96.
4. Only if Track1 and Track3 pass, expand to Track2 and Track4.

## Rejection Rule

Reject and restore v80 if Track1 runtime becomes materially shorter than v80,
or if Track3 does not improve enough to justify the change.
