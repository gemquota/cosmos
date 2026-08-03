---
type: "concept"
title: "Knowledge Acquisition Workflow: Open Threads"
description: "Open threads on how captures become curated concepts, sources, and syntheses"
tags: ["stub", "knowledge-acquisition", "open-questions"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Knowledge Acquisition Workflow: Open Threads

## Summary
The knowledge-acquisition workflow is the pipeline that turns raw captures into curated concepts, sources, and syntheses: capture, triage, deduplicate, link, and synthesize. The open threads concern how much of that pipeline can be automated before quality degrades, and how the triage decision — concept versus source versus question — should be made.

## Details
- **The automation boundary** — what fraction of curation can be automated (dedup, linking, summarization) before quality degrades? Deduplication and link suggestion are reliably automatable; summarization is automatable for compression but not for judgment — deciding what a note means to the system's work is the part automation cannot do well. The working split is machines for volume (detect duplicates, propose links, draft summaries) and humans or high-assurance loops for judgment (choose the claim, set the type, commit to the synthesis).
- **The triage question** — when should a capture become a concept versus a source versus a question? The rules of thumb: a stable, reusable claim becomes a concept; raw material that supports claims becomes a source; an unresolved gap becomes a question. The failure mode is premature typing — minting a concept from a single observation, or burying a durable pattern in a source page where it cannot be linked.
- **Concrete example** — a session produces three artifacts: a mechanism the session discovered (concept), the log of the session itself (source), and an effect the team could not explain (question). The pipeline types them differently, links the concept to the source for provenance, and registers the question in the open-questions index so a later session can close it.
- **The loop context** — acquisition is the front half of the knowledge-system loop; the weekly review is the ritual that catches triage errors and promotes or demotes items. Automation should be measured against the loop's outcome — can a later session find and reuse what was acquired? — not against the pipeline's throughput.
- **Failure modes** — capture that is never triaged (the inbox becomes the archive); automation that over-deduplicates and merges distinct ideas; triage by convenience rather than by the item's nature; and a pipeline that acquires but never synthesizes, so the wiki grows without any of its conclusions being committed.
- **Tradeoffs** — automation scales acquisition but flattens judgment; full manual curation preserves quality but does not scale to session volume. The balance is a two-stage design: automated first pass at capture time (typing suggestions, link candidates), curated second pass at review time (final type, links, synthesis).
- **Next step** — resolve against the knowledge-system loop and the weekly review ritual, and validate by measuring retrieval: a workflow is correct if the right artifact is findable when a later loop needs it.

## Related
- [[wiki/syntheses/knowledge-synthesis|Knowledge Synthesis]] — the terminal step of the acquisition workflow
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — the curation half of acquisition
- [[wiki/syntheses/knowledge-system|Knowledge System]] — the loop this stub asks about
- [[wiki/questions/index|Open Questions]] — where these threads are tracked
- [[wiki/syntheses/README|Syntheses]] — the namespace this stub belongs to
