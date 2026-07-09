# Four-Track Candidate Review: v48 Opposing-Steer Guard

Status: review_ready_new_best_candidate_with_runtime_caveat, 2026-07-10 CST

## Summary

v48 continues from accepted v45 and adds one unified ControlAllocate mechanism:

```modelica
gain3.u = if speed_oa < 0 and steer_oa * unitDelay1.y < 0 then
  0.5 * unitDelay1.y
else
  unitDelay1.y;
```

The intent is to reduce path-planner steering cancellation only when obstacle
avoidance is actively reversing and the obstacle steering command opposes the
path steering command. It is not a per-track branch and does not edit official
vehicle, road, sensor, scoring, example, or track files.

## Four-Track Evidence

| Track | Evidence | Runtime | Exit | T/s | cR | cO | P |
|---|---|---|---:|---:|---:|---:|---:|
| Saidao1Eval | `Results/simulations/controller_v48_opposing_steer_guard_saidao1_120s_20260710/` | `simulate_returned_true` | 0 | 120.0 | 2 | 0 | 9.2 |
| Saidao2Eval | `Results/simulations/controller_v48_opposing_steer_guard_saidao2_120s_20260710/` | `simulate_failed` with result variables | 2 | 60.15 | 1 | 0 | 9.6 |
| Saidao3Eval | `Results/simulations/controller_v48_opposing_steer_guard_saidao3_120s_20260710/` | `simulate_failed` with result variables | 2 | 112.45 | 1 | 1 | 9.2 |
| Saidao4Eval | `Results/simulations/controller_v48_opposing_steer_guard_saidao4_120s_20260710/` | `simulate_failed` with result variables | 2 | 112.4 | 2 | 0 | 9.2 |

Total wrapper score:

```text
v45: 36.8
v48: 37.2
delta: +0.4
```

Compared with v45:

- Track1 improves from `P=8.8`, `cR=3`, `cO=0` to `P=9.2`, `cR=2`, `cO=0`.
- Track2 stays at `P=9.6`, `cR=1`, `cO=0`, but stops at `T=60.15` with
  `simulate_failed`.
- Track3 stays at `P=9.2`, `cR=1`, `cO=1`, but stops at `T=112.45` with
  `simulate_failed`.
- Track4 stays at `P=9.2`, `cR=2`, `cO=0`, but stops at `T=112.4` with
  `simulate_failed`.

## Static And Runtime Gates

Source and model gates:

```text
Results/evidence/controller_deployability_static_check_v48_opposing_steer_guard_20260710.md
```

The checker reports `ready_for_physical_claim=true`, `high=0`, `medium=0` for
the obstacle-controller source. Because v48 changes `ControlAllocate/package.mo`,
the acceptance basis also requires the saved four-track `CheckModel=true` and
runtime result-variable evidence above.

Important caveat: Track2, Track3, and Track4 are scored from exported result
variables after `SimulateModel` returned false with `exit_state=2`. This is the
same evidence path used by prior M6 wrapper evaluations, but v48 is not final
competition or physical UGV proof.

## Decision

Accept v48 as the current review-ready best candidate for continued long-task
development because it improves total wrapper score to `37.2` without worsening
the recorded `P/cR/cO` score variables on any track. Keep the terminal-state
caveat visible and continue with evidence-backed unified mechanisms rather than
final packaging.

Operational note: pushing the prior local v47 closeout commit failed because
GitHub was unreachable on port 443. This is a Git/network blocker, not a reason
to stop controller tuning.
