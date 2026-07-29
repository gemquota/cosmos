# 🌌 COSMOS — Complete Ecosystem Reference

**Comprehensive Ontological System for Meta-cognitive Orchestration & Synthesis**

*Generated:* 2026-07-29
*Version:* 0.1.0
*Location:* `~/dev/cosmos/`

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Unification Specification](#2-unification-specification)
   - 2.1 [Purpose](#21-purpose)
   - 2.2 [Component Map](#22-component-map)
   - 2.3 [Relationship Diagram](#23-relationship-diagram)
   - 2.4 [Directory Structure](#24-directory-structure)
   - 2.5 [Implementation Phases](#25-implementation-phases)
3. [Architecture](#3-architecture)
   - 3.1 [System Context](#31-system-context)
   - 3.2 [Component Communication](#32-component-communication)
   - 3.3 [Deployment Model](#33-deployment-model)
4. [Development Roadmap](#4-development-roadmap)
   - 4.1 [Phase 0: Specification & Structure](#41-phase-0-specification--structure)
   - 4.2 [Phase 1: Shared Infrastructure](#42-phase-1-shared-infrastructure)
   - 4.3 [Phase 2: Orchestrator CLI](#43-phase-2-orchestrator-cli)
   - 4.4 [Phase 3: Dashboard](#44-phase-3-dashboard)
   - 4.5 [Phase 4: Integration](#45-phase-4-integration)
5. [Current Status](#5-current-status)
   - 5.1 [What Was Built](#51-what-was-built)
   - 5.2 [Component Inventory](#52-component-inventory)
   - 5.3 [Running Services](#53-running-services)
6. [Component Details](#6-component-details)
   - 6.1 [SPACE — Prompt Engine](#61-space--prompt-engine)
   - 6.2 [myKB — Knowledge Base](#62-mykb--knowledge-base)
   - 6.3 [myRSIKB — RSI Knowledge Base](#63-myrsikb--rsi-knowledge-base)
   - 6.5 [RSIS3 — 3-Loop RSI System](#65-rsis3--3-loop-rsi-system)
7. [CLI Reference](#7-cli-reference)
8. [Dashboard Reference](#8-dashboard-reference)
9. [Infrastructure](#9-infrastructure)
10. [Quick Start](#10-quick-start)

---

## 1. Executive Summary

COSMOS unifies four RSI-family projects — SPACE, myKB, myRSIKB, and RSIS3 — into a coherent ecosystem with shared infrastructure, a unified orchestrator CLI, and a consolidated dashboard.

The four projects began as independent efforts:
- **SPACE** evolved from the `prompt-framework` audit into a full TypeScript prompt/spec engine
- **myKB** grew as a daily Obsidian wiki knowledge base
- **myRSIKB** became an RSI knowledge base with audit reports
- **RSIS3** is a Python-based recursive self-improvement system

---

## 2. Unification Specification

### 2.1 Purpose

COSMOS unifies four RSI-family projects — SPACE, myKB, myRSIKB, and RSIS3 — into a coherent ecosystem with shared infrastructure, a unified orchestrator CLI, and a consolidated dashboard.

### 2.2 Component Map

| ID | Component | Source | Role | Language |
|:--:|-----------|--------|------|:--------:|
| C1 | **SPACE** | `~/dev/space/` | Prompt engine, CLI, spec generation | TypeScript |
| C2 | **myKB** | `~/dev/codex/mykb/` | Daily knowledge base (Obsidian wiki) | Markdown/Python |
| C3 | **myRSIKB** | `~/dev/codex/myrsikb/` | RSI knowledge base, audit reports | Python |

| C5 | **RSIS3** | `~/dev/codex/rrp+/rsis/` | 3-loop RSI system | Python |


### 2.3 Relationship Diagram

```
myKB ◄──► myRSIKB ◄── RSIS3
  ▲                   ▲
  │                   │
  └────── SPACE ──────┘
```

- **myRSIKB** feeds into RSIS3 with audit reports and analysis
- **SPACE** provides prompt/spec generation that feeds into the knowledge ecosystem


### 2.4 Directory Structure

```
cosmos/
├── COSMOS-SPEC.md              # Unification specification
├── ARCHITECTURE.md              # Architecture overview
├── ROADMAP.md                   # Development roadmap
├── README.md                    # Entry point
├── components/                  # Duplicated project sources
│   ├── space/                   # C1 — TypeScript prompt engine (9.4MB)
│   ├── mykb/                    # C2 — Obsidian knowledge base (335MB)
│   ├── myrsikb/                 # C3 — RSI knowledge base (3.1MB)
│   
│   ├── rsis3/                   # C5 — 3-loop RSI system (4.7MB)
│   
├── infra/                       # Shared infrastructure
│   ├── heartbeat/               # Sentry monitoring
│   │   ├── watches.json         # Service definitions
│   │   └── heartbeat.mjs        # Monitor daemon
│   ├── ci/                      # Shared CI/CD (TBD)
│   └── deployment/              # Deploy scripts (TBD)
├── cli/                         # Orchestrator CLI
│   └── cosmos                   # Unified command (symlinked to ~/.local/bin/)
├── dashboard/                   # Unified web dashboard
│   └── index.html               # SPA with component cards + meta viewer
├── serve-dashboard.mjs          # Dashboard HTTP server
├── docs/                        # Shared documentation
│   └── COSMOS-COMPLETE.md       # This file — complete ecosystem reference
└── meta/                        # Cycle audit/review docs (TBD)
```

### 2.5 Implementation Phases

| Phase | Focus | Deliverables | Status |
|:-----:|-------|-------------|:------:|
| **0** | Specification & Structure | COSMOS-SPEC.md, ARCHITECTURE.md, component copies, ROADMAP.md | ✅ **Complete** |
| **1** | Shared Infrastructure | Sentry heartbeat for all components, CI/CD, deploy scripts | 🔄 Partial |
| **2** | Orchestrator CLI | `cosmos` command with all subcommands | ✅ **Complete** |
| **3** | Dashboard | Unified web UI with status, cards, embedded meta viewer | ✅ **Complete** |
| **4** | Integration | Cross-component data flow integration | ⬜ Pending |

---

## 3. Architecture

### 3.1 System Context

```
┌────────────────────────────────────────────────────────────┐
│                    COSMOS Ecosystem                         │
│                                                             │
│  ┌──────────┐  ┌────────────────────────────────────────┐ │
│  │          │  │           Shared Infrastructure         │ │
│  │   CLI    │  │  ┌──────────┐ ┌──────┐ ┌──────────┐   │ │
│  │ (cosmos) │──┼─▶│ Heartbeat│ │ CI/CD│ │Dashboard │   │ │
│  │          │  │  └──────────┘ └──────┘ └──────────┘   │ │
│  └──────────┘  └────────────────────────────────────────┘ │
│       │                                                    │
│       │ controls                                           │
│       ▼                                                    │
│  ┌──────────────────────────────────────────────────┐     │
│  │                   Components                      │     │
│  │  ┌───────┐ ┌──────┐ ┌───────┐ ┌────────┐ ┌───┐  │     │
│  │  │ SPACE │ │ myKB │ │myRSIKB│ │RSIS3│  │     │
│  │  │  TS   │ │MD/Py │ │  Py   │ │  Py    │ │ Py  │  │     │
│  │  └───────┘ └──────┘ └───────┘ └────────┘ └───┘  │     │
│  └──────────────────────────────────────────────────┘     │
└────────────────────────────────────────────────────────────┘
```

### 3.2 Component Communication

| From | To | Mechanism | Data |
|------|----|-----------|------|
| SPACE | myKB | File export | Spec documents → wiki pages |
| myKB | RSIS3 | File read | Knowledge → RSI processing |
| RSIS3 | myKB | File write | RSI outputs → wiki storage |
| Dashboard | All | HTTP health check | Status polling |

### 3.3 Deployment Model

```
GitHub ──► CI/CD ──► Build ──► GitHub Pages / Local Servers
                                      │
                                      ▼
                              Sentry Heartbeat
                              (auto-restart on failure)
```

---

## 4. Development Roadmap

### 4.1 Phase 0: Specification & Structure ✅

- [x] Create COSMOS directory structure
- [x] Write COSMOS-SPEC.md
- [x] Write ARCHITECTURE.md
- [x] Write ROADMAP.md
- [x] Copy SPACE into components/
- [x] Copy myKB into components/
- [x] Copy myRSIKB into components/
- [x] Copy myRSIKB into components/ (was myRSISKB)
- [x] Copy RSIS3 into components/


### 4.2 Phase 1: Shared Infrastructure

- [ ] Unified Sentry watcher for all components
- [ ] Shared CI/CD workflow (GitHub Actions)
- [ ] Shared deployment scripts
- [ ] Centralized logging
- [x] Sentry heartbeat for COSMOS servers (partial — monitors Dashboard + SPACE)

### 4.3 Phase 2: Orchestrator CLI ✅

- [x] `cosmos status` — check all components
- [x] `cosmos start/stop` — control component servers
- [x] `cosmos logs` — tail component logs
- [x] `cosmos list` — inventory all components
- [x] `cosmos build/test` — build and test all
- [x] `cosmos help` — usage reference
- [x] Install via `~/.local/bin/` symlink

### 4.4 Phase 3: Dashboard ✅

- [x] Status panel with component cards
- [x] Health metrics and file counts
- [x] Quick links to component servers
- [x] Embedded meta document viewer
- [x] Server on port 9000

### 4.5 Phase 4: Integration

- [ ] SPACE → myKB spec export
- [ ] Cross-component data flow integration
- [ ] Cross-component data flows
- [ ] Live health checking from dashboard
- [ ] Aggregated logging

---

## 5. Current Status

### 5.1 What Was Built

During the initial COSMOS bootstrap (2026-07-29), all Phase 0, 2, and 3 items were delivered:

| What | Path | Status |
|------|------|:------:|
| **Directory structure** | `~/dev/cosmos/` | ✅ |
| **Unification spec** | `COSMOS-SPEC.md` | ✅ |
| **Architecture doc** | `ARCHITECTURE.md` | ✅ |
| **Roadmap** | `ROADMAP.md` | ✅ |
| **4 components copied** | `components/{space,mykb,myrsikb,rsis3}/` | ✅ |
| **Sentry heartbeat** | `infra/heartbeat/` (watches dashboard + SPACE servers) | ✅ |
| **Orchestrator CLI** | `cli/cosmos` → `~/.local/bin/cosmos` | ✅ |
| **Dashboard** | `dashboard/index.html` on `:9000` | ✅ |

### 5.2 Component Inventory

| Component | Type | Files | Size | Language |
|-----------|:----:|:-----:|:----:|:--------:|
| **SPACE** | Engine | 540 | 9.4 MB | TypeScript |
| **myKB** | Knowledge Base | 2,492 | 335 MB | Markdown + Python |
| **myRSIKB** | RSI Knowledge Base | 44 | 3.1 MB | Python |
| **RSIS3** | 3-Loop RSI | 137 | 4.7 MB | Python |

### 5.3 Running Services

| Service | Port | Status | Monitored |
|:-------:|:----:|:------:|:---------:|
| COSMOS Dashboard | 9000 | 🟢 UP | ✅ Sentry |
| SPACE Meta Viewer | 8899 | 🟢 UP | ✅ Sentry |
| SPACE Web UI | 8888 | 🔴 DOWN | ✅ Sentry |

---

## 6. Component Details

### 6.1 SPACE — Prompt Engine

- **Source:** `~/dev/space/`
- **COSMOS path:** `components/space/`
- **Language:** TypeScript
- **npm package:** `@gemquota/space`
- **Version:** 2.1.0
- **Tests:** 150 passing (14 suites)
- **CLI commands:** init, run, export, list, framework, config, serve, status
- **LLM providers:** 7 (OpenAI, Anthropic, Gemini, Mistral, Ollama, Local, Null)
- **Export formats:** 6 (JSON, Markdown, YAML, Prompt, HTML, Diff)
- **Storage:** Filesystem + SQLite
- **Web UI:** React 18 + Vite

SPACE is a prompt engineering and specification generation engine. It evolved from an audit of the original `prompt-framework` codebase (a 326-probe elicitation methodology across 7 series and 25 rounds). The TypeScript codebase implements a full session lifecycle, question routing, artifact tracking, dependency resolution, LLM integration, multi-format export, and an intelligence layer with analytics and contradiction detection.

**Key servers:**
- Meta Viewer: port 8899 — browses cycle audit/review documents
- Web UI: port 8888 — React frontend (requires `npm run build` in `ui/`)

### 6.2 myKB — Knowledge Base

- **Source:** `~/dev/codex/mykb/`
- **COSMOS path:** `components/mykb/`
- **Language:** Markdown + Python
- **Type:** Obsidian wiki / OKF bundle

myKB is a personal wiki knowledge iteration system for daily learning, formatted as an Open Knowledge Format (OKF) bundle. It contains daily notes (`daily/`), processed wiki entries (`wiki/`), raw material (`raw/`), templates (`templates/`), and operational workflows (`ops/`). It includes Python scripts for building exports and indexes.

### 6.3 myRSIKB — RSI Knowledge Base

- **Source:** `~/dev/codex/myrsikb/`
- **COSMOS path:** `components/myrsikb/`
- **Language:** Python
- **Files:** 44

myRSIKB contains RSI knowledge base content with audit reports, inventory, and analysis scripts. It generates standalone audit report HTML and JSON.

### 6.5 RSIS3 — 3-Loop RSI System

- **Source:** `~/dev/codex/rrp+/rsis/`
- **COSMOS path:** `components/rsis3/`
- **Language:** Python
- **Files:** 137

RSIS3 (Recursive Self-Improvement System) implements a three-loop architecture defined by an RRP session (11 locked decisions, 0 contradictions):

```
L3 ─ Cross-Session Evolution (hours/days)
  ├─ Memory consolidation (git → KG → vectors)
  ├─ Meta-strategy derivation
  ├─ Redundancy refinement
  └─ L2 heuristic evolution

L2 ─ Improvement Loop (per-session)
  ├─ Code change generation
  ├─ Feature implementation
  └─ Refactoring

L1 ─ Execution Loop (real-time)
  └─ Task execution
```

### Example Usage

```bash
cosmos status            # 🟢 space running, others idle
cosmos list              # all 6 components with file counts
cosmos start space       # fires up SPACE servers (meta viewer + web UI)
cosmos start all         # starts all component servers + heartbeat
cosmos stop              # kills all servers
cosmos logs              # tails the sentry log
cosmos logs space        # tails only SPACE entries
cosmos build space       # builds SPACE
cosmos test rsis3        # tests RSIS3
```

---

## 8. Dashboard Reference

The COSMOS dashboard is a single-page application served on port 9000.

### Features

- **6 component cards** — Each card shows name, type icon, file count, test count (where available), and status indicator
- **Status indicators** — Running (🟢), Idle (⚪), Missing (🔴)
- **Quick links** — Direct links to component web servers (e.g., SPACE Meta Viewer, SPACE Web UI)
- **Meta document viewer** — Embedded reader for COSMOS-SPEC.md, ARCHITECTURE.md, ROADMAP.md, and README.md with syntax-highlighted markdown rendering
- **Global status badge** — Shows aggregate component health

### Starting

```bash
cd ~/dev/cosmos
node serve-dashboard.mjs 9000
# → http://localhost:9000
```

Or via the orchestrator:
```bash
cosmos start all   # starts dashboard + all servers
```

---

## 9. Infrastructure

### 9.1 Sentry Heartbeat

Located at `infra/heartbeat/`. Monitors COSMOS services and auto-restarts on failure.

**Config:** `infra/heartbeat/watches.json`

```json
[
  { "name": "COSMOS Dashboard", "port": 9000, "path": "/" },
  { "name": "SPACE Meta Viewer", "port": 8899, "path": "/" },
  { "name": "SPACE Web UI", "port": 8888, "path": "/" }
]
```

Each watch has `startCmd`, `startArgs`, and `cwd` for auto-restart.

### 9.2 CI/CD (Planned)

Shared GitHub Actions workflow (TBD — Phase 1):
- Run tests for all components on push
- Lint all codebases
- Build all artifacts
- Deploy dashboard to GitHub Pages

### 9.3 Logging

Centralized logging at `~/dev/cosmos/sentry.log` with component-prefixed entries.

---

## 10. Quick Start

```bash
# 1. Source the environment
export PATH="$HOME/.local/bin:$PATH"

# 2. Check the ecosystem
cosmos status

# 3. List all components with details
cosmos list

# 4. Start everything
cosmos start all

# 5. Open the dashboard
#    http://localhost:9000

# 6. Check individual component health
cosmos status
sentry status

# 7. View logs
cosmos logs

# 8. Stop everything
cosmos stop
```

---

*End of COSMOS Complete Ecosystem Reference*
