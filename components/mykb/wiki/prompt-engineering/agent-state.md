---
type: "concept"
title: "Agent State"
description: "The accumulated conversation, tool results, goals, and memory an agent carries across its action loop"
tags: ["agent-state", "agents", "memory", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Agent State

## Summary
Agent state is everything an agent persists between turns: message history, tool results, pending goals, and pointers to long-term memory. How state is represented, capped, and summarized determines agent reliability.

## Details
- State representations: raw transcript, structured memory objects, working scratchpads, or compressed summaries.
- State hygiene is the main engineering problem — unbounded transcripts blow context budgets and confuse the model.
- Persistent state crosses sessions via memory systems (mykb), while working state lives in the context window.
- RSIS3 relevance: pulses write distilled state into mykb wiki entities, making the agent's memory survivable across restarts.

## Related
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — Tool results are the main state mutations
- [[wiki/prompt-engineering/context-windows|Context Windows]] — The capacity that bounds working state
- [[wiki/prompt-engineering/token-budgets|Token Budgets]] — The policy that caps state size
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — Deciding what state the model sees
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — Persistent state flows into the wiki
