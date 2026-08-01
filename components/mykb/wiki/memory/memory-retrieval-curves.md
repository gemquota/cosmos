---
type: "concept"
title: "Memory Retrieval Curves"
description: "Curves describing how recall probability decays with time since last review"
tags: ["memory", "forgetting-curve", "retention", "spacing"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Memory Retrieval Curves

## Summary
Memory retrieval curves — forgetting curves — show recall probability falling steeply after learning, then more slowly with each successful review. They are the empirical basis for spaced-repetition scheduling and for deciding when an agent should re-surface old knowledge.

## Details
- **Ebbinghaus curve** — retention decays roughly exponentially without review; the rate varies with material difficulty and prior strength.
- **Review effect** — each successful retrieval flattens the curve, extending the safe interval between reviews.
- **Agent relevance** — a temporal engine that models decay can schedule re-reads of stale wiki pages, keeping consolidated knowledge fresh.

## Related
- [[wiki/memory/spaced-repetition|Spaced Repetition]] — the scheduler that targets these curves
- [[wiki/memory/active-recall|Active Recall]] — retrieval events that flatten the curve
- [[wiki/memory/memory-consolidation|Memory Consolidation]] — the process behind curve flattening
- [[wiki/memory/just-in-time-learning|Just-in-Time Learning]] — lookup-based alternative to curve scheduling
- [[wiki/meta-learning/index|Meta-Learning]] — learning science that studies the curves
