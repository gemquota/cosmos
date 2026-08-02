---
type: "concept"
title: "Episodic Memory for Agents"
description: "Storing and retrieving records of past agent experiences and events"
tags: ["agents", "memory", "episodic", "experience"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2307.09288", "https://arxiv.org/abs/2203.02155"]
---

# Episodic Memory for Agents

## Summary
Episodic memory for agents stores structured records of past events — what was attempted, what happened, what worked. It lets agents learn from their own history instead of starting cold each run. Episodic records are the raw material that consolidation turns into durable knowledge.

## Details
- **Record shape** — goal, context, actions, outcomes, timestamps, and success signals; enough detail to be replayed or reasoned over.
- **Retrieval** — episodes are retrieved by similarity to the current situation, by failure markers, or by entity association.
- **Uses** — avoiding repeated mistakes, reusing successful sub-plans, and providing evidence during reflection.
- **Worked example** — a support agent fails to resolve an issue; the episode is stored; next time a similar issue arrives, the retrieved episode suggests a different path.
- **Cost** — unbounded episode stores grow fast; retention policies, summarization, and deduplication keep them useful.
- **mykb relevance** — RSIS3 reflections and pulse records are episodic memory; mykb's episodic-memory concept documents the idea.

## Related
- [[wiki/llm-agents/memory-consolidation-agents|Memory Consolidation for Agents]] — distilling episodes into knowledge
- [[wiki/agent-systems/agent-memory-systems|Agent Memory Systems]] — memory systems generally
- [[wiki/llm-agents/semantic-memory-agents|Semantic Memory for Agents]] — the distilled counterpart
- [[wiki/llm-agents/memory-augmented-agents|Memory-Augmented Agents]] — memory-backed agents
- [[wiki/concepts/episodic-memory|Episodic Memory]] — the cognitive concept
- [[wiki/agent-systems/session-replay-agents|Session Replay for Agents]] — replaying recorded episodes
- [[wiki/agent-systems/agent-logs-and-audits|Agent Logs and Audits]] — episodes as audit records
- [[wiki/llm-agents/retention-policies-agents|Retention Policies for Agents]] — retention of experience
