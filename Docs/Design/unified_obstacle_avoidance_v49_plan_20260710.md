# Unified Obstacle Avoidance v49 Plan

Status: planned_candidate, 2026-07-10 CST

## Goal

Continue from accepted v48 and test one unified mechanism across the official
wrapper tracks. Do not branch by track and do not edit official vehicle, road,
sensor, scoring, example, or official material files.

## Evidence Basis

Current best:

```text
v48 opposing-steer guard
Results/metrics/four_track_candidate_review_v48_opposing_steer_guard_20260710.md
```

Post-v48 analysis shows the Track3 early obstacle collision at about `1.05 s`
occurs while obstacle avoidance is already active:

```text
speed_pp = 1
speed_oa = -1
oa_speed_filtered ~= -0.2804
final_speed ~= 0.7196
df ~= 0.8306
dl ~= 0.5677
dr ~= 0.5673
```

This means the remaining early obstacle contact is not simply a missing
trigger. The trigger is active, but the path-planner speed contribution still
dominates before the filtered obstacle speed contribution catches up.

Rejected adjacent routes:

- v24 made obstacle-avoidance filters faster and did not improve Track3.
- v28/v46 increased speed-channel gain and shortened runtime without score
  improvement.
- v35 stronger front braking triggered but still did not improve Track3.

Therefore v49 should not increase reverse speed, speed-channel gain, or shorten
the obstacle filter again.

## Candidate Mechanism

Add a path-speed authority reduction in `ControlAllocate`:

```modelica
gain2.u = if speed_oa < 0 then 0.6 * unitDelay3.y else unitDelay3.y;
```

Keep the existing v48 opposing-steer guard:

```modelica
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0
  then 0.5 * unitDelay1.y
  else unitDelay1.y;
```

Rationale:

- During obstacle avoidance, reduce forward path-speed authority instead of
  making the reverse command more aggressive.
- Preserve path planning when no obstacle avoidance is active.
- Keep the behavior deployable as bounded scalar command arbitration.
- Remain one algorithm for all four tracks.

## Edit Scope

Allowed source edit:

```text
Models/UGV/Control/ControlAllocate/package.mo
```

No changes to:

```text
Models/UGV/Vehicle/
Models/UGV/Road/
Models/UGV/saidao/
Models/UGV/CountPoint/
Models/UGV/Example/
References/official_materials/
```

## Gates

1. Run the deployability static checker with `--fail-on-high`.
2. Run Track3 first because the mechanism targets the early obstacle contact.
3. Accept only if Track3 improves score or collision count without an
   obviously non-comparable early stop.
4. If Track3 improves, run four-track regression.
5. If Track3 does not improve, reject v49, restore v48 source semantics,
   record the review, send the sparse terminal email, and continue with the
   next evidence-backed mechanism or targeted research.

## Non-Claims

- This is not a final competition score claim.
- This is not physical UGV proof.
- This does not authorize final submission packaging or sending.
