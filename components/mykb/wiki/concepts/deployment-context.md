---
type: "concept"
title: "Deployment Context"
description: "RSIS3 runs on Android Termux and Codex web app — dual-environment deployment"
tags: ["deployment", "termux", "android", "codex", "environment"]
timestamp: "2026-07-21T11:10:00Z"
---


## Deployment Context

# Deployment Context

## Current Environments

### 1. Android Termux (Primary)
- **Device:** Android phone running Termux terminal emulator
- **OS:** Android Linux environment via Termux
- **Shell:** bash
- **Python:** 3.13+
- **SQLite:** WAL mode, thread-safe singleton
- **Storage:** Internal device storage
- **Networking:** Mobile data / WiFi
- **Path:** `/data/data/com.termux/files/home/dev/codex/`

### 2. Codex Web App
- **Platform:** Codex CLI web interface
- **Access:** Browser-based terminal
- **Environment:** Remote/cloud execution environment
- **Same filesystem:** The web app accesses the same workspace

## Implications

### Persistent Services
- Dashboard (FastAPI, port 8765) runs in Termux
- PulseScheduler daemon runs as background thread
- TelemetryWriter writes to device storage

### Resource Constraints
- Mobile CPU/thermal constraints (10s pulse cycle monitoring)
- No GPU for embeddings (CPU-only TF-IDF fallback)
- Limited RAM for large models

### Connectivity
- No production LLM API key — agent acts as proxy
- Git operations for code versioning
- mykb wiki sync via git

## Production Target
When API key is added, the system will:
1. Use MemoryClient to retrieve context from mykb
2. Call LLM API for pulse generation, RRP analysis, codegen
3. Write results back to mykb automatically
4. Agent shifts to supervisor/monitoring role

**Domain:** Concepts

## Related

- [[wiki/concepts/mykb-analysis|Mykb Analysis]]
- [[wiki/concepts/mykb-research-report|Mykb Research Report]]
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]]
- [[wiki/concepts/triad-architecture|Triad Architecture]]
- [[wiki/concepts/pulse-cycle|Pulse Cycle]]
- [[wiki/concepts/identity-system|Identity System]]
