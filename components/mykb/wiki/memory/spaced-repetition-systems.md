---
type: "concept"
title: "Spaced Repetition Systems"
description: "Schedulers that time reviews at expanding intervals to combat forgetting"
tags: ["spaced-repetition", "scheduling", "retention"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Spaced_repetition", "https://super-memory.com/english/ol/sm2.htm"]
---

# Spaced Repetition Systems

## Summary

Spaced Repetition Systems — Schedulers that time reviews at expanding intervals to combat forgetting.

## Details

- Spaced repetition systems (SRS) schedule reviews of individual items at expanding intervals, timing each review just before the item is likely to be forgotten. The family ranges from Leitner boxes to per-item algorithms like SM-2 and FSRS.
- SM-2 (SuperMemo's 1987 algorithm) grades each card and multiplies or resets the interval based on quality; Anki popularized it. FSRS is a modern free-spaced-repetition predictor that fits a forgetting model to each learner's history. Leitner boxes offer a simple error-driven version with fixed box intervals.
- Worked example: a card answered 'easy' on day 1 might reappear day 4, then day 10, then day 25; an 'again' grade resets it to day 1. The schedule adapts to actual retention.
- Research support: spaced review reliably increases long-term retention versus massed review across materials and learners. The systems operationalize the spacing effect and the testing effect at scale.
- mykb relevance: the memory layer's scheduled re-review of notes mirrors SRS; intervals could be driven by the same item history and success data.

## Related

- [[wiki/memory/forgetting-curve|Forgetting Curve]] — the curve schedulers flatten
- [[wiki/memory/retrieval-practice|Retrieval Practice]] — the event being scheduled
- [[wiki/memory/leitner-system|Leitner System]] — simplest scheduler
- [[wiki/memory/anki-workflow|Anki Workflow]] — popular implementation
- [[wiki/memory/spacing-effect|Spacing Effect]] — empirical basis
- [[wiki/memory/flashcard-design|Flashcard Design]] — item quality
- [[wiki/memory/spaced-repetition|Spaced Repetition]] — existing wiki article
- [[wiki/agent-systems/agent-planning-systems|Agent Planning Systems]] — existing wiki article
