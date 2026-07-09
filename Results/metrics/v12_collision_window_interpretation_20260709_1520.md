# v12 Collision Window Interpretation - 20260709_1520

## Scope

This note interprets saved v12 evidence only. It does not modify the model and
does not rerun MWORKS.

Primary evidence:

```text
Results/metrics/collision_window_analysis_v12_side_trigger_20260709_1500.md
Results/metrics/signal_window_summary_v12_side_trigger_20260709_1515.md
Results/simulations/diagnostic_v12_signals_saidao1_120s_20260709_1508/
Results/simulations/diagnostic_v12_signals_saidao4_120s_20260709_1510/
```

## Findings

### Track1

The first two obstacle collisions happen at:

```text
21.75 s
22.30 s
```

Nearest signal values:

```text
df ~= 2.12
dl ~= 0.46
dr ~= 0.63
flag = 0
```

Interpretation:

- v12's side trigger threshold `0.30` is still too late for this obstacle pair.
- The controller remains in cruise (`flag=0`) while obstacle collisions occur.
- Raising the side trigger threshold may catch these events, but it may also
  worsen road-boundary behavior on Track4, so it should be tested as a narrow
  candidate, not accepted blindly.

Late Track1 collisions at `99.95 s` and `106.5 s` show large downstream
`ctrlAlloc.steer` values while `flag=0`. That suggests post-controller steering
wrap/allocation behavior is relevant; do not judge only from the chart-level
`steer` limit.

### Track4

Track4 v12 road collisions happen at:

```text
5.10 s
55.25 s
78.10 s
```

Nearest signal values for the later two events:

```text
dl ~= 0.024 / 0.049
dr ~= 0.141 / 0.116
flag = 1
ctrlAlloc.steer ~= +2.04 / -2.75
```

Interpretation:

- Later Track4 road collisions are not missed-trigger events; avoid mode is
  already active.
- The failure is more likely recovery/oversteer near the boundary.
- A simple larger side-distance trigger could help Track1 but may not fix
  Track4 and could increase boundary interactions.

## Next Candidate Hypotheses

H1: widen side trigger only slightly, then test Track1/Track4 first.

```text
dl <= 0.45 or dr <= 0.45
```

Risk: may enter avoid more often near road boundaries.

H2: add a low-speed side-risk mode instead of immediate reverse avoid.

```text
side near, front clear -> speed reduction, no reverse
```

Risk: requires a larger state-machine change and more Sysblock editing.

H3: inspect/limit downstream steering wrap/allocation behavior.

```text
chart steer is limited, but ctrlAlloc.steer can exceed +/-2 in collision windows
```

Risk: may require touching `ControlAllocate`, which is not the normal
controller target and should not be changed without a boundary review.

## Recommendation And Follow-up

Do not broad-rewrite the controller yet. The next low-risk runtime experiment
was a narrow v13 threshold test, starting with:

```text
df <= mindis or dl <= 0.45 or dr <= 0.45
```

Acceptance for v13:

- Track1 must improve or remain no worse than v12.
- Track4 must not lose more score than v12.
- Static deployability checker must remain `high=0`, `medium=0`.

Follow-up result:

```text
Results/metrics/four_track_summary_v13_side_trigger045_20260709_1535.md
```

v13 met the gate and is now the current review-ready candidate.
