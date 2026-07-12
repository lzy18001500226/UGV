# Track3 v154 Candidate Review

Status: rejected.

The native run terminated at `T=19.75`, `cR=3`, `cO=1`, `P=8.4`, and
finish-distance squared `316.0781`. It neither finishes nor improves v148's
failure boundary. Adding a 0.10 m reversal margin after shortening the entry
commitment is therefore rejected.

Evidence:

- `Results/simulations/candidate_v154_lateral_direction_hysteresis_track3_1s_20260712/`
- `Results/simulations/candidate_v154_lateral_direction_hysteresis_track3_700s_20260712/`

Decision: restore exact v148 lateral semantics. The next investigation must
use path/pose geometry and allocator interaction rather than more dwell,
commitment-time, or side-distance hysteresis tuning.
