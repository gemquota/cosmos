---
type: "concept"
title: "Agentic RAG"
description: "Retrieval-augmented generation where an agent decides when, what, and how often to retrieve"
tags: ["rag", "agents", "retrieval"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Agentic RAG

## Summary
Agentic RAG is retrieval-augmented generation in which an agent controls the retrieval loop: it decides when to retrieve, what to search for, which tools to call, and whether to iterate. Unlike one-shot RAG, which retrieves a fixed set of chunks and generates once, agentic RAG treats retrieval as a sequence of decisions interleaved with reasoning.

## Details
- **When to retrieve** — the agent may retrieve zero, one, or many times depending on whether the current context suffices; need-based gating avoids paying retrieval cost for every query.
- **What to retrieve** — query rewriting and decomposition let the agent search for different facets of a question instead of issuing one ambiguous query.
- **Tool surface** — retrieval is exposed as a tool (vector search, web search, database lookup) alongside other tools, so the agent composes it with computation or API calls.
- **Iteration** — retrieved context can trigger follow-up searches, answer drafts, or verification steps; the loop continues until the agent judges the answer complete.
- **Strengths** — multi-hop and ambiguous queries improve because the agent can gather evidence piecewise and reconcile contradictions.
- **Costs** — planning and repeated tool calls add latency, token spend, and failure modes (runaway loops), so budget, timeouts, and a stopping policy are required.
- **Relationship to the RAG family** — it extends classic retrieval-augmented generation with the planning-and-tool-use machinery of agent systems, and it overlaps with retrieval prompting at the prompt level.
- **Evaluation** — measure both retrieval quality (hit rate, faithfulness) and agent behavior (number of retrievals, loop termination, cost per answer), not just final-answer accuracy.

- **Architecture shapes** — a ReAct-style loop interleaves thought, retrieval, and answer drafts; a plan-then-execute agent can pre-decompose the query into retrievals before generating; both keep the retrieval budget explicit.
## Related
- [[wiki/data-storage/retrieval-augmented-generation|Retrieval-Augmented Generation]] — baseline pattern it extends
- [[wiki/prompt-engineering/retrieval-prompting|Retrieval Prompting]] — prompt-level retrieval control
- [[wiki/llm-agents/tool-use-function-calling|Tool Use and Function Calling]] — retrieval as a tool
- [[wiki/data-storage/vector-databases|Vector Databases]] — the retrieval store
- [[wiki/ai-ml/reranking-strategies|Reranking Strategies]] — post-retrieval precision
- [[wiki/ai-ml/rag-benchmarks|RAG Benchmarks]] — measuring the pipeline
