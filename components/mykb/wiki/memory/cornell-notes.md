---
type: "concept"
title: "Cornell Notes"
description: "Two-column note format with a cue column, note area, and summary row for active review"
tags: ["note-taking", "cornell", "study", "retrieval"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Cornell Notes

## Summary
Cornell Notes split each page into a narrow cue column, a wide note area, and a bottom summary band. The cue column doubles as a self-test prompt, turning passive notes into an active-recall device: cover the note area, answer the cues, then verify. It is one of the few note formats that builds retrieval practice into the page layout itself.

## Details
- **Layout** — main notes on the right (lectures, readings, sessions); questions/keywords on the left; a one-paragraph summary at the bottom written in your own words. The cue column is populated after the fact, ideally by converting each chunk of the note area into a question the chunk answers.
- **Review loop** — cover the notes, answer the cues, verify; this is active recall embedded in the format. A second pass can grade cue-answer pairs and promote the ones that fail into flashcards, connecting Cornell notes to spaced-repetition practice.
- **Concrete example** — a study session on TCP congestion control yields note-area chunks ("slow start doubles cwnd each RTT until ssthresh") with cues ("What does slow start do to cwnd? When does it stop?"), and the summary band states the mechanism in one sentence; a week later, the cue column alone reproduces the whole page.
- **Failure modes** — writing cues that are mere labels ("slow start") rather than questions, so review becomes recognition; skipping the summary band, which is where the material gets compressed into a transferable claim; and treating the layout as a transcription format instead of a retrieval scaffold.
- **Tradeoffs** — the structure is rigid and page-oriented, which suits lectures and readings but fights freeform idea capture; the payoff is a built-in review mechanism that unstructured notes lack. For wikis, the cue-answer shape maps naturally onto atomic notes and flashcards.
- **Agent relevance** — a summary band plus cue field maps to mykb's `summary` plus `description` frontmatter: both force distillation at capture time, so a page's frontmatter is already the cue and the body is the note area.
- **RSIS3/mykb relevance** — capture hooks that emit wiki pages can adopt the Cornell discipline: record the raw detail, then write the cue and the summary immediately, so retrieval quality is decided at write time.

## Related
- [[wiki/memory/note-taking-methods|Note-Taking Methods]] — Cornell is one structured capture method
- [[wiki/memory/active-recall|Active Recall]] — the cue column exists for retrieval practice
- [[wiki/memory/mind-mapping|Mind Mapping]] — a visual alternative layout
- [[wiki/reflections/00-index|Reflections]] — retrospective summaries share the cue-answer shape
