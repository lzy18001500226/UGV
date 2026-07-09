# Unified Obstacle Avoidance v66 Plan - Road-Edge Initial Steering Boost

timestamp: 2026-07-10 06:16 CST
baseline: v48 opposing-steer guard
scope: one unified controller mechanism for all four official tracks

## Purpose

Continue the long controller task after v65 rejection without repeating blind
scalar tuning.

The v48 Track3 attribution note shows:

```text
Results/evidence/track3_v48_event_source_attribution_20260710.md
Results/metrics/track3_v48_countpoint_source_attribution_20260710.md
```

Both Track3 score events occur while `flag=1` and while `steer_oa` is the
fixed initial avoid-lateral command `0.6`. v59 proved that switching the
initial direction can create early-stop artifacts, and v62 proved that a
front-centered negative initial bypass worsens Track3. v66 therefore keeps
v48's initial direction and changes only the magnitude in a narrow road-edge
window.

## Candidate Change

Modify only:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Inside the `avoid_lateral` initial state, replace:

```modelica
steer := 0.6;
```

with:

```modelica
if dl < 0.16 or dr < 0.16 then
  steer := 0.8;
else
  steer := 0.6;
end if;
```

Interpretation:

- Keep the default v48 direction and default magnitude in normal avoid entries.
- Add a bounded boost only when a side distance is already near the official
  road-collision threshold.
- Do not branch on track name, wrapper name, score variables, or run id.
- Do not edit official vehicle, road, sensor, scoring, example, or official
  material files.

## Why This Is Not A Repeated Rejected Route

- Not v17: v17 globally changed the initial steering magnitude; v66 gates the
  boost on side-distance road-edge risk.
- Not v30: v30 changed later side-distance steering floor under v13; v66
  targets the fixed initial avoid-lateral state under the current v48 baseline.
- Not v59/v62: v66 does not switch the initial direction.
- Not v65: v66 does not change reverse speed or front emergency hold.

## Acceptance Gate

Run Track3 first because the target evidence is the v48 Track3 road event:

```powershell
python Scripts\quality\check_controller_deployability.py --repo C:\Users\HP\Desktop\UGV --md-out Results\evidence\controller_deployability_static_check_v66_road_edge_initial_steer_boost_20260710.md --json-out Results\evidence\controller_deployability_static_check_v66_road_edge_initial_steer_boost_20260710.json

& 'D:\Program Files\MWORKS\Sysplorer 2026a\External\python64\python.exe' Scripts\mworks\ugv_baseline_probe.py --project-root C:\Users\HP\Desktop\UGV --model-name UGV.Test.Saidao3Eval --stop-time 120 --out-dir Results\simulations\controller_v66_road_edge_initial_steer_boost_saidao3_120s_20260710 --request-id v66_track3 --run-label controller_v66_road_edge_initial_steer_boost_saidao3_120s_20260710 --controller-version v66_road_edge_initial_steer_boost --extra-var-substring CountPoint --extra-var-substring obsAvoidController_Sysblock --extra-var-substring ctrlAlloc --save-variable-names --use-simulate-ex --relax-translation-checks
```

Accept v66 only if Track3 improves against v48's accepted review metrics:

```text
T=112.45, cR=1, cO=1, P=9.2
```

If Track3 does not improve, immediately restore v48 semantics, save rejection
evidence, send the sparse terminal notice, commit, push, and continue to the
next evidence-backed mechanism or research path.

If Track3 improves, run Track1 regression before any four-track expansion
because earlier initial-steering changes produced Track1 early-stop artifacts.

## Non-Claims

This plan does not claim final competition score, physical UGV readiness, or
final submission approval.
