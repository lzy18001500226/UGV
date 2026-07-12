# Unified Obstacle Avoidance v167 Front-Clear Directional Entry Plan

## Goal

Retain v162's obstacle traversal while removing the fixed positive lateral
entry bias only after the front sector is genuinely clear.

## Evidence Basis

v166 directed every lateral entry from `dl/dr`. It removed road collisions but
produced five obstacle collisions and stopped at `T=39.8`. Diagnostic exports
show its first two obstacle events occurred with `df=0.86` and `df=0.008` while
`dl` and `dr` were equal, causing zero lateral command and direct obstacle
traversal.

The controller already defines `safeF=1.5`. This provides a non-track-specific
separation between an obstacle still occupying the front sector and a truly
front-clear side-risk re-entry.

## Unified Mechanism

Inside `avoid_lateral.ini_state`:

1. Keep v162's measured direction when `df<0.15`.
2. Keep the original fixed `+0.6` obstacle bypass while `df<=safeF`.
3. Only when `df>safeF`, choose direction and proportional magnitude from
   `dl/dr`; use zero only when the distances are equal.

No new state, signal, parameter, planner equation, track id, or official model
change is introduced.

## Gates

1. Static checker and project tests.
2. Track3 1 s native gate.
3. Track3 700 s strict completion gate.
4. Cross-track expansion only after verified Track3 completion.

Reject and restore v148 on non-finish or material collision regression.
