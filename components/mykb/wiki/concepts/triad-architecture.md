---
type: "concept"
title: "Triad Architecture"
description: "Three-project architecture: RSIS3 (cognitive engine) + mykb (knowledge OS) + myrsikb (memory bridge)"
tags: ["architecture", "triad", "rsis3", "mykb", "myrsikb", "cognitive-architecture"]
timestamp: "2026-07-21T10:00:00Z"
---


## Triad Architecture

# Triad Architecture

The triad is a three-project architecture that separates cognition from memory:

## Layers

### RSIS3 — The Mind (Cognitive Engine)
- **Identity** — Self-model with genesis hash, layer scores, crisis monitor
- **Pulse Engine** — 9-phase evaluation protocol, telemetry writer
- **RRP** — Recursive Refinement Protocol, 2,025-line state machine
- **Code Generation** — AST-aware surgical patching
- **Self-Direction (L3)** — Goal generation, prioritization, execution
- **Dashboard** — FastAPI server on port 8765
- **Recovery** — Git-based rollback on test failure

### mykb — The Memory (Knowledge OS)
- **Wiki** — 2,385 OKF markdown files in Obsidian-compatible format
- **Graph Engine** — NetworkX co-occurrence graph with community detection
- **Vector Search** — TF-IDF and embedding-based semantic search
- **Temporal Engine** — Rising/falling topic detection, monthly activity
- **Gap Detector** — Knowledge coverage analysis, acronym detection
- **Backlink Engine** — Entity backlink traversal
- **Daemon** — Search/embed/graph/curate pipeline

### myrsikb — The Interface (Memory Bridge)
- **MemoryClient** — 5 sub-interface facade (wiki, graph, semantic, temporal, gaps)
- **ExperienceMemory** — Episodic pulse encoding
- **ReflectionEngine** — Meta-goal generation from system state
- **ExperimentManager** — A/B testing lifecycle
- **MetaLearningEngine** — Parameter tuning from outcomes
- **ExecutivePlanner** — Hierarchical planning with contingency
- **TelemetryWriter** — Rate-limited subconscious observation stream

## Data Flow

```
RSIS3 (thinks)
  │
  │  Identity snapshots → mykb/wiki/identity/
  │  Pulse outcomes     → mykb/wiki/pulses/
  │  RRP sessions       → mykb/wiki/sessions/
  │  Decisions          → mykb/wiki/decisions/
  │  KG nodes/edges     → mykb/wiki/entities/ + graph engine
  │
  ▼
mykb (remembers)
  │
  │  Semantic search   → RSIS3 planning
  │  Temporal trends   → RSIS3 goal generation
  │  Knowledge gaps    → RSIS3 reflection
  │  Similar pulses    → RSIS3 decision support
  │
  ▼
RSIS3 (improves)
```

## Key Design Decisions

1. **Graceful degradation** — Every bridge call wrapped in try/except. mykb unavailable? RSIS3 continues without memory.
2. **mykb is human-readable** — Plain markdown in Obsidian layout. No binary-only formats.
3. **RSIS3 is test-gated** — No mutation accepted unless all tests pass. git-rollback on failure.
4. **Bridge is the contract** — myrsikb/memory_bridge/ is the only interface. Neither RSIS3 nor mykb imports the other directly.
5. **Version alignment** — VERSION files in all three projects. MemoryClient warns on mismatch.

## Current Versions

- RSIS3: 0.1.0
- mykb: 0.1.0
- myrsikb: 0.1.0

**Domain:** Concepts

## Related

- [[wiki/concepts/mykb-analysis|Mykb Analysis]]
- [[wiki/concepts/mykb-research-report|Mykb Research Report]]
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]]
- [[wiki/concepts/pulse-cycle|Pulse Cycle]]
- [[wiki/concepts/identity-system|Identity System]]
- [[wiki/concepts/project-lineage|Project Lineage]]
