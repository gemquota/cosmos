---
type: "concept"
title: "Memory-Augmented Agents"
description: "Agents with persistent, tiered memory beyond a single context window"
tags: ["memory", "agents", "llm", "context", "mykb"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2310.08560"]
---

# Memory-Augmented Agents

## Summary
Memory-augmented agents keep state that survives the end of a turn: what was decided, what was learned, what the user prefers. This matters because a model context window is ephemeral and bounded, while real work spans hours and sessions. MemGPT formalizes the pattern by paging information between a small working context and larger external storage; mykb is RSIS3's persistent memory layer in exactly this role.

## Details
- **Memory tiers**: working memory (context), episodic memory (event records), and semantic memory (facts and abstractions).
- **Write path**: after each session, important facts and decisions are distilled into the wiki; the graph engine links them.
- **Read path**: before planning, retrieval pulls relevant memories into context (TF-IDF, embeddings, backlinks).
- **Forgetting**: temporal decay and consolidation keep the store from drowning in noise.
- RSIS3 delegates memory to mykb: pulses become episodic notes, analyses become concept pages.
- Worked example: a month-old decision about architecture is retrieved during a new session and prevents re-litigating it.

## Related

- [[wiki/concepts/working-memory|Working Memory]] — the active context tier
- [[wiki/concepts/episodic-memory|Episodic Memory]] — records of events and sessions
- [[wiki/concepts/semantic-memory|Semantic Memory]] — facts and abstractions
- [[wiki/llm-agents/rag-agent|RAG Agent]] — retrieval as the read mechanism
- [[wiki/concepts/mykb-analysis|Mykb Analysis]] — analysis of the memory layer
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]] — how the memory layer was built
- [[wiki/concepts/mykb-research-report|Mykb Research Report]] — research behind personal LLM memory