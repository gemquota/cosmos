---
type: "concept"
title: "Knowledge Capture"
description: "The act of getting external information into a knowledge system while it is still fresh"
tags: ["capture", "inbox", "workflow", "knowledge"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Knowledge Capture

## Summary
Knowledge capture is the front end of every knowledge loop: turning an experience, reading, or conversation into a durable record. Good capture lowers friction so nothing valuable is lost; bad capture produces an unsearchable pile. The test of capture is not whether something was recorded — it is whether the record can be found and used later.

## Details
- **Design** — a low-friction inbox (drop anything, tag lightly, move on); processing happens later, not at capture time. Capture and curation are deliberately separate: interrupting the capture moment to organize defeats the purpose, so the inbox must tolerate mess and the processing pass must be scheduled.
- **Modes** — manual (notes, clippings), automated (session logs, telemetry, browser extensions), and agent-assisted (LLM extraction). Each mode has its own failure profile: manual capture depends on discipline, automated capture generates noise, and extraction can hallucinate or flatten nuance.
- **Concrete example** — a debugging session produces a root cause, a workaround, and three false leads. The session log captures everything; the curation pass later promotes the root cause to a concept page, links the workaround as a related note, and discards the false leads — the capture was complete, the curation made it usable.
- **Failure modes** — capture without provenance, so a record cannot be traced to its source; capture without processing, so the inbox becomes the archive and search degrades; capture that strips context ("fixed the bug" with no details); and the opposite failure of over-processing at capture time, which causes people to skip capture entirely.
- **Tradeoffs** — capture everything is cheap in the moment but expensive to curate; capture only what matters saves curation but risks losing the unexpected. The robust answer is cheap full capture plus a separate triage step, with provenance attached at the moment of capture where it is still known.
- **Agent relevance** — RSIS3's session capture hooks would write pulses and decisions into mykb automatically; capture is where the wiki's raw material originates, so capture quality sets an upper bound on everything the memory layer can later retrieve.
- **RSIS3/mykb relevance** — the standing practice of consolidating significant sessions into syntheses depends on capture having recorded the session faithfully; capture is the encoding step that memory consolidation later builds on.

## Related
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — what happens after capture: triage and connect
- [[wiki/memory/memory-consolidation|Memory Consolidation]] — capture is the encoding before consolidation
- [[wiki/memory/note-taking-methods|Note-Taking Methods]] — human capture techniques
- [[wiki/memory/provenance|Provenance]] — capture should record where each item came from
- [[wiki/sources/index|Sources]] — the namespace where raw captures land
