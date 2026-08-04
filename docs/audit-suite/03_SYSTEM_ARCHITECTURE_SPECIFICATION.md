# 03 — System Architecture Specification

**Doc ID:** COSMOS-AUDIT-03 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [02 Architecture Analysis](02_ARCHITECTURE_ANALYSIS.md) · [33 Engineering Specification](33_ENGINEERING_SPECIFICATION.md)

> This document is the *as-built* architecture specification (reverse-engineered). It is written in the
> same register as the existing `docs/ARCHITECTURE-SPEC.md` but reflects the observed 2026-08-04 state.

---

## 1. System Identity

- **Name:** COSMOS — Cognitive Orchestration System for Meta-cognitive Orchestration & Synthesis
- **Version:** 0.2.0 (root manifest); SPACE 2.1.0; RSIS3 `__version__` in `rsis/__init__.py`; MyKB `VERSION`
- **Purpose:** Provide a persistent, self-improving cognitive loop where an LLM agent executes goals
  (L1), improves its own approach (L2), evolves across sessions (L3), and tunes the parameters of lower
  loops (L4–L9), while memory (MyKB) and ideation (SPACE) feed the cycles.

## 2. Scope

In scope: RSIS3 engine and RRP rack; MyKB wiki + daemons; SPACE CLI/web/storage/LLM; diagrams generators;
root orchestration (`start.sh`, `cli/cosmos`); `infra/heartbeat`; `gen-static-data.py`; `ops/reports`.
Out of scope: external hubs (`gemquota.github.io/hub`), archived `rsisb`.

## 3. Component Specifications (As-Built)

### 3.1 RSIS3 — Core Engine
- **Language:** Python 3; stdlib-first; optional `psutil`, `pytest`.
- **Entry:** `python3 -m rsis <command>` (17 commands incl. init/run/evolve/optimize/strategies/identity/
  metacog/metameta/mmm/dashboard/status/check/recovery-test/check-practices).
- **Key modules:** `loop_l1..l9.py`, `pipeline.py`, `scheduler.py`, `telemetry.py`, `memory.py`,
  `checkpoint.py`, `evaluator.py`, `recovery.py`, `resource_monitor.py`, `priority_pool.py`,
  `extrapolation.py`, `shared_memory.py`, `event_bus.py`, `timeout.py`, `tools/` (manager, sandbox, hitl,
  workspace_tools), `config.py`, `practices.py`.
- **State:** workspace `.rsis/` JSON/JSONL; telemetry under `rack/pulses/`.
- **Interfaces:** CLI; filesystem; optional FastAPI dashboard (`dashboard/app.py`); static HTTP rack server.

### 3.2 MyKB — Long-Term Memory
- **Language:** Python + Markdown (OKF/Obsidian conventions).
- **Entry:** `server.py [port]` (default 8765); daemons in `.wiki-daemon/` (`search_fusion.py serve`,
  `build_graph.py`, `enrich_links.py`, `kb_linter.py`, `link_check.py`, `temporal_engine.py`,
  `build_stats.py`, stub builders).
- **Content:** `wiki/` (5,397 md files), `syntheses/` (51), `log.md`, `files.json`, `graph.json`.
- **Interfaces:** HTTP (static + `/api/v2/history/*`, `/api/v2/search/*`), subprocess invocations of
  daemons, hooks (`hooks/post-tool-use.py`, `hooks/session-stop.py`).

### 3.3 SPACE — RRP Ideation Engine
- **Language:** TypeScript (strict, NodeNext ESM), Node ≥18.
- **Entry:** CLI (`src/cli/index.ts`, bin `space`), web UI (`web/server.mjs`), engine (`src/engine/core.ts`).
- **Framework:** 326 probes / 7 series / 6 export formats; i18n en/es/fr.
- **Storage:** `StorageProvider` interface → `FileSystemStorage` | `SQLiteStorage` (sql.js).
- **LLM:** `LLMProvider` interface → OpenAI/Anthropic/Gemini/Mistral/Ollama/Template/Null.

### 3.4 Diagrams — Visualization Generators
- 26 Python generators (`diagrams/gen/*.py`) producing 95 SVGs in `diagrams/`; `generate.py` orchestrates.
- Purpose: architecture/ontology/telemetry visualization; single-source generation.

### 3.5 Orchestration & Infra
- `start.sh`: static server :9000 (0.0.0.0) + MyKB :8765; pid lifecycle; `fuser -k` port cleanup.
- `cli/cosmos`: bash CLI (status/list/start/stop/logs/build/test/update/dashboard).
- `infra/heartbeat/heartbeat.mjs`: polls watches.json services every 30s, restarts on failure.
- `gen-static-data.py`: regenerates `files.json`, `ecosystem.json`, `loops.json`; `--check` validates.

## 4. Data Flow (Top Level)

```
SPACE (RRP pulse) ──► exports/spec JSON ──► .rsirrp/work ──► RSIS3 L2/L3 ideation inputs
RSIS3 loops ──telemetry──► rack/pulses/*.json ──gen-static-data.py──► dashboard-data.json ──► dashboard
RSIS3 conclusions ──► MyKB syntheses (via hooks/bridge) ──► wiki + graph.json ──► future sessions
```

## 5. State Specification (Schema Inventory)

| State file | Schema (observed fields) | Versioned? |
|---|---|---|
| `.rsis/optimizer_state.json` | `{params: {...}, outcomes?, stats?}` | No |
| `.rsis/strategies.json` | `{population: [{id, fitness, params}]}` | No |
| `.rsis/identity_state.json` | `{params: {...}, signal?}` | No |
| `.rsis/metacog_state.json` / `metameta_state.json` / `mmm_state.json` | `{params: {...}}` | No |
| `.rsis/audit.jsonl` / `hitl.jsonl` | JSONL events | No |
| `rack/pulses/pulse-NNN.json` | goal + outcomes + steps | No |
| `rack/pulses/dashboard-data.json` | pulses/goals/score_history/telemetry_aggregates/summary | No |
| MyKB `graph.json` | nodes/edges | No |
| MyKB `files.json` | array of md paths | No |
| SPACE session files | `SessionMeta` + answers + artifacts (`serializeSession`) | framework_version field |

**Finding:** no schema version field on any RSIS3/MyKB state file; SPACE sessions carry
`framework_version` but "no version compatibility checking" (documented in SPACE exports) [O, High].

## 6. Protocol Specification (As-Built)

| Channel | Protocol | Auth | Notes |
|---|---|---|---|
| Dashboard static | HTTP/1.1 GET | none | `rack/server.py`, 0.0.0.0, no cache headers on most assets |
| MyKB server | HTTP GET (`/`, `/api/v2/history/*`, `/files.json`) | none | triggers subprocess (`server.py:275,292,303`) |
| MyKB search daemon | HTTP GET `/api/v2/search/{hybrid,stats,semantic}` | none | `search_fusion.py` |
| SPACE web | HTTP REST `/api/*` (GET/POST/DELETE) | none | `web/server.mjs`; `{data: T}` / `{error: string}` envelope |
| FastAPI dashboard | `/api/status`, `/api/trends`, `/api/velocity`, `/api/search`, `/health` | none | optional |

## 7. Error Specification (As-Built)

- RSIS3: `TimeoutError` (custom, `timeout.py`), `Budget`/`deadline()` context managers, `ToolResult`
  status enum (OK/TIMEOUT/ERROR), `error_classifier.py` categories, `recovery.py` failure injection +
  `RecoveryManager`.
- SPACE: `FRAMEWORK_INVALID` error; `{error: string}` HTTP envelope; validator rejects answers.
- MyKB: exception-tolerant loops (`try/except: pass` in `get_system_stats`), silent fallbacks.

## 8. Deployment Specification (As-Built)

- **Local:** `start.sh` / `cosmos dashboard` — single host, 3 ports (9000, 8765, 8888/8899 optional).
- **Static:** GitHub Pages `https://gemquota.github.io/cosmos/` (root `index.html` redirects to
  `components/rsis3/dashboard/index.html`; `404.html` shims deep MyKB links).
- **No containerization, no CI, no rollback strategy** [O].

## 9. Configuration Specification (As-Built)

| Component | Mechanism | Env vars |
|---|---|---|
| RSIS3 | dataclasses + env + state files | `RSIS_WORKSPACE`, `RSIS_LOG_LEVEL`, `RSIS_EVALUATOR_MODEL`, `RSIS_BUDGET_CAP_USD`, `RSIS_COST_LOG`, `RSIS_TOOLS_ENABLED`, `RSIS_SANDBOX_BACKEND`, `RSIS_SANDBOX_TIMEOUT`, `RSIS_HITL_ENABLED`, `RSIS_APPROVAL_MODE`, `RSIS_APPROVAL_THRESHOLD`, `RSIS_L2_*` (parallel, retries, aging, preemption, shared_memory) |
| SPACE | `DEFAULT_CONFIG` + env | `SPACE_PROJECTS_DIR`, `SPACE_FRAMEWORK_DIR`, `SPACE_LLM_PROVIDER`, `SPACE_LLM_API_KEY`, `SPACE_LLM_MODEL` |
| MyKB | JSON + CLI args | — |
| Heartbeat | `watches.json` | interval/restart flags |

## 10. Gaps Between Spec'd Ideal and As-Built

| Area | Ideal (per docs) | As-built |
|---|---|---|
| Dashboard location | root `index.html` | redirect; real dashboard `components/rsis3/dashboard/index.html` |
| Components | space/mykb/mykb+rsiskb/rsis3/rsisb | space/mykb/rsis3 only (rsisb absent) |
| CI/CD | "shared GitHub Actions" (COSMOS-SPEC §4.2) | none found |
| Ports | RSIS3 :8080 (ARCHITECTURE-SPEC) | rack server default 8765 / FastAPI default |
| Orchestrator | 7 commands over all components | status bug; update = manual rsync advice |

---
*End of document 03. Next: [04 Repository Inventory](04_REPOSITORY_INVENTORY.md).*
