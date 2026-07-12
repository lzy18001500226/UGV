# Unified Obstacle Avoidance v200 Heading-Error Low-Floor Plan

## Status

Rejected; exact v199 source semantics restored.

## Evidence basis

v199 extended Track3 from `T=21.1,d=301.4313` to
`T=92.85,d=1.0824` without changing `cR=1,cO=1,P=9.2`. During the final
approach, the wrapped heading error grew to about `0.65-0.92 rad`, the speed
governor was pinned at its `0.35` ratio floor, and the PID command reached
about `-65` to `-92 rad/s` before termination. The vehicle was approaching the
origin but could not shed enough speed to track the closure heading.

## Candidate

Keep v199's unified measured-heading governor and reduce only its speed ratio
floor from `0.35` to `0.15`. This is an evidence-backed saturation correction,
not a track-specific speed schedule. All other path, obstacle, allocator,
vehicle, PID, road, and scoring semantics remain unchanged.

## Gates

Static deployability, all project tests, Track3 1 s plain native gate, then a
Track3 700 s plain completion gate. Expand unchanged source only if Track3
officially finishes or improves closure without collision regression. Restore
the exact pre-candidate bytes on failure.

No four-track completion, 80/80, physical-car, or submission claim is made by
this plan.

## Result

Static deployability (`high=0, medium=0`), 14 project tests, and the Track3 1 s
plain native gate passed. The 700 s decisive invocation exceeded the bounded
five-minute wall-clock limit without returning a result packet or score export.
The candidate is therefore rejected under the runtime-efficiency gate and the
speed floor is restored to v199's `0.35`. No score or completion gain is
claimed.
