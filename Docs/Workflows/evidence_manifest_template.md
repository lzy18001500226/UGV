# Evidence Manifest Template

Copy this template into each meaningful run folder as `MANIFEST.md`.

```yaml
run_id:
timestamp:
phase:
model_root: Models/UGV
entry_model:
track:
controller_file: Models/UGV/Control/ObstacleAvoidanceController/ObsAvoidController_Sysblock2.mo
controller_version:
runtime:
status:
completion:
time_s:
road_collisions:
obstacle_collisions:
avoidance_score:
artifacts:
  logs:
  screenshots:
  metrics:
blockers:
notes:
```

Rules:

1. Use `status: blocked` if load, translate, simulate, animation, or metric extraction fails.
2. Record exactly where manually read metrics came from.
3. A screenshot alone is review evidence, not score evidence.
4. A source check is not a runtime pass.
