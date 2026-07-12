# Track3 Candidate Review - v149

Decision: reject v149 and restore v148.

- static deployability: `high=0, medium=0`
- tests: `14 passed`
- Track3 1 s: load/check/simulate passed
- Track3 120 s request: stopped at `T=18.7`, `cR=1`, `cO=1`, `P=9.2`
- finish distance squared: `299.51524654235504`
- v148 comparison: `T=21.1`, `cR=1`, `cO=1`, `P=9.2`

The same-sign OA heading addition is not the Track3 completion root cause.
Do not continue zero/attenuation scans of that term. The next candidate must
preserve v148 heading behavior and target excessive speed during large-heading
side-only traversal.
