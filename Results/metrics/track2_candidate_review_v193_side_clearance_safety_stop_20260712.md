# Track2 v193 Side-Clearance Safety Stop Review

## Verdict

Rejected and rolled back. The candidate passed static, test, and 1 s gates,
but stopped non-comparably at `T=4.75` during the 120 s Track2 screen.

## Candidate

- Encoded side-clearance risk continuously in `speed_oa`, with
  `speed_oa<-0.5` exactly when `min(dl,dr)<0.20`.
- The allocator immediately commanded neutral speed `0` in that state.
- Steering and all normal allocation semantics were unchanged.
- The rule was sensor-only and identical for all tracks.

The first source form used an unsupported state-action `if` expression and was
rejected by `CheckModel`; it was mechanically rewritten as an equivalent
bounded `min/max` expression before runtime validation.

## Gates And Result

- Static deployability: `high=0`, `medium=0`.
- Repository tests: `14 passed`.
- Corrected Track2 1 s gate: `T=1,cR=0,cO=0,P=10`.
- Track2 120 s gate: rejected.

```text
T=4.75
cR=0
cO=0
P=10
finish_distance_squared=12.90190717057353
termination=unclassified_early_termination
```

The displayed score is not accepted because the run did not complete and did
not pass the 28.55 s cold-baseline termination point. The neutral safety stop
is incompatible with sustained progress in the current vehicle/solver chain.

## Decision

Restore the exact pre-candidate source objects. Do not expand to 700 s or other
tracks, and do not repeat side-risk encoding followed by an immediate zero
speed command. Future work needs a reference-backed moving safety controller
or a broader local-planner/interface change, not another stop/reverse scalar.
