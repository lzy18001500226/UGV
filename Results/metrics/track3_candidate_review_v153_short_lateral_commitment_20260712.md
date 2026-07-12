# Track3 v153 Candidate Review

Status: rejected as a standalone mechanism.

The native run stopped at `T=35.05`, `cR=3`, `cO=3`, `P=7.6`, and
finish-distance squared `312.4945`. It does not finish and increases both road
and obstacle collisions over v148. Reducing the fixed lateral commitment alone
is insufficient.

Evidence:

- `Results/simulations/candidate_v153_short_lateral_commitment_track3_1s_20260712/`
- `Results/simulations/candidate_v153_short_lateral_commitment_track3_700s_20260712/`

Decision: do not scan more commitment durations. The next candidate must add a
physical clearance margin before reversing the selected lateral direction.
