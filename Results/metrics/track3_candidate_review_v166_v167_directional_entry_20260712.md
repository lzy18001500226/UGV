# Track3 v166/v167 Directional Entry Review

Status: both rejected; exact v148 source semantics restored.

## v166

v166 replaced the lateral avoid entry state's fixed `+0.6` command with a
directional proportional command from `dl/dr`. Static checks, 14 project tests,
and the 1 s native gate passed.

The strict run stopped at `T=39.8,cR=0,cO=5,P=8.0`, finish-distance squared
`366.0912`. A 45 s diagnostic export including `db` showed the first obstacle
events at `df=0.86` and `df=0.008` while `dl` and `dr` were equal; v166 output
zero lateral command and drove through the obstacle. It removed road events
but materially regressed obstacle safety.

## v167

v167 preserved v162's fixed bypass while `df<=safeF=1.5` and enabled
directional proportional entry only for `df>safeF`. Static checks, 14 tests,
and the 1 s native gate passed.

The strict run stopped at `T=42.8,cR=2,cO=3,P=8.0`, finish-distance squared
`383.5516`. Front-clear direction gating still altered avoidance behavior on
other curve/obstacle windows and did not approach completion.

## Decision

Reject both candidates and close global directional lateral-entry changes.
Restore v148. Preserve v162 as near-complete diagnostic evidence. The next
candidate must use existing path progress only near the generic closure
segment, rather than changing every front-clear side-risk event.

Evidence:

- `Docs/Design/unified_obstacle_avoidance_v166_directional_lateral_entry_plan_20260712.md`
- `Docs/Design/unified_obstacle_avoidance_v167_front_clear_directional_entry_plan_20260712.md`
- `Results/simulations/candidate_v166_directional_lateral_entry_track3_1s_20260712/`
- `Results/simulations/candidate_v166_directional_lateral_entry_track3_700s_20260712/`
- `Results/simulations/diagnostic_v166_rear_clearance_track3_45s_20260712/`
- `Results/simulations/candidate_v167_front_clear_directional_entry_track3_1s_20260712/`
- `Results/simulations/candidate_v167_front_clear_directional_entry_track3_700s_20260712/`

No Track3 finish, 80/80, physical-vehicle, package, or submission claim is
made.
