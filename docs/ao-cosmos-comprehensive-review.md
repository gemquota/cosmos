# COSMOS × AO — Exhaustive Analytical Review & Integration Study

**Date:** 2026-08-04
**Status:** Analysis complete (architecture, overlap, integration options, quantified harvest)
**Subjects:** COSMOS (`~/dev/cosmos`) · AO — "Agent OS" (`~/dev/codex/ao`)
**Prior work:** `docs/ao-assessment.md` (Phases A–C) · MyKB synthesis
`wiki/syntheses/ao-agent-os-integration-assessment.md`

---

## 0. Executive Summary

- COSMOS is a **self-improvement ecosystem**: RSIS3 (nine-loop cognitive core),
  MyKB (persistent semantic memory), SPACE (RRP ideation engine), one unified
  dashboard, one CLI, GitHub-Pages deployment. AO is a **multi-agent runtime**:
  LLM tier routing, three-tier memory, sandboxed tools, priority scheduler,
  HITL approvals, telemetry/cost accounting, and a family of dashboards.
- The two are **architecturally adjacent, not competing**: COSMOS is the
  cognitive architecture (loops, evaluator, memory, ideation); AO is execution
  infrastructure (kernel, scheduler, sandbox, observability) for exactly the
  kind of multi-agent pipelines COSMOS's L2 has begun to need.
- **Already integrated (Phases A–C, 2026-08-03/04):** AO's sandbox + tool
  manager + HITL gate + workspace tools, scheduler guards, DAG worker pool,
  LLM cost ledger, and offline semantic search. This is ~1.4k LOC of AO
  (~14%), ported and committed into `components/rsis3/`.
- **Remaining high-value harvest (Phase D candidate):** ~1.7k LOC of AO
  (~17.5%) — resilient/priority/checkpoint worker pools, error classifier,
  event bus, shared-memory OCC registers, context-window GC, sqlite-vec
  store, GitHub tool, operator intercom kernel.
- **Reject (~55% of AO):** the four dashboards (3.6k LOC), agent personas,
  `main.py`/demo harnesses, and standalone web control center — they
  duplicate COSMOS invariants (one memory, one dashboard, one telemetry)
  and demo-grade personas.
- **Verdict:** *selective porting wave 2*, never a full merge, never a fourth
  top-level component. AO is not versioned, is ~9.7k LOC of infrastructure,
  and its durable value is already 40% claimed by COSMOS.

---

## 1. System A — COSMOS (`/data/data/com.termux/files/home/dev/cosmos`)

### 1.1 Identity
"**C**ognitive **O**rchestration **S**ystem for **M**eta-cognitive **O**rchestration &
**S**ynthesis" — unifies SPACE, MyKB, RSIS3 (and predecessors myRSIKB /
myRSISKB) under one CLI and one dashboard. Deployed at
`gemquota.github.io/cosmos/`.

### 1.2 Component map (measured)

| Component | Role | Language | Measured footprint |
|---|---|---|---|
| `components/rsis3/` | Core cognitive engine (nine loops L1–L9) | Python | ~8.7k LOC |
| `components/mykb/` | Long-term memory (wiki + search + graph + daemon) | Python/Markdown | ~3.7k LOC (py) + 6,855 wiki files |
| `components/space/` | RRP ideation engine (7 series, 326 probes, 6 exports) | TypeScript | 299 files |
| `cli/`, `infra/`, `ops/`, `diagrams/` | Orchestration, heartbeat, deployment | — | — |

### 1.3 RSIS3 core architecture
- **Nine nested loops**, evaluator-gated and bounded: L1 per-task action,
  L2 per-session improvement, L3 cross-session evolution, L4 optimizer,
  L5 strategy evolution, L6 identity, L7 meta-cog, L8 meta-meta, L9 MMM.
- **+3 tuning diagonal:** loop *k*+3 tunes loop *k* (L4→L1 … L9→L6);
  registered tunables, disjoint state files, no top loop tunes the top three.
- **Immutable evaluator** (`evaluator/evaluator.py` + `prompt.txt`): separate
  process, read-only mount, SHA-256 self-verify, never in scope.
- **Memory hierarchy:** git (truth) → knowledge graph (NetworkX) → vectors
  (numpy n-gram); persisted under `.rsis/`; MyKB as the long-term store.
- **Checkpoint-before-mutation:** every destructive action is checkpointed
  (`rsis/checkpoint.py`, `rsis-checkpoint:` git commits) with rollback.
- **Practice enforcement:** `python -m rsis check-practices` — 17 checks
  (registry invariants, state-file disjointness, telemetry coverage,
  checkpoint hygiene) via `rsis/practices.py`.
- **CLI:** `rsis init/run/evolve/optimize/strategies/identity/metacog/
  metameta/mmm/dashboard/status/check/scheduler/pipeline/recovery-test`.

### 1.4 AO-derived code already inside RSIS3 (Phases A–C)
| Ported module | Source AO file | Role in RSIS3 |
|---|---|---|
| `rsis/tools/sandbox.py` | `tools/sandbox.py` | 3-tier execution sandbox (subprocess+limits → RestrictedPython → Docker) |
| `rsis/tools/hitl.py` | `observability/hitl_gate.py` + `approvals.py` | 5-level risk matrix, auto/interactive/api/deny, fail-closed |
| `rsis/tools/manager.py` | `tools/tool_manager.py` | Registry + per-agent allowlists + SecretVault + redacted audit |
| `rsis/tools/workspace_tools.py` | `tools/workspace_tools.py` | Path-contained file I/O + `run_code` |
| `rsis/scheduler.py` | `kernel/scheduler.py` | Priority queue, strict FIFO, depth caps, cycle guards |
| `rsis/pipeline.py` | `kernel/parallel_pipeline.py` | DAG fan-out/fan-in, dependency readiness, deadlock guard |
| `rsis/telemetry.py` CostLedger | `observability/telemetry.py` | JSONL cost ledger, `guard_budget`, `--budget-cap` |
| `mykb/.wiki-daemon/search_fusion.py` | idea from `memory/vector_store.py` | Offline hashed n-gram semantic retrieval, RRF fusion |

L2 parallel mode (`--parallel N`) wires planner → N coders → fan-in reviewer
through `DAGWorkerPool` + `AgentScheduler`, still gated by the immutable
evaluator. Default remains sequential.

### 1.5 MyKB (memory layer)
- 6,855 markdown docs; BM25 + TF-IDF + hashed-semantic fusion
  (`search_fusion.py`); knowledge graph (`graph.json`); temporal engine;
  `.wiki-daemon` HTTP API (`/search`, `/api/v2/search/hybrid`,
  `/api/v2/graph/topology`, `/api/v2/health/lint`, history snapshots);
  session-capture hooks (`hooks/post-tool-use.py`, `session-stop.py`);
  dual wiki Content|Meta view; self-contained browsers (wiki, graph, stats).
- This is the **single memory surface** invariant: no second vector store.

### 1.6 SPACE (ideation)
- 7 series × multi-round probe framework (326 probes), 6 export formats,
  self-contained SPA + `meta-viewer.html`; consumed by RSIS3's L2 ideation.

### 1.7 Known debt (from `docs/ARCHITECTURE-SPEC.md` §9)
SPACE `dist/` not built; MyKB `server.py` and RSIS3 rack server share port
8765; dashboard data is a hardcoded snapshot (not live); hub has orphaned
pages; no dashboard test coverage.

---

## 2. System B — AO "Agent OS" (`~/dev/codex/ao`)

### 2.1 Identity
A lightweight, modular **operating-system metaphor for autonomous agents** in
pure Python (~9.7k LOC, 51 files): LLM kernel (CPU), memory (RAM/disk),
tools (actuators) with security boundary, scheduler, observability. Its own
README: "all swappable at config time". **No git history** (not versioned).

### 2.2 Module inventory (measured)

| Layer | Module | LOC | Role |
|---|---|---|---|
| Kernel | `event_loop.py` | 440 | Async AgentOS scheduler: priority queue, process table, recursion guards |
| Kernel | `scheduler.py` | 185 | Sync Module-4 port (blueprint-compatible) |
| Kernel | `parallel_pipeline.py` | 215 | DAG worker pool |
| Kernel | `llm_kernel.py` | 210 | LiteLLM tier routing (complex/standard/fast) + fallback |
| Kernel | `opencode_kernel.py` | 143 | OpenAI-compatible intercom kernel (token streaming) |
| Kernel | `advanced_priority_pool.py` | 222 | Priority aging + preemption |
| Kernel | `resilient_worker_pool.py` | 321 | Retry budgets, exponential backoff + jitter |
| Kernel | `priority_worker_pool.py` | 109 | Base priority pool |
| Kernel | `checkpoint_worker.py` | 87 | Step-level task resume after preemption |
| Kernel | `error_classifier.py` | 40 | Transient/rate-limit/fatal classification |
| Kernel | `messages.py` | ~90 | AgentMessage envelope (context_ref, parent_id, depth) |
| Memory | `context_manager.py` | 280 | 3-tier memory, token-budgeted window, LLM-summary GC |
| Memory | `vector_store.py` | 176 | sqlite-vec store, hashed-embedding fallback |
| Memory | `shared_memory.py` | 147 | Race-safe registers, OCC compare-and-swap |
| Tools | `sandbox.py` | 353 | 3-tier sandbox |
| Tools | `tool_manager.py` | 199 | Registry, allowlists, SecretVault, audit |
| Tools | `workspace_tools.py` | 91 | Path-contained file I/O |
| Tools | `github_tool.py` | 82 | gh CLI wrapper, scoped secrets |
| Obs | `telemetry.py` | 245 | Cost ledger, token/tool metrics, JSONL |
| Obs | `approvals.py` + `hitl_gate.py` | 182+238 | Risk-graded HITL |
| Obs | `event_bus.py` | 99 | Pub/sub broker, replayable history |
| Obs | `web_app.py` | 2,250 | FastAPI control center: SSE, WS intercom, task dispatch |
| Obs | `worker_dashboard.py` | 901 | Async worker-pool dashboard |
| Obs | `tui_dashboard.py` | 321 | rich-based TUI |
| Obs | `dashboard.py` | 155 | stdlib zero-dep dashboard |
| Agents | `base_agent.py` + planner/coder/reviewer/factory | ~350 | Demo personas |
| Entry | `main.py` + `test_run.py` + 4 examples | ~1,190 | Bootstrap, e2e test, demos |
| Config | `settings.py` + `agents.yaml` | ~200 | Env-overridable config |

Total ≈ **9.7k LOC**.

### 2.3 Maturity assessment
- Verified by prior session: `ao run selftest` passes in dry-run mode with
  graceful fallbacks (sqlite-vec → keyword, docker → subprocess, fastapi →
  stdlib dashboard).
- Optional deps (`sqlite-vec`, `docker`, `fastapi`, `rich`) are **not
  installed** in this environment — those tiers are untested here.
- Known v0.1 limits (README): linear pipeline by default, no tool-retry
  budgets in the linear path, single-process dashboards, hashed embeddings
  until `EMBEDDING_MODEL` is set.
- Quality signals: strong docstrings, consistent module boundaries, config
  surface is clean. Risk: no version control, no tests beyond `test_run.py`
  and demo scripts.

---

## 3. Functional Overlap — What COSMOS Already Covers

| AO capability | COSMOS equivalent | Verdict |
|---|---|---|
| Vector store / memory | MyKB (TF-IDF+BM25+hashed semantic, KG, temporal) | **Duplicate — do not import** |
| Dashboards (4) | Unified `dashboard/index.html` (mandate) | **Duplicate — do not import** |
| Telemetry/cost | RSIS3 telemetry + pulses + CostLedger | **Merge into existing pipeline (done)** |
| Agent personas | RSIS3 loop layers (L1–L9) | **Duplicate — demo-grade** |
| LLM tier routing | RSIS3's own model handling | **Adapt ideas only** |
| HITL approvals | RSIS3 checkpoint-before-mutation | **Upgrade (done)** |
| Sandbox/allowlists | None (L1 was open handlers) | **Harvest (done)** |
| Scheduler/guards | None (sequential L2) | **Harvest (done)** |
| Worker pools/retry | DAGWorkerPool only, no retry budgets | **Harvest wave 2** |
| Event bus | None (telemetry is append-only) | **Harvest wave 2** |
| Shared memory | None | **Harvest wave 2** |
| Context-window GC | L1 plain-dict context | **Harvest wave 2** |
| GitHub tool | None | **Harvest wave 2** |

---

## 4. Module-by-Module Integration Disposition (Wave 2)

### 4.1 Port — high value, low risk (Phase D)
| AO module | LOC | Why / how |
|---|---|---|
| `error_classifier.py` | 40 | Transient/rate-limit/fatal → feeds L1 retry policy (`l1.max_retries`) and worker-pool budgets. Trivial sync port. |
| `resilient_worker_pool.py` | 321 | Retry budgets + exponential backoff with jitter over the event bus — upgrades L2 parallel candidates beyond one-shot. |
| `advanced_priority_pool.py` | 222 | Priority aging (anti-starvation) + preemption — for mixed CRITICAL/HIGH/LOW L2 workloads. |
| `priority_worker_pool.py` | 109 | Base pool refactor dependency of the two above. |
| `checkpoint_worker.py` | 87 | Step-index resume after preemption — pairs with RSIS3 checkpoints (reuse step index, not git). |
| `event_bus.py` | 99 | Topic pub/sub with replayable history — gives L2/parallel pipelines a live event stream the dashboard can subscribe to (SSE-style) without a second telemetry DB. |
| `shared_memory.py` | 147 | OCC registers for parallel agents — L2 parallel coders sharing verdicts/artifacts safely. |
| `context_manager.py` | 280 | Token-budgeted window + LLM-rollup GC → replace L1's plain-dict context; degrade to verbatim archive like AO does. |
| `github_tool.py` | 82 | gh CLI wrapper with vault-injected secrets — natural sibling to `workspace_tools.py`; allowlist + risk=CRITICAL. |

Subtotal: **~1,387 LOC** (~14% of AO). Combined with Phase A–C (~1.4k),
the addressable harvest is **~2.8k LOC ≈ 29% of AO**.

### 4.2 Port-with-adaptation — concept + sync transport
| AO module | LOC | Adaptation |
|---|---|---|
| `vector_store.py` | 176 | MyKB gains sqlite-vec as an *optional backend* under `search_fusion.py` (embedding model optional; keep hashed fallback). Do not create a second memory system — fold into MyKB's single index. |
| `opencode_kernel.py` | 143 | Intercom pattern → optional "operator chat" channel in the unified dashboard via the wiki daemon; not a standalone UI. |
| `llm_kernel.py` | 210 | Adopt tier-routing *idea* (complex/standard/fast + fallback) in RSIS3's evaluator/improvement calls; keep LiteLLM optional. |

### 4.3 Reject — duplicates COSMOS invariants or demo-grade
| AO module | LOC | Reason |
|---|---|---|
| `web_app.py` | 2,250 | Standalone control center — violates one-dashboard mandate. Harvest *API patterns* (SSE state stream, HITL resolve endpoint) into the wiki daemon instead. |
| `worker_dashboard.py` | 901 | Standalone worker dashboard — same reason. |
| `tui_dashboard.py` | 321 | Standalone TUI — same reason (could live as a rsis subcommand if wanted; low priority). |
| `dashboard.py` | 155 | stdlib dashboard — superseded by the above. |
| `agents/` (all) | ~350 | Personas are demo-grade; RSIS3's L2 planner/coder/reviewer roles are the real ones (already mirrored in `loop_l2.py`). |
| `main.py`, `test_run.py`, examples | ~1,360 | Demo harnesses; port *assertions* as unit tests for the ported modules instead. |
| `bundle/` (docs) | — | Packaging artifact, not code. |

Rejected total ≈ **~5.3k LOC (~55% of AO)**. The remainder (README, config,
`.env.example`, small helpers) is documentation/reference.

### 4.4 Cumulative disposition
| Category | AO LOC | Share |
|---|---|---|
| Ported (Phases A–C, committed) | ~1.4k | ~14% |
| Port now (Phase D) | ~1.4k | ~14% |
| Adapt (concept-only) | ~0.5k | ~5% |
| Reject (UI/personas/demos) | ~5.3k | ~55% |
| Docs/config remainder | ~1.2k | ~12% |
| **Addressable integration total** | **~2.8–3.3k** | **~29–34%** |

---

## 5. Merge / Combine Options

### Option 1 — Status quo (selective harvest, Phases A–C)  ⚠️ not enough
Already delivered the security and concurrency baseline. Leaves retry
resilience, live events, and the GitHub surface unclaimed; AO's unique
remaining machinery continues to rot unversioned.

### Option 2 — Phase D selective port into RSIS3  ✅ recommended
Port §4.1 modules into `components/rsis3/rsis/` (sync-first, config-gated),
fold §4.2 concepts into MyKB/RSIS3 surfaces, add unit tests ported from
AO's assertions, refresh `docs/ao-assessment.md` + MyKB synthesis. Keeps all
COSMOS invariants; ~1.4k LOC of new code; low blast radius.

### Option 3 — AO as a fourth COSMOS component  ❌ rejected
Would add a second dashboard, second memory store, second telemetry
pipeline, and a competing scheduler — exactly the fragmentation COSMOS was
built to prevent (see `COSMOS-SPEC.md` and the synthesis rules).

### Option 4 — Full merge / absorb AO  ❌ rejected
~2/3 of AO is UI/personas/demos COSMOS must not ship. A full merge would
import 5k+ LOC of duplicate surfaces and unversioned code with no test
suite. Not justified.

### Option 5 — Reverse: COSMOS features into AO  ⚠️ only at interface level
AO could *consume* MyKB (as its long-term store) and RSIS3 (as its
improvement loop) rather than reimplementing them. Only meaningful if AO is
ever revived as a standalone runtime; today RSIS3's L2 parallel mode already
plays the role AO would play inside COSMOS.

---

## 6. Integration Points & Coupling Rules

1. **Single memory:** any semantic store (sqlite-vec) lives inside MyKB's
   `.wiki-daemon`, never beside it.
2. **Single dashboard:** any live state stream (event bus → SSE) is exposed
   by the wiki daemon / rack server and consumed by the existing dashboard
   iframe; no new standalone page.
3. **Single telemetry:** worker-pool and retry events append to RSIS3
   telemetry JSONL + CostLedger; no second ledger.
4. **Sync-first ports:** AO's asyncio transports become sync wrappers
   (thread + timeout) as in Phase A, so RSIS3's stdlib-only constraint holds.
5. **Config-gated:** every port defaults off, mirroring `ToolConfig` /
   `parallel_candidates=0`.
6. **Vendor before rely:** all Phase D ports committed into COSMOS (AO has
   no git history); optional deps keep graceful fallbacks.
7. **Evaluator stays the gate:** worker pools may parallelize *candidates*,
   never the immutable evaluator.

---

## 7. Risks

- **Unversioned source:** AO changes/rot without history; snapshot it in
  `docs/` or vendor the bundle before further ports.
- **Untested tiers:** sqlite-vec, Docker, FastAPI, rich are not installed
  here; fallbacks exist but are unproven.
- **Concurrency complexity:** priority aging/preemption and OCC registers
  are subtle; port with the AO semantics intact and unit tests first.
- **Scope creep:** resisting "port the nice dashboard" is the main
  governance risk — the four dashboards are the biggest LOC block and must
  stay out.
- **Context-window GC cost:** LLM-summary rollups add spend; keep
  verbatim-archive fallback and tie to the CostLedger budget cap.

---

## 8. Recommended Roadmap

- **Phase D1 (safety/resilience) — DONE 2026-08-04:** `error_classifier`
  (`rsis/error_classifier.py`) → retry policy in L1 (`l1.max_retries` now
  enforced, fatal failures fail fast, recovered retries report success);
  retry budgets + exponential backoff with jitter added to `DAGWorkerPool`
  (`rsis/pipeline.py`, `max_retries` param, `dag_task_retrying` events),
  wired to L2 via `l2.parallel_retries` / `--parallel-retries` /
  `RSIS_L2_PARALLEL_RETRIES`.
- **Phase D2 (concurrency):** `priority/advanced pools` + `checkpoint_worker`
  + `shared_memory` behind `parallel_candidates`; event bus emits
  pool/retry/preempt events into telemetry.
- **Phase D3 (memory/context):** `context_manager` GC into L1 context;
  sqlite-vec optional backend in MyKB `search_fusion.py`.
- **Phase D4 (capability surface):** `github_tool` into `rsis/tools/` with
  risk=CRITICAL + HITL; intercom endpoint on the wiki daemon if desired.
- **Phase D5 (verify):** port AO's `test_run.py` assertions as pytest cases;
  `check-practices` still passes; update `docs/ao-assessment.md`, MyKB
  synthesis, and dashboard `ecosystem.json` counts.

## 9. Bottom Line

**How much of AO can be integrated into COSMOS?** Roughly **one third** —
about **2.8–3.3k of ~9.7k LOC** is infrastructure worth claiming; ~1.4k is
already committed (Phases A–C), ~1.4k more is a clean Phase D port, and the
rest is UI surfaces, demo personas, and harnesses COSMOS should explicitly
reject. The correct mechanism is **selective porting into RSIS3/MyKB**, never
a component-level merge — the two systems occupy different layers, and
COSMOS's "one memory, one dashboard, one telemetry" invariants are exactly
what make the combination coherent.
