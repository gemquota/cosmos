---
type: "concept"
title: "Spaced Repetition"
description: "Learning technique that schedules reviews at expanding intervals to maximize long-term retention"
tags: ["memory", "learning", "spaced-repetition", "scheduling", "retention"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Spaced_repetition"]
---

# Spaced Repetition

## Summary
Spaced repetition schedules reviews of an item just before it would be forgotten, using expanding intervals driven by each answer's difficulty. It exploits the spacing effect and the testing effect to make retention dramatically more efficient than cramming. For agents, the same idea applies to re-reviewing memories so old knowledge stays retrievable.

## Details
- **Mechanism** — each review grades difficulty (again/hard/good/easy); the algorithm grows or shrinks the interval accordingly (SM-2, FSRS, Leitner boxes).
- **Spacing effect** — distributed practice beats massed practice for long-term retention; the effect is among the most replicated findings in cognitive psychology.
- **Worked example** — a note 'BM25 parameters: k1, b' is reviewed after 1 day, 3 days, 8 days, then 21 days; failure resets the interval and strengthens encoding.
- **Comparison table** — Leitner (simple boxes) vs SM-2 (per-item intervals, Anki) vs FSRS (predictive, free-spaced repetition).
- **Agent relevance** — a temporal engine can resurface stale memories on a decaying schedule, mirroring spaced review for knowledge consolidation.

## Related
- [[wiki/memory/active-recall|Active Recall]] — the retrieval practice spaced repetition schedules
- [[wiki/memory/memory-retrieval-curves|Memory Retrieval Curves]] — the forgetting curve spaced repetition flattens
- [[wiki/memory/memory-consolidation|Memory Consolidation]] — the offline process repetition supports
- [[wiki/memory/just-in-time-learning|Just-in-Time Learning]] — an alternative to scheduled review
- [[wiki/memory/personal-knowledge-management|Personal Knowledge Management]] — the practice spaced repetition serves
- [[wiki/memory/README|Memory Layer]] — where scheduled re-reviews would surface memories
- [[wiki/meta-learning/00-index|Meta-Learning]] — learning-to-learn patterns that use spacing
