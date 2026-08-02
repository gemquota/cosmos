---
type: "concept"
title: "Working Memory"
description: "The small, active set of information an agent holds while reasoning"
tags: ["working-memory", "memory", "context", "cognition"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Working_memory", "https://www.ncbi.nlm.nih.gov/books/NBK545203/", "https://www.nature.com/articles/nrn3333"]
---

# Working Memory

## Summary
Working memory is the limited, immediately accessible information an agent uses during a task — in LLM terms, the current context window. It matters because it bounds how much can be considered at once. Managing it well is the core of context management.

## Details
- Capacity is limited; overflow degrades performance (cognitive load).
- Content is chosen by attention and retrieval, then held until task completion.
- RSIS3 relevance: mykb offloads overflow so working memory stays focused.
- Open questions: optimal refresh policies and compression strategies.
- Working memory is the limited-capacity system that holds and manipulates information for current tasks — the mental scratchpad.
- Its capacity is famously small (about four chunks), which is why chunking and external storage matter for complex work.
- Working memory is where comprehension happens: to understand a sentence, the reader holds its parts active long enough to integrate them.
- Cognitive load theory builds on working-memory limits to explain why instructional design either helps or overwhelms learners.
- **Worked example / comparison** — Worked example — a reader of a dense wiki article holds the definition, the mechanism, and the example in working memory; the article's structure (summary, details, related) is what makes that feasible.
- For mykb, working memory is documented as the capacity constraint that motivates the wiki's short summaries and chunked structure.

## Related
- [[wiki/llm-agents/memory-augmented-agents|Memory-Augmented Agents]]
- [[wiki/llm-agents/context-management|Context Management]]
- [[wiki/concepts/episodic-memory|Episodic Memory]]
- [[wiki/concepts/cognitive-load|Cognitive Load]]
- [[wiki/concepts/attention-mechanisms|Attention Mechanisms]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
