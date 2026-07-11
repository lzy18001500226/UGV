# Track2 v80 Termination Classification

Evidence:
`Results/simulations/diagnostic_v80_track2_termination_classification_700s_20260712_rerun/`.

## Reproduction

```text
runtime_status=simulate_failed
exit_state=2
T=305.15 s
cR=1
cO=0
P=9.6
distanceSensor1.d=1004.6703
closest_index=30
path_progress=0.07797
position=(28.0947, 14.6752)
```

The run is not a finish because the official origin distance is far above
`0.02`. `GetLastErrors` and `MessageText` contain no usable termination text.
The exported `road.assertlevel=2` is a static road-model parameter and does
not prove that a road assertion fired. The correct classification is therefore
`unclassified_early_termination`, not road-boundary assertion.

The useful behavioral diagnosis comes from the earlier full-signal export:
after reaching index 30, side-only risk keeps the obstacle controller at
`speed_oa=-1`, while the final allocated speed is about `0.059 m/s`. The next
candidate should remove repeated reverse longitudinal authority for side-only
risk without repeating rejected forward side-hold or steering-sign scans.
