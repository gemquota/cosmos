---
type: synthesis
title: "AO (Agent OS) Integration Assessment — Selective Harvest Rules"
description: "Durable rules from assessing the Agent OS codebase for COSMOS: harvest infrastructure (sandbox, HITL approvals, scheduler guards, cost ledger) into RSIS3, never duplicate memory/dashboard/telemetry surfaces"
tags: [synthesis, rsis3, agent-os, ao, multi-agent, sandbox, hitl, telemetry, integration, cosmos, 2026-08]
timestamp: "2026-08-03T22:10:00Z"
status: stable
source: []
---
# AO (Agent OS) Integration Assessment — Selective Harvest Rules

## Context
The Agent OS codebase (`~/dev/codex/ao`, ~6.9k lines of pure Python) is a
multi-agent runtime: tiered LiteLLM routing, three-tier memory, sandboxed
tools with per-agent allowlists, an async priority scheduler with recursion
guards, HITL approval gates, and a telemetry/cost ledger. COSMOS was assessed
for what to include. The assessment is archived at `docs/ao-assessment.md`;
this note keeps the durable conclusions so future sessions do not re-derive
them.

## Rules
1. **Harvest infrastructure, not personas.** AO's planner/coder/reviewer
   agents are demo-grade; RSIS3's loop layers are the real architecture. Port
   the sandbox, tool manager, approval gate, scheduler guards, and cost
   ledger — never AO's agent definitions or its LLM routing as a replacement
   for RSIS3's own model handling.
2. **RSIS3's L1 tool execution is the integration point.** L1 currently runs
   arbitrary handlers with no isolation, allowlists, or secret redaction.
   AO's three-tier sandbox (subprocess+limits → RestrictedPython → Docker)
   and per-agent tool allowlists close the real gap; wire them into
   `rsis/loop_l1.py`'s `ToolCall`/checkpoint path, config-gated so behavior
   stays reversible.
3. **Map HITL onto the checkpoint-before-mutation practice.** AO's
   risk-graded approval modes (auto/interactive/api/deny, fail-closed
   timeouts) are a strict upgrade over rollback-only checkpoints: risky tools
   suspend execution until an operator resolves, instead of only recording a
   rollback point.
4. **One memory, one dashboard, one telemetry.** COSMOS's single unified
   dashboard and MyKB as the memory layer are invariants. AO's vector store,
   FastAPI control center, TUI, and telemetry pipeline must not be added as
   parallel surfaces; only their ideas may migrate (e.g. sqlite-vec semantic
   search into MyKB, cost/budget fields into RSIS3 telemetry).
5. **Scheduler guards are the multi-agent prerequisite.** Priority
   preemption, depth caps, directed-edge cycle detection, semantic-loop
   detection, and DAG fan-out/fan-in are the missing machinery for parallel
   L2 improvement candidates — with RSIS3's immutable evaluator kept as the
   verification gate.
6. **Vendor before relying.** AO has no git history; any port must be
   committed into COSMOS before it becomes a dependency. Optional deps
   (sqlite-vec, docker, fastapi) degrade gracefully but are untested in this
   environment.

## Phase D1 implementation patterns (2026-08-04)
Second harvest wave, safety/resilience. Durable patterns:
1. **Retry = classification + budget + terminal-attempt success.** A retry
   policy is three things: an error classifier (transient/rate-limit vs
   fatal), a bounded budget, and a success definition based on the terminal
   attempt — otherwise a recovered retry still reports failure. RSIS3 now
   has `rsis/error_classifier.py` (`classify_error` / `classify_error_text` /
   `is_retryable`) and L1 enforces `l1.max_retries` (fatal fails fast;
   recovered retries return success).
2. **Worker pools take retry budgets, not retry logic.** `DAGWorkerPool`
   gained `max_retries` + `retry_base_delay_s`/`retry_max_delay_s`
   (exponential backoff, full jitter), classifies failures at the pool
   boundary, emits `dag_task_retrying` events, and keeps the deadlock guard
   backoff-aware. Default `max_retries=0` preserves fail-fast behavior.
3. **Text-path classification needs syntax markers.** AO only treats
   SyntaxError as fatal via `isinstance`; stringified tool errors (L1's
   `ToolCall.error`) miss it. Extend the text path with
   syntaxerror/syntax error/invalid syntax tokens so fail-fast works on
   real tool output.
4. **Config surface stays env/CLI gated:** `l2.parallel_retries`,
   `RSIS_L2_PARALLEL_RETRIES`, `--parallel-retries`; default 0 = off.

## Related
- [[wiki/syntheses/nine-loop-stack-implementation|Nine-Loop Stack Implementation & Dashboard Wiring]]
- [[wiki/syntheses/loop-graph-engineering-wave-2026-08|Loop & Graph Engineering Wave]]
- [[wiki/syntheses/cosmos-dashboard-mykb-integration|Cosmos Dashboard & MyKB Integration Patterns]]
- [[wiki/syntheses/parallel-agent-acquisition|Parallel Agent Acquisition & Writer Reliability]]
- [[wiki/agent-systems/agent-pipelines|Agent Pipelines]]
- [[wiki/agent-systems/agent-prioritization|Agent Prioritization]]
- [[wiki/agent-systems/queueing-agents|Queueing Agents]]
- [[wiki/llm-agents/approval-gates|Approval Gates]]
- [[wiki/llm-agents/human-in-the-loop|Human in the Loop]]
- [[wiki/llm-agents/handoff-protocol|Handoff Protocol]]
- [[wiki/llm-agents/context-management|Context Management]]
- [[wiki/llm-agents/agent-telemetry-schema|Agent Telemetry Schema]]
- [[wiki/llm-agents/multi-agent-research-systems|Multi-Agent Research Systems]]
- [[wiki/llm-agents/dont-build-multi-agents|Don't Build Multi-Agents]]
- [[wiki/llm-agents/agentic-loops|Agentic Loops]]

## Phase A implementation patterns (2026-08-03)
The selective harvest was executed: `components/rsis3/rsis/tools/` (sandbox,
hitl, manager, workspace_tools) wired into `rsis/loop_l1.py` via a
`ToolConfig` gate. Durable port patterns:
1. **Sync port, not copy-paste.** AO's asyncio ToolManager became a sync
   manager: tool runs go through a worker thread with a hard timeout
   (`concurrent.futures`), and the async ApprovalGate was merged into a sync
   `HITLSafetyGate` whose `api` mode registers a pending request and polls
   (0.25s) until operator resolution or a fail-closed timeout. Behavior
   surface (auto/interactive/api/deny, SAFE→CRITICAL risk ladder) is
   identical; only the transport differs.
2. **Stub planners need argument discipline.** The keyword router cannot feed
   strict tool schemas. Rules that worked: consume the matched keyword and
   pass the remainder as the payload; fill a tool's single required string
   param with the payload; special-case free-text tools (`run_code` →
   `code=payload`); run each tool at most once per task (skip after one
   success, retry after failure); unmatched tasks complete instead of
   defaulting to an arbitrary tool.
3. **Allowlist + containment + audit are the L1 security triad.** Write tools
   restrict to implementing agents (`l1`, `coder`); reviewers are read-only.
   Paths resolve inside the sandbox root with a parents-check. Every call and
   every HITL decision lands redacted in `.rsis/audit.jsonl` /
   `.rsis/hitl.jsonl` (secret patterns masked even when never loaded).
4. **Config gates keep the port reversible.** `ToolConfig` with
   `RSIS_TOOLS_ENABLED=0` restores pre-port behaviour; HITL defaults off so
   unattended runs never prompt; `RSIS_SANDBOX_BACKEND=docker` escalates
   isolation without code changes. Legacy `tools={...}` callable dicts still
   work — the manager path merely takes precedence for its own tools.
5. **Verify through the real entry point.** Smoke tests alone missed the
   `main.py` path; driving `cmd_run` (with the disk-limit gate raised) proved
   L2 → L1 tool execution and audit end-to-end. The repo's resource check
   (disk >80%) and an undefined `logger` in main's throttle callback are
   pre-existing environment/code issues, not port regressions.

## Phase B implementation patterns (2026-08-03)
The second harvest wave: a persistent LLM cost ledger with budget caps in
RSIS3, and offline semantic retrieval in the mykb search engine.
1. **Persistent ledger, not per-process counters.** Each RSIS loop runs as its
   own process, so budget enforcement must survive restarts: every LLM call
   appends to `.rsis/costs.jsonl` and `CostLedger` replays it at construction
   (rebuilding aggregates + the `budget_exceeded` latch). A per-process cap
   would silently reset between `run`/`evolve`/`optimize` invocations.
2. **Two-stage enforcement: pre-flight guard + latch.** `guard_budget` refuses
   a call when (running total + estimated cost) crosses the cap; once spend
   reaches the cap, the latch makes new sessions refuse at `cmd_run` startup.
   The pre-flight estimate must include the *out* tokens (guard uses
   prompt+completion estimates; error paths record completion=0, so latches
   come from successful calls or lowered caps).
3. **Client-side token estimates are a baseline, not a bill.** The evaluator
   client estimates `len(json)//4 + prompt allowance` because exact usage is
   unknowable without the provider. Price table is a local $/1M-token table
   keyed by model substring; swap in real per-call costs when available.
4. **Semantic search offline = hashed n-grams, not embeddings API.** mykb's
   search now fuses a third signal: deterministic blake2b-hashed 2-4 char
   n-grams + tokens into 256-dim signed vectors (sign by hash parity,
   L2-normalized). Pure numpy, no model/API, reproducible across runs — and
   it catches lexical gaps (query "operator approval before risky automation"
   ranks `approval-gates.md` #1). Old indexes degrade gracefully
   (`sem_vectors=None` → hybrid falls back to BM25+TF-IDF).
5. **Test hygiene with the checkpoint manager.** L1's checkpoint-before-
   mutation commits to git on tool failure — running tests from inside the
   repo both pollutes history with `rsis-checkpoint` commits AND `git init`s
   a nested repo when the CWD has no `.git`. Test runs must use a temp CWD,
   or disable `CONFIG.checkpoint_before_mutation`.
6. **Watch out for non-reentrant locks and deque slicing in ports.** The ao
   telemetry port deadlocked (snapshot() re-acquiring its own Lock via
   budget_remaining()) and crashed on `deque[-20:]` — both caught only by
   running the full e2e path, not unit-level smoke checks.

## Phase C implementation patterns (2026-08-04)
The third harvest wave: AO's scheduler + DAG worker pool, wired into RSIS3's
L2 as an optional parallel session. Durable patterns:
1. **Fan-out is bounded by the existing budget, not a new one.** Parallel
   mode takes `n = clamp(parallel_candidates, 2, budget.max_iterations)` and
   each coder still calls `budget.tick()`; the persistent cost ledger and its
   pre-flight `guard_budget` gate every evaluator call exactly as in
   sequential mode (a refused call becomes a FAIL candidate — fail-closed,
   no partial writes).
2. **The DAG fan-in is the immutable evaluator, not the pool.** Parallelism
   must never bypass the verification gate: N coders fan out, the fan-in task
   routes every candidate through the same `EvaluatorClient.evaluate()` and
   only a PASS candidate is applied. The pool only parallelises generation;
   acceptance policy is unchanged.
3. **Re-dispatch after settle, then judge deadlock.** A DAG loop that checks
   "nothing in flight and nothing dispatchable → deadlock" immediately after
   collecting settled futures is wrong: a completed dependency can unlock new
   tasks in the same pass. The pool must re-run the fan-out pass after any
   settle before raising; the guard then only fires on genuinely stuck
   graphs (circular/missing deps).
4. **Scheduler guards protect the review wave.** Fan-in reviews run through
   `AgentScheduler` (depth cap + directed-edge cycle detection) so a
   repeating coder↔reviewer hand-off aborts the branch instead of spinning;
   a guard-rejected review fails closed to a FAIL candidate.
5. **Telemetry must expose the DAG shape.** `on_event` bridges per-task
   status/latency (`dag_task`) plus a `dag_complete` summary into the
   existing telemetry stream, and the session records `l2_parallel_start`
   with the candidate count — the dashboards can then distinguish parallel
   fan-out from sequential attempts without new surfaces.
6. **CLI flag overrides config; env var feeds config.** `--parallel N`
   overrides `L2Config.parallel_candidates` at `cmd_run` time; `RSIS_L2_PARALLEL`
   feeds the same field at load. Default stays `0` (sequential), so the
   behaviour is opt-in and reversible.
