# Unified Obstacle Avoidance v64 Plan - Front-Clear Side-Reentry Steering

## Goal

Continue from accepted v48 and test one unified mechanism for road-edge losses
without per-track branches and without editing official no-edit zones.

## Evidence Basis

Current accepted review baseline remains v48:

- `Results/metrics/four_track_candidate_review_v48_opposing_steer_guard_20260710.md`
- `Results/metrics/track3_candidate_review_v63_early_steer_feedforward_20260710.md`
- `Results/metrics/signal_window_summary_v48_all_tracks_timeaxis_fix_20260710.md`

The refreshed v48 all-track event summary shows the remaining road events share
the same shape:

| Track | Event | df | dl | dr | flag | steer_oa |
|---|---:|---:|---:|---:|---:|---:|
| Track1 | 6.55 s | 3.774 | 0.1037 | 0.2667 | 1 | 0.6 |
| Track1 | 30.35 s | 2.025 | 0.1087 | 0.2699 | 1 | 0.6 |
| Track2 | 4.70 s | 2.052 | 0.1089 | 0.2710 | 1 | 0.6 |
| Track3 | 4.85 s | 2.050 | 0.1060 | 0.2708 | 1 | 0.6 |
| Track4 | 4.35 s | 2.052 | 0.1052 | 0.2674 | 1 | 0.6 |
| Track4 | 90.15 s | 2.025 | 0.1087 | 0.2710 | 1 | 0.6 |

The Track3 early obstacle event is different:

```text
time=1.05 s, df=0.013, dl=0.4876, dr=0.6474, steer_oa=0.6
```

Therefore the next candidate should target front-clear side-road re-entry, not
front-obstacle approach.

## Candidate Mechanism

Edit only:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Inside `avoid_lateral.ini_state`, replace the fixed initial command:

```modelica
steer := 0.6;
```

with a front-clear, side-directed rule:

```modelica
if df > mindis and dl < 0.45 and dl < dr then
  steer := -min(0.8, 2 * abs(dl - dr));
elseif df > mindis and dr < 0.45 and dr < dl then
  steer := min(0.8, 2 * abs(dl - dr));
else
  steer := 0.6;
end if;
```

Rationale:

- When front clearance is still dangerous, keep v48 behavior. This avoids
  repeating v62/v63's failed front-obstacle direction scans.
- When front is clear but one side is already near the road threshold, do not
  restart every avoid re-entry with the fixed positive `0.6` steer.
- The rule is based only on live sensor distances, so it is a unified algorithm
  and not a track branch.

## Why This Is Different From Rejected Routes

- Not v31/v41: it does not lengthen or guard longitudinal avoid release.
- Not v36-v38: it does not clamp final steering globally.
- Not v47/v49/v51/v52: it does not add path-speed attenuation or braking.
- Not v62/v63: it does not change front-close obstacle behavior.
- Not a scalar scan: it changes the state-machine re-entry behavior for a
  specific source-observed side-road failure mode.

## Gate

1. Apply the one-source-file patch above.
2. Run `Scripts/quality/check_controller_deployability.py`.
3. Run Track3 first because the candidate should preserve the 1.05 s obstacle
   result while targeting the 4.85 s road event.
4. If Track3 improves or stays comparable without earlier terminal-state
   inflation, run Track4 next.
5. Expand to Track1/Track2 and four-track review only if the weak-track result
   is not worse.
6. Reject and restore v48 if Track3 worsens or if the result is an early-stop
   score artifact.

## Non-Claims

This plan does not create final submission material and does not claim physical
UGV success.
