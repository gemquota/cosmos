---
type: "entity"
title: "PromptSession"
description: "A bounded, stateful interaction between a user or agent and a language model"
tags: ["entity", "prompt", "session", "llm", "conversation"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
---

# PromptSession

## Summary

A prompt session is a bounded, stateful interaction with a language model — the accumulated conversation, tool results, and context that shape each response. It matters because model behavior is path-dependent: what came before determines what comes next. Managing session boundaries, persistence, and context budgets is core agent engineering.

## Details

- **Definition** — A session groups turns of a conversation, carrying the history and metadata that make responses coherent across calls.
- **State** — Message history, tool results, user identity, and session metadata form the state; its size and freshness are controlled deliberately.
- **Persistence** — Sessions are stored so work can resume across crashes, be audited, and be replayed for debugging.
- **Budgeting** — Long sessions overflow context; summarization, truncation, and selective eviction keep the window usable.
- **Worked example** — A coding agent's session holds the task, the files touched, and each command result; when history grows, older turns are summarized into a digest.
- **Common failure modes** — History that grows unbounded, sessions that lose identity after restart, and context pollution from stale turns.
- **Practical relevance** — Session design determines cost, coherence, and debuggability, making it a central artifact of agent systems.
- **Variants** — Stateless calls re-send full context each time; sessioned APIs maintain server-side state with explicit lifecycle.
- **Telemetry note** — Recorded among CLI and backend tags, matching interactive and automated prompt workflows.
- **Resumption** — Persisted sessions can resume after crashes; restoring state without re-running prior tools is what makes long tasks interruptible.
- **Audit** — Session logs provide the full record of what was asked and answered, which is the basis for debugging and accountability.
- **Worked example** — A support bot's session stores the customer context and policy snippets; each turn appends, and after an hour the oldest turns collapse into a summary.
- **Isolation** — Separating sessions per task or user prevents cross-contamination of context and keeps prompts focused.

## Related

- [[wiki/api-services/categories/api-rest/subcategories/rest-http/gce-2|GCE]] — managing session context
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/context-efficiency|Context Efficiency]] — budgeting the window
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/ingestioncontext-2|IngestionContext]] — context entering the system
- [[wiki/llm-agents/prompt-debugging|Prompt Debugging]] — diagnosing session failures
- [[wiki/agent-systems/identity-and-continuity|Identity and Continuity]] — session identity across time
- [[wiki/concepts/working-memory|Working Memory]] — the cognitive analogue
