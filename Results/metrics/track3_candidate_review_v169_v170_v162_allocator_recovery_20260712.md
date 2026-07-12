# Track3 v169/v170 v162 Allocator Recovery Review

Status: both rejected; exact v148 controller and allocator semantics restored.

## v169 Immediate Recovery

v169 combined v162's narrow obstacle-entry recovery with v158's guarded
feed-forward cancellation at the final steering sum. Static checks, 14 tests,
and the 1 s native gate passed.

The strict run reached `T=116.75,cR=7,cO=2,P=6.4`, finish-distance squared
`88.6103`. It made route progress but accumulated nine collisions and did not
finish. Immediate cancellation is too aggressive even with v162 entry
stabilization.

## v170 Bounded Decay

v170 replaced immediate cancellation with v157's existing guarded `0.35` OA
filter-input attenuation. Static checks, 14 tests, and the 1 s native gate
passed.

The strict run reached `T=84.6,cR=2,cO=2,P=8.4`, finish-distance squared
`22.4341`. Offline review shows the terminal path index was only `81`; the
small origin distance occurred mid-route and is not closure progress. It did
not finish the main loop and cannot justify an attenuation-factor scan.

## Decision

Reject v169/v170 and close v162 plus stateless allocator recovery combinations.
Restore v148 controller and allocator semantics. Future work requires a
structurally different controller architecture or evidence-backed reference
algorithm, not another conflict threshold/gain variant.

Evidence:

- `Docs/Design/unified_obstacle_avoidance_v169_v162_neutral_path_recovery_plan_20260712.md`
- `Docs/Design/unified_obstacle_avoidance_v170_v162_bounded_oa_decay_plan_20260712.md`
- `Results/simulations/candidate_v169_v162_neutral_path_recovery_track3_1s_20260712/`
- `Results/simulations/candidate_v169_v162_neutral_path_recovery_track3_700s_20260712/`
- `Results/simulations/candidate_v170_v162_bounded_oa_decay_track3_1s_20260712/`
- `Results/simulations/candidate_v170_v162_bounded_oa_decay_track3_700s_20260712/`

No Track3 finish, 80/80, physical-vehicle, package, or submission claim is
made.

Terminal notice evidence:
`C:\Users\HP\Desktop\MoSim\Results\coagent_gateway\email\email_alert_20260712_144305.json`.
