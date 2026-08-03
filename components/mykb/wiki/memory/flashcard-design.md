---
type: "concept"
title: "Flashcard Design"
description: "Principles for writing flashcards that trigger retrieval instead of recognition"
tags: ["memory", "flashcards", "retrieval-practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Flashcard Design

## Summary
Flashcard design is the craft of writing prompts that trigger retrieval instead of recognition: each card tests one specific fact, gives no answer-side cues, and is hard enough to strengthen the memory but fair enough to answer from what you know. A well-designed card is a tiny retrieval-practice event; a poorly designed one is a puzzle or a triviality.

## Details
- Cards should be atomic: one prompt, one answer, no compound questions. "What are the failure modes of X?" is not one card — it is a list that lets recognition of the first item stand in for recall of the rest. Split it into one card per failure mode.
- Avoid cloze overuse and answer-side cues that let recognition replace recall. A cloze card "_____ is the process of ..." can be answered by pattern-matching the sentence; a question card "What process converts X into Y?" forces generation of the term from the concept.
- Design for the failure mode: a card that is too easy teaches nothing, too hard discourages review. Calibrate difficulty to your actual error rate: if a card never fails, it is either too easy or not worth keeping; if it always fails, it is too broad or the material is not yet learned.
- Good prompts are specific enough to test the exact fact, general enough to transfer. "What does RoCE assume about the fabric?" tests a claim; "Tell me about RoCE" tests nothing.
- Concrete example — bad: "What are the 3-2-1 backup rule and its variants?" Good: "In the 3-2-1 rule, what does the '2' refer to?" (two media types) and separately "Why does the offsite copy resist ransomware?" (it is physically offline).
- Failure modes — answer-side cues embedded in the prompt's phrasing; cards whose questions are visible in the deck name or neighboring cards; and cards that drift from their source so the answer becomes wrong without anyone noticing, which is why provenance links matter.
- Tradeoffs — hand-written cards are higher quality but slower to produce; auto-generated cards scale but frequently test trivia or leak answers. The sustainable path is a hybrid: auto-suggest candidates, then curate by hand.
- RSIS3/mykb relevance — flashcards are the canonical tool of retrieval practice; in the memory layer they pair with Anki so stable facts from syntheses can become reviewable prompts.

## Related
- [[wiki/memory/retrieval-practice|Retrieval Practice]] — flashcards are its canonical tool
- [[wiki/memory/anki-workflow|Anki Workflow]] — the scheduler cards feed
- [[wiki/memory/card-design-practice|Card Design Practice]] — deep-dive on card anatomy
- [[wiki/memory/active-recall|Active Recall]] — the mechanism cards exploit
- [[wiki/memory/spaced-repetition|Spaced Repetition]] — the schedule cards follow
