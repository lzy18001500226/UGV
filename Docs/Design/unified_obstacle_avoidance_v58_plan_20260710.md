# Unified Obstacle Avoidance v58 Plan - Reactive Gap Initial Bypass

timestamp: 2026-07-10 CST
baseline: v48 opposing-steer guard
scope: one unified controller mechanism for all four official tracks

## Purpose

v55-v57 did not improve Track3 because they only changed low-speed planner
lookahead, obstacle-speed filtering, or the front trigger threshold. The v48
Track3 evidence shows both score losses occur in the first five seconds:

| Event | Time/s | v48 evidence |
|---|---:|---|
| obstacle collision | 1.05 | `df=0.8306`, `dl=0.5677`, `dr=0.5673`, `flag=1`, `final_speed=0.7196`, `final_steer=0.1623` |
| road collision | 4.85 | `df=0.07106`, `dl=0.5177`, `dr=0.6173`, `flag=1`, `final_speed=0.5105`, `final_steer=0.1849` |

The next attempt should therefore target the early bypass behavior, not another
late-run scalar scan.

## Research Basis

Reference manifest:

```text
References/research/reactive_gap_obstacle_avoidance_20260710/MANIFEST.md
```

The directly transferable pattern is not a full VFH/DWA implementation. The
current controller has only four distance inputs, so v58 uses a compact
gap-navigation idea:

```text
front-risk detection
  -> choose an open side only when side evidence is strong
  -> otherwise keep a bounded default initial arc
  -> release through existing v48 hysteresis/timing
```

## Candidate Change

Keep v48 longitudinal logic and ControlAllocate logic. Modify only the
obstacle controller lateral startup state:

1. During the initial lateral avoid state, inspect side-distance imbalance.
2. If the left side is clearly more open than the right side, use a bounded
   left-bypass steering command.
3. If the right side is clearly more open than the left side, use a bounded
   right-bypass steering command.
4. If neither side is clearly open, keep the existing bounded default initial
   arc instead of using a larger blind steering constant.

This is intentionally different from rejected v17/v18:

- v17 changed the fixed startup steering from `0.6` to `0.8` everywhere.
- v18 changed it to `0.45` everywhere.
- v58 changes only the startup steering direction/authority when side evidence
  is strong enough; otherwise it preserves the v48 default behavior.

## Initial Parameter Choice

Use conservative, explainable thresholds:

```text
side_gap_delta = 0.12
default_initial_steer = 0.6
gap_initial_steer = min(0.8, 0.6 + abs(dl - dr))
```

Rationale:

- v48/v55 Track3 first obstacle event has `abs(dl-dr) ~= 0.0004`, so v58 should
  not overreact at that exact ambiguous moment.
- v48 Track3 road event has right side about `0.10` more open than left; the
  first test uses `0.12` to avoid reacting to noise. If no effect is observed,
  the next evidence-backed candidate may test a lower side-gap threshold, but
  only after recording v58.

## Acceptance Gate

Run Track3 first because it is the active weak-track focus:

```powershell
python Scripts\quality\check_controller_deployability.py --repo C:\Users\HP\Desktop\UGV --md-out Results\evidence\controller_deployability_static_check_v58_reactive_gap_initial_bypass_20260710.md --json-out Results\evidence\controller_deployability_static_check_v58_reactive_gap_initial_bypass_20260710.json

python Scripts\mworks\ugv_baseline_probe.py --project-root C:\Users\HP\Desktop\UGV --model-name UGV.Test.Saidao3Eval --stop-time 120 --out-dir Results\simulations\controller_v58_reactive_gap_initial_bypass_saidao3_120s_20260710 --request-id v58_track3 --run-label controller_v58_reactive_gap_initial_bypass_saidao3_120s_20260710 --controller-version v58_reactive_gap_initial_bypass --extra-var-substring CountPoint --extra-var-substring obsAvoidController_Sysblock --extra-var-substring ctrlAlloc --save-variable-names --use-simulate-ex --relax-translation-checks
```

Accept v58 only if Track3 improves one of these without introducing an obvious
non-comparable early stop:

- lower `cO` or `cR`;
- higher `P`;
- materially better terminal/runtime status with equal score and no new Track1
  regression after follow-up.

If Track3 does not improve, reject v58, restore v48 semantics, record the
review/static gate evidence, send a sparse Chinese terminal notice, commit, and
continue with the next evidence-backed mechanism instead of stopping.

## Boundaries

- Do not edit official vehicle, road, sensor, scoring, example, or official
  material files.
- Do not create a final submission package from this candidate.
- Do not claim physical UGV success from static or wrapper evidence.
