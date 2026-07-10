# Track2 Candidate Review - v89 Side-Squeeze Marker

Status: rejected_as_accepted_baseline, 2026-07-10 CST

## Candidate

v89 tested a narrow unified mechanism after v87/v88 failed to improve Track2:

- In the front-clear left side-squeeze window, mark the obstacle-avoidance steer
  command with `steer := 1.0`.
- In `ControlAllocate`, only when reversing and the marked avoid steer opposes
  negative path steering, neutralize the path contribution.

The first source attempt used an inline `if ... then ... else ...` expression in
a state-machine action and failed `CheckModel` because MWORKS does not support
inline if expressions there. The candidate was rewritten as a normal
`if ... then ... else ... end if` statement, matching the existing Sysblock
state-machine pattern.

## Target Gate

Target track:

```text
UGV.Test.Saidao2Eval
```

Accepted v80 baseline:

```text
T=120.0
cR=1
cO=0
P=9.6
simulate_returned_true
```

v89 target result:

```text
T=5.15
cR=1
cO=0
P=9.6
simulate_failed / exit_state=2
```

Evidence:

```text
Results/simulations/controller_v89_side_squeeze_marker_saidao2_120s_20260710/
Results/evidence/controller_deployability_static_check_v89_side_squeeze_marker_20260710.md
Results/evidence/controller_deployability_static_check_v80_restored_after_v89_20260710.md
```

## Decision

Reject v89.

Reason:

- It did not improve Track2 score or road-collision count.
- It regressed runtime severely from v80 clean `T=120.0` to
  `simulate_failed/T=5.15`.
- The source has been restored to v80 semantics and the restore static gate
  passed.

## Follow-Up

Do not continue the same side-squeeze marker / path-neutralization route without
new source-level evidence. Continue the 80-point score sprint from v80 using a
different unified mechanism or targeted research.
