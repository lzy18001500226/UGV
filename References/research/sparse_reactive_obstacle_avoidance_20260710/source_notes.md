# Sparse Reactive Obstacle Avoidance - Source Notes

timestamp: 2026-07-10 CST
baseline: v48 opposing-steer guard
recent screen: v69 lateral hysteresis rejected before source edit

## Current Interface

The contest controller boundary remains:

```text
inputs: front_dist, rear_dist, left_dist, right_dist
outputs: speed, steer
```

This is a sparse reactive safety-layer interface, not a full local-planning
interface. A future candidate must therefore be expressed as a bounded
four-distance rule and must remain one algorithm for all four official tracks.

## What The Sources Support

### VFH / Histogram Methods

The Vector Field Histogram method uses a grid-like world model updated from
range sensor data. Its transferable lesson is not the implementation itself,
because the current controller has no grid, pose integration, or dense scan.

Usable idea:

```text
convert obstacle proximity into a local steering preference and keep moving
toward a safe direction
```

Not directly usable:

```text
histogram grid, polar obstacle density, sector search, full target steering
```

### Follow-the-Gap / Disparity Extender

F1TENTH/RoboRacer material treats Follow-the-Gap as a reactive algorithm over
LaserScan-like data. Disparity Extender inflates close obstacles so adjacent
directions are treated as unsafe.

Usable idea under four-distance input:

```text
front risk + side imbalance -> choose a conservative two-bin gap proxy
```

But v58/v59/v66 already tested initial side-gap direction or magnitude changes
and were rejected, so a future candidate must not simply repeat startup
steering direction/magnitude logic.

### Bug / Wall-Following / Potential-Field Family

These methods are relevant as concepts because the current system already has
an official path-following layer. The obstacle controller can behave like a
short boundary-following safety overlay while path following remains in charge
outside risk.

Usable idea:

```text
when side clearance is critical, reduce forward exposure and bias away from the
closer side, but release cautiously
```

Already exhausted nearby routes:

```text
side-trigger threshold scanning
side-danger speed-only regulation
side-danger steering floor
longer guarded release
simple planner-steering suppression
complete path-steer neutralization
path-authority scalar scanning
```

### Braitenberg-Style Sparse Sensor Coupling

Braitenberg-style controllers show that sparse sensors can directly drive
actuators and produce obstacle-avoidance behavior. This supports keeping the
UGV controller simple and deployable for a physical car.

Usable idea:

```text
left/right distance imbalance can drive a bounded steer bias; front distance
can drive a bounded speed/braking bias
```

But the current v48 evidence shows that obstacle avoidance is already active at
remaining score-loss events. Therefore the next useful design must consider
effective command after allocation/filtering, not only raw sensor-to-output
mapping.

## Post-v69 Mechanism Filter

Before editing source again, require a candidate to pass all checks:

1. It is one unified algorithm across all four tracks.
2. It uses only `front_dist`, `rear_dist`, `left_dist`, `right_dist`, current
   controller state, and existing allocation/planner signals inside editable
   controller/allocation boundaries.
3. It is materially different from rejected v49-v67 and v69 families.
4. Offline saved-signal evidence predicts why it should improve a specific
   event window.
5. It does not rely on early-stop `P=10` artifacts.
6. It preserves bounded speed/steer and physical retuning readability.

## Current Decision

No immediate source patch is justified solely from this research pack.

The most useful next engineering work is:

```text
v48 report/evidence hardening
  -> trajectory-event visualization in report
  -> source-static deployability and readiness checks
  -> then only implement a new candidate if post-v69 evidence shows a genuinely
     new mechanism, not a renamed scalar scan
```

## Non-Claims

- No MWORKS runtime was opened or rerun for this note.
- No controller source was edited.
- This note does not claim final score, submission readiness, or physical UGV success.
