---
type: "concept"
title: "Leitner System"
description: "Box-based spaced repetition using error-driven movement between review boxes"
tags: ["memory", "spaced-repetition", "flashcards"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Leitner System

## Summary
The Leitner system is the simplest family of spaced-repetition schedules: cards live in a series of boxes, a correct answer promotes a card to the next box, and a wrong answer demotes it back to box one. Because each box is reviewed at a longer interval, the system automatically makes difficult cards appear more often and easy cards less often — scheduling by outcome with almost no machinery.

## Details
- **Mechanics** — cards live in boxes; a correct answer promotes a card up, a wrong answer demotes it to box one. Each box is reviewed at a different interval — box one daily, box two every other day, box three weekly, and so on — giving a simple error-driven scheduler where the box number encodes the card's apparent difficulty.
- **Implementation** — easy to implement physically (paper boxes, index cards) or digitally, and a good mental model for SM-2/FSRS. In practice, five boxes with doubling intervals is a common configuration; the exact intervals matter less than the error-driven movement, which is the core idea.
- **Concrete example** — a learner has 100 vocabulary cards. Box one gets reviewed daily; cards answered correctly move to box two and are seen again in two days; a card missed in box three drops to box one and is seen tomorrow. Over a month, the deck self-organizes: weak cards dominate the daily queue, strong cards drift toward weekly or monthly review.
- **Failure modes** — over-promotion, where one lucky guess moves a card too far up and it is not seen again for a long time (mitigated by demoting on any error and by reviewing new cards before the first promotion); box overflow, where box one grows unbounded because too many new cards are added; and the absence of a "hard" grade — the binary correct/incorrect feedback is coarser than SM-2's four grades.
- **Trade-offs** — coarse intervals compared with per-card algorithms like FSRS; Leitner treats all cards in a box identically, so it cannot adapt interval length to a card's history the way FSRS does. Its strengths are transparency, zero-complexity implementation, and a clear visual model of what spaced repetition is doing.
- **RSIS3/mykb relevance** — the Leitner box metaphor is useful for any system that re-surfaces items by past performance: wiki pages could sit in review tiers, and the demote-on-error rule is the same error-driven signal that meta-learning loops use to reschedule failing knowledge.

## Related
- [[wiki/memory/spaced-repetition-systems|Spaced Repetition Systems]] — Leitner is the simplest family
- [[wiki/memory/flashcard-design|Flashcard Design]] — what goes in the boxes
- [[wiki/meta-learning/error-driven-learning|Error-Driven Learning]] — errors drive box demotion
- [[wiki/memory/active-recall|Active Recall]] — reviews are retrieval events
