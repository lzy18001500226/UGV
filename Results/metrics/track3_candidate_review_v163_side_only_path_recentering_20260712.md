# Track3 v163 Candidate Review

Status: rejected; exact v148 source restored.

v163 retained v162's narrow recovery and set lateral re-entry steering to zero
only when `df>mindis`, intending to let the path planner recenter the final
straight. Static checks, tests, and the 1 s MWORKS gate passed.

The strict request ended at `T=80.0,cR=5,cO=7,P=5.2`; official finish distance
was `124.9077`. It did not finish and materially regressed both collision
categories. Front-clear side-only observations still occur during necessary
obstacle traversal, so an instantaneous zero command is not a valid recovery
state discriminator.

Evidence:

- `Results/simulations/candidate_v163_side_only_path_recentering_track3_1s_20260712/`
- `Results/simulations/candidate_v163_side_only_path_recentering_track3_700s_20260712/`
- `Results/evidence/controller_deployability_static_check_v163_side_only_path_recentering_20260712.md`

Decision: reject v163. Do not scan side-only zero/attenuation thresholds. The
next mechanism must retain obstacle-side authority and use bounded encounter
state to distinguish obstacle traversal from post-obstacle recentering.

No finish, 80/80, physical, package, or submission claim is made.
