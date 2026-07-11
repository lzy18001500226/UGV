# v132 Side-Hold Progress State Plan

Status: rejected; v80 semantics restored.

## Evidence

The unchanged v80 Track2 diagnostic shows that the longitudinal controller is
in avoidance for 98.58 percent of the first 120 s.  At 100-120 s, the front
distance is about 1.316 m (above `mindis=1`), while the right side remains near
0.14 m.  The controller therefore continuously exports `speed_oa=-1`; with the
existing allocator this reduces vehicle speed to about 0.058 m/s even though
the path planner requests 0.55 m/s.

The unchanged v80 700 s completion gate then stops abnormally at 305.15 s,
with only path index 30/231 and no origin return.  This disproves the idea that
Track2 simply needed a longer fixed horizon.

Evidence roots:

```text
Results/simulations/diagnostic_v80_track2_speed_state_120s_20260712/
Results/simulations/controller_v80_track2_completion_gate_700s_20260712/
```

## Candidate

Add one longitudinal `side_hold` state in the editable obstacle controller.

1. Existing `avoid` remains the complete two-second reverse safety action.
2. After that action, when the front is clear but either side remains near,
   transition to `side_hold` instead of returning to `cruise` and immediately
   re-entering `avoid` on the next sample.
3. `side_hold` retains `flag=true` so the existing lateral safety state remains
   active, but exports forward speed `1` rather than repeated reverse speed.
4. A new front risk (`df <= mindis`) immediately returns to full `avoid`.
5. Only when front and both sides clear does `side_hold` release to `cruise`.

This differs from rejected v43: side risk is not removed from the controller;
it continues to own the lateral guard. It differs from rejected v125/v126:
the reverse command magnitude is not tuned. It differs from v120-v122: it does
not hold or rewrite the lateral gap-direction state across the longitudinal
release pulse.

## Scope

Only edit:

```text
Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
```

Do not edit the vehicle, road, track, scoring, wrapper, or allocator model.

## Gates

1. Static deployability checker and `python -m pytest Scripts/tests -q` pass.
2. Track2 1 s `-gui` load/check/simulate gate passes.
3. Track2 120 s diagnostic must show substantially lower persistent-reverse
   occupancy and must not create an abnormal early stop or new collision.
4. Only then run a bounded 700 s Track2 completion gate.
5. Expand to the other tracks only for a verified Track2 completion or a
   material, comparable progress improvement without collision regression.
6. Restore the exact v80 controller if any target gate fails.

No official finish, 80-point score, physical-car result, report readiness, or
submission claim is made by this plan.

## Decision

The target Track2 120 s diagnostic failed the third gate and therefore did not
enter the 700 s completion gate or four-track regression.

| Controller | Runtime | T/s | cR | cO | P | Finish-distance squared |
|---|---:|---:|---:|---:|---:|---:|
| v80 comparison baseline | returned true | 120.0 | 1 | 0 | 9.6 | 813.7304 |
| v132 side-hold | failed, exit state 2 | 43.6 | 2 | 0 | 9.2 | 761.4365 |

The candidate created one additional road collision, stopped well before the
120 s diagnostic horizon, and reduced the avoidance score. A smaller terminal
distance alone is not accepted as progress because no official origin-return
finish was observed. The `side_hold` state, parameterized `avoid` speed, and
its transitions were removed; the controller is semantically restored to v80.

Evidence:

```text
Results/simulations/diagnostic_v132_side_hold_progress_track2_120s_20260712/
Results/evidence/controller_deployability_static_check_v80_restored_after_v132_20260712.md
```
