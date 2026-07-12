# v186 Coupled Edge Braking Plan

Status: rejected after Track2 early termination

## Goal

Pass the reproducible Track2 boundary-exit window without v184's repeated
road-edge oscillation, using one sensor-only rule for all tracks.

## Evidence Basis

At the Track2 failure window, the front is clear (`df` rises above `2.0`) while
one side distance falls below `0.10`. The baseline longitudinal controller
therefore outputs zero OA speed and full path speed keeps driving the vehicle
through the boundary. v184 corrected steering direction but retained forward
authority, reaching the horizon with 61 road contacts. v185 reduced only the
steering magnitude and terminated at 28.75 s with 17 road contacts.

## Candidate

Use the same narrow front-clear severe-side window in both controller channels:

```modelica
if df > safeF and min(dl, dr) < 0.10 then
  speed := -1;
  steer := 0.6 * sign(dl - dr);
end if;
```

Outside this window, preserve committed v148 semantics, including the narrow
front-obstacle recovery branch used for Track3 diagnosis. This candidate adds
no track id, time, score, position, path-index, or official-model dependency.
It differs from rejected v150 because the braking is not applied to the broad
side-only `<0.45` region; it is coupled only to the measured edge-emergency
window.

## Gates

1. Static deployability and all project tests.
2. Track2 1 s native load/check/simulation gate.
3. Track2 120 s must pass 28.55 s and keep road/obstacle contacts bounded.
4. Only then run Track3 120 s and strict completion gates.
5. Any early termination, contact explosion, or syntax/runtime failure rejects
   v186 and restores exact committed controller semantics.

## Result

Static deployability passed with `high=0, medium=0`, and the 1 s native gate
passed with `T=1.0,cR=0,cO=0,P=10.0`. The Track2 120 s run nevertheless
returned `SimulateModel=false` and terminated at `T=25.15` with
`cR=17,cO=0,P=3.2`; official finish distance squared was `530.7769` and the
termination was `unclassified_early_termination`.

The narrow braking command did not stabilize the edge event. v186 is rejected,
its controller edits are restored, and no Track3 or four-track expansion is
authorized.
