# Track2 v192 Safety-Priority Speed Arbiter Review

## Verdict

Rejected and rolled back. v192 removed obstacle collisions and extended the
Track2 run, but it did not satisfy the official completion predicate and
increased road collisions from one to two.

## Candidate

- Controller `mindis=1.5`.
- Allocator immediately commanded `-0.5` while `speed_oa < -0.5`, bypassing
  the positive path-speed dominance and one-second obstacle-speed filter.
- One rule was used for every track; no track, time, score, or position branch
  was added.

## Gates And Result

- Static deployability: `high=0`, `medium=0`.
- Repository tests: `14 passed`.
- Track2 1 s native gate: `T=1,cR=0,cO=0,P=10`.
- Track2 strict 700 s attempt: rejected.

```text
T=112.8
cR=2
cO=0
P=9.2
finish_distance_squared=378.4063339104481
termination=unclassified_early_termination
```

Runtime evidence:
`Results/simulations/controller_v192_safety_priority_speed_saidao2_700s_20260712_retry1/`.

## Diagnosis

Both score events were road collisions outside the immediate-front braking
predicate:

```text
t=5.25:  df=2.10, dl=0.108, dr=0.273, speed_oa=0, final_steer=0.0768
t=101.5: df=2.055, dl=0.336, dr=0.171, speed_oa=0, final_steer=1.65
```

The direct speed arbiter therefore cannot solve Track2 alone. It improved
progress and avoided obstacle hits, but lateral clearance and path-steering
authority remain the active failure mechanism. Do not continue scalar scans
of the front threshold or immediate reverse command.

## Decision

Restore both edited files to their exact pre-candidate Git objects. A future
candidate must use a coherent side-clearance/path-authority safety rule or a
reference-backed local-planner interface and must still pass Track2 completion
before expansion.
