---
type: "concept"
title: "RSIS3 Memory Bridge"
description: "The contract by which mykb serves as RSIS3's long-term memory and semantic knowledge database"
tags: ["rsis3", "mykb", "memory", "architecture", "integration", "semantic"]
timestamp: "2026-07-31T00:00:00Z"
---

# RSIS3 Memory Bridge

mykb is RSIS3's persistent memory layer: a human-readable knowledge base
(OKF/Obsidian markdown) that the cognitive engine reads for planning and writes
to after every loop. This page is the contract between the two systems.

## Read Paths (RSIS3 → mykb)

| Query | Mechanism | Files |
|---|---|---|
| Concept retrieval | `okf search` / hybrid index (`search_fusion.py`) | `wiki/concepts/`, `wiki/syntheses/` |
| Semantic graph | `graph.json` (nodes + edges from wikilinks & shared tags) | `graph.json`, `wiki/**/*.md` |
| Temporal trends | `temporal_engine.py` (rising/falling topics) | `wiki/daily/`, `wiki/log.md` |
| Knowledge gaps | gap detector over tag/type coverage | `wiki/index.md`, `ops/wiki-schema.md` |
| Decision recall | tag `decision` | `wiki/decisions/` |
| Session memory | per-session captures | `wiki/sessions/` (archive) |

## Write Paths (RSIS3 → mykb)

| Event | Target |
|---|---|
| Pulse outcome | `wiki/pulses/` (type `pulse`) |
| RRP conversation | `wiki/sessions/` (type `session`) |
| Decision | `wiki/decisions/` (type `decision`) |
| Identity snapshot | `wiki/identity/` (type `snapshot`) |
| Learned strategy | `wiki/concepts/`, `wiki/syntheses/` (type `concept`/`synthesis`) |
| Log line | `wiki/log.md` (ISO date heading) |

## API Surface

- `GET /graph.json` — full knowledge graph
- `GET /api/v2/graph/topology?root=<id>&depth=<n>` — subgraph
- `GET /api/stats` — bundle health
- `GET /search?q=<term>` — hybrid search
- Static fallback: `files.json`, `wiki/index.json`, `graph.json` serve the same
  data on GitHub Pages without the daemon.

## Semantic Database Role

The wiki doubles as a semantic database:

- **Nodes** are files; **edges** are markdown links (explicit) plus tag-sharing
  edges (≥3 shared tags) — the graph is emergent from real references.
- **Types** (`concept`, `synthesis`, `source`, `decision`, `pulse`, ...) form a
  lightweight ontology; `ops/wiki-schema.md` defines the vocabulary.
- **Tags** are the cross-cutting dimensions used for clustering and retrieval.

## Related

- [[wiki/concepts/triad-architecture|Triad Architecture]]
- [[wiki/concepts/pulse-cycle|Pulse Cycle]]
- [[wiki/syntheses/knowledge-system|Knowledge System]]
- [[wiki/entities/memory-client|Memory Client]]
- [[wiki/entities/rrp-state-machine|RRP State Machine]]
- [[ops/knowledge-acquisition|Knowledge Acquisition]]
- [[ops/wiki-schema|Wiki Schema]]
