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

## Related
- [[wiki/syntheses/nine-loop-stack-implementation|Nine-Loop Stack Implementation & Dashboard Wiring]]
- [[wiki/syntheses/loop-graph-engineering-wave-2026-08|Loop & Graph Engineering Wave]]
- [[wiki/syntheses/cosmos-dashboard-mykb-integration|Cosmos Dashboard & MyKB Integration Patterns]]
- [[wiki/llm-agents/approval-gates|Approval Gates]]
- [[wiki/llm-agents/human-in-the-loop|Human in the Loop]]
- [[wiki/llm-agents/handoff-protocol|Handoff Protocol]]
- [[wiki/llm-agents/context-management|Context Management]]
- [[wiki/llm-agents/agent-telemetry-schema|Agent Telemetry Schema]]
- [[wiki/llm-agents/multi-agent-research-systems|Multi-Agent Research Systems]]
- [[wiki/llm-agents/dont-build-multi-agents|Don't Build Multi-Agents]]
- [[wiki/llm-agents/agentic-loops|Agentic Loops]]
