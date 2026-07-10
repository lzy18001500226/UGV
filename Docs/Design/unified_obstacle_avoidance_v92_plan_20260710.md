# Unified Obstacle-Avoidance v92 Plan

Status: planned_before_source_edit, 2026-07-10 CST

## Baseline

Continue from the accepted local high-score candidate:

```text
v80 sharp curve speed cap
four-track wrapper score: 38.0 / 40
effective competition target: about 76 / 80
runtime caveat: Track3 still exits early with cR=1, cO=1, P=9.2
```

## Evidence Trigger

The v80 signal-window review shows two different classes of events:

1. Track3 first obstacle event at `1.05 s`:
   - `df ~= 0.013`
   - `dl ~= 0.488`, `dr ~= 0.647`
   - `speed_oa = -1`, `steer_oa = 0.6`
   - `ctrlAlloc.speed ~= 0.72`, `ctrlAlloc.steer ~= 0.16`
2. Track1/2/3/4 road events around `4.35-4.85 s`:
   - `df ~= 2.05`
   - left side distance is already close
   - the fixed `steer_oa = 0.6` behavior is active

Prior rejected candidates cover broad speed clamps, emergency reverse alone,
negative/gap-directed initial steer, steering feedforward, shorter lateral
dwell, guarded release, and side-threshold scans. v92 therefore tests only the
distinct Track3 early-front class and does not touch the later side-road class.

## Candidate Mechanism

When the obstacle controller is in avoid mode and sees a very close front
obstacle while both side distances are still open, treat it as a front-emergency
straight hold:

```modelica
front emergency gate:
  df <= 0.25 and dl > 0.3 and dr > 0.3

longitudinal avoid state:
  speed := -3 under the emergency gate, otherwise -1

avoid_lateral initial state:
  steer := 0 under the emergency gate, otherwise 0.6
```

This is one unified four-sensor rule. It does not branch on track name, wrapper,
score variable, run id, time, or official geometry. It does not edit official
vehicle, road, sensor, scoring, example, or training material files.

## Why This Is Not A Repeated Rejected Scan

- Not v65: v65 changed only emergency reverse speed and kept the fixed positive
  initial lateral steer.
- Not v62/v91: those changed initial lateral direction toward a negative or
  gap-directed steer; v92 freezes lateral steer only inside the very-close-front
  and side-open emergency gate.
- Not v70: it is not a broad active-avoid speed clamp in `ControlAllocate`.
- Not v85/v86: it does not change lateral dwell timing.

## Validation Gate

1. Apply the v92 source edit only to
   `Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo`.
2. Run `Scripts/quality/check_controller_deployability.py --fail-on-high`.
3. Run `UGV.Test.Saidao3Eval` for 120 s first.
4. Accept only if Track3 improves comparably:
   - removes `cO` or `cR`, or improves `P`;
   - does not rely on early-stop `P=10` or short-run artifact;
   - does not regress into unreadable/non-diagnostic output.
5. If Track3 does not improve, reject v92, restore v80 semantics, run the
   restore static gate, record evidence, commit, push, email, and continue with
   the next evidence-backed mechanism.
