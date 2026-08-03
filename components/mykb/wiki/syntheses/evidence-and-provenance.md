---
type: "concept"
title: "Evidence and Provenance: Open Threads"
description: "Open threads on claims, sources, and version history so syntheses stay auditable"
tags: ["stub", "provenance", "evidence", "open-questions"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Evidence and Provenance: Open Threads

## Summary
Evidence and provenance is the discipline of keeping synthesized conclusions auditable: every claim should trace to a source, every source to a version, and every version to a moment in history. The core difficulty is that knowledge bases change — sources are edited, pages are deleted, models update — so the question is not whether to record provenance but how it should degrade gracefully when the thing it points to moves.

## Details
- **The degradation problem** — how should provenance degrade when a source page is edited or deleted? A claim pinned to a deleted page becomes an orphan; a claim pinned to an edited page silently starts meaning something different. The design options are to snapshot quoted material at citation time, to flag dangling provenance during the weekly review, or to treat a claim as provisional once its source changes.
- **Version pinning** — which claims are important enough to pin to a specific source version? Not every sentence needs a version anchor; the rule of thumb is to pin load-bearing claims — those that appear in syntheses or drive decisions — while letting background context float. Pinning everything creates maintenance debt; pinning nothing creates silent drift.
- **Concrete example** — a synthesis claims "the retry policy caps at five attempts" citing a source page; an update later changes the cap to three. With provenance that stores the cited version or the quoted text, the synthesis still reads true historically and the review finds the mismatch; without it, the synthesis now describes a policy that no longer exists and no one notices.
- **Mechanism** — provenance fields should record at minimum: source reference (which page or record), retrieval date, version or commit, and the quoted claim. Where the corpus is versioned with git, the version field can be the commit; where it is not, a timestamp plus snapshot of the claim is the fallback.
- **Failure modes** — provenance that points at a page, not a version, so edits silently invalidate conclusions; provenance attached only to whole documents, not to the specific claim, so a true claim and a false one in the same page share an anchor; and provenance that exists in the data model but is never checked, which is indistinguishable from no provenance.
- **Tradeoffs** — deep provenance (snapshots, version pins, verification jobs) is expensive to maintain and can overconstrain the corpus; shallow provenance is cheap but rots. The working balance is layered: cheap provenance at capture (source + date), version pins only for load-bearing claims, and a review ritual that detects and repairs drift.
- **Next step** — design the provenance fields and review them against data-versioning practice; the design should be validated by asking, for every field, what happens to a claim when this field is wrong or missing.

## Related
- [[wiki/syntheses/knowledge-synthesis|Knowledge Synthesis]] — synthesized claims are what provenance protects
- [[wiki/memory/provenance|Provenance]] — the thread this stub continues
- [[wiki/syntheses/weekly-review|Weekly Review]] — the ritual that should re-check evidence
- [[wiki/sources/README|Sources]] — the namespace holding evidence
- [[wiki/questions/index|Open Questions]] — where these threads are tracked
