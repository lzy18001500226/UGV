# Research Manifest: Post-v64 Limited-Sensor Behaviors

Status: source_notes_only, 2026-07-10 CST

## Purpose

After v64, the accepted controller remains v48. Track3 still has an early
front-obstacle event while most remaining road-contact events happen in active
avoidance with low side clearance. This note records a narrow algorithm review
before trying another unified controller candidate.

## Sources

1. Bug / wall-following obstacle-avoidance summaries for range-limited robots.
   - Search topic: `range sensor obstacle avoidance wall following bug algorithm mobile robot limited sensors`
   - Use: boundary-following behavior is a reasonable fallback when a robot
     cannot plan globally and must stay conservative near obstacles.
2. Follow-the-Gap obstacle avoidance.
   - Search topic: `follow the gap obstacle avoidance algorithm range sensor autonomous vehicle`
   - Use: gap selection is useful with dense range scans, but this UGV only
     exposes front/rear/left/right distances, so the full algorithm is not a
     direct fit.
3. Vector Field Histogram / sonar-range obstacle avoidance.
   - Search topic: `vector field histogram obstacle avoidance sonar range sensors mobile robot`
   - Use: VFH-style histograms need many angular bins; the official controller
     boundary has too few range directions for a faithful implementation.

## Local Applicability

The next candidate should not copy VFH or Follow-the-Gap. The feasible local
lesson is a conservative emergency band: when the front range is already below
a very small threshold, treat the situation as collision-imminent and command a
bounded strong reverse hold through the existing obstacle controller output.

## Non-Reuse Boundary

No external code is copied. These notes only justify a narrow local behavior
candidate under the existing four-distance Sysblock interface.
