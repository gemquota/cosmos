---
type: "concept"
title: "Just-in-Time Learning"
description: "Learning a skill or fact exactly when a task requires it rather than in advance"
tags: ["learning", "workflow", "performance", "pkm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Just-in-Time Learning

## Summary
Just-in-time learning delays study until the moment of need: look up the API, technique, or fact while doing the task, apply it immediately, and retain the part that worked. It optimizes for throughput over scheduled mastery — you learn what the task actually demands, right when the task demands it.

## Details
- **Trade-off** — immediate relevance and low overhead vs shallow, context-dependent retention; complements rather than replaces deliberate practice. Facts learned only in context are recalled mainly in that context, which is why just-in-time learning must be paired with a system that re-surfaces the same fact later (spaced repetition or wiki retrieval).
- **Pattern** — task → search → apply → save the worked snippet for the next occurrence. The critical step is the last one: without writing back what worked, the knowledge dies with the task and the next occurrence starts from zero.
- **Concrete example** — an operator needs to resize a filesystem; instead of studying storage administration in advance, they retrieve the resize procedure from the wiki, execute it, hit one failure mode (an in-use partition), search again for the unmount workaround, and append the workaround to the wiki page with a note about when it applies.
- **Failure modes** — search failure at the moment of need (the knowledge was never captured, so there is nothing to retrieve — the wiki only helps if the capture loop ran earlier); context-switching cost that makes the lookup slower than guessing; and the "just-in-case" inversion where a system captures so much that nothing is findable quickly.
- **Tradeoffs** — just-in-time beats scheduled learning for infrequent, practical tasks and for anything that changes (APIs, tool versions); scheduled learning wins for foundational material that every task builds on. The two are complements: scheduled practice builds the base, just-in-time covers the long tail.
- **Agent relevance** — RSIS3 already learns just-in-time: it retrieves relevant wiki context when a pulse needs it, then writes back what worked. The write-back step is what upgrades the agent from a searcher to a learner.
- **RSIS3/mykb relevance** — the wiki's role in just-in-time learning is to make capture cheap and retrieval fast; every search that ends in "not found" is a signal to add a page, and every search that succeeds is a validation of the capture loop.

## Related
- [[wiki/meta-learning/curriculum-learning|Curriculum Learning]] — the scheduled opposite of just-in-time
- [[wiki/memory/spaced-repetition|Spaced Repetition]] — scheduled review vs on-demand lookup
- [[wiki/memory/active-recall|Active Recall]] — retrieval practice vs retrieval from a search engine
- [[wiki/memory/personal-knowledge-management|Personal Knowledge Management]] — a PKM that supports lookup on demand
- [[wiki/questions/index|Open Questions]] — questions that trigger just-in-time research
