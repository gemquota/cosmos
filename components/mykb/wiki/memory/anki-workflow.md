---
type: "concept"
title: "Anki Workflow"
description: "End-to-end practice of importing, reviewing, and maintaining cards in Anki"
tags: ["memory", "anki", "workflow", "spaced-repetition"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Anki Workflow

## Summary
An Anki workflow is the end-to-end practice of turning captured knowledge into reviewable cards: importing material, converting it into well-formed prompts, reviewing daily, and maintaining the deck so the scheduler keeps teaching you what you actually forget. Anki is the operationalization of spaced retrieval for the memory layer — the schedule is the discipline.

## Details
- Typical flow: capture notes from reading or sessions, convert each atomic idea into a question-answer card, review daily (the "due" queue), then prune and revise cards that never fail or that keep failing for the wrong reason. Importing raw text wholesale without converting it into prompts produces recognition cards, not retrieval cards.
- Schedulers: the classic SM-2 algorithm sets intervals from per-card grades (again/hard/good/easy), while the modern FSRS scheduler predicts recall probability from your review history and tunes intervals per card. Both assume consistent daily review; missed days compress the schedule's effectiveness.
- Deck and add-on hygiene: use subdecks or tags to separate subjects, enable sync so reviews and edits survive device changes, and use add-ons such as the browser, image occlusion, and scheduler upgrades. Cards should reference a single fact, avoid answer-side cues, and be self-contained — a card that depends on context you have to reconstruct is a broken prompt.
- Concrete example: after reading a paper, an operator creates three cards — one for the core mechanism, one for its failure mode, one for the operational tradeoff — tags them by cluster, reviews them over successive days, and deletes the mechanism card once it has been "again" free for a year.
- Failure modes: card overload (hundreds of new cards per day) leads to buried decks and skipped reviews; copy-pasted textbook sentences test recognition, not recall; orphan cards with no source lose provenance; and sync conflicts silently drop edits when two devices review offline.
- Tradeoffs: Anki gives durable, efficient retention for facts and vocabulary, but it is poor at storing relationships and arguments — that is what a wiki is for. Use Anki for the atomic facts a loop must not forget and mykb for the structured knowledge those facts support.
- RSIS3/mykb relevance: Anki is one operationalization of spaced retrieval for the memory layer; in this wiki it pairs with flashcard design and spaced repetition so self-improvement cycles can convert stable conclusions into reviewable facts.

## Related
- [[wiki/memory/spaced-repetition-systems|Spaced Repetition Systems]] — Anki implements SM-2/FSRS
- [[wiki/memory/flashcard-design|Flashcard Design]] — quality cards in, quality memory out
- [[wiki/memory/cloze-deletion|Cloze Deletion]] — a common Anki card type
- [[wiki/memory/incremental-reading|Incremental Reading]] — Anki's reading workflow
