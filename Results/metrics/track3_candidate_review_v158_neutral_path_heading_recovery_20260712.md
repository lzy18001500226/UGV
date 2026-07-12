# Track3 v158 Candidate Review

Status: rejected with structural progress evidence.

v158 used feed-forward cancellation of the filtered OA heading only when
`speed_oa=0`, OA opposed the path heading, and `abs(path heading)>0.15`. The
initial front-obstacle maneuver remained unchanged.

The 1 s native gate passed. The strict run stopped at `T=79.8`, `cR=2`,
`cO=3`, `P=8.0`, path index 76, and finish-distance squared `122.2830`. It did
not satisfy the official origin assertion. Compared with v148, it made much
more route progress but regressed collision count and score, so it cannot be
retained.

Geometry evidence shows:

- first road collision moved from v148 `t=4.10` to v158 `t=13.80`;
- v158 followed most of the official loop before failing on the left leg;
- the straight segment oscillated because small path recovery commands were
  excluded by the `0.15` magnitude gate.

Evidence:

- `Results/simulations/candidate_v158_neutral_path_heading_recovery_track3_1s_20260712/`
- `Results/simulations/candidate_v158_neutral_path_heading_recovery_track3_700s_20260712/`
- `Results/metrics/v158_track3_geometry_review_20260712.md`
- `Results/metrics/track3_v158_terminal_progress_20260712.json`

Decision: reject v158 and restore v148 before the next edit. One structural
follow-up may remove the delayed magnitude gate while retaining the neutral
longitudinal-state guard. Do not scan cancellation gains.
