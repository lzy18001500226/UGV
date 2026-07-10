# Four-Sensor Gap Avoidance Research Manifest

Status: source_notes_created, 2026-07-10 CST

Purpose: support the post-v77 UGV high-score sprint with external obstacle
avoidance patterns that fit the current model's limited sensor interface:
front, rear, left, and right distances.

Scope:

- Read-only research notes.
- No imported source code.
- No official model, vehicle, road, sensor, scoring, example, or official
  material edits.

Outputs:

```text
References/research/four_sensor_gap_avoidance_20260710/source_notes.md
```

Main takeaway:

```text
Do not continue fixed-steer, dwell, speed-gain, or one-signal scalar scans.
Use saved collision windows to design a small gap/safety-bubble style rule
that chooses direction from available clearance and preserves dynamic limits.
```
