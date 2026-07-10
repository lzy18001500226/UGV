# Track3 Candidate Review - v100 Side-Squeeze Initial Damping

Status: rejected, 2026-07-11 CST.

## Baseline

Accepted baseline remains:

```text
v80_sharp_curve_speed_cap
Results/metrics/four_track_candidate_review_v80_sharp_curve_speed_cap_20260710.md
wrapper total: 38.0 / 40
Track3: simulate_failed, T=59.4, cR=1, cO=1, P=9.2
```

## Candidate

Plan:

```text
Docs/Design/unified_obstacle_avoidance_v100_plan_20260711.md
```

Mechanism tested in the lateral avoid initial state:

```modelica
if dl < 0.2 and dr > dl then
  steer := 0.2;
else
  steer := 0.6;
end if;
```

This candidate intentionally did not use a negative initial-steer override. It
only reduced the fixed initial obstacle-avoidance steering authority during a
severe side-squeeze window.

## Static And Syntax Gate

The first source form used an inline `if ... then ... else ...` expression in a
state-machine action and failed `CheckModel`:

```text
Results/simulations/controller_v100_side_squeeze_initial_damping_saidao3_120s_20260711/
error: 状态机内暂不支持if表达式
```

The logic was rewritten as a normal `if` statement block. Static deployability
then passed:

```text
Results/evidence/controller_deployability_static_check_v100_side_squeeze_initial_damping_stmt_20260711.md
ready_for_physical_claim=true
high=0
medium=0
```

## Runtime Result

Track3 runtime evidence:

```text
Results/simulations/controller_v100_side_squeeze_initial_damping_stmt_saidao3_120s_20260711/
simulate_returned_true
exit_state=0
T=120.0
cR=3
cO=1
P=8.4
```

Comparison:

```text
v80 Track3:  T=59.4,  cR=1, cO=1, P=9.2
v100 Track3: T=120.0, cR=3, cO=1, P=8.4
```

v100 improves runtime completeness but materially worsens score variables, so
it is not accepted.

## Diagnostics

Collision windows:

```text
Results/metrics/collision_window_analysis_v100_side_squeeze_initial_damping_track3_20260711.md
```

Events:

```text
1.05s:  cO 0 -> 1
4.85s:  cR 0 -> 1
26.35s: cR 1 -> 2
32.45s: cR 2 -> 3
```

Signal summary:

```text
Results/metrics/signal_window_summary_v100_side_squeeze_initial_damping_track3_20260711.md
```

Key observation:

```text
4.85s:  steer_oa=0.2, steer_pp=-0.221, final steer=0.130, cR still occurs
26.35s: steer_oa=0.2, steer_pp=-0.097, final steer=0.050, new cR
32.45s: steer_oa=0.2, steer_pp=0.606, final steer=0.714, new cR
```

Reducing initial obstacle-avoidance steering authority does not remove the
first road event and introduces later road-edge weakness.

## Decision

Reject v100. Do not expand to Track1/2/4 because Track3 already regressed from
`P=9.2` to `P=8.4`.

Source was restored to the accepted v80 semantics after this review and
rechecked:

```text
Results/evidence/controller_deployability_static_check_v80_restored_after_v100_20260711.md
ready_for_physical_claim=true
high=0
medium=0
```

## Reusable Learning

- Inline `if` expressions are not accepted inside this Sysblock state-machine
  action context; use statement blocks when conditional state actions are
  needed.
- Damping the lateral avoid initial steer from `0.6` to `0.2` during side
  squeeze is too weak for the first road event and creates later road
  collisions.
- Future candidates should avoid direct initial-steer sign flips and avoid
  simple initial-steer magnitude scans. The next useful direction should
  inspect trajectory/state timing or a smoother recovery that is active after
  the initial 2 s window, not only at entry.

No final 80/80 claim, physical UGV success claim, report readiness claim, or
submission claim is made from v100.
