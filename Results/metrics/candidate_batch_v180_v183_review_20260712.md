# Candidate Batch v180-v183 Review

## Decision

Reject v180-v183 and retain v148 as the reproducible completion baseline.
The batch produced the first saved Track3 official finishes, proving the
remaining gap is controllable, but no candidate preserved every existing
finish.

| Candidate | Track1 | Track2 | Track3 | Track4 | Decision |
|---|---|---|---|---|---|
| v180 narrow recovery + closer endpoint | `T=67.20`, non-finish | not expanded | official finish, `T=89.50` | official finish, `T=89.65` | reject |
| v181 exact endpoint + narrow recovery | `T=67.20`, non-finish | not expanded | inherited v180 mechanism | inherited v180 mechanism | reject |
| v182 v148 OA + exact endpoint | official finish, `T=162.95` | two runs at `T=28.55`, non-finish | official finish, `T=89.15` | not expanded | reject |
| v183 open-side recovery | 120 s horizon | `T=28.55`, non-finish | 120 s horizon | not expanded | reject |

## Engineering Conclusion

The endpoint edit changes translated numerical behavior before it becomes
logically active; the resulting Track3 finish is not a stable cross-track
improvement. The open-side gate removes the Track1 regression but not the
Track2 road-boundary weakness. Further work should target a deterministic
road-boundary margin mechanism and validate Track2 before full expansion.

The score target remains 80, but the active hard gate remains four official
finish assertions from one unchanged algorithm.
