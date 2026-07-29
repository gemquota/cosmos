---
type: "project"
title: "Triad Integration — RSIS3 + mykb + myrsikb"
description: "Making mykb the long-term memory and knowledge substrate for RSIS3 while keeping them as separate codebases"
tags: ["project", "triad", "integration", "rsis3", "mykb", "myrsikb"]
timestamp: "2026-07-21T10:11:00Z"
status: "active"
---


## Triad Integration

# Triad Integration Project

## Goal
RSIS3 is the cognitive engine (mind). mykb is the knowledge OS (memory). myrsikb is the bridge (interface). Keep them separate, wire them cleanly.

## Architecture
```
RSIS3 (thinks) → MemoryClient → mykb (remembers)
```

## Completed Milestones

### Phase 1 — Foundation ✅
- sys.path.insert eliminated → importlib-based loader
- 5 cognitive subsystems (~2,477 LOC)
- Genesis hash identity
- Temporal horizon (4h deadline)
- mykb search consolidation (6 canonical formats)
- 13 integration tests

### Phase 2 — Automation ✅
- Pulse engine auto-mode (--auto)
- mykb git rollback (pre-commit hook, .gitignore)
- Dual KG resolution (mykb preferred, local fallback)

### Phase 3 — API + RRP + Metacognition ✅
- Write-enabled dashboard API (7 new endpoints)
- RRP state machine wired into auto-mode
- Dual-layer metacognition (TelemetryWriter, Subconscious Dashboard)

### Phase 4 — Audit Resolution ✅
- SQLite test isolation
- TelemetryWriter in scheduler
- --fast mode with StubScanner
- Version manifests
- Dashboard frontend (Knowledge/Goals/Subconscious tabs)
- RRP audit (20 items analyzed, key functions wired)
- Episodic planning
- KG delete/batch endpoints + UI
- ExperimentManager in auto-mode

## Remaining Work

### Near-term
- Full autonomy loop (PulseScheduler → PulseEngine auto-trigger)
- Meta-learning loop (MetaLearningEngine → pulse outcomes)
- Experiment Manager dashboard tab

### Medium-term
- Version enforcement (RSIS3_MIN_MYKB_VERSION)
- Episode retrieval in goal generation
- Dashboard tab for plans

### Long-term
- Contradiction resolution in reflection
- Autonomous experiment hypothesis generation

**Domain:** Projects

## Related

- [[wiki/projects/README|Readme]]
