---
type: "concept"
title: "Cognitive Load"
description: "The demand placed on working memory by a task or context"
tags: ["cognitive-load", "context", "performance", "cognition"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Cognitive_load", "https://www.ncbi.nlm.nih.gov/books/NBK447141/", "https://www.cmu.edu/teaching/principles/learning.html"]
---

# Cognitive Load

## Summary
Cognitive load is the amount of mental resources a task consumes; overload degrades judgment and recall. It matters because agent context windows have the same property: too much irrelevant information reduces performance. Managing load is context management in cognitive terms.

## Details
- Sources: task complexity, information density, and interference.
- Symptoms in agents: dropped instructions, degraded answers, repetition.
- Mitigation: summarization, retrieval, and pinning critical items.
- Open questions: measuring load in LLM context windows directly.
- Cognitive load is the total mental effort imposed on working memory by a task, split into intrinsic load (the task's inherent difficulty) and extraneous load (how the material is presented).
- Learning fails when total load exceeds working-memory capacity; good design reduces extraneous load so capacity goes to the intrinsic content.
- The germane load concept covers the effort devoted to building understanding — the load that actually produces learning.
- Measurements are indirect (self-report, performance, dual-task), but the theory's design prescriptions are widely validated.
- **Worked example / comparison** — Worked example — a wiki article with a summary, chunked details, and worked examples reduces extraneous load; a wall of undifferentiated text blows the reader's working-memory budget.
- For mykb, cognitive load theory is the design rationale for the article format rules: short summaries, structured details, and linked examples.

## Related
- [[wiki/llm-agents/context-management|Context Management]]
- [[wiki/concepts/working-memory|Working Memory]]
- [[wiki/concepts/attention-mechanisms|Attention Mechanisms]]
- [[wiki/concepts/metacognition|Metacognition]]
- [[wiki/concepts/calibration|Calibration]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
