# Cosmos — Agent Instructions

This repo integrates three component projects under `components/`.

## Architecture (RSIS3-Centric)

```
┌─────────────────────────────────────┐
│           RSIS3 (core)              │
│  Recursive Self-Improvement System  │
│  3-loop architecture (L1/L2/L3)     │
│  with RRP protocol                  │
└────────┬────────────┬───────────────┘
         │            │
         ▼            ▼
┌─────────────────┐  ┌────────────────────┐
│  MyKB (memory)  │  │  SPACE (ideation)  │
│  Persistent     │  │  RRP prompt engine │
│  knowledge      │  │  for self-improve- │
│  store for      │  │  ment cycles —     │
│  RSIS3          │  │  ideation & theory │
└─────────────────┘  └────────────────────┘
```

## Components

### `rsis3/` — Core Cognitive Engine (Python)
Three-loop recursive self-improvement system. The central component.
- L1: Per-task action loop (tool calls, observations, retries)
- L2: Per-session improvement (code gen, prompt tuning)
- L3: Cross-session evolution (memory consolidation, strategy evolution)

### `mykb/` — Long-term Memory (Python + Markdown)
RSIS3's persistent memory layer. Obsidian wiki with TF-IDF search, temporal engine,
knowledge graph, and session capture hooks. `.wiki-daemon` server for API access.

### `space/` — RRP Ideation Engine (TypeScript)
SPACE generates structured prompt specifications via the Recursive Refinement Protocol.
Used during RSIS3's self-improvement cycles for initial ideation and theory-crafting.
326-probe question framework across 7 series with 6 export formats.

## Deployed

- **Hub dashboard:** https://gemquota.github.io/hub/ (all non-COSMOS projects)
- **Cosmos:** https://gemquota.github.io/cosmos/ (RSIS3 + MyKB + SPACE)
