# Track3 v155 Candidate Review

Status: rejected.

Track3 terminated at `T=209.35`, `cR=7`, `cO=6`, `P=4.8`, and
finish-distance squared `304.6513`. The longer runtime is not completion
progress: terminal evidence cycles over path indices 11-29 and accumulates
collisions. Suppressing same-sign OA contribution whenever path steering
exceeds `1.0 rad` intervenes too early and creates a loop.

Evidence:

- `Results/simulations/candidate_v155_extreme_same_sign_oa_suppression_track3_1s_20260712/`
- `Results/simulations/candidate_v155_extreme_same_sign_oa_suppression_track3_700s_20260712/`
- `Results/metrics/track3_v155_terminal_progress_20260712.json`

Decision: reject v155. Test one final threshold tied to the observed v148
terminal command (`1.734 rad`): `1.5 rad`. If that fails, restore v148 and
close this allocator-suppression family.
