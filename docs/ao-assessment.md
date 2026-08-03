# AO (Agent OS) — Inclusion Assessment for COSMOS

**Date:** 2026-08-03
**Status:** Assessment complete — selective harvest recommended
**Subject:** `~/dev/codex/ao` — "Agent OS", a pure-Python multi-agent runtime (~6.9k LOC)
**Synthesis:** `components/mykb/wiki/syntheses/ao-agent-os-integration-assessment.md`

## 1. What AO Is

Agent OS is a modular operating-system metaphor for autonomous agents: an LLM
kernel with tiered routing and fallback, a three-tier memory hierarchy, a
sandboxed tool layer with per-agent allowlists and human-in-the-loop (HITL)
approvals, an async priority scheduler with recursion guards, and an
observability stack (telemetry/cost ledger, stdlib dashboard, rich TUI,
FastAPI web control center with SSE + WebSocket intercom).

Key modules (all under `~/dev/codex/ao/`):

| Module | File | Capability |
|---|---|---|
| LLM kernel | `kernel/llm_kernel.py` | LiteLLM tier routing (complex/standard/fast) + fallback + audit |
| Scheduler | `kernel/event_loop.py` | Async priority queue, CRITICAL preemption, process table |
| Scheduler (sync) | `kernel/scheduler.py` | Self-contained Module 4 port, blueprint-compatible |
| Parallel DAG | `kernel/parallel_pipeline.py` | Fan-out/fan-in worker pool with dependency readiness + deadlock guard |
| Messages | `kernel/messages.py` | `AgentMessage` envelope: context_ref, parent_id, depth |
| Memory | `memory/context_manager.py` | 3-tier: working memory, token-budgeted context window with LLM-summary GC, long-term store |
| Vector store | `memory/vector_store.py` | sqlite-vec with hashed-embedding and keyword fallbacks |
| Shared memory | `memory/shared_memory.py` | Versioned registers, per-key locks, OCC compare-and-swap |
| Sandbox | `tools/sandbox.py` | 3 tiers: subprocess+limits / RestrictedPython / Docker; secret-scrubbed env |
| Tool manager | `tools/tool_manager.py` | Registry, per-agent allowlists, approval hooks, audit log |
| GitHub tool | `tools/github_tool.py` | Explicit capability surface (list_repos/create_issue/push_file/read_file) |
| HITL gate | `observability/approvals.py`, `observability/hitl_gate.py` | Risk-graded approval modes: auto/interactive/api/deny |
| Telemetry | `observability/telemetry.py` | Per-call cost estimates, budget caps, JSONL ledger |
| Web control center | `observability/web_app.py` | FastAPI + SSE state stream, task dispatch, HITL resolve, WS intercom |

Verified: `ao run selftest` passes in dry-run mode with graceful fallbacks
(sqlite-vec/docker/fastapi degrade to keyword search / subprocess / stdlib
dashboard rather than failing boot).

## 2. Overlap with COSMOS — Do Not Duplicate

- **Memory:** AO's vector store and context windows duplicate MyKB's role.
  MyKB is the integrated, mature memory layer (TF-IDF, temporal engine,
  knowledge graph, `.wiki-daemon` API); AO's memory is lightweight and
  single-process. Two competing memory systems would fragment RSIS3 context.
- **Dashboard:** COSMOS mandates a single unified dashboard
  (`components/rsis3/dashboard/index.html`). AO's FastAPI/SSE control center
  and rich TUI must not ship as a second UI surface.
- **Telemetry:** RSIS3 already has telemetry + pulses + `rack/pulses/`
  snapshots. AO telemetry should be *merged into* that pipeline, not run
  alongside it.
- **Agent definitions:** AO's example agents (planner/coder/reviewer) are
  demo-grade; RSIS3's loop layers are the real cognitive architecture.

## 3. Additive Value — What to Harvest

1. **Tool safety layer (highest value).** RSIS3's L1 executes arbitrary tool
   handlers with no isolation, no allowlists, and no secret redaction
   (`components/rsis3/rsis/loop_l1.py` — stub keyword router). AO's
   `tools/sandbox.py` + `tools/tool_manager.py` add: subprocess isolation with
   resource limits and minimal env, RestrictedPython tier, optional Docker
   tier, per-agent tool allowlists enforced at call time, and secret redaction.
2. **HITL approval gate.** `observability/approvals.py` +
   `observability/hitl_gate.py` map directly onto RSIS3's
   "checkpoint before mutation" practice, upgrading rollback-only checkpoints
   to risk-graded operator escalation (auto/interactive/api/deny, fail-closed
   timeouts).
3. **Scheduler patterns.** `kernel/event_loop.py` / `kernel/scheduler.py` /
   `kernel/parallel_pipeline.py`: priority preemption, strict FIFO, depth
   caps, directed-edge cycle detection, semantic-loop detection, and a DAG
   worker pool — the missing machinery for multi-agent L2 improvement
   candidates (with the immutable evaluator as the verification gate).
4. **Cost accounting.** `observability/telemetry.py` provides per-call
   token/cost estimates and a hard `BUDGET_CAP_USD`; RSIS3 has
   iteration/time budgets but no LLM spend cap.
5. **Context window GC (minor).** `memory/context_manager.py`'s
   token-budgeted window with LLM rollup summarization could replace L1's
   plain-dict context. The sqlite-vec semantic-search idea is a natural MyKB
   enhancement (MyKB currently uses TF-IDF only).

## 4. Recommendation

**Do not** add AO as a fourth top-level COSMOS component with its own
dashboard. **Do** selectively port modules into RSIS3's execution layer:

- **Phase A (now):** sandbox + tool allowlists + HITL approval gate wired
  into `rsis/loop_l1.py` (and the `ToolCall`/checkpoint path), config-gated.
- **Phase B:** extend RSIS3 telemetry with the cost ledger + budget cap;
  optionally add sqlite-vec semantic search to MyKB.
- **Phase C:** adopt scheduler patterns (priority, cycle detection, DAG pool)
  for multi-agent L2 improvement pipelines if parallel candidates are wanted.

## 5. Risks & Caveats

- AO is **unversioned** (no git history) — vendor/port it before relying on it.
- Optional deps (`sqlite-vec`, `docker`, `fastapi`) are not installed in this
  environment; fallbacks work but those tiers are untested here.
- README documents v0.1 limits: linear pipeline by default, no tool-retry
  budgets, single-process dashboards, hashed embeddings until
  `EMBEDDING_MODEL` is set.
- AO's own L1-style planning is demo-grade keyword routing; harvest the
  *infrastructure* (sandbox, approvals, scheduler, telemetry), not the
  agent personas.
