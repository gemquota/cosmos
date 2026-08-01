---
type: "concept"
title: "Identity and Continuity"
description: "Stable self-model and persistent memory that let an agent be the same entity across sessions"
tags: ["identity", "continuity", "memory", "self-model", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2304.03442"]
---

# Identity and Continuity

## Summary
Identity and continuity are what make an agent recognizably the same entity from one session to the next: a stable self-model, persistent goals, and memory that carries over. This matters because agents that forget who they are and what they decided cannot accumulate trust or improvement. Generative agents show the pattern of believable, memory-driven continuity; RSIS3 persists identity snapshots and a genesis hash.

## Details
- **Identity snapshot**: goals, constraints, version, and history are stored and reloaded each session.
- **Genesis hash**: RSIS3's self-model hash lets the system verify it is still running the intended lineage.
- **Continuity through memory**: episodic records let the agent answer 'what did we decide and why'.
- **Persona** is the surface layer of identity; the deep layer is policy and history.
- Continuity also implies change control: identity updates are versioned, not silent.
- Worked example: a long-running wiki agent remembers its curation rules and past decisions across restarts.

## Related

- [[wiki/llm-agents/agent-personas|Agent Personas]] — the surface expression of identity
- [[wiki/concepts/episodic-memory|Episodic Memory]] — event records that provide continuity
- [[wiki/concepts/semantic-memory|Semantic Memory]] — facts that persist across sessions
- [[wiki/llm-agents/agent-versioning|Agent Versioning]] — versioned identity changes
- [[wiki/concepts/mykb-analysis|Mykb Analysis]] — analysis of identity and memory records
- [[wiki/ops/gap-report|Gap Analysis Report]] — continuity gaps in the record
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]] — how the memory and identity layer was built