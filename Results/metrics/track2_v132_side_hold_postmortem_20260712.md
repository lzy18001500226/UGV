# Track2 v132 Side-Hold Postmortem

## Question

Did v132 fail because the new `side_hold` state was unreachable, or because
the reachable state did not preserve safe progress?

## Offline Evidence

The analysis uses saved MWORKS exports only:

```text
Results/simulations/diagnostic_v80_track2_speed_state_120s_20260712/
Results/simulations/diagnostic_v132_side_hold_progress_track2_120s_20260712/
Results/metrics/track2_v80_v132_event_windows_20260712.md
Results/metrics/track2_v80_v132_ctrlalloc_events_20260712.md
```

`chart.speed=1` is the cruise or v132 `side_hold` output; `chart.speed=-1` is
the full avoid output. This export cannot distinguish cruise from side-hold,
but the v132 run has a materially larger forward-output interval after the
initial safety action than the v80 comparison.

| Run | `chart.speed=1` samples | `chart.speed=-1` samples | Runtime |
|---|---:|---:|---:|
| v80 Track2 | 170 | 11,832 | 120.0 s |
| v132 Track2 | 971 | 3,391 | 43.6 s |

Therefore the new forward-hold path was reachable; the rejection is not an
unreachable-transition or no-op finding.

## Failure Window

At v132's second road collision (`39.55 s`):

```text
df = 1.3060 m
dl = 0.1517 m
dr = 0.1050 m
chart.flag = true
chart.speed = -1
chart.steer = +0.0933
ctrlAlloc.steer_pp = +0.6255
ctrlAlloc.steer_oa = +0.0933
ctrlAlloc.steer = +0.6455
```

The controller had already returned to full avoid, but its lateral command was
small while the path command dominated the final steering. This rules out the
specific v132 hypothesis that repeated reverse alone was the complete cause of
the crawl. It does not prove that a stronger steering magnitude is safe: v30,
v76, and v87 already rejected closely related side-steer-floor or front-clear
boost mechanisms.

## Consequence

Do not retry any of these as a new candidate without new evidence:

- forward `side_hold` after a fixed two-second avoid period;
- a scalar side-steering floor or sustained front-clear side-steer boost;
- a speed-only anti-crawl or speed-floor scan.

The next mechanism must be different in kind: it needs a bounded,
state-consistent arbitration between near-side clearance and path steering, or
fresh diagnosis showing that controller-only changes cannot satisfy the
official origin-return gate.
