# Track3 v156 Candidate Review

Status: rejected.

v156 raised the same-sign OA suppression threshold from v155's `1.0 rad` to
`1.5 rad`, so the rule would intervene only near the observed v148 terminal
path-heading command. Static checks and tests passed, but the strict Track3 run
stopped at `T=21.65`, `cR=1`, `cO=1`, `P=9.2`, and finish-distance squared
`300.3642`. Track3 did not reach the official origin assertion.

Compared with v148 (`T=21.10`, `cR=1`, `cO=1`, `P=9.2`), v156 adds only
`0.55 s` and no completion or score-variable improvement. This is not enough
to promote the candidate to the other tracks.

Evidence:

- `Results/simulations/candidate_v156_terminal_only_oa_suppression_track3_1s_20260712/`
- `Results/simulations/candidate_v156_terminal_only_oa_suppression_track3_700s_20260712/`
- `Results/evidence/controller_deployability_static_check_v156_terminal_only_oa_suppression_20260712.md`

Decision: reject v156, restore exact v148 allocator semantics, and close the
same-sign OA suppression family. The next candidate must address the neutral
side-only opposite-sign path/OA conflict and remain one unified controller.
