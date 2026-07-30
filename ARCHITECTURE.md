# COSMOS — Architecture

## System Architecture

```
┌────────────────────────────────────────────────────────────┐
│                    COSMOS Ecosystem                         │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                  RSIS3 (Core)                        │   │
│  │  Recursive Self-Improvement System                   │   │
│  │  3-loop architecture (L1/L2/L3)                      │   │
│  │  RRP protocol · Knowledge graph · Telemetry          │   │
│  │  Evaluator · 7 CLI commands                          │   │
│  └──────┬──────────────────────────────────┬────────────┘   │
│         │                                  │                │
│         ▼                                  ▼                │
│  ┌──────────────┐                  ┌──────────────────┐     │
│  │  MyKB        │                  │  SPACE           │     │
│  │  (Memory)    │                  │  (Ideation)      │     │
│  │              │                  │                  │     │
│  │  Persistent  │                  │  326-probe RRP   │     │
│  │  knowledge   │                  │  prompt framework│     │
│  │  store for   │                  │  for ideation &  │     │
│  │  RSIS3       │                  │  theory-crafting │     │
│  │  TF-IDF      │                  │  in self-improve │     │
│  │  search      │                  │  ment cycles     │     │
│  │  Temporal    │                  │  6 export formats│     │
│  │  engine      │                  │  7 LLM providers │     │
│  └──────────────┘                  └──────────────────┘     │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Shared Infrastructure                   │   │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────────────┐    │   │
│  │  │  CLI     │ │Dashboard │ │ GH Pages Deploy  │    │   │
│  │  │ (cosmos) │ │(HTML)    │ │ hub + cosmos     │    │   │
│  │  └──────────┘ └──────────┘ └──────────────────┘    │   │
│  └─────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────┘
```

## How They Fit Together

RSIS3 is the core cognitive engine. During its self-improvement cycles:

1. **L3 (Cross-Session):** RSIS3 consolidates experiences into MyKB (memory).
   MyKB stores knowledge graphs, session data, and temporal snapshots.

2. **L2 (Per-Session):** RSIS3 uses SPACE for initial ideation and theory-crafting.
   SPACE generates structured specifications via the RRP prompt framework.

3. **L1 (Per-Task):** RSIS3 executes tool calls and observations, referencing
   both MyKB (past knowledge) and SPACE outputs (current plan).

## Component Communication

| From | To | Mechanism | Data |
|------|----|-----------|------|
| RSIS3 | MyKB | `.wiki-daemon` API | Memory storage/retrieval, session tracking |
| RSIS3 | SPACE | CLI invocation | Prompt specs, structured outputs |
| Dashboard | All | HTTP (static/local) | Status checks, iframe embeds |

## Deployment

- **Cosmos dashboard** → `gemquota.github.io/cosmos/` (single HTML file)
- **Hub dashboard** → `gemquota.github.io/hub/` (non-COSMOS projects)
- **Local** → `./start.sh` serves everything from port 9000
