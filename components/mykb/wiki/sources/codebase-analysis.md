---
type: "source"
title: "Codebase Analysis — RSIS3 + mykb + myrsikb"
description: "Deep analysis of all three triad codebases: architecture, implementation status, and integration points"
tags: ["source", "analysis", "codebase", "audit", "triad"]
timestamp: "2026-07-21T10:12:00Z"
---


## Codebase Analysis

# Codebase Analysis

## Methodology
Analyzed all source files across the three triad projects using AST parsing, import tracking, and manual review.

## Key Metrics

### RSIS3 (rsis3/)
- Source files: ~60 Python modules across 12 subsystems
- Total functions: 435 (StubScanner)
- Stub ratio: 0% (no pass-only functions)
- Test count: 23 integration tests
- Lines of code: ~15,000+
- Database: SQLite with 13 tables

### mykb (mykb/)
- Wiki files: 2,385 OKF markdown files
- Daemon files: ~15 Python modules
- Graph: NetworkX-based co-occurrence
- Search: TF-IDF + embedding hybrid
- Lines of code: ~5,000+

### myrsikb (myrsikb/)
- Bridge files: 15 Python modules
- Cognitive subsystems: 5 (ExperienceMemory, ReflectionEngine, ExperimentManager, MetaLearningEngine, ExecutivePlanner)
- Bridge facade: MemoryClient with 11 sub-interfaces
- Lines of code: ~4,200

## Architecture Assessment

### Strengths
1. Clean separation of concerns (mind vs memory)
2. Graceful degradation everywhere
3. Human-readable knowledge (markdown, not binary)
4. Test-gated code mutations
5. Event-driven telemetry

### Gaps
1. No full autonomy loop (auto-mode requires human trigger)
2. Meta-learning not connected to pulse outcomes
3. Contradiction detection imported but not fully wired
4. Version enforcement advisory-only
5. No dashboard for Experiment Manager or Planner

**Domain:** Sources

## Related

- [[wiki/sources/README|Readme]]
