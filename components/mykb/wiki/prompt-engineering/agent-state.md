---
type: "concept"
title: "Agent State"
description: "The accumulated conversation, tool results, goals, and memory an agent carries across its action loop"
tags: ["agent-state", "agents", "memory", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Agent State

## Summary
Agent state is everything an agent persists between turns: message history, tool results, pending goals, and pointers to long-term memory. How state is represented, capped, and summarized determines agent reliability — the difference between a coherent worker and a confused one.

## Details
- State representations: raw transcripts, structured memory objects, working scratchpads, and compressed summaries; each trades fidelity for cost — a full transcript preserves everything and blows the context budget, while summaries lose detail.
- State hygiene is the main engineering problem: unbounded transcripts exceed context windows, confuse the model with stale information, and inflate cost; capping, truncation, summarization, and attention to recency are the standard controls.
- Concrete example: an agent run accumulates 50 tool calls; the loop summarizes old turns into a running digest, keeps the last 10 turns verbatim, and writes key conclusions to the wiki; after a restart, the agent reloads the digest and pointers — the session survives because state crossed the persistence boundary.
- Failure modes: state that grows without bound, degrading quality and cost; summaries that drop the information later steps need; tool results stored at full size, flooding the context; state that does not persist across restarts, forcing rework; conflicting state (two sources of truth) confusing the loop.
- Tradeoffs: richer state improves coherence at the cost of tokens and noise; the alternative, minimal state, is cheap and forgetful; the mature pattern is tiered state — verbatim recent turns, summarized history, and persistent memory for durable facts.
- Operational notes: cap and summarize, log state transitions, and test restart recovery.
- RSIS3 relevance: pulses write distilled state into mykb wiki entities, making the agent's memory survivable across restarts — the persistence tier of agent state.

## Related
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — Tool results are the main state mutations
- [[wiki/prompt-engineering/context-windows|Context Windows]] — The capacity that bounds working state
- [[wiki/prompt-engineering/token-budgets|Token Budgets]] — The policy that caps state size
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — Deciding what state the model sees
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — Persistent state flows into the wiki
