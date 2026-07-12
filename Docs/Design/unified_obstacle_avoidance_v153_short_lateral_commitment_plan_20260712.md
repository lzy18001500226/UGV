# v153 Short Lateral Commitment Plan

Status: rejected; diagnostic basis for v154 hysteretic direction memory.

## Hypothesis

The lateral sub-state always commands `steer=+0.6` for two seconds after each
avoid entry. In v148 Track3, positive steering is appropriate near `T=1.0`
because the right side is closer, but at the road collision near `T=4.1` the
left side is closer (`dl=0.1064`, `dr=0.2709`) while the command remains
`+0.6`. The fixed commitment is therefore stale relative to the geometry.

v153 preserves a short 0.5 s direction commitment to avoid instantaneous
sensor-sign chatter, then allows the existing left/right state logic to select
the direction from `dl` and `dr`:

```modelica
transition(ini_state, state, after(0.5,sec), reset=false);
```

All v148 longitudinal, threshold, path-planner, and allocator semantics remain
unchanged. This differs from rejected v145 instantaneous directional re-entry:
v153 retains a bounded commitment window instead of switching direction at
entry.

## Gates

Static checker and tests, Track3 1 s, then Track3 700 s. A strict Track3 finish
promotes first to Track4 regression, then Tracks 1 and 2. Any non-finish or
loss of a v148 finish rejects v153 and restores the two-second lateral
commitment.

## Result

Track3 terminated at `T=35.05`, `cR=3`, `cO=3`, `P=7.6`, and
finish-distance squared `312.4945`. The shorter commitment avoids the exact
v148 timing but allows more obstacle contacts and still leaves the road. v153
is rejected as a standalone mechanism. Its result motivates adding explicit
lateral direction hysteresis rather than scanning more commitment durations.
