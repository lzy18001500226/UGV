# v162 Rear-Observability Diagnostic Plan

Status: completed diagnostic; v148 restored

## Question

Can the currently unused rear-distance input `db` distinguish v162's safe
obstacle traversal from its return-to-origin window, where `df/dl/dr` remain
too similar for prior stateless recovery rules?

## Method

Temporarily reproduce exact v162 controller semantics and run Track3 to a
bounded 200 s horizon while exporting:

- `df`, `db`, `dl`, `dr`, `flag`, controller speed/steer;
- allocated and path speed/steer;
- vehicle position and path progress.

Compare the initial obstacle window, loop traversal, and return straight. This
is observation only. Restore exact v148 source after capture. A future
candidate may use `db` only if the saved data shows a stable, track-agnostic
separation with a physical interpretation.

No finish, score gain, physical-car, package, or submission claim is made.

## Result

The bounded 200 s reproduction reached the configured horizon with
`T=200,cR=2,cO=1,P=8.8`. Rear distance adds information, but no clean recovery
predicate was found:

- initial departure: `db≈0.85`;
- first return near the origin: `db≈0.017`;
- main-loop windows also reach `db<0.02`, including around `t=55–60 s` and
  `t=160–170 s`.

Combining `db` with front clearance and side asymmetry still activates on both
main-loop and return segments. A `db` threshold would therefore encode an
accidental Track3 timing/geometry correlation, not a deployable unified state.
Do not promote rear distance into the controller without a new physically
separable predicate. Exact v148 source was restored after capture.
