---
type: "concept"
title: "Checkpointing Agent Runs"
description: "Persisting agent state at milestones so runs can pause, resume, or roll back"
tags: ["agents", "checkpoints", "resume", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://github.com/langchain-ai/langgraph", "https://arxiv.org/abs/2307.09288"]
---

# Checkpointing Agent Runs

## Summary
Checkpointing saves the full state of an agent run — context, plan position, tool results, and variables — at defined milestones. Checkpoints enable pause-and-resume, rollback on failure, and safe interruption. They are the durability layer for long-running agents.

## Details
- **What to persist** — serialized state machine, message history or its summary, plan state, and any local artifacts.
- **Checkpoint strategies** — at every step (fine-grained, expensive), at milestones, or before risky actions.
- **Uses** — resume after crash, replay for debugging, fork a run for experiments, and rollback after a bad action.
- **Worked example** — a migration agent checkpoints before applying each schema change; on failure it restores the last checkpoint and replans.
- **Costs** — storage growth and serialization latency; summaries and differential checkpoints keep this manageable.
- **mykb relevance** — checkpoint-rollback is an existing mykb concept, and RSIS3 commits state at checkpoints for the same reasons.
- **What to store** — full agent state (context, tool results, step index) plus the version IDs of prompts and models, so a resume is bit-identical.
- **Cost** — checkpoint size grows with context; periodic and event-triggered checkpoints balance overhead against recovery granularity.

- **Checkpoint hygiene** — checkpoints must be restorable and tested: a checkpoint that cannot restore is worse than none, so recovery drills are part of the routine.
- **Version coupling** — prompts and model versions are stored with the checkpoint, because resuming with different versions is not a bit-identical resume.
## Related
- [[wiki/concepts/checkpoint-rollback|Checkpoint & Rollback]] — the checkpoint-rollback concept
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — restoring from checkpoints
- [[wiki/agent-systems/idempotent-agent-actions|Idempotent Agent Actions]] — idempotency makes resume safe
- [[wiki/agent-systems/session-state-machine|Session State Machine]] — session-level checkpoints
- [[wiki/agent-systems/session-replay-agents|Session Replay for Agents]] — related concept in this cluster
- [[wiki/agent-systems/agent-cancellation|Agent Cancellation]] — related concept in this cluster
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
- [[wiki/memory/memory-consolidation|Memory Consolidation]] — memory consolidation research
