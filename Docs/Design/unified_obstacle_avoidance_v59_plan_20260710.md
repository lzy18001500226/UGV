# Unified Obstacle Avoidance v59 Plan - Close-Side Initial Direction Guard

timestamp: 2026-07-10 CST
baseline: v48 opposing-steer guard
scope: one unified controller mechanism for all four official tracks

## Purpose

v58 rejected the broad side-gap initial bypass route because it reduced road
collisions but increased Track3 obstacle collisions. The useful evidence is
more specific:

- v48 Track1 second road-collision window at `30.35 s` has `dl=0.2055`,
  `dr=0.3704`, `flag=1`, and `steer_oa=0.6`.
- That looks like the lateral sub-state is in its fixed initial steering
  window while the left side is already close.
- v58's stronger side-gap bypass is too broad: it can trigger at moderate side
  distances and trade road safety for obstacle collisions.

v59 tests a narrower rule: only when one side is very close, choose the initial
avoid-lateral steering direction away from the closer side. Do not increase the
steering magnitude above v48's default `0.6`.

## Candidate Change

Modify only the avoid-lateral initial state in:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Candidate logic:

```modelica
if dl < 0.25 and dr - dl > 0.12 then
  steer := -0.6;
elseif dr < 0.25 and dl - dr > 0.12 then
  steer := 0.6;
else
  steer := 0.6;
end if;
```

Interpretation:

- Keep the default v48 initial steering for ambiguous or non-critical side
  windows.
- Change only direction, not magnitude, in a close-side edge-risk window.
- This is not a per-track branch and does not read score variables.

## Why This Is Not v58 Repeated

v58 changed initial steering whenever a side looked clearly more open and could
raise steering to `0.8`. v59 requires a close-side risk (`dl < 0.25` or
`dr < 0.25`) and keeps magnitude at `0.6`.

Expected effect:

- Track1 may improve because the second v48 road-collision window has
  `dl=0.2055`, `dr=0.3704`.
- Track3's first obstacle event should remain unchanged because both side
  distances are around `0.567`.
- Track3's v58-added later obstacle event around `dl=0.4228`, `dr=0.5876`
  should also remain unchanged because neither side is below `0.25`.

## Acceptance Gate

Run Track1 first because this candidate targets a Track1 road-collision
mechanism:

```powershell
python Scripts\quality\check_controller_deployability.py --repo C:\Users\HP\Desktop\UGV --md-out Results\evidence\controller_deployability_static_check_v59_close_side_initial_direction_20260710.md --json-out Results\evidence\controller_deployability_static_check_v59_close_side_initial_direction_20260710.json

& 'D:\Program Files\MWORKS\Sysplorer 2026a\External\python64\python.exe' Scripts\mworks\ugv_baseline_probe.py --project-root C:\Users\HP\Desktop\UGV --model-name UGV.Test.Saidao1Eval --stop-time 120 --out-dir Results\simulations\controller_v59_close_side_initial_direction_saidao1_120s_20260710 --request-id v59_track1 --run-label controller_v59_close_side_initial_direction_saidao1_120s_20260710 --controller-version v59_close_side_initial_direction --extra-var-substring CountPoint --extra-var-substring obsAvoidController_Sysblock --extra-var-substring ctrlAlloc --save-variable-names --use-simulate-ex --relax-translation-checks
```

Accept only if Track1 improves against v48 (`T=120.0`, `cR=2`, `cO=0`,
`P=9.2`) without an early-stop artifact. If Track1 improves, immediately run
Track3 regression before four-track expansion. If Track1 does not improve,
restore v48 and reject v59.

## Boundaries

- No edits to official vehicle, road, sensor, scoring, example, or official
  material files.
- No final package or final submission.
- Static and wrapper evidence do not prove physical UGV success.
