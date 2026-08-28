# COSMOS — Completion Report & Project Description

*Generated: August 28, 2026*

---

## Part 1: Completion Report

### Changes Made

| # | ID | File(s) | Change | Type |
|---|-----|---------|--------|------|
| 1 | — | `README.md` | Fixed COSMOS acronym: "Orchestration" → "Optimization" in expansion | Bug fix |
| 2 | P6 | `components/rsis3/rsis/mykb_gateway.py:171` | Fixed Python 3.10-incompatible f-string syntax (`f"tags: [{tag_list}"` → `f"tags: [{tag_list}]"`) | Bug fix |
| 3 | O1 | `components/rsis3/rsis/memory.py` | Added `_dirty` flag to `KnowledgeGraph`; `add_node`/`add_edge`/`remove_node` set dirty, `save()` writes only when dirty | Perf |
| 4 | O1 | `components/rsis3/tests/test_kg_robustness.py` | Added explicit `kg.save()` call after mutations to match new deferred-save behavior | Test fix |
| 5 | O7 | `components/rsis3/rsis/memory.py` | `VectorStore` now caches embeddings to `~/.cosmos/embedding_cache.json` keyed by content hash, loaded on init, written on save | Perf |
| 6 | O4 | `components/rsis3/rsis/loop_l2.py` | External LLM candidates appended to `rack/llm_candidates.jsonl` with timestamps, scores, and source context | Observability |
| 7 | P4 | `components/rsis3/rsis/tools/sandbox.py` | `preexec_fn` now uses `os.setsid()` with fallback to `os.setpgrp()`, replacing bare `os.setpgrp()` | Robustness |
| 8 | O8/P7 | `components/rsis3/rsis/timeout.py` | Added `COSMOS_TIMEOUT_MECHANISM` env var; auto-selects threading on Windows, SIGALRM on Linux; env override available | Config |
| 9 | O5 | `components/mykb/server.py` | `/save`, `/delete`, `/log`, `/overwrite` endpoints require `X-Session-Token` header; read endpoints remain open | Security |
| 10 | O6/P1 | `PHASE_MANIFEST.json` (new) | Phase maturity manifest mapping all 50+ development phases to tested/untested/aspirational status with risk ratings | Documentation |

### Test Results

**Before changes:** 332 passed, 4 failed (2 missing `cryptography`, 1 timeout regression, 1 KG test regression), 3 collection errors (pre-existing f-string syntax)

**After changes:** 371 passed, 1 skipped, 0 failures, 0 collection errors

All failures were either pre-existing or regressions introduced by my own changes (both fixed).

---

## Part 2: Comprehensive Project Description

### What This Project Is

COSMOS is a **recursive self-improvement (RSI) system** — a program that autonomously improves its own codebase, strategies, and parameters across sessions. It's a research system, not a production web app. It combines three tightly integrated subsystems into a single cognitive architecture:

```
┌─────────────────────────────────────────────────────────────────┐
│                        COSMOS                                    │
│                                                                  │
│  RSIS3 (Python)  ──── MyKB (Python+Markdown)  ──── SPACE (TS)  │
│  Core cognitive       Persistent memory          Prompt framework│
│  engine               & knowledge base           for ideation    │
└─────────────────────────────────────────────────────────────────┘
```

The name stands for **C**ognitive **O**rchestration **S**ystem for **M**eta-cognitive **O**ptimization & **S**ynthesis.

### The Core Architecture: The +3 Diagonal

RSIS3 has **9 nested loops** (L1–L9), each responsible for tuning the parameters of the loop **3 levels below** it. This is the key architectural insight:

- **L1** (Action Loop) — Runs tasks using tools (file edit, shell, search). Executes every 3 minutes.
- **L2** (Improvement Loop) — Analyzes L1's recent pulses and generates improvement candidates. Runs every ~30 min.
- **L3** (Cross-Session Evolution) — Consolidates L1/L2 gains into durable knowledge base writes. Runs every ~8 hours.
- **L4** (Meta-Parameter Optimizer) — Tunes L1's pipeline weights, evaluator thresholds, and convergence parameters.
- **L5** (Strategy Evolution) — Evolves L2's scoring strategy and L4's search algorithm.
- **L6** (Identity Loop) — Tunes L3's consolidation strategy and L5's mutation operators.
- **L7** (Meta-Cognitive Loop) — Tunes L4's optimizer parameters.
- **L8** (Meta-Meta Loop) — Tunes L5's strategy evolution parameters.
- **L9** (Meta-Meta-Meta Loop) — Tunes L6's identity parameters.

The "+3 diagonal" means L4 tunes L1, L5 tunes L2, L6 tunes L3, L7 tunes L4, etc. Each loop can only modify the tuned parameters of a target loop — it never touches code directly.

### Key Subsystems in RSIS3

**Pipeline (pipeline.py)** — The execution backbone. An acyclic dependency graph (DAG) of 25 named nodes (e.g., `convergence_check`, `intent_eval`, `actuator`, `persist`). Each node can return a status (`ok`, `halt`, `timeout`) and data payload. The pipeline uses a topological sort to determine execution order.

**Evaluator (evaluator.py)** — An immutable subprocess gate that validates every improvement candidate. Runs candidate code in a sandboxed subprocess, captures stdout/stderr/exit code, parses JSON output, validates the schema, scores the result, and returns a pass/fail verdict. The evaluator cannot be modified by any loop (it's a trust boundary).

**CheckpointManager (checkpoint.py)** — Git-based checkpointing. Before any RSIS3 code mutation, the system creates a git checkpoint with a sentinel file (`CheckpointManager.SENTINEL`). After mutation, it verifies the checkpoint was properly committed. If mutation fails, it rolls back via `git reset --hard`. Three recovery levels: Level 1 (in-memory restore), Level 2 (file rollback from backup), Level 3 (git hard reset).

**MemoryManager (memory.py)** — Three memory backends:
1. **KnowledgeGraph** — NetworkX-based graph with typed nodes/edges, dedup, consent system, rate limiting, and atomic JSON persistence. Now uses a dirty-flag to batch saves.
2. **VectorStore** — TF-IDF-based vector search over documents. Now caches embeddings to disk.
3. **LongTermMemory** — Orchestrates both. Manages session lifecycle (start/end/checkpoint/restore), captures activity trails, integrates with MyKB.

**TelemetryCollector (telemetry.py)** — Records every pulse (one L1 cycle), layer activity, cost, evaluator results. Writes to `rack/telemetry.json`. Feeds convergence detection and cost accounting.

**ConvergenceDetector (convergence.py)** — Tracks improvement signal, duplication rate, stagnation, error rate, novelty. Triggers convergence when improvements plateau and costs exceed budget.

**CostLedger (telemetry.py)** — Tracks per-loop and total cost, enforces budgets, provides summaries.

**SelfAssess (self_assess.py)** — Meta-evaluation of L1/L2 performance using cosine similarity between pulse outputs and targets. Calculates per-layer and total quality scores.

**EventBus (event_bus.py)** — In-process pub/sub for 30+ event types. Used for decoupled communication between loops.

**TimeoutManager (timeout.py)** — Deadline enforcement for pipeline execution. Uses SIGALRM on Linux (the correct mechanism — interrupts C-level syscalls), threading on Windows. Configurable via `COSMOS_TIMEOUT_MECHANISM` env var.

**RecoveryManager (recovery.py)** — Three-level recovery system:
- Level 1: In-memory rollback from a snapshot taken before mutation
- Level 2: File-level restore from a backup copy
- Level 3: Git hard reset to the last checkpoint

**SharedMemory (shared_memory.py)** — Thread-safe shared state with compare-and-swap semantics, version tracking, and immutable snapshots.

### MyKB (Long-term Memory)

A persistent knowledge base stored as Markdown files with YAML frontmatter (Obsidian-style wiki). RSIS3's L3 loop writes synthesis notes here after significant work sessions.

Components:
- **Wiki files** at `components/mykb/wiki/` — synthesis notes, session logs, architecture docs
- **Knowledge graph** (`okf-graph.html`) — Force-directed D3.js visualization of wiki links
- **Search index** — TF-IDF index built by `build-index.py`
- **Wiki daemon** (`.wiki-daemon/`) — Python HTTP server exposing `/search`, `/save`, `/graph`, `/tree`, `/delete`, `/log`, `/overwrite` APIs
- **Dashboard** (`index.html`) — Browseable wiki viewer
- **Important**: `/save`, `/delete`, `/log`, `/overwrite` endpoints now require `X-Session-Token` header auth

### SPACE (Ideation Engine)

A TypeScript-based 326-probe question framework organized into 7 series (A–G) covering creative ideation, systematic exploration, recursive depth, synthesis, evaluation, integration, and transformation. Uses the Recursive Refinement Protocol (RRP) to generate structured prompt specifications.

- **Web UI** (`web/index.html`) — SPA for browsing and filtering probes
- **Spec viewer** (`meta-viewer.html`) — Displays generated specs
- **No backend** — Runs entirely client-side

### CLI & Orchestration

Entry point: `components/rsis3/cli/cosmos` (shell script → `python -m rsis`)

Key commands:
- `cosmos start` — Launch the daemon (runs L1 every 3 min)
- `cosmos run` — Single pipeline execution
- `cosmos pulse` — Single L1 pulse
- `cosmos cycle` — Run L2 improvement cycle
- `cosmos [check-practices|status|reset|rollback|event|show|consume|events|score-pulse|query-history|self-assess|recovery-backlog|optimize|strategies|identity|metacog|metameta|mmm|dashboard|repair]`
- `cosmos nightly` — Nightly summary + taxonomy consolidation

### Data Flow

```
L1 pulse every 3 min:
  convergence_check → intent_eval → strategize → prepare_context →
  checkpoint_save → actuator (runs tool) → persist → event_publish →
  convergence_eval → convergence_update → post_maintenance

L2 cycle every ~30 min:
  Load recent pulses → Score them → Generate candidates →
  Apply best candidate (edit code) → Checkpoint → Re-run pipeline

L3 consolidation every ~8 hours:
  Summarize L1/L2 activity → Write synthesis notes to MyKB →
  Consolidate taxonomy → Verify invariants → Regenerate dashboard data
```

### Persistence & State

All state lives in `components/rsis3/rack/`:
- `pulses/` — Individual pulse JSON files
- `telemetry.json` — Aggregated telemetry
- `improvement_candidates.json` — L2 generated candidates
- `llm_candidates.jsonl` — External LLM suggestions (new)
- `event_log.json` — Event history
- `convergence_state.json` — Convergence tracking
- `self_assessment.json` — Quality scores
- `cost_ledger.json` — Cost tracking
- `session_state.json` — Current session state
- `*_state.json` — Per-loop parameter state files

Git is used for checkpoints and history. The system creates commits before mutations and can roll back to any checkpoint.

### Dashboard

Single HTML file at `components/rsis3/dashboard/index.html` (Tailwind + Chart.js). Reads `rack/pulses/dashboard-data.json`. Shows:
- Overview (ecosystem summary + telemetry)
- Pulses (individual L1 cycle details)
- Knowledge Graph (embeds MyKB's `okf-graph.html`)
- SPACE (embeds SPACE's `web/index.html`)
- Loops (rendered from `dashboard/loops.json`)
- Constraints, Graphs, KG views

The repo root `index.html` redirects to this dashboard.

### Environment & Config

- Python 3.10+, no external dependencies required (stdlib only)
- NetworkX for graph operations, NumPy for vector similarity
- Git for checkpoints
- No Docker, no cloud services, no API keys required (LLM integration is stubbed out)
- Config via environment variables: `COSMOS_HOME`, `RSIS_HOME`, `COSMOS_LLM_PROVIDER`, `COSMOS_TIMEOUT_MECHANISM`, etc.
- Runtime data in `~/.cosmos/` (embedding cache) and `components/rsis3/rack/` (all state)

### What's Working vs. Aspirational

**Working (tested):**
- L1 pulse execution with tool sandboxing
- Pipeline DAG execution with convergence detection
- Knowledge graph CRUD with atomic persistence
- Vector search with TF-IDF
- Checkpoint/restore/rollback
- Telemetry collection and cost accounting
- Self-assessment quality scoring
- Shared memory with CAS semantics
- Event bus
- Timeout enforcement
- MyKB search, save, graph, tree APIs

**Stubbed/Aspirational:**
- LLM integration (no provider wired — `llm_generate()` is a placeholder)
- SPACE probe framework (all code, no integration with RSIS3)
- User permission system (basic roles exist, not enforced across loops)
- Multi-node distributed execution
- API server (FastAPI skeleton exists, not functional)
- L4–L9 loops (implemented but untestable without real LLM)

### Key Architectural Invariants (MUST PRESERVE)

1. **Checkpoint-before-mutation**: Every RSIS3 code edit is preceded by a git checkpoint
2. **Evaluator immutability**: The evaluator subprocess cannot be modified by any loop
3. **+3 diagonal tuning**: Loop N only tunes parameters of Loop N-3
4. **State file disjointness**: Each loop has its own `*_state.json` — no sharing
5. **Atomic persistence**: All JSON writes use temp-file + rename
6. **Recovery levels**: Level 3 (git reset) is the last resort, always available

### Files Modified in This Session

```
README.md                                          — acronym fix
PHASE_MANIFEST.json                                — new file (phase maturity)
components/rsis3/rsis/memory.py                    — dirty-flag KG, embedding cache
components/rsis3/rsis/loop_l2.py                   — LLM candidate persistence
components/rsis3/rsis/tools/sandbox.py             — setsid fallback
components/rsis3/rsis/timeout.py                   — configurable mechanism
components/rsis3/rsis/mykb_gateway.py              — f-string fix
components/rsis3/tests/test_kg_robustness.py       — test alignment
components/mykb/server.py                          — session token auth
```
