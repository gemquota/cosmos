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

## Unified Dashboard

The single dashboard lives at `components/rsis3/dashboard/index.html` and hosts all three
components in one page:

- **Overview** — ecosystem summary + RSIS3 telemetry (pulses, layers, success rate)
- **Pulses / KG / Graphs / Constraints** — RSIS3 telemetry views
- **MyKB** — embeds `components/mykb/index.html` (wiki browser) + `okf-graph.html` (knowledge graph)
- **SPACE** — embeds `components/space/web/index.html` (web UI) + `meta-viewer.html` (spec viewer)

The repo root `index.html` redirects to the dashboard. No other standalone dashboards should be added.

## Components

### `rsis3/` — Core Cognitive Engine (Python)
Three-loop recursive self-improvement system. The central component.
- L1: Per-task action loop (tool calls, observations, retries)
- L2: Per-session improvement (code gen, prompt tuning)
- L3: Cross-session evolution (memory consolidation, strategy evolution)
- Dashboard: `dashboard/index.html` (Tailwind + Chart.js, reads `rack/pulses/dashboard-data.json` via `config.js`)

### `mykb/` — Long-term Memory (Python + Markdown)
RSIS3's persistent memory layer. Obsidian wiki with TF-IDF search, temporal engine,
knowledge graph, and session capture hooks. `.wiki-daemon` server for API access.
- Wiki browser: `index.html` (self-contained)
- Knowledge graph: `okf-graph.html` (self-contained)

### `space/` — RRP Ideation Engine (TypeScript)
SPACE generates structured prompt specifications via the Recursive Refinement Protocol.
Used during RSIS3's self-improvement cycles for initial ideation and theory-crafting.
326-probe question framework across 7 series with 6 export formats.
- Web UI: `web/index.html` (self-contained SPA)
- Spec viewer: `meta-viewer.html`

## Deployed

- **Hub dashboard:** https://gemquota.github.io/hub/ (all non-COSMOS projects)
- **Cosmos:** https://gemquota.github.io/cosmos/ (redirects to unified dashboard)
