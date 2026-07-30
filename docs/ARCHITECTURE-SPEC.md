# COSMOS — Architecture Specification

> A machine-readable architecture document for generating architectural visualizations.
> Designed to be fed into an LLM with the prompt: "Generate architectural diagrams from this spec."

---

## 1. System Overview

### 1.1 Identity

- **Name:** COSMOS (Cognitive Orchestration System for Meta-cognitive Orchestration & Synthesis)
- **Purpose:** Unified cognitive ecosystem for recursive self-improvement
- **Core paradigm:** RSIS3 is the central cognitive engine. MyKB serves as its long-term memory. SPACE provides RRP-based ideation during self-improvement cycles.
- **Deployment:** Static GitHub Pages + local development servers

### 1.2 Architecture Style

- **Pattern:** Hub-and-spoke with RSIS3 as the hub
- **Communication:** Synchronous HTTP (local), file-system sharing, CLI invocation
- **State:** Ephemeral (runtime) + persistent (MyKB wiki + filesystem)
- **Hosting:** GitHub Pages for dashboards, local Python/Node servers for services

### 1.3 Layer Diagram (Conceptual)

```
┌──────────────────────────────────────────────────────────────┐
│                      PRESENTATION LAYER                       │
│  ┌────────────────────────────────────────────────────────┐  │
│  │  COSMOS Dashboard (index.html)                         │  │
│  │  Hub Dashboard (hub/index.html)                        │  │
│  │  GitHub Pages                                          │  │
│  └──────────────────────────┬─────────────────────────────┘  │
│                             │ HTTP/iframe                     │
├─────────────────────────────┼────────────────────────────────┤
│                      SERVICE LAYER                            │
│  ┌──────────────┐  ┌───────┴────────┐  ┌──────────────────┐  │
│  │  RSIS3 Core  │  │  MyKB Memory  │  │  SPACE Ideation  │  │
│  │  port:8080   │  │  port:8765    │  │  port:8888       │  │
│  │  (or static) │  │  server.py    │  │  (static files)  │  │
│  └──────┬───────┘  └───────┬────────┘  └────────┬─────────┘  │
│         │                  │                     │            │
├─────────┼──────────────────┼─────────────────────┼────────────┤
│         │         DATA LAYER                     │            │
│  ┌──────┴──────────────────┴─────────────────────┴────────┐  │
│  │  File System (/dev/cosmos/components/)                  │  │
│  │  ├── rsis3/    (112 files, 4.1MB)                      │  │
│  │  ├── mykb/     (2,436 files, 58MB)                     │  │
│  │  └── space/    (333 files, 8.0MB)                      │  │
│  └─────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

---

## 2. Component Architecture

### 2.1 RSIS3 — Core Cognitive Engine

**Role:** Central self-improvement system. Three-loop recursive architecture.

**Location:** `components/rsis3/`
**Size:** 112 files, 4.1MB, ~67k LOC
**Languages:** Python (4,858), JavaScript (20,023), HTML (7,760), JSON (33,738), CSS (94), Shell (32)
**Status:** Active triad member

#### Architecture (Three-Loop)

```
L3 ── Cross-Session Evolution (hours/days)
  ├── Memory consolidation (git → KG → vectors)
  ├── Strategy & meta-parameter evolution
  └── Redundancy refinement pruning
  │
L2 ── Per-Session Improvement (minutes)
  ├── Code generation & architecture modification
  ├── Prompt/tool tuning
  └── Validated by IMMUTABLE AI evaluator
  │
L1 ── Per-Task Action Loop (seconds)
  ├── Tool calls, observations, retries
  └── Immediate feedback
```

#### Subsystems

| Subsystem | Path | Description |
|-----------|------|-------------|
| Dashboard UI | `dashboard/` | Telemetry dashboard with Chart.js, Tailwind |
| Rack | `rack/` | Pulse engine, testing, Vue-based diagnostics |
| RSI Core | `rsis/` | Main RSI package with dashboard templates |
| Telemetry | `telemetry-dashboard/` | Backend + frontend telemetry views |
| Evaluator | `evaluator/` | IMMUTABLE AI evaluator module |
| Vercel Deploy | `vercel-deploy/` | Vercel deployment config |

#### API Surface (when running via `python3 -m rsis`)

Not formally defined — primarily CLI-based. The rack dashboard serves static HTML with Chart.js visualizations. The telemetry dashboard has a Flask-style backend.

#### Key Files

- `rsis/__init__.py` — Package entry point
- `dashboard/index.html` — Main telemetry dashboard (Tailwind + Chart.js)
- `rack/telemetry-dashboard.html` — 20-pulse telemetry view
- `rack/pulses/` — Pulse data directory
- `rsis/dashboard/templates/` — Search results and base templates

---

### 2.2 MyKB — Long-term Memory

**Role:** Persistent knowledge store for RSIS3. Obsidian wiki with search daemon.

**Location:** `components/mykb/`
**Size:** 2,436 files, 58MB, ~103k LOC (mostly markdown)
**Languages:** Python (2,377), Markdown (97,790), JSON (51,490), HTML (4,154), Shell (66)
**Status:** Active triad member

#### Structure

```
mykb/
├── server.py              # HTTP server (port 8765)
├── wiki/                  # Wiki content (2,360+ .md files)
│   ├── agent-systems/
│   ├── ai-ml/
│   ├── android-core/
│   ├── api-protocols/
│   ├── api-services/
│   ├── cloud-infra/
│   ├── concepts/
│   ├── development/
│   ├── frontend/
│   ├── llm-agents/
│   ├── meta-learning/
│   ├── prompt-engineering/
│   ├── security/
│   └── ... (48 domains total)
├── .wiki-daemon/          # Daemon server, search index, graph, temporal engine
│   ├── config.json
│   ├── search_index.json
│   ├── graph.json
│   ├── temporal_engine.py
│   ├── search_fusion.py
│   ├── enrich_links.py
│   ├── kb_linter.py
│   └── buffers/
├── templates/             # Note templates
├── hooks/                 # Session capture hooks
├── ops/                   # Workflows, schema, prompts, reports
├── raw/                   # Raw material / inbox
└── daily/                 # Daily notes
```

#### API Surface (server.py on port 8765)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Serve markdown files as HTML |
| `/files.json` | GET | List all .md files (recursive) |
| `/api/file?path=` | GET | Return raw file content |
| `/api/search?q=` | GET | TF-IDF search across all docs |
| `/api/v2/search?q=` | GET | Enhanced TF-IDF search |
| `/api/v2/info` | GET | System stats (file counts, domains, tags) |
| `/api/v2/history/snapshot?path=&ts=` | GET | Time-travel snapshot |
| `/api/v2/search/build` | POST | Rebuild search index |
| `/*.html` | GET | Static HTML files (okf-graph.html, index.html) |

#### Knowledge Graph

- Nodes: wiki pages (entities, concepts, sources)
- Edges: links between pages
- Stored in `.wiki-daemon/graph.json`
- Visualized via `okf-graph.html` (force-directed graph)

---

### 2.3 SPACE — RRP Ideation Engine

**Role:** Prompt engineering tool used by RSIS3 during self-improvement cycles for initial ideation and theory-crafting.

**Location:** `components/space/`
**Size:** 333 files, 8MB, ~69k LOC
**Languages:** TypeScript (9,468), Python (239), JavaScript (61), Markdown (21,640), JSON (26,139), HTML (6,444), CSS (710), Shell (136), YAML (101)
**Status:** Standalone, v2.1.0

#### Structure

```
space/
├── src/                    # TypeScript source
│   ├── cli/               # CLI entry (commander)
│   │   ├── index.ts
│   │   └── commands/
│   ├── engine/            # Core engine
│   ├── llm/providers/     # 7 LLM providers
│   ├── export/formatters/ # 6 export formats
│   ├── template/          # Template engine
│   ├── intelligence/      # AI integration
│   ├── storage/           # File system persistence
│   ├── config/            # Configuration
│   ├── data/              # Framework data
│   ├── i18n/locales/      # Internationalization
│   └── integration/       # External integrations
├── web/                    # Web UI (52KB SPA)
│   ├── index.html         # Full SPA with Tailwind, no build needed
│   └── server.mjs         # Node.js web server with REST API
├── ui/                     # Vite React app (alternative UI)
│   ├── src/
│   └── vite.config.ts     # Port 3000
├── prompt-framework/       # RRP prompt app
│   └── prompt-app/        # React app for running prompt sessions
├── exports/                # Generated specifications
├── meta/                  # Meta documentation
├── tests/                 # Test suite (142 tests)
└── docs/                  # Documentation (ADR, etc.)
```

#### RRP Framework Profile

- **326 questions** across 7 series
- **Series:** Conceptual Depth, Ontology, Semantics, Procedures, Technical Specs, Methodology, Operations
- **Question types:** Open-ended + multiple choice
- **Export formats:** JSON, Markdown, YAML, HTML, System Prompt, PDF
- **LLM providers:** 7 (OpenAI, Anthropic, Google, etc.)

#### API Surface (web/server.mjs on port 8888)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Serve SPA |
| `/api/framework` | GET | Framework metadata + series list |
| `/api/framework/full` | GET | Full framework with all questions |
| `/api/projects` | GET | List projects |
| `/api/projects` | POST | Create project |
| `/api/sessions/:id` | GET | Get session state |
| `/api/sessions/:id/question` | GET | Get current question |
| `/api/sessions/:id/answer` | POST | Submit answer |
| `/api/sessions/:id/skip` | POST | Skip question |
| `/api/sessions/:id/progress` | GET | Get progress |
| `/api/sessions/:id/artifacts` | GET | Get artifacts |
| `/api/sessions/:id/export` | POST | Export session |
| `/api/sessions/:id/save` | POST | Save session to disk |

---

## 3. Dashboard Architecture

### 3.1 COSMOS Dashboard (`index.html`)

**Type:** Single-file HTML application
**Deployment:** GitHub Pages at `gemquota.github.io/cosmos/`
**Size:** ~33KB (self-contained, no external dependencies)

#### Tab Structure

```
COSMOS Dashboard
├── 📊 Overview
│   ├── Quick stats bar (3 components, 2,881 files, ~70MB, 239k LOC, 235 dirs)
│   ├── Project chips (RSIS3, MyKB, SPACE — clickable to switch tabs)
│   ├── Donut charts (Files %, Disk %) — 50% width each, same row
│   └── Bar charts (Code LOC, Total LOC, Disk, Files) — stacked w/ toggle
├── 🔄 RSIS3 (Core)
│   └── App viewport with sub-tabs: Launcher | Dashboard | Telemetry | Rack
├── 📚 MyKB (Memory)
│   └── App viewport with sub-tabs: Launcher | Wiki | Graph | Search
└── 🚀 SPACE (Ideation)
    └── App viewport with sub-tabs: Launcher | Web UI | Prompt | Specs
```

#### Service Controls

- Auto-detects localhost vs GitHub Pages
- Local: shows ONLINE/OFFLINE status per service, iframe embeds for web UIs
- GH Pages: shows "GH Pages" badge, Open button copies CLI command to clipboard
- Port cleanup on startup (kills stale processes)

#### Data Model (hardcoded snapshot)

| Metric | Value |
|--------|-------|
| Components | 3 |
| Total Files | 2,881 |
| Total Disk | ~70MB |
| Total LOC | ~239k |
| Directories | 235 |
| Languages | 3 (Python, TypeScript, JavaScript) |

### 3.2 Hub Dashboard (`hub/index.html`)

**Type:** Single-file HTML application
**Deployment:** GitHub Pages at `gemquota.github.io/hub/`
**Purpose:** Non-COSMOS project overview

#### Project Pages (all return 200)

| Page | Description | Size |
|------|-------------|------|
| `vepa.html` | VEPA2 — Vector Emergent Physics Automata | 17KB |
| `hmxot.html` | HMXOT — Harmonic Overtones Synthesizer | 32KB |
| `golf.html` | GOLF — Scraper framework | 29KB |
| `gog.html` | Gemini on Gemini — introspection sandbox | 4KB |
| `ww.html` | WW Bridge — agentic coding tool | 4KB |
| `ace.html` | ACE — Agentic Context Engineering | 4KB |
| `hz.html` | HZ — Harmonica Control Explorer | 4KB |
| `sim.html` | SIM — Simulation Platform | 4KB |

#### Charts (Hub Overview)

- Code vs Data (stacked horizontal bar, per project)
- File Types (stacked horizontal bar)
- Completion Status (stacked horizontal bar, toggle for separate)
- Entity Density (stacked horizontal bar, toggle for separate)

---

## 4. Deployment Architecture

### 4.1 Production (GitHub Pages)

```
┌──────────────────────────────────────────────────────┐
│                   github.com/gemquota                  │
│                                                       │
│  ┌──────────────┐        ┌──────────────────────┐    │
│  │  cosmos repo │        │   hub repo           │    │
│  │  gh-pages    │        │   main branch        │    │
│  │  branch      │        │                      │    │
│  └──────┬───────┘        └──────────┬───────────┘    │
│         │                           │                 │
│         ▼                           ▼                 │
│  ┌──────────────┐        ┌──────────────────────┐    │
│  │ gemquota.    │        │ gemquota.            │    │
│  │ github.io/   │        │ github.io/hub/       │    │
│  │ cosmos/      │        │                      │    │
│  │              │        │  8 project pages     │    │
│  │  Dashboard   │        │  + index.html         │    │
│  │  index.html  │        │  + charts            │    │
│  └──────────────┘        └──────────────────────┘    │
└──────────────────────────────────────────────────────┘
```

### 4.2 Local Development

```
┌──────────────────────────────────────────────────────┐
│                 localhost:9000                         │
│  python3 -m http.server (cosmos root)                 │
│                                                       │
│  /                         → Dashboard               │
│  /components/rsis3/         → RSIS3 static files      │
│  /components/rsis3/dashboard/ → RSIS3 telemetry UI    │
│  /components/mykb/          → MyKB static fallback    │
│  /components/space/web/     → SPACE web UI            │
│  /components/space/meta-viewer.html → SPEC viewer     │
├──────────────────────────────────────────────────────┤
│                 localhost:8765                         │
│  python3 server.py (MyKB wiki daemon)                 │
│  → Full wiki with markdown rendering, search, API     │
└──────────────────────────────────────────────────────┘
```

### 4.3 URL Map

| URL | Environment | Serves |
|-----|-------------|--------|
| `gemquota.github.io/cosmos/` | Production | COSMOS dashboard |
| `gemquota.github.io/hub/` | Production | Hub project overview |
| `localhost:9000/` | Local | COSMOS dashboard + static components |
| `localhost:8765/` | Local | MyKB wiki daemon |
| `cosmos dashboard` | CLI | Runs start.sh (launches all) |
| `./start.sh` | CLI | Same as above |

---

## 5. Data Flow Diagrams

### 5.1 Self-Improvement Cycle

```
User/LLM
  │
  ▼
┌──────────┐    SPACE (ideation)     ┌──────────────────┐
│  L3      │◄────────────────────────│  Generate spec   │
│  Cross-  │                         │  via RRP prompts │
│  Session │                         └──────────────────┘
│          │
│  Evolve  │    MyKB (memory)        ┌──────────────────┐
│  strategy│◄────────────────────────│  Store session   │
│          │                         │  data, KG,       │
│  Prune   │                         │  temporal snaps  │
│  redundancy                       └──────────────────┘
└────┬─────┘
     │
     ▼
┌──────────┐                         ┌──────────────────┐
│  L2      │    SPACE (ideation)     │  Generate plan   │
│  Per-    │◄────────────────────────│  via RRP prompts │
│  Session │                         └──────────────────┘
│          │
│  Code    │    MyKB (memory)        ┌──────────────────┐
│  gen     │◄────────────────────────│  Reference past   │
│  Prompt  │                         │  knowledge        │
│  tuning  │                         └──────────────────┘
└────┬─────┘
     │
     ▼
┌──────────┐                         ┌──────────────────┐
│  L1      │                         │  Execute tool     │
│  Per-    │────────────────────────►│  calls, observe   │
│  Task    │                         │  retry on failure │
│          │                         └──────────────────┘
│  Tool    │    MyKB (memory)
│  calls   │◄────────────────────────│  Log results      │
└──────────┘                         └──────────────────┘
```

### 5.2 Dashboard Data Sources

```
COSMOS Dashboard
  │
  ├── Static snapshot (index.html inline data)
  │   ├── File counts (from filesystem scan)
  │   ├── LOC totals (from wc -l)
  │   ├── Disk usage (from du -sh)
  │   └── Component descriptions (from READMEs)
  │
  ├── Service detection (local only)
  │   ├── fetch() to localhost:{port}/
  │   └── Shows ONLINE/OFFLINE badges
  │
  └── Iframe embeds (local only)
      ├── http://localhost:9000/components/rsis3/dashboard/
      ├── http://localhost:8765/    (MyKB wiki)
      └── http://localhost:9000/components/space/web/
```

---

## 6. File System Topology

### 6.1 Repository Structure

```
/dev/cosmos/                      # Root (served from port 9000)
├── index.html                    # COSMOS dashboard (~33KB self-contained)
├── dashboard.html                # Alternate/simple dashboard
├── start.sh                      # One-command launcher
├── serve-dashboard.mjs           # Node.js server (alternative)
├── AGENTS.md                     # Agent instructions
├── ARCHITECTURE.md               # Architecture overview
├── ARCHITECTURE-SPEC.md          # This file
├── README.md                     # Quick start
├── COSMOS-SPEC.md                # Original spec (historical)
├── ROADMAP.md                    # Development roadmap
├── cli/cosmos                    # CLI entry (symlinked to PATH)
├── dashboard/                    # Separate Vite/TS dashboard (vestigial)
├── docs/                         # Documentation
├── infra/heartbeat/              # Sentry monitoring
└── components/
    ├── rsis3/    (112 files,   4.1MB)
    ├── mykb/     (2,436 files, 58MB)
    └── space/    (333 files,   8.0MB)

/dev/codex/dashboards/            # Hub repo (deployed to /hub/)
├── index.html                    # Hub dashboard
├── vepa.html, hmxot.html, ...   # Project pages (8 total)
├── mykb.html, rsis3.html, ...   # Cosmos project pages (orphaned here)
├── cosmos-control.html           # Old RSIS3 control (orphaned)
└── projects/                     # Additional project pages
```

### 6.2 File Type Distribution (COSMOS total)

```
Markdown:    119,430 lines  (50.0%)
JSON:        111,367 lines  (46.6%)
Python:       7,474 lines   (3.1%)
HTML:        18,358 lines   (7.7%)
TypeScript:   9,468 lines   (4.0%)
CSS:            804 lines   (0.3%)
Shell:          234 lines   (0.1%)
JavaScript:  20,084 lines   (8.4%)
YAML:           101 lines   (0.04%)
```

Note: totals exceed 100% because LOC counts overlap across file types.

---

## 7. Visualization Requirements

For generating architectural diagrams, the following views would be useful:

### 7.1 Context Diagram
- COSMOS as a system boundary
- External entities: User, LLM, GitHub Pages, File System
- Relationships: serves, stores, processes

### 7.2 Container Diagram
- The 3 components (RSIS3, MyKB, SPACE) as containers
- Dashboard as a container
- Hub as a separate container
- Relationships with data flows

### 7.3 Component Diagrams (per container)
- RSIS3: L1/L2/L3 loops with subsystems
- MyKB: wiki structure, daemon, search engine
- SPACE: CLI, web server, prompt framework

### 7.4 Deployment Diagram
- GitHub Pages for dashboards
- Local Python servers for services
- File system for persistence

### 7.5 Data Flow Diagram
- Self-improvement cycle through all 3 components
- Dashboard data sourcing

### 7.6 Dashboard Layout Diagram
- Tab structure
- Chart layout (donuts, stacked bars)
- Service control panel

---

## 8. Key Metrics for Diagrams

| Entity | Count |
|--------|-------|
| Total files | 2,881 |
| Total LOC | ~239,000 |
| Total disk | ~70MB |
| Directories | 235 |
| Git repos | 2 (cosmos + hub) |
| GH Pages deployments | 2 |
| Dashboard sub-tabs | 12 (4 per component) |
| Bar charts | 4 (stacked with toggle) |
| Donut charts | 2 |

---

## 9. Known Technical Debt

| Issue | Impact |
|-------|--------|
| SPACE `dist/` not built | web/server.mjs won't run; falls back to static serving |
| MyKB `server.py` shares default port 8765 with RSIS3 rack server | Port conflict if both run |
| Dashboard data is hardcoded snapshot | Not live-updating |
| Hub has orphaned pages (myrsikb.html, cosmos-control.html) | Confusion, stale content |
| No test coverage on dashboard HTML | Visual regressions possible |
| ARCHITECTURE.md and AGENTS.md previously stale | Now updated |
| cosmos-ts repo still deployed | User said abandoned |

---

## 10. CLI Reference

```
cosmos dashboard   → Launches ./start.sh (all services + dashboard)
cosmos status      → Shows component status
cosmos start       → Starts component servers
cosmos stop        → Stops component servers
cosmos list        → Lists components with file counts
cosmos logs        → Tails sentry log
cosmos build       → Builds TypeScript components
cosmos test        → Runs component tests
```
