# v192 Safety-Priority Speed Arbiter Candidate

## Objective

Restore reproducible Track2 completion with one track-agnostic controller and
allocator rule. v191 showed that the obstacle controller requested reverse
motion while the allocator still commanded strong forward motion because the
path command dominated the one-second filtered obstacle contribution.

## Mechanism

- Set the controller front-risk distance parameter to `mindis=1.5` metres.
- Keep the existing obstacle-controller state machine and steering semantics.
- Treat `speed_oa < -0.5` as the existing controller's collision-imminent
  signal. In that state only, the allocator immediately commands `-0.5`
  instead of adding a slowly filtered obstacle command to the positive path
  speed.
- Outside that state, preserve the committed allocator output exactly.

This uses only existing controller outputs and editable controller/allocator
files. It adds no track, time, score, absolute-coordinate, or official-wrapper
branch and remains suitable for code generation.

## Gates

1. Static deployability checker and repository tests.
2. Track2 1 s native compile/simulation gate.
3. Track2 strict 700 s run with official completion predicate and diagnostic
   exports.
4. Expand the unchanged bytes to Tracks 1, 3, and 4 only after Track2 finishes.

## Acceptance And Rollback

Retain v192 only if Track2 officially finishes without a material collision
regression. Otherwise restore both edited files to their exact pre-candidate
Git object hashes and record the rejection evidence.
