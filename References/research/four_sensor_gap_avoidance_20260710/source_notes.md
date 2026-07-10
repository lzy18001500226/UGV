# Four-Sensor Gap Avoidance Source Notes

Status: reviewed_for_controller_hypothesis, 2026-07-10 CST

## Sources

1. Borenstein and Koren, Vector Field Histogram / VFH:
   `https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated1/borenstein_VFHisto.pdf`
2. VFH publication summary:
   `https://cris.technion.ac.il/en/publications/the-vector-field-histogramfast-obstacle-avoidance-for-mobile-robo/`
3. Follow-the-Gap overview / F1TENTH teaching material:
   `https://f1tenth-coursekit.readthedocs.io/en/latest/lectures/ModuleB/lecture05.html`
4. Follow-the-Gap research summary:
   `https://research.itu.edu.tr/en/publications/predictive-follow-the-gap-method-for-dynamic-obstacle-avoidance/`
5. Low-speed autonomous vehicle obstacle avoidance / safety-filter direction:
   `https://grizzle.robotics.umich.edu/files/YuxiaoChen_BarrierPaper_Short.pdf`

## What Applies To This UGV Model

The current UGV controller does not have LiDAR or a full polar histogram. It
only has four scalar distances: front, rear, left, and right. Therefore VFH or
FGM cannot be copied directly.

The useful common pattern is still applicable:

- avoid fixed direction when clearance evidence is available;
- choose a direction from the safest available gap or side clearance;
- reduce speed when risk is high rather than relying on steering alone;
- avoid oscillation with dwell/hysteresis, but do not let dwell lock the robot
  into a bad fixed turn;
- consider vehicle dynamics: a command that looks collision-free in a scalar
  score window can still be invalid if the run terminates early.

## Mapping To Current Evidence

Current accepted v74 still has these events:

```text
Track1: road event at 4.45 s, T=17.4 early terminal caveat.
Track2: road event at 4.70 s, otherwise clean 120 s.
Track3: obstacle event at 1.05 s and road event at 4.85 s.
Track4: road events at 4.35 s and 104 s.
```

Rejected follow-ups show:

```text
v76: increasing fixed side steering worsened Track1 early terminal time.
v77: clamping path speed on top of v74 produced a non-comparable early-stop
     artifact.
v22: shortening avoid-lateral initialization dwell badly regressed Track1.
v62/v63/v65: simple front-close steering/feedforward/reverse holds did not
             remove the Track3 obstacle event.
```

## Candidate Direction

The next useful candidate should not be another scalar magnitude scan. A better
candidate would first check whether the current fixed `avoid_lateral.ini_state`
can be replaced by a bounded, clearance-selected command only when the saved
signals show a clear gap preference. If the same condition overlaps heavily
with v22/v62/v76 failure windows, do not edit source; record a blocker or
shift to path/geometry-level diagnosis.

Potential v78 criterion before source edit:

```text
Use offline screening on v74 extra_timeseries to count samples where:
  flag == 1
  df > safeF
  min(dl, dr) < 0.15
  abs(dl - dr) is large enough to identify a safe side

If this condition mostly targets the road-edge events and avoids Track3's
front-obstacle event, consider a bounded gap-side command. Otherwise do not
touch source.
```
