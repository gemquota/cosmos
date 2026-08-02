---
type: "concept"
title: "Agentic Memory Hierarchy"
description: "Layering working, episodic, semantic, and procedural memory for agents"
tags: ["memory", "agents", "architecture", "hierarchy"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2307.09288", "https://arxiv.org/abs/2210.03629"]
---

# Agentic Memory Hierarchy

## Summary
The agentic memory hierarchy organizes agent memory by timescale and abstraction: fast working memory, recorded episodic memory, distilled semantic memory, and learned procedural skills. Each layer serves a different retrieval need. Designers trade off recall latency, storage cost, and consolidation effort across the layers.

## Details
- **Working memory** — the active context window; fast but small, managed by summarization and pruning.
- **Episodic memory** — records of past runs and events; retrieved to avoid repeating mistakes and to ground decisions.
- **Semantic memory** — distilled facts and concepts, often in a vector store or knowledge graph; the layer mykb embodies.
- **Procedural memory** — skills and workflows, encoded as prompts, code, or fine-tuned behavior.
- **Worked example** — a coding agent keeps the current diff in working memory, recalls a similar past fix from episodic memory, checks project conventions from semantic memory, and applies a learned patch procedure.
- **mykb relevance** — the triad architecture (RSIS3 + mykb + myrsikb) is a concrete instantiation of this hierarchy.

## Related
- [[wiki/llm-agents/memory-augmented-agents|Memory-Augmented Agents]] — memory as an augmentation
- [[wiki/concepts/memory-hierarchy|Memory Hierarchy]] — the cognitive hierarchy concept
- [[wiki/prompt-engineering/context-window-management|Context Window Management]] — working memory limits
- [[wiki/concepts/knowledge-graph-memory|Knowledge-Graph Memory]] — graph-based semantic memory
- [[wiki/llm-agents/conversation-history-management|Conversation History Management]] — related concept in this cluster
- [[wiki/llm-agents/dialog-state-tracking|Dialog State Tracking]] — related concept in this cluster
- [[wiki/concepts/semantic-memory|Semantic Memory]] — memory type it builds on
- [[wiki/concepts/episodic-memory|Episodic Memory]] — memory type it builds on
