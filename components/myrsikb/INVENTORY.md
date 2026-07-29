# RSIS3 + mykb + myrsikb — Complete Code Inventory

**183 files** across **3 projects**, each analyzed for purpose,
dependencies, dependents, classes, and architectural role.

---

# rsis3

**120 files** — `/data/data/com.termux/files/home/dev/codex/rsis3`

A Python 3.13+ Recursive Self-Improving System with a FastAPI dashboard, SQLite persistence, and 9 cognitive layers. The system manages its own identity, generates goals from telemetry, runs structured reasoning protocols, writes pulse cycles, generates code via AST-targeted patches, and monitors its own health. Every subsystem has been modified to mirror state to mykb through the memory_bridge.

---

## 📁 `root`/

Project root. Entry points, configuration, and documentation that govern the entire system.

### `AGENTS.md`

*4.6KB*

Constitution and operating manual for AI agents in RSIS3. Defines the architectural overview, all 9 core components, the Constitution v2.0.0 invariants, and quick-start instructions. Governs every agentic interaction with the codebase. Key rules: test absolutism, zero deletion, identity snapshots before mutation, telemetry before and after every change.

No code imports — this is a document consumed by human and AI readers. The invariants here are enforced across `src/identity/crisis_monitor.py`, `src/recovery/manager.py`, and `src/codegen/engine.py`.

### `pyproject.toml`

*1.5KB*

Python project configuration. Declares the project name `rsis3`, version 0.1.0, Python >=3.13, and six dependencies (fastapi, uvicorn, jinja2, rich, httpx, pydantic). Defines 8 CLI entry points — one per sub-package — and configures pytest with coverage targeting `src/`. Every source module depends on the packages declared here.

### `start.sh`

*1.1KB*

Shell orchestrator that starts the RSIS3 dashboard. Adds the `myrsikb` directory to PYTHONPATH for memory bridge integration. Detects available ports using bash TCP redirection (Android-safe). Initializes the SQLite database if missing. Launches uvicorn serving `src.dashboard.api:app` and verifies startup with a health check against `/api/info`. This is the primary runtime entry point.

Calls `src.db.schema.SchemaManager` for DB init and launches `src.dashboard.api:app` as a uvicorn process. Updated to include `myrsikb/` in PYTHONPATH.

---

## 📁 `scripts/`

Utility scripts for project maintenance, code concatenation, and tooltip injection.

### `scripts/concat_project.py`

*15KB*

Project concatenation utility. Scans the repository, classifies files as "code" or "content" by extension, and generates two markdown files (`rsis3-code.md` and `rsis3-content.md`) containing all source code or documentation respectively. Uses `os.walk` with exclusion lists for `__pycache__`, `.git`, `rack/`, and patterns like `*.db`, `*.pyc`. Outputs a directory tree and grouped-by-directory file listings with syntax-highlighted code blocks.

Reads every source file in the project. Writes markdown outputs to the project root. No internal project imports.

### `scripts/add_tooltips.py`

*18KB*

Comprehensive tooltip injection script for the dashboard. Defines building blocks to generate HTML tooltip content with proper quote escaping for inline onclick handlers. Patches each tab JS file to add help-icon tooltips with rich content (tables, lists, sections) on every accordion header, chart, and component.

Dependencies: reads/writes all `src/dashboard/static/js/tabs/*.js` files. Called manually during dashboard enhancement.

### `scripts/patch_tooltips.py`

*2KB*

Supporting module for `add_tooltips.py`. Defines helper functions for constructing tooltip HTML content with proper single-quote escaping for JavaScript string safety. Not executable by itself; imported by the add_tooltips workflow.

---

## 📁 `src/`

Root of the RSIS3 Python source tree. Contains 15 sub-packages organized by cognitive domain: `codegen/`, `dashboard/`, `db/`, `discover/`, `evaluator/`, `identity/`, `knowledge_graph/`, `l3_self_direction/`, `pulse/`, `rebirth/`, `recovery/`, `rrp/`, `shared/`, `state_machine/`, `tools/`. The `tools/` directory serves as a backward-compat consolidation layer with stubs that re-export from proper domain packages.

### `src/codegen/`

AST-targeted code generation. Finds stub coordinates in Python source files, renders Jinja2 templates against them, validates surgical patches, and records every successful mutation in mykb.

#### `src/codegen/engine.py`

*5KB*

`CodegenEngine` — template rendering engine for AST-targeted code generation. Uses Jinja2 with a template directory containing `fix_stub.j2`. `generate_patch()` replaces stub body lines with implementation, validates surgical precision (same line count), and renders through the template. `record_success()` mirrors every successful mutation to mykb via MemoryClient for searchable history.

Imports from `src.codegen.ast_parser` (StubCoordinate, find_stubs, validate_patch_is_surgical). Optionally imports `memory_bridge.MemoryClient` for recording mutations. Called by `src.tools.pulse_engine` during cycle execution.

#### `src/codegen/ast_parser.py`

*8KB*

AST coordinate parser that locates stub positions in Python source. `StubCoordinate` dataclass holds name, stub_type, start/end line, and indent. `find_stubs()` walks AST for FunctionDef/AsyncFunctionDef nodes with stub bodies. `validate_patch_is_surgical()` ensures replacement has the same line count as the original. Stub types: empty_body, pass, ellipsis, raise_not_implemented, empty_return, unknown_stub.

Depends only on Python stdlib `ast`. Imported by `src.codegen.cli`, `src.codegen.engine`, `src/tools/debug_test.py`. Core dependency for the entire codegen system.

#### `src/codegen/cli.py`

*3.5KB*

Command-line interface for codegen. Three subcommands: `scan` (find stubs in a file/directory), `generate` (render Jinja2 template against a stub), `validate` (check patch is surgical). Registers entry point `rsis3-codegen` in pyproject.toml.

Imports from `src.codegen.ast_parser` and `src.codegen.engine`.

#### `src/codegen/templates/fix_stub.j2`

*<1KB*

Jinja2 template for surgical stub replacement. Single line: `{{ implementation }}`. This minimal template ensures the engine outputs only the replacement code without wrapper lines, preserving the surgical line-count constraint.

### `src/dashboard/`

FastAPI dashboard serving the RSIS3 SPA on port 8765. Contains ~45 REST endpoints across 8 OpenAPI tag groups, including 11 `/api/knowledge/*` endpoints for the mykb knowledge explorer. Static frontend uses vanilla JS with 10 tab views.

#### `src/dashboard/api.py`

*22KB*

The main FastAPI application with CORS middleware, startup event (SchemaManager init), and all REST endpoints. Key endpoint groups: System (`/api/info`), Cycles (CRUD + search), Telemetry (event query + metrics), Identity (self-model, snapshots, crisis, value axioms), RRP (sessions, fork/merge/compare), Scheduler (start/stop/config), Errors (list/resolve), Database (tables/rows), and Knowledge (11 endpoints — search, similar, graph neighbors, centrality, communities, trends, activity, gaps, gap-goals, memory health, weekly).

Imports broadly: all identity modules, RRP persistence and protocol, knowledge graph, pulse scheduler, DB schema. The `get_kb()` function provides lazy singleton access to `MemoryClient` from `memory_bridge`. Serves static files from `src/dashboard/static/`.

#### `src/dashboard/build_ghpages.py`

*3KB*

GitHub Pages static snapshot generator. Renders current dashboard state (cycle count, telemetry, snapshots, RRP sessions) as a standalone HTML page with embedded CSS. Copies static assets. Run as `python3 -m src.dashboard.build_ghpages`.

### `src/dashboard/static/`

Frontend assets. HTML shell, CSS stylesheet, and 16 JavaScript files organized into `js/components/` (7 reusable widgets) and `js/tabs/` (10 tab modules). Served by FastAPI.

#### `src/dashboard/static/index.html`

*2KB*

SPA shell HTML. Loads Chart.js from CDN, then all JS modules in dependency order: tooltips → api.js → components → tabs → app.js. The `<body>` has `id="app"` — the app.js controller injects the entire dashboard UI into this element. Updated to include the new `knowledge.js` tab module.

#### `src/dashboard/static/css/style.css`

*15KB*

Single comprehensive stylesheet (~545 lines) with CSS custom properties for dark/light theming. Defines styles for: header, tabs, sub-tab bar, cards, grids, metric values, status badges, cycle items, empty states, buttons, modal overlays, accordions, phase timelines, charts, skeleton loaders, system graph, settings panel, form elements, tables, pulse groups, snapshot items, axis bars, axiom tags, and full-screen guide overlays.

### `src/dashboard/static/js/`

All dashboard JavaScript. Shared namespace pattern: `window.RSIS3 = window.RSIS3 || {};`.

#### `js/api.js`

*2KB*

Lightweight fetch wrapper. Exposes `RSIS3.api` with `get()`, `post()`, `setBase()`, `getBase()`, `onStatusChange()`, `getStatus()`. Implements unified error handling, connection state machine (disconnected → connecting → connected/error), and localStorage persistence for API URL. Used by every tab module.

#### `js/app.js`

*8KB*

Dashboard controller. Builds the entire UI via innerHTML injection. Manages tab switching, auto-connect, polling (8s per tab, 15s for header), keyboard shortcuts (1-9 tabs, r refresh, n new cycle, s snapshot, k knowledge, ? help), theme toggle with localStorage, and settings panel. Updated to include the `knowledge` tab in the TABS array and register `k` keyboard shortcut.

#### `js/components/accordion.js`

*1KB*

Accordion UI. Click-to-toggle with CSS height transitions and aria-expanded accessibility.

#### `js/components/modal.js`

*4KB*

Modal, tooltip popup, banner notification, and full-screen guide overlay system.

#### `js/components/navigator.js`

*3KB*

RSIS letter-based navigation. 4 groups (R/S/I/S) mapping to the 10 tabs.

#### `js/components/system-graph.js`

*8KB*

Canvas-based force-directed component dependency graph. 16 components with 24 directed edges, color-coded by group. Implements force layout with velocity Verlet, pan/zoom, node selection, and glow effects.

#### `js/tabs/knowledge.js`

*13KB*

Knowledge tab — the mykb knowledge explorer. Search, entity similarity, graph neighborhoods, centrality, communities, rising/falling trends, monthly activity, knowledge gaps (low-coverage, undefined acronyms, missing tags), gap-driven goals, and memory health. Makes 11 different API calls. Registers `NS.tabs.knowledge` with 10 methods.

#### `js/tabs/overview.js` (17KB), `cycles.js` (8KB), `telemetry.js` (9KB), `rrp.js` (7KB), `identity.js` (15KB), `scheduler.js` (7KB), `errors.js` (7KB), `db.js` (7KB), `explore.js` (3KB)

Tab-specific renderers. Each loads data from the API, renders accordion-based layouts with charts (Chart.js), tables, status badges, and action buttons. The `knowledge.js` tab is the newest addition, providing the mykb integration frontend.

### `src/db/`

SQLite persistence layer. Thread-safe connection manager with singleton pattern and versioned forward-only migrations.

#### `src/db/connection.py`

*2KB*

`DatabaseConnection` — thread-safe SQLite connection manager. Singleton with double-checked locking, thread-local connections, WAL mode, foreign keys, and `sqlite3.Row` factory. Imported by every module that touches the database.

#### `src/db/schema.py`

*5KB*

Schema definitions and versioned migration system. `SchemaManager` manages the `schema_version` table and applies forward-only migrations. Migration v1 creates all 10 core tables with 11 indexes: rrp_sessions, cycles, identity_snapshots, telemetry_events, tasks, knowledge_graph_nodes, knowledge_graph_edges, goals, signals. Uses SHA-256 checksums for migration integrity verification.

### `src/identity/`

Identity Core — the system's sense of self. SelfModel tracks layer scores across 9 cognitive layers, purpose, narrative, aspirations, and core beliefs. CrisisMonitor detects threshold breaches. SnapshotManager persists identity state over time. ValueReinforcementTracker records axiom reinforcement. All modules now mirror state to mykb.

#### `src/identity/self_model.py`

*6KB*

`SelfModel` — Enhanced identity state with self-conception fields. Manages layer scores (L1-L6 as `LayerScore` objects), value axioms, self-concept (purpose, self-description, aspirations, core beliefs, current narrative), version tracking, snapshot count, attempts/successes, and KG node counts. Persists to `rack/shared/self_model.json` and mirrors every write to mykb as an identity snapshot.

Imports `MemoryClient` from `memory_bridge` for the mirror. The `_mirror_to_mykb()` method is called at the end of `_save()` — non-blocking, catches all exceptions. Imported by `CrisisMonitor`, `SnapshotManager`, and dashboard identity endpoints.

#### `src/identity/snapshot.py`

*5KB*

`SnapshotManager` — creates timestamped identity snapshots. Each `IdentitySnapshot` records layer scores, value axioms, self-concept, total attempts/successes, KG node counts, and narrative. Stored as JSON in `rack/L6/snapshot-{id:04d}.json` and mirrored to mykb via `kb.store_identity_snapshot()`.

Imports `DatabaseConnection` for state capture, `SelfModel` for data, `MemoryClient` for mykb mirroring. Used by dashboard `/api/snapshots/take` and the pulse engine.

#### `src/identity/crisis_monitor.py`

*5KB*

`CrisisMonitor` — automated health check and identity crisis detection. Monitors 6 layer scores (L1-L6) against configurable thresholds, success rate decline, and consecutive failures. `check_health(self_model)` produces per-layer health report. Automatically triggers crisis state when thresholds breach and logs to mykb via `kb.wiki.write_decision()`. `resolve_crisis()` clears crisis and records resolution, also logged to mykb.

Imports `MemoryClient` for crisis logging. Thresholds in `CRISIS_THRESHOLDS` dict. Consumed by dashboard and pulse engine.

#### `src/identity/value_reinforcement.py`

*3KB*

`ValueReinforcementTracker` — tracks 9 core value axioms (robustness, coherence, efficiency, maintainability, autonomy, identity, learning, stability, growth). Each `AxiomState` tracks reinforced_count, last_reinforced, and total_applications. `reinforce()` increments and persists through `self_model.json`. `get_weight()` returns 1.0 + 0.1 per reinforcement.

No external imports. Used by dashboard identity endpoints and L3 goal generator for priority calculations.

#### `src/identity/cli.py`

*3KB*

CLI for Identity Core. Subcommands: `snapshot create`, `snapshot list`, `rollback <id>`, `check` (crisis detection), `values` (list axiom weights). Registers entry point `rsis3-identity`.

### `src/knowledge_graph/`

Local SQLite-backed knowledge graph that replaced the external mykb dependency. All data lives in `knowledge_graph_nodes` and `knowledge_graph_edges` tables.

#### `src/knowledge_graph/graph.py`

*9KB*

`LocalKnowledgeGraph` — the full SQLite-backed knowledge graph. Implements node/edge CRUD, search (SQL LIKE), similarity (by type), neighborhood traversal (k-hop JOINs), centrality (edge count), community detection (by node_type), trends (rising/falling), monthly activity, gap analysis (isolated nodes, sparse types), gap-driven goals, and memory health status. All 11 `/api/knowledge/*` dashboard endpoints delegate here.

Imports `DatabaseConnection` from `src.db.connection`. This is the primary KG implementation currently active.

### `src/l3_self_direction/`

Level 3 Self-Direction — the meta-cognitive layer. SignalWatcher polls for filesystem changes. GoalGenerator ranks goals by priority, now including knowledge gaps from mykb. QueueManager orchestrates execution order with priority sorting.

#### `src/l3_self_direction/goal_generator.py`

*5KB*

`GoalGenerator` — produces ranked goals from signals, system state, and mykb knowledge gaps. The constructor auto-registers a gap handler that queries `MemoryClient.gap_driven_goals()` and converts knowledge gaps into Goal objects with priority, value alignment, and suggested tasks. `generate_from_state()` also pulls gap-driven goals directly. `process_signal()` runs custom handlers first, then falls back to default file-change heuristics.

Imports `MemoryClient` from `memory_bridge` for gap detection. The `_register_mykb_gap_handler()` method is called during `__init__()` when `use_mykb_gaps=True` (default). Goals are consumed by `QueueManager`.

#### `src/l3_self_direction/signal_watcher.py`

*4KB*

`SignalWatcher` — polls configured paths at configurable intervals (default 30s), tracking mtime snapshots. Returns `Signal` objects for file_created, file_modified, file_deleted events. Respects .gitignore-like patterns.

#### `src/l3_self_direction/queue_manager.py`

*3KB*

`QueueManager` — priority queue balancer. Maintains sorted Goal list (max 30). Enqueue inserts by priority descending. Dequeue returns highest priority. Failed goals have priority halved and are re-queued.

#### `src/l3_self_direction/evolution.py`

*5KB*

`Evolution` — analyzes cycle history for meta-tuning. Calculates variant performance (pass rate, confidence), detects diminishing returns via first-half vs second-half comparison, and generates recommendations.

### `src/pulse/`

Pulse Engine — the heartbeat of recursive improvement. Scheduler runs periodic cycles. Writer persists pulse data as JSON. Each pulse captures system state, layer scores, evaluation decisions, and patch outcomes. Pulses are now also mirrored to mykb as daily notes.

#### `src/pulse/scheduler.py`

*5KB*

`PulseScheduler` — configurable interval scheduler. `ScheduleConfig` dataclass holds id, name, interval, enabled, auto-apply, run counts. Runs a background thread that checks every 60 seconds for due configs. Supports hook callback for cycle execution.

#### `src/pulse/pulse_writer.py`

*2KB*

`PulseWriter` — writes pulse cycle data to `rack/pulses/pulse-{id:03d}.json`. Serializes complete pulse state: goal, evaluation report, patch, tests, timing, KG data.

### `src/tools/pulse_engine.py`

*16KB*

The 9-phase pulse cycle coordinator — the main orchestration engine. `main()` runs one complete pulse cycle: parse goal, record identity snapshot, run evaluator (4-phase reasoning), apply codegen patch, run tests, record telemetry, update KG, detect signals and generate L3 goals, auto-commit via Recovery Manager. After writing the pulse JSON, it now also mirrors the pulse to mykb via `MemoryClient.store_pulse()`.

Imports broadly across all subsystems. The mykb mirror step is inserted after the `write_and_link(pulse_data)` call at the end of `main()`. Non-blocking — gracefully skips if mykb is unavailable.

### `src/rrp/`

Recursive Refinement Protocol — the core decision-making engine. Deterministic state machine with ambiguity tracking, constraint locking, decision capture, checkpoint/rollback, and multi-session coordination.

#### `src/rrp/state_machine.py`

*19KB*

The largest file in the project. Pure deterministic RRP v2.0 state machine with no IO. Key types: `RRPState` (full session state), `AmbiguityVector` (4D tracking), `Constraint` (key/value with locking), `DecisionLog`, `Checkpoint`, `TokenBudget`, `UserSatisfaction`, `QuestionQuality`, `TemporalVelocity`, `TopicCoverage`, `TransactionLedger`. All enum mappings for use cases, execution modes, depth levels, expertise levels. Core functions: advance_round, resolve_ambiguity, add/lock constraint, make/modify decision, check_early_termination, checkpoint, fork, merge (4 strategies).

No internal project imports beyond stdlib. Imported by protocol, compact, CLI, multisession modules.

#### `src/rrp/protocol.py`

*25KB*

High-level RRP protocol operations. `RRPEngine` provides `init_session()`, `process_user_input()`, `apply_semantic_ambiguity_json()` (hybrid calibration), `add_decision()`, `check_early_termination()`, `get_state_dict()`. Handles the full v2.1 protocol with token budget tracking, question quality scoring, user satisfaction delta, and topic coverage maps.

#### `src/rrp/persistence.py`

*3KB*

SQLite-backed session persistence. `RRPPersistence` saves/loads RRP sessions to/from `rrp_sessions` table. When a session reaches "completed" or "early_term" status, it mirrors the session to mykb as a wiki session page with extracted decisions, constraints, and ambiguity vectors.

#### `src/rrp/compact.py`

*6KB*

Compact state encoding for LLM context windows. Produces ~60-80 character strings encoding full RRP state with arrow-indicated ambiguity trends and constraint codes.

### `src/recovery/`

Recovery system. HexCheck health audits, git-based rollback on test failure, and pytest test runner. Implements defensive recovery patterns for identity crisis resolution.

### `src/tools/`

Backward-compatible stubs that re-export from proper domain packages. Each file is <1KB and redirects imports. `tools/knowledge_graph.py` wraps `memory_bridge.KnowledgeGraph` with backward-compatible API.

### `src/tools/knowledge_graph.py`

*5KB*

Legacy Knowledge Graph wrapper using `memory_bridge` as backend. Maintains backward-compatible API: `create_node()`, `create_edge()`, `record_improvement()`, `get_node()`, `get_edges_for_node()`, `neighborhood()`, `shortest_path()`, `community_detection()`, `centrality()`. Also maintains a local JSON mirror for backward compatibility.

Imports `KnowledgeGraph` from `memory_bridge.knowledge_graph`. Being phased out in favor of the local SQLite-backed `LocalKnowledgeGraph` in `src/knowledge_graph/graph.py`.

---

# mykb

**51 files** — `/data/data/com.termux/files/home/dev/codex/mykb`

A personal knowledge operating system. Wiki daemon, vector database, TF-IDF embeddings, hybrid search, graph engine, gap detection, backlinks, temporal analysis, QA API, curation, and consolidation. Runs as background daemon processing session buffers into OKF-format wiki pages.

---

## 📁 `root`/

Project root. Server, index builder, export script, startup shell, and the single-page wiki viewer.

### `server.py`

*12.3KB*

Core documentation web server — a self-contained recursive markdown viewer on Python's `http.server`. Serves `.md` files with auto-discovery, syntax highlighting, dark mode, and full-text search. REST API endpoints at `/api/v2/`: search, graph data, graph topology, linter health, temporal file history/time-travel snapshots (via `temporal_engine.py`), search index rebuilding (via `search_fusion.py`), and file listing.

The primary consumer of the `.wiki-daemon` infrastructure. Imports nothing from within the project — calls daemon Python scripts at runtime via subprocess. The `Handler` class extends `SimpleHTTPRequestHandler`. Search is a pure-Python TF-IDF scorer. Graph endpoints use networkx on `graph.json`.

### `index.html`

*80KB*

Complete single-page application for browsing the wiki — all CSS, HTML, and JavaScript in one file. Split-pane layout with collapsible sidebar (file tree by directory or entity type), search bar, markdown renderer, dark/light theme toggle with `history.pushState`, keyboard shortcuts (Ctrl+K search, Ctrl+B sidebar, t theme), mobile hamburger menu and swipe gestures.

No external JS dependencies — every feature is hand-rolled vanilla JS. Depends on `server.py` for all API data.

### `build-export.py`

*8.5KB*

Project bundling tool. Concatenates all mykb files into `mykb-code.md` and `mykb-content.md`. Classifies files as code or content by extension and directory. Standalone utility with no project dependencies.

### `build-index.py`

*1.5KB*

Lightweight index builder. Scans `wiki/*.md` files, parses YAML frontmatter, writes `wiki/index.json` with file paths, types, titles, and tags for sidebar grouping.

### `start.sh`

*1.2KB*

Server startup script. PID management, stale cleanup, launches `python3 server.py` in background via `nohup`, opens browser with platform-specific commands.

### `AGENTS.md`

*2.5KB*

Agent configuration for Codex sessions. Describes the OKF bundle layers, frontmatter requirements, valid note types and statuses, and the LLM Wiki Daemon architecture post-tool-use pipeline.

---

## 📁 `.wiki-daemon/`

The operational heart of mykb. All analysis engines: session extraction, vector embedding, hybrid search, graph engine, gap detection, backlinks, temporal analysis, curation, consolidation, QA API, and domain article writing. This is what the memory_bridge wraps.

### `.wiki-daemon/daemon.js`

*3.5KB*

Main LLM wiki daemon — Node.js background service. Polls buffer directory for `.ndjson` session turn files and `.end` signal files. When a session completes, calls `analyzeSession()` and `generateConcepts()` from `extract.js`, writes concept files via `store.js`. Runs periodic curation cycles (OKF validate + lint, default 30min). Handles stale buffer cleanup (>24h without end signals).

Depends on `extract.js`, `store.js`, `config.json`. Started/stopped by `wiki-d.sh`.

### `.wiki-daemon/extract.js`

*5.5KB*

NLP extraction engine — pure JavaScript. Analyzes conversation turns and extracts: technical terms (multi-word capitalized phrases), acronyms (2-5 uppercase letters), decisions (regex-matched from "decided/chose/opted/selected"), inline code references, URLs, tech tags (200+ term keyword list), tool usage statistics. 250+ entry stop-word list.

Exports `analyzeSession(turns)` and `generateConcepts(analysis, sessionId)`. Heuristic NLP — no ML dependencies. Imported by `daemon.js`, `import-sessions.js`, `import-gemini.js`.

### `.wiki-daemon/store.js`

*2KB*

OKF concept writer. Maps concept types to subdirectories (session → `wiki/sessions/`, entity → `wiki/entities/`, decision → `wiki/decisions/`, tool → `wiki/tools/`, topic → `wiki/topics/`). Generates URL-safe slugs, avoids filename collisions, constructs YAML frontmatter, appends log entries.

Imported by `daemon.js`, `import-sessions.js`, `import-gemini.js`.

### `.wiki-daemon/vectordb.py`

*3KB*

Lightweight numpy-based vector database. `VectorDB` class manages (N, D) numpy array with metadata. Supports add, add_batch, search (cosine similarity), get, update_metadata, remove, count, persist (`.npz` + JSON), load. Zero external dependencies beyond numpy.

Foundational storage for all semantic search. Consumed by `embedder.py` and `retriever.py`.

### `.wiki-daemon/embedder.py`

*3KB*

TF-IDF embedding pipeline. `TfidfVectorizer` class fits vocabulary (default 3000 features) on wiki documents, computes IDF, transforms to L2-normalized vectors via numpy. `embed_all()` scans all wiki `.md` files, fits vectorizer, builds VectorDB, persists both. Designed for nightly cron runs.

Imports `VectorDB` from `vectordb.py`. Results saved to `vdb.npz` and `vdb_tfidf.json`.

### `.wiki-daemon/retriever.py`

*3KB*

Hybrid search engine combining vector similarity + BM25 keyword via RRF fusion. `BM25` class (Okapi BM25 implementation). `HybridRetriever` wraps VectorDB, TfidfVectorizer, and BM25. `hybrid_search()` runs both searches, merges via RRF with configurable weights and metadata filtering. `find_similar()` for semantic similarity.

Imports `VectorDB` from `vectordb.py`, `TfidfVectorizer` from `embedder.py`. Primary search interface consumed by `server.py` and `qa_api.py`.

### `.wiki-daemon/graph_engine.py`

*4KB*

Entity co-occurrence graph engine. Builds weighted networkx Graph from session data. Edge between entities co-occurring in same session (weight ≥ 2). Community detection via `greedy_modularity_communities`. Graph traversal (k-hop neighborhood, shortest path). Centrality analysis (degree centrality). Bridge entity detection between communities.

Depends on `networkx`. Graph persisted as `graph.json`. Community pages written to `wiki/communities/`. Consumed by `qa_api.py` for graph endpoints.

### `.wiki-daemon/qa_api.py`

*6KB*

FastAPI Q&A server on port 8810. Lazy-loads `HybridRetriever` and graph engine. Endpoints: `POST /qa/ask` (question → answer with sources, tries Gemini/OpenAI, falls back to context-only), `GET /qa/search` (hybrid search), `GET /qa/similar/{entity}`, graph navigation endpoints, community listing.

The `generate_answer()` function tries Google GenerativeAI first, then OpenAI, then returns context-only. This is the intelligence layer on top of the vector DB and graph.

### `.wiki-daemon/gap_detector.py`

*5KB*

Knowledge gap analysis. Scans entities and sessions, detects four gap types: low coverage (3+ sessions, <500b body), stubs (auto-extracted minimal content), acronyms without definitions, entities with few/no tags. Generates prioritized open questions and writes gap report to `wiki/ops/gap-report.md`.

Output consumed by `memory_bridge.gap_detector` which converts gaps into RSIS3-compatible goals.

### `.wiki-daemon/backlinks.py`

*2KB*

Reverse-link index builder. For each entity in `wiki/entities/`, finds all other wiki files that mention the entity's title. Output is `backlinks.json` — consumed by the viewer UI for "Linked from" sections and by the graph engine for edge detection.

### `.wiki-daemon/temporal.py`

*3KB*

Temporal analysis engine. Builds entity mention timelines from session data by cross-referencing entity bodies with session timestamps. `detect_trends()` uses first-half/second-half comparison to classify entities as rising (ratio > 1.5), falling (ratio < 0.5), or stable. Output written to `timeline.json`.

### `.wiki-daemon/consolidate.py`

*6KB*

Duplicate concept consolidation. Three-phase pipeline: Phase 1 merges exact duplicates (union tags, append bodies). Phase 2 clusters fuzzy duplicates by combined Jaccard + Levenshtein similarity (threshold 0.55). Phase 3 writes cluster summaries to `wiki/clusters/`. Critical for keeping auto-extracted wiki free of duplicate entities.

### `.wiki-daemon/curate.py`

*8KB*

Rule-based wiki classifier. Assigns each concept to a 10-domain hierarchy with nested supercategories. Writes domain index pages, navigation pages, and unclassified list. Generates profile report with domain distribution, tag analysis, cross-domain connection stats.

### `.wiki-daemon/curate-wiki.py`

*11KB*

Entity enrichment curator. Extends stub entity pages with synthesized content from session data. Uses 900+ entry `KNOWN_TECH` dictionary to generate definitions, usage patterns, and cross-references. Detects stubs, prioritizes by session count, writes enriched content.

---

## 📁 `hooks/`

Codex lifecycle hooks. Post-tool-use and session-stop handlers written in both Node.js and Python. Capture session data in real-time, writing to buffer files for the daemon to process asynchronously. Both implementations complete in under 2 seconds and silently catch all exceptions.

### `hooks/post-tool-use.js` / `post-tool-use.py`

~1.5KB each

Called by Codex after every tool execution. Read session context from stdin JSON, extract session/thread ID, tool name, input content, and response, then append structured turn entry to NDJSON buffer file.

### `hooks/session-stop.js` / `session-stop.py`

~1KB each

Called when a session ends. Write `.end` signal file to buffers/signals/ directory. Daemon polls this directory and triggers processing when end signals appear.

---

# myrsikb

**12 files** — `/data/data/com.termux/files/home/dev/codex/myrsikb`

Integration project containing the `memory_bridge` package and cross-project analysis/export scripts. memory_bridge is what RSIS3 imports to access mykb as its semantic memory, knowledge graph, temporal memory, and gap detector.

---

## 📁 `root`/

Project root. Utility scripts for cross-project analysis, export, and inventory generation.

### `build-export.py`

*4.1KB*

Concatenates all source files in myrsikb into `myrsikb-code.md` (Python, JSON, TOML) and `myrsikb-content.md` (markdown). Classifies by extension, groups by directory. Excludes itself, `__pycache__`, `.git`, `*.pyc`, `*.md` outputs.

Standalone utility with no project dependencies beyond standard library.

### `concat-combined.py`

*8.0KB*

Orchestrates the full cross-project export pipeline. Runs concat scripts for all 3 projects, copies outputs, then merges all 6 individual exports into `combined-code.md`, `combined-content.md`, and `combined-all.md` with hierarchical headers and summary tables.

### `scan-inventory.py`

*15.2KB*

Comprehensive inventory generator for all 3 projects. Walks every code file, extracts docstrings and JSDoc via AST parsing, identifies shebang lines, lists classes and functions, traces imports, maps reverse dependencies. Outputs the relationship-aware `INVENTORY.md`.

---

## 📁 `memory_bridge/`

The core of myrsikb — a standalone Python package that RSIS3 imports to access mykb as its semantic memory, knowledge graph, temporal/episodic memory, and gap-driven goal generator. Each module wraps a corresponding mykb wiki-daemon engine and provides a clean RSIS3-compatible API. Lazy-loads mykb modules by injecting `.wiki-daemon/` into `sys.path`.

### `__init__.py`

*846B*

Package initializer. Exports 6 public classes: `MemoryClient`, `WikiWriter`, `KnowledgeGraph`, `SemanticMemory`, `TemporalMemory`, `GapDetector`. This is what RSIS3's import system resolves on `from memory_bridge import MemoryClient`.

Imports all sub-modules. No external dependencies.

### `client.py`

*8.2KB*

`MemoryClient` — the unified facade that RSIS3 subsystems import. Composes 5 sub-interfaces: `.wiki` (WikiWriter), `.graph` (KnowledgeGraph), `.semantic` (SemanticMemory), `.temporal` (TemporalMemory), `.gaps` (GapDetector). Convenience methods `store_identity_snapshot()`, `store_rrp_session()`, `store_pulse()`, `store_code_change()` that write wiki pages AND update vector index atomically. Search, graph, temporal, and gap methods delegate to sub-interfaces. `status()` returns memory subsystem health.

Imports all 5 sub-modules and `memory_bridge.config.resolve_wiki_path`. This is the single import RSIS3 uses.

### `config.py`

*2.2KB*

Wiki path resolution strategy. `resolve_wiki_path()` checks: (1) `MYKB_WIKI_PATH` env var, (2) `.memory_bridge.json` config file, (3) fallback to `~/dev/codex/mykb/wiki` (canonical location). `resolve_mykb_daemon()` derives `.wiki-daemon/` path from wiki root. `write_config()` persists choice.

Imported by every memory_bridge module that needs to locate mykb.

### `wiki_writer.py`

*14.4KB*

`WikiWriter` — writes RSIS3 cognitive artifacts as mykb wiki pages in OKF format (YAML frontmatter + markdown body). Manages 6 subdirectories: sessions, entities, decisions, tools, topics, daily, identity. Each write method renders structured RSIS3 data: `write_identity_snapshot()` (layer scores + value axioms + narrative), `write_rrp_summary()` (multi-round decisions + constraints + ambiguity), `write_daily_note()` (pulse data), `write_codegen_event()` (AST mutations), `write_entity()` (named concepts), `write_concept_link()` ([[wiki-link]] backlinks), `write_goal()`.

No RSIS3 or mykb imports — only writes markdown files to disk. Every memory_bridge subsystem that needs persistence calls this.

### `knowledge_graph.py`

*7.9KB*

`KnowledgeGraph` — replaces RSIS3's original flat-JSON KG with mykb's networkx co-occurrence graph. Wraps mykb's `graph_engine.py` via lazy sys.path injection. Backward-compatible API: `create_node()`, `create_edge()`, `record_improvement()`, `get_node()`, `get_nodes_by_type()`. Enhanced queries: `neighborhood()` (k-hop), `shortest_path()`, `central_entities()` (degree centrality), `communities()` (modularity). Node creation also writes wiki entity pages; edge creation writes concept links.

Imports `WikiWriter` from within memory_bridge, mykb's `graph_engine` lazily. The `_ensure_graph()` method loads mykb's `graph.json` into a networkx Graph.

### `vector_search.py`

*6.2KB*

`SemanticMemory` — wraps mykb's hybrid retriever (TF-IDF + BM25 + RRF fusion), embedder, and VectorDB. `search()` returns `{id, score, title, type, snippet}`. `find_similar()` finds semantically similar entities by vector cosine similarity. `store()` writes a wiki page AND embeds into vector DB incrementally. `ensure_indexed()` rebuilds full index if missing. `count()` returns indexed vector count.

Every `store_*()` call in `MemoryClient` pushes content here. Wraps mykb's `retriever`, `embedder`, and `vectordb` modules lazily.

### `temporal_memory.py`

*4.6KB*

`TemporalMemory` — timeline queries and trend detection over mykb's session history. Wraps mykb's `temporal.py`. `entity_timeline()` returns dated mentions for an entity. `monthly_activity()` lists active entities per month. `rising_entities()` / `falling_entities()` detect attention trends. `trend_summary()` returns full rising/falling/stable report. `recent_sessions()` lists activity from last N days.

Provides RSIS3's L3 self-direction with awareness of what topics are active or fading.

### `gap_detector.py`

*5.5KB*

`GapDetector` — analyzes mykb for knowledge gaps and converts them into RSIS3-compatible goals. Wraps mykb's `gap_detector.py`. Four gap types: low_coverage (many sessions, tiny body), stubs (minimal content), acronyms (uppercase without definitions), missing_tags. `to_goals()` converts gaps into `{id, description, priority, source_signal, value_alignment, suggested_tasks}` dicts — directly consumable by RSIS3's L3 GoalGenerator.

Imported by `MemoryClient.gap_driven_goals()`. This is the bridge between mykb's gap analysis and RSIS3's goal generation.

