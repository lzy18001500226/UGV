# Track3 v157 Candidate Review

Status: rejected.

v157 preserved full initial front-obstacle authority and attenuated the OA
heading offset to 35% only in v148's neutral side-only state when OA and a
meaningful path heading opposed each other. This was structurally distinct
from v94/v119, which acted during active reverse avoidance.

The Track3 1 s translation/simulation gate passed. The strict 700 s request
stopped at `T=20.40`, `cR=1`, `cO=1`, `P=9.2`, and finish-distance squared
`305.6024`, with `unclassified_early_termination`. It did not reach the
official origin assertion.

Compared with v148 (`T=21.10`, `cR=1`, `cO=1`, `P=9.2`, finish-distance
squared `301.4313`), v157 is slightly worse and has no completion or score
gain. It is not promoted to the other tracks.

Evidence:

- `Results/simulations/candidate_v157_neutral_opposite_sign_oa_attenuation_track3_1s_20260712/`
- `Results/simulations/candidate_v157_neutral_opposite_sign_oa_attenuation_track3_700s_20260712/`
- `Results/evidence/controller_deployability_static_check_v157_neutral_opposite_sign_oa_attenuation_20260712.md`

Decision: reject v157 and restore exact v148 allocator semantics. Do not scan
more attenuation factors. The next design must use path/pose geometry and a
bounded local recovery state, while remaining one unified controller.
