# v124 Native Derivative Front-Risk Plan

Status: planned deployability probe, not accepted

## Purpose

v123 showed that adding an external derived-signal port to the generated
Sysblock state machine is not deployable. v124 tests the narrow remaining
representation: use the existing `df` input directly in the transition with
its native derivative, without adding components, ports, parameters, or
connections.

Conceptually:

```modelica
df <= mindis or
  (der(df) < -0.05 and df + 0.60 * der(df) <= mindis)
```

All v80 output actions, lateral states, path planning, control allocation, and
official track models remain unchanged.

## Gates

1. Static checker and targeted tests pass.
2. Track3 1 s translation/simulation gate passes.
3. Only after a valid 1 s gate, run Track3 120 s with normal diagnostics.
4. Accept only an official finish or material comparable progress without
   increased collisions or a shorter abnormal stop.
5. If the derivative expression cannot translate, reject this predictive-risk
   family as incompatible with the current four-distance Sysblock interface;
   restore v80 and do not tune derivative thresholds or horizons.
