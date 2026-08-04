# 02 — Architecture Analysis

**Doc ID:** COSMOS-AUDIT-02 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Cross-references:** [03 System Architecture Specification](03_SYSTEM_ARCHITECTURE_SPECIFICATION.md) · [06 Module-by-Module Audit](06_MODULE_BY_MODULE_AUDIT.md) · [11 Dependency Analysis](11_DEPENDENCY_ANALYSIS.md)

---

## 1. Reverse-Engineered Architecture Style

COSMOS is a **hub-and-spoke ecosystem** whose hub is RSIS3, containing a **layered, pipeline-of-loops
core** inside it. Classifying precisely:

| Pattern | Present? | Evidence |
|---|---|---|
| Layered architecture | **Yes** | RSIS3: CLI layer → loop layer → subsystem layer (telemetry/checkpoint/memory/evaluator/recovery/enforcer) |
| Pipeline architecture | **Yes** | L1→L2→L3→…→L9 form a pipeline with +3 diagonal feedback |
| Plugin architecture | Partial | SPACE LLM providers are a clean plugin set; RSIS3 tools are extensible via `tools/__init__.py` |
| Event-driven | Partial | `rsis/event_bus.py` exists and is tested; not used everywhere |
| Functional-core/imperative-shell | Partial | `practices.py` checkers are pure-ish; loops are imperative |
| Microservices | No | All processes are local; no network partition of components |
| Actor model | No | Threads + queues, no actor framework |
| Reactive | No | Polling (heartbeat, monitor threads), not reactive |
| Clean/Hexagonal/Onion | Partial | SPACE approaches hexagonal (storage provider interface, engine boundary); RSIS3 couples modules directly |
| ECS / data-oriented | No | — |

**Overall:** a *hybrid layered + pipeline-of-loops* architecture with clean vertical seams between the
three components (they communicate through filesystem + HTTP, not shared code).

## 2. RSIS3 Internal Layering (Observed)

```
┌───────────────────────────────────────────────────────────────┐
│ Layer 0: CLI (main.py) — argparse dispatch, 17 commands        │
├───────────────────────────────────────────────────────────────┤
│ Layer 1: Loop stack (loop_l1.py … loop_l9.py)                  │
│         + pipeline.py (orchestration), scheduler.py            │
├───────────────────────────────────────────────────────────────┤
│ Layer 2: Subsystems — memory, telemetry, checkpoint,           │
│         evaluator, recovery, resource_monitor, priority_pool,  │
│         extrapolation, shared_memory, event_bus, timeout       │
├───────────────────────────────────────────────────────────────┤
│ Layer 3: Tools — manager, sandbox, hitl, workspace_tools, base │
├───────────────────────────────────────────────────────────────┤
│ Layer 4: Config & state — config.py (tunables registry),      │
│         .rsis/*.json state files, practices.py (git hygiene)   │
└───────────────────────────────────────────────────────────────┘
```

Dependency direction is **downward only within the loop layer** (L_k uses L_{k-1} subsystems), which is
correct for the intended design [O]. Violations: `main.py` imports every layer (acceptable for a CLI);
`practices.py` shells out to `git`; `telemetry.py` reads workspace state directly.

## 3. The "+3 Diagonal Ownership" Design

`config.py` encodes a registry of tunable parameters with strict ownership (observed):

- L4 owns L1 params (`l1.max_retries`, `l1.max_tool_calls`)
- L5 owns L2 params (`l2.max_attempts`)
- L6 owns L3 params (`l3.plateau_timeout_s`)
- L7 owns L4 params (windows/thresholds)
- L8 owns L5 params (mutation rate, population size)
- L9 owns L6 params (shrink/grow bands)

At startup, `_apply_tuned_state()` reads each owner's `.rsis/<owner>_state.json` and clamps values to
registry bounds. This is a **sound feedback-control topology** (prevents a loop from tuning its own
knobs), with one architectural caveat: L7–L9 were added after L4–L6 and the registry treats them
symmetrically, so "meta-meta" chains are linear, not branching — genuine self-referentiality is limited
to depth-9 [I, Med].

## 4. Control Flow: One RSIS Pulse

Observed flow (from `main.py cmd_run`, `pipeline.py`, `loop_l1.py`):

1. `_init_subsystems()` builds telemetry, checkpoint, memory, evaluator, recovery, enforcer.
2. `enforcer.start()` + `telemetry.start()` (threads).
3. `cmd_run` executes the L1 loop for the goal: tool calls → sandbox → evaluator → retries.
4. Outcomes recorded to the ledger; budget cap enforced (`ledger.budget_cap_usd`, `budget_exceeded`).
5. `finally:` stops telemetry and enforcer (graceful path), and on failure paths `recovery` runs
   `FailureInjector`/`RecoveryManager` (see [09 Control Flow](09_CONTROL_FLOW_ANALYSIS.md)).

## 5. Boundaries & Information Hiding

| Boundary | Mechanism | Rating |
|---|---|---|
| RSIS3 ↔ MyKB | Filesystem (workspace `.rsis/`), plus documented bridge (`mykb/ops/rsis3-memory-bridge.md`) | OK — but no typed API |
| RSIS3 ↔ SPACE | RRP pulse artifacts (`rack/pulses/*.json`, `rack/rrp_engine.py`) | OK — JSON contract |
| CLI ↔ components | Shell + pgrep/pid files | Weak — status only probes SPACE |
| Dashboard ↔ data | `config.js` → `../rack/pulses/dashboard-data.json` (static) | OK — no backend needed |
| SPACE engine ↔ storage | `StorageProvider` interface (`storage/types.ts`) | Strong — clean seam |
| SPACE engine ↔ LLM | `LLMProvider` factory (`llm/factory.ts`) | Strong — clean seam |

## 6. Configuration Strategy

- **RSIS3:** dataclass defaults + env overrides (`RSIS_*`) + state-file tuning, all composed in
  `load_config()` → `CONFIG` singleton (see [21 Configuration Analysis](21_CONFIGURATION_ANALYSIS.md)).
- **SPACE:** `DEFAULT_CONFIG` + `SPACE_*` env vars + per-instance overrides; `config/validation.ts`.
- **MyKB:** JSON config files (`.wiki-daemon/config.json`, `watches.json`) + CLI args.
- **No central config file; no secrets in config** [O].

## 7. Initialization & Lifecycle

- `start.sh` orchestrates: static `http.server` on :9000 (0.0.0.0), MyKB `server.py` on :8765; pid files
  in `.cosmos-pids/`; SIGINT/SIGTERM trap stops all. `heartbeat.mjs` (optional) restarts watched
  services every 30s (`--interval 30 --restart`).
- RSIS3 subsystems have explicit `start()/stop()` (threads); loops run in-process with `deadline()`.
- SPACE has no lifecycle manager in-repo; the README recommends PM2/systemd externally [O].

## 8. State & Persistence Topology

| Store | Location | Format | Owner |
|---|---|---|---|
| Loop tunables | `.rsis/optimizer_state.json`, `strategies.json`, `identity_state.json`, `metacog_state.json`, `metameta_state.json`, `mmm_state.json` | JSON | RSIS3 |
| Telemetry | `rack/pulses/*.json`, `dashboard-data.json` | JSON | RSIS3 |
| Audit/HITL | `.rsis/audit.jsonl`, `.rsis/hitl.jsonl` | JSONL | RSIS3 |
| Wiki | `components/mykb/wiki/**/*.md` | Markdown+frontmatter | MyKB |
| Search index | `.wiki-daemon/search_*.json/npy` | JSON + NumPy | MyKB |
| Graph | `graph.json` (nodes/edges) | JSON | MyKB |
| SPACE sessions | `~/.space/projects/**` or sql.js DB | JSON/SQLite | SPACE |
| RRP work | `.rsirrp/work/`, `rack/pulses/` | JSON/md | RSIS3+SPACE |

## 9. Architectural Strengths (Observed)

1. **Vertical seams between components are clean** — three independent codebases with filesystem/JSON
   contracts; no import coupling.
2. **The loop stack is genuinely parameterized, not hardcoded** — the tunables registry + ownership table
   is a real meta-programming design.
3. **SPACE's engine/storage/LLM boundaries are textbook** (interfaces, DI via `createSpace(config)`).
4. **Sandbox + HITL + budget caps** show security-and-cost awareness rare at this project age.

## 10. Architectural Weaknesses (Observed / Inferred)

1. **RSIS3 subsystem coupling** — `loop_l*.py` import each other and subsystems directly; no interfaces
   for MemoryManager/TelemetryCollector, making unit testing and replacement harder [I, Med].
2. **State files are schema-unversioned** — `.rsis/*.json` evolve by convention; a stale L4 state can
   silently override newer defaults (mitigated by clamping) [O, Med].
3. **Orchestration shell layer is the weakest link** — `cli/cosmos` has a bug where status only checks
   SPACE; `watches.json` startArgs reference a nonexistent `serve-dashboard.mjs` [O, High].
4. **Static dashboard coupling** — dashboard reads `dashboard-data.json` generated by `gen-static-data.py`;
   regeneration is a manual step that can drift from live telemetry [O, Med].
5. **No formal extension points documented** for adding loops beyond L9 or new providers beyond the
   existing registry [I, Med].

## 11. Architecture Style Assessment (FAANG-Staff Lens)

Would this pass a design review? **Partially.** The loop-stack + ownership-registry concept is
defensible and well-documented in code comments. The review would fail on: (a) absence of interface
contracts for core subsystems, (b) unversioned state schemas, (c) shell orchestration fragility,
(d) no deployment/rollback story, (e) single-writer concurrency assumptions in telemetry/memory
(see [17 Concurrency Analysis](17_CONCURRENCY_ANALYSIS.md)). All fixable without redesign.

---
*End of document 02. Next: [03 System Architecture Specification](03_SYSTEM_ARCHITECTURE_SPECIFICATION.md).*
