# v142 Side-Choice Hysteresis With Neutral Side Longitudinal Authority

## Status

Candidate under validation. v80 remains the rollback baseline until the
comparable Track2 gate passes.

## Evidence Basis

- v80 can stall in side-only risk because its longitudinal avoidance output
  remains `speed=-1` while the front is clear.
- v137 removed that repeated reverse contribution and restored progress, but
  its fixed side choice produced one additional road collision.
- v138 changed turn magnitude without removing the longitudinal stall.
- v139-v141 did not provide a comparable progress/collision improvement.

## Unified Mechanism

Use one controller and one parameter set on all four official tracks:

1. Keep full reverse authority for front risk.
2. In side-only risk, use neutral longitudinal authority so the path planner
   can continue contributing forward motion.
3. Add a 0.15 m clearance advantage deadband to the side-choice state machine.
   Once a side is selected, the controller does not switch sides merely
   because the two measurements are nearly equal; it switches only when the
   opposite side is clearly more open. This is state hysteresis, not a
   per-track route or a speed/steering scalar scan.

The deadband is applied symmetrically to both direction-selection state
machines. No new port, timer, track parameter, wrapper change, or official
model edit is introduced.

## Acceptance Gates

1. Run the source deployability checker and the project test suite.
2. Run `UGV.Test.Saidao2Eval` for 1 s as a load/check/simulate gate.
3. Run the same model for 120 s. Require comparable runtime, `cO=0`, no
   increase over v80's `cR=1`, and material progress beyond v80's path index
   26 / terminal-distance result.
4. Only after gate 3 passes, run the 700 s official completion gate. A finish
   requires `SimulateModel=false`, `T>10`, and `distanceSensor1.d<0.02`.
5. Only after a Track2 finish, run Track1 collision regression and then
   Tracks 3-4 with the unchanged source and parameters.

Any syntax/runtime failure, collision regression, absent material progress, or
non-comparable early stop rejects v142. Restore exact v80 semantics and keep
the candidate evidence and review note. This plan does not claim an official
finish, an 80/80 score, physical UGV success, or submission readiness.
