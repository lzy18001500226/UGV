# v185 Proportional Edge Recovery Plan

Status: rejected after Track2 early termination and road-contact regression

## Goal

Retain v184's ability to pass the reproducible Track2 boundary exit while
removing its repeated road-boundary oscillation.

## Candidate

Keep v184's two mutually exclusive sensor windows. In the front-clear severe
side window, replace the fixed `0.6` direction command with:

```modelica
sign(dl - dr) * min(0.3, 2 * abs(dl - dr))
```

At the measured Track2 event, the side difference is about `0.165 m`, so the
command is capped at `0.3` rather than `0.6`. Near symmetry decays continuously
to zero. No other controller state, threshold, path, or official model changes.

## Gates

1. Static checker and tests.
2. Track2 120 s must pass 28.55 s and materially reduce v184's 61 road events.
3. Track3 120 s must preserve loop progress.
4. Strict completion and four-track expansion only after both short gates.

## Result

Static deployability reported `high=0, medium=0`, all 14 project tests passed,
and the Track2 1 s native gate passed. The 120 s Track2 run terminated at
`T=28.75,cR=17,cO=0,P=3.2`, with official finish distance squared
`787.6683`; the engine classified it as `unclassified_early_termination`.

The proportional `0.3` cap avoided v184's 61-road-contact horizon run but did
not produce a finish and still increased road contacts from the committed
baseline's `cR=1` to `cR=17`. v185 is rejected, exact committed controller
semantics are restored, and smaller scalar caps in this same severe-side
steering family must not be scanned. The next candidate must change the
speed/path-authority arbitration mechanism rather than only the steering
magnitude.
