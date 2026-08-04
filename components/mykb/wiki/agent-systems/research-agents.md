---
type: "concept"
title: "Research Agents"
description: "Agents that gather, synthesize, and cite information across many sources"
tags: ["research-agents", "research", "agents", "synthesis"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Research Agents

## Summary
Research agents gather information across many sources, synthesize it, and cite what they found. They matter because open-ended questions cannot be answered from a single retrieval call, and unsourced answers are dangerously unreliable. The core engineering problem is keeping synthesis grounded in verified sources. The research loop's value comes from questioning sources, not just collecting them.

## Details
- **Definition** — a research agent plans queries, retrieves or browses sources, evaluates their reliability, and produces a cited synthesis.
- **Loop structure** — research is iterative: ask, retrieve, evaluate, refine the question, and repeat until the evidence is sufficient.
- **Grounding** — claims must be tied to specific sources via citations-and-provenance so readers can verify and so hallucination can be caught.
- **Reliability** — source quality varies, so agents must weigh authoritative sources and flag contradictions rather than blending them blindly.
- **Variants** — multi-hop retrieval chains, agentic-rag loops, and human-in-the-loop research assistants differ in how much autonomy they have.
- **Worked example** — a product team asks why churn rose; the agent pulls support tickets, analytics notes, and release history, then drafts a cited briefing on likely causes.
- **Failure modes** — circular citations, stale sources, and confirmation bias are the classic failure modes; source timestamps and diversity checks help.
- **Evaluation** — research quality is judged on citation correctness, coverage, and the absence of invented facts, often via rubric-based evaluation.
- **Practical relevance** — research agents are the gathering half of knowledge systems like MyKB, feeding summarization and synthesis stages.
- **Source scoring** — agents should weigh authority, recency, and corroboration when combining evidence.
- **Contradiction handling** — conflicting sources should be surfaced as open questions rather than averaged away.
- **Cost control** — retrieval budgets and step limits prevent open-ended research from running away.
- **Failure example** — an agent that cites a forum post as authoritative produces a confident but unreliable answer.

## Related
- [[wiki/ai-ml/multi-hop-retrieval|Multi-Hop Retrieval]] — chaining retrieval across sources
- [[wiki/ai-ml/citations-and-provenance|Citations and Provenance]] — the citation layer
- [[wiki/ai-ml/grounded-generation|Grounded Generation]] — keeping output tied to evidence
- [[wiki/ai-ml/agentic-rag|Agentic RAG]] — retrieval as an agent loop
- [[wiki/agent-systems/summarization-agents|Summarization Agents]] — the synthesis skill research depends on
