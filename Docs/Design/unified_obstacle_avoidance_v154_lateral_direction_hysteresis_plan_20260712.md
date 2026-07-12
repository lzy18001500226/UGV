# v154 Lateral Direction Hysteresis Plan

Status: rejected; exact v148 lateral semantics restored.

## Mechanism

v153 lets the controller react to side geometry after 0.5 s, but the existing
turn states reverse whenever `dl` and `dr` merely cross. Noisy or near-equal
side distances can therefore chatter the chosen bypass side. v154 adds a
0.10 m Schmitt-style margin:

```modelica
transition(turn_left, turn_right, dr > dl + 0.10, reset=false);
transition(turn_right, turn_left, dl > dr + 0.10, reset=false);
```

The 0.10 m margin is below the 0.45 m side-risk threshold and preserves a
clear emergency-side reversal while rejecting small crossings. Combined with
the 0.5 s entry commitment, it forms bounded direction memory. Longitudinal,
path-planner, allocator, official track, and scoring semantics remain v148.

## Gates

Static checker and tests, Track3 1 s, then Track3 700 s. Only a strict Track3
finish promotes to Track4, Track1, and Track2 regression. Otherwise restore
both the two-second entry commitment and zero-margin direction transitions.

## Result

Track3 terminated at `T=19.75`, `cR=3`, `cO=1`, `P=8.4`, and
finish-distance squared `316.0781`. The hysteresis does not produce a finish
and terminates earlier than v148. v154 is rejected; the two-second entry
commitment and zero-margin transitions are restored exactly.
