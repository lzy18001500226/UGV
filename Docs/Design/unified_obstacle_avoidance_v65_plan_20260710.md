# Unified Obstacle-Avoidance v65 Plan

Status: planned_before_source_edit, 2026-07-10 CST

## Baseline

Continue from accepted review candidate v48:

```text
v48 opposing-steer guard
total wrapper score: 37.2
runtime caveat: Track2/3/4 have readable score variables after terminal-state caveats
```

## Evidence Trigger

Track3 v48 first obstacle event shows:

```text
avoid flag active from about 0.12 s
df drops to about 0.013 by 1.05 s
final allocated speed is still about 0.51 at 1.05 s
```

The failure is therefore not a missing avoid-state transition. It is a missing
collision-imminent low-speed hold after avoid mode is already active.

## Mechanism

Inside the existing `avoid` longitudinal state only:

```modelica
if df <= 0.25 then
  speed := -3;
else
  speed := -1;
end if;
flag := true;
```

This keeps one unified controller for all tracks. It does not branch by track,
wrapper, score variable, or run id. It does not edit official vehicle, road,
sensor, scoring, or example packages.

## Why This Is Not A Repeated Rejected Scan

- It is not a broad speed-channel gain scan like v21/v28.
- It is not side-danger speed regulation like v29.
- It is not v35 front-open braking, which used a broad `df <= 0.9 and open side`
  condition.
- It is not path-speed attenuation, brake-turn coupling, or path-steer
  neutralization.

The only question is whether a very narrow collision-imminent band can remove
the early Track3 obstacle event without destroying comparability.

## Validation Gate

1. Run `check_controller_deployability.py --fail-on-high`.
2. Run `UGV.Test.Saidao3Eval` first for 120 s as `v65_front_emergency_hold`.
3. Accept only if Track3 improves against v48 without non-comparable early-stop
   artifacts.
4. If Track3 does not improve or early-stops, reject v65, restore v48
   semantics, run the restore static gate, record evidence, send a sparse email,
   and continue with the next mechanism or research.
