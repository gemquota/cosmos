---
type: "entity"
title: "MemoryClient"
description: "Unified facade over all mykb subsystems — RSIS3's only interface to persistent memory"
tags: ["bridge", "facade", "memory", "myrsikb", "api"]
timestamp: "2026-07-21T10:05:00Z"
---


## Memory Client

# MemoryClient

**Source:** `myrsikb/memory_bridge/client.py`

MemoryClient is the central facade that RSIS3 imports. It wraps 11 sub-interfaces:

- `wiki` — WikiWriter (entity/rrp/tool pages)
- `graph` — KnowledgeGraph (nodes, edges, community detection)
- `semantic` — SemanticMemory (vector search, TF-IDF)
- `temporal` — TemporalMemory (rising/falling trends, monthly activity)
- `gaps` — GapDetector (low coverage, acronyms, missing tags)
- `experiences` — ExperienceMemory (pulse encoding, episodic retrieval)
- `reflection` — ReflectionEngine (meta-goals, strategy)
- `experiments` — ExperimentManager (A/B testing, adoption)
- `meta_learning` — MetaLearningEngine (parameter tuning)
- `planner` — ExecutivePlanner (hierarchical plans, contingencies)

### Usage Pattern
```python
from memory_bridge import MemoryClient
kb = MemoryClient()  # auto-discovers wiki path
kb.store_identity_snapshot(sid, data)
kb.store_rrp_session(session_id, ...)
results = kb.search("crisis recovery patterns")
```

### Version Checking
On init, reads VERSION files from all three triad projects. Warns if versions mismatch.

### Graceful Degradation
All bridge methods are wrapped in try/except. If mykb is unavailable, RSIS3 continues without memory.

**Domain:** Entities

## Related

- [[wiki/entities/identity-snapshot-0001|Identity Snapshot 0001]]
- [[wiki/entities/pulse-engine|Pulse Engine]]
- [[wiki/entities/rrp-state-machine|Rrp State Machine]]
- [[wiki/entities/llm-proxy-agent|Llm Proxy Agent]]
- [[wiki/entities/e2e-test-001|E2E Test 001]]
- [[wiki/entities/e2e-entity|E2E Entity]]
