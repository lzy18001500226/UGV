# Track3 v152 Candidate Review

Status: rejected.

The native Track3 run terminated at `T=48.45`, `cR=9`, `cO=1`, `P=6.0`, and
finish-distance squared `397.5869`. This does not finish and materially
increases road collisions over v148. The three-second hard cap is insufficient
to make extended avoid persistence safe.

Evidence:

- `Results/simulations/candidate_v152_bounded_clearance_release_track3_1s_20260712/`
- `Results/simulations/candidate_v152_bounded_clearance_release_track3_700s_20260712/`

Decision: restore v148's `after(2,sec)` release. Do not extend the longitudinal
avoid-state dwell again without a different state architecture.
