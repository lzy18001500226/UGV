# Source Notes - Wall-Following Residual

## What The References Say

F1TENTH/RoboRacer wall following uses a distance-to-wall error, often with
PID/PD control, to command steering and speed. The useful idea for this project
is not the LiDAR scan processing; it is the control pattern:

```text
measure side clearance -> compute lateral error -> apply bounded steering correction
```

Disparity Extender and Follow-the-Gap style methods need a dense scan. The
current UGV model exposes only front, left, and right distances to the
controller, so those methods are not directly portable.

## Mapping To Current UGV

The v80 four-track evidence shows a repeated early road-edge pattern:

```text
flag=1
dl around 0.10 at road collision
speed_oa=-1
steer_oa=0.6
final speed still around 0.51-0.54 at the first road contact
```

v71 showed that stronger severe-left steering can remove a later Track1 road
event, but it does not remove the first early road contact and regresses Track4
under the v48 baseline. v66 showed that a narrow fixed initial steering boost
does not remove Track3's first obstacle event and creates an early-stop
artifact. Therefore the next candidate should not be another fixed steering
magnitude boost.

## Candidate Direction

A viable v82 should satisfy all of these:

1. Start from v80, not v48 or v74.
2. Use side-distance error as a bounded residual or mode-timing decision, not a
   global fixed steer increase.
3. Target early road-edge contacts first, because all four v80 tracks still
   lose one point there.
4. Run one target track first and expand only after real collision-count/score
   improvement.

Rejected repeats to avoid:

```text
fixed initial steer boost
side-danger speed-only regulation
side-danger steering floor
longer avoid release
broad active-avoid speed clamp
path-authority scalar scan
max-steer clipping
```
