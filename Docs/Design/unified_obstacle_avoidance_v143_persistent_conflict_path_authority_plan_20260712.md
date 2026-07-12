# v143 Persistent-Conflict Path-Authority State

## Status

Candidate under validation. v80 remains the rollback baseline until the
comparable Track2 gate passes.

## Evidence Basis

- v80 Track2 enters repeated path/avoidance steering conflict from about
  `t=30.15 s` through the 120 s horizon. During those windows, front clearance
  remains above `1.31 m`, obstacle steering stays at `+0.6`, delayed path
  steering remains negative, and path progress stalls near index 26.
- The current allocator uses a fixed `0.5` path-steering multiplier whenever
  reverse avoidance and path steering oppose each other. It does not
  distinguish a short transient conflict from a persistent conflict.
- Fixed path-authority changes and complete path neutralization have already
  regressed other tracks. v143 therefore changes the arbitration state, not a
  track, speed threshold, steering magnitude, or side-selection threshold.

## Unified Mechanism

Use one controller and one parameter set on all four official tracks. Add one
discrete path-authority state inside `ControlAllocate.CtrlAlloc`:

```text
conflict := speed_oa < 0 and steer_oa * delayed_path_steer < 0

if conflict:
    path_authority := max(0.2, previous_path_authority - 0.01)
else:
    path_authority := min(1.0, previous_path_authority + 0.02)
```

At the existing 0.01 s sample period, a persistent conflict requires about
0.8 s to reduce path authority from 1.0 to 0.2. Conflict release restores full
path authority in about 0.4 s. The final path contribution is multiplied by
this state only while the conflict predicate is true.

This is a temporal arbitration mechanism. It preserves near-v80 behavior for
short conflicts and gives sustained obstacle steering progressively more
authority during the measured Track2 failure window. It adds no track ID,
wrapper input, external port, official-model edit, or per-track parameter.

## Acceptance Gates

1. Run the source deployability checker and the complete project test suite.
2. Run `UGV.Test.Saidao2Eval` for 1 s as the translation/simulation gate.
3. Run Track2 for 120 s. Require comparable runtime, `cO=0`, no increase over
   v80's `cR=1`, and material progress beyond v80 path index 26 or terminal
   distance.
4. Only after gate 3 passes, run the 700 s completion gate. A finish requires
   `SimulateModel=false`, `T>10`, and `distanceSensor1.d<0.02`.
5. Only after a Track2 finish, run Track1 collision regression and then Tracks
   3-4 with unchanged source and parameters.

Any syntax/runtime failure, collision regression, absent material progress,
or non-comparable early stop rejects v143. Restore exact v80 semantics and
keep the candidate evidence and review note. This plan does not claim an
official finish, an 80/80 score, physical UGV success, or submission readiness.
