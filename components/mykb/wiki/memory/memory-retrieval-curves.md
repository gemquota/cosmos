---
type: "concept"
title: "Memory Retrieval Curves"
description: "Curves describing how recall probability decays with time since last review"
tags: ["memory", "forgetting-curve", "retention", "spacing"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Memory Retrieval Curves

## Summary
Memory retrieval curves — forgetting curves — show recall probability falling steeply after learning, then more slowly with each successful review. They are the empirical basis for spaced-repetition scheduling and for deciding when an agent should re-surface old knowledge: the curve tells you the right moment to review before recall collapses.

## Details
- **Ebbinghaus curve** — retention decays roughly exponentially without review; the rate varies with material difficulty and prior strength. The steep initial drop is why one session of study produces so little durable memory, and why the first review must come soon after learning.
- **Review effect** — each successful retrieval flattens the curve, extending the safe interval between reviews. The flattening is not linear: successive intervals can grow while keeping recall above threshold, which is exactly the schedule SM-2 and FSRS compute from per-card history.
- **Concrete example** — a fact reviewed on day one has recall probability near 90% after a day, but 40% after a week; if the learner reviews on day two, the new curve might stay above 90% for four days, then above threshold for three weeks. The scheduler aims to trigger each review just before the curve crosses the target threshold (commonly 90%), maximizing efficiency.
- **Failure modes** — reviewing too early wastes effort (the curve was still near peak, no retrieval challenge occurred); reviewing too late means the item was already forgotten, forcing relearning; and treating the curve as universal ignores material difficulty, so fixed intervals fit nothing well.
- **Tradeoffs** — curve-based scheduling optimizes retention per unit of review time, but it assumes retrievals actually happen and are graded; it tells you *when* to review, not *how* to make the item meaningful. It also models single facts better than complex relational knowledge, which needs the context a wiki provides.
- **Agent relevance** — a temporal engine that models decay can schedule re-reads of stale wiki pages, keeping consolidated knowledge fresh: pages whose retrieval probability has decayed below threshold get re-surfaced to the consolidation loop.
- **RSIS3/mykb relevance** — retrieval curves justify the memory layer's re-surface policies: knowledge that is never revisited decays regardless of how well it was written, so the wiki's health depends on a review schedule derived from these curves.

## Related
- [[wiki/memory/spaced-repetition|Spaced Repetition]] — the scheduler that targets these curves
- [[wiki/memory/active-recall|Active Recall]] — retrieval events that flatten the curve
- [[wiki/memory/memory-consolidation|Memory Consolidation]] — the process behind curve flattening
- [[wiki/memory/just-in-time-learning|Just-in-Time Learning]] — lookup-based alternative to curve scheduling
- [[wiki/meta-learning/00-index|Meta-Learning]] — learning science that studies the curves
