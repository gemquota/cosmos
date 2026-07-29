# Cosmos — Agent Instructions

This repo contains four component projects organized under `components/`.

## Components

### `mykb/` — Knowledge OS
OKF/Obsidian wiki knowledge system with a `.wiki-daemon` server, full-text search, knowledge graph, and session capture hooks. The persistent memory layer.

### `myrsikb/` — Memory Bridge
Integration bridge between `rsis3` and `mykb`. Audit/inventory tools, context checkpoint handoffs, and memory consolidation pipelines.

### `rsis3/` — Cognitive Engine
Recursive Self-Improvement System — a three-loop architecture (L1–L3) for automated self-improvement, memory consolidation, telemetry, and recovery. Python package with CLI entry point.

### `space/` — Prompt Engineering Tool
SPACE (Superb Prompt Automatic Creation Engine) — Node.js/TypeScript project that generates structured specification documents via a multi-probe question framework.

## Active Triad

`rsis3/` + `mykb/` + `myrsikb/` form a working triad:
- `rsis3/` = the mind (cognitive engine)
- `mykb/` = the memory (knowledge OS)
- `myrsikb/` = the interface (memory bridge)

`space/` is a standalone project with no dependency on the triad.

## Deployed

- **Hub dashboard:** https://gemquota.github.io/hub/
- **Cosmos:** https://gemquota.github.io/cosmos/
