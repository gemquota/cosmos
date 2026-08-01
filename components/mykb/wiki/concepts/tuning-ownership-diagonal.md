---
type: "concept"
title: "Tuning Ownership Diagonal"
description: "The +3 rule: loop k+3 tunes loop k, so every parameter has exactly one writer"
tags: [ownership, topology, rsis3, architecture, concurrency]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# Tuning Ownership Diagonal

## Summary
The tuning ownership diagonal is the rule that resolves overlapping loops: loop k+3 tunes loop k. L4→L1, L5→L2, L6→L3, L7→L4, L8→L5, L9→L6. Every tunable parameter has exactly one writer, which makes concurrent loops safe by construction: no two loops share a write key, even though many share reads.

## Details
- **Why +3**: it creates exactly three meta-levels — core (L1–L3), tuners (L4–L6), meta-tuners (L7–L9) — capping modification depth.
- **Registry enforcement**: `config.py` holds one `L{N}_TUNABLES` registry per tuner; the practices checker verifies the keys are disjoint.
- **Reads are shared**: L3, L4, L5 all read outcome telemetry; sharing reads is intended and safe.
- **Writes are exclusive**: state files are per-loop (`optimizer_state.json`, `strategies.json`, …) so file-level ownership matches key-level ownership.
- Worked example: only L8 may write `l5.mutation_rate`; L5 reads it from config but never writes it.

## Related
- [[wiki/concepts/nine-loop-hierarchy|Nine-Loop Hierarchy]] — the loop roster this rule governs
- [[wiki/concepts/recursion-guard|Recursion Guard]] — why the diagonal terminates at L9
- [[wiki/concepts/meta-parameter-tuning|Meta-Parameter Tuning]] — the act the diagonal arbitrates
- [[wiki/concepts/triad-architecture|Triad Architecture]] — the wider ownership picture