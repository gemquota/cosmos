---
type: "synthesis"
title: "MyKB Guidance UI — from Stub Auditor to Research Direction"
description: "The Guide tab: area direction, research & feedback queue, and stub triage in one surface that steers the research and nature of mykb"
tags: ["guidance", "stub-auditor", "curation", "research-direction", "feedback", "mykb"]
timestamp: "2026-08-06T00:00:00Z"
status: "growing"
---

# MyKB Guidance UI — from Stub Auditor to Research Direction

## Summary
The stub auditor grew into the general mykb **Guide** tab
(`index.html#guidance`): one surface for (1) **area direction** — live
coverage health showing where the wiki is thinnest, (2) a **research &
feedback queue** — wanted pages, research directions, open questions, and
page-level notes with P1–P3 priority, and (3) the original **stub triage**.
The queue persists to `guidance-queue.json` and merges into the inference
manifest, so acquisition and enrichment passes are steered by human
direction rather than a mechanical stub backlog.

## Details
- **Direction data** — `build_stub_audit.py` now emits `guidance.json`:
  per-area pages / stubs / stub % / avg words, a ranked focus list (top 10
  areas by stub burden), and a snapshot of the guidance queue. Live mode
  serves `GET /api/v2/guidance`; static pages read `guidance.json`. The
  shared wiki walk (`walk_wiki`) keeps stub and coverage scans consistent.
- **Research & feedback queue** — UI kinds: wanted page, research direction,
  open question, suggestion, correction, priority, note. Persists via
  `POST /api/v2/guidance/queue` to
  `.wiki-daemon/buffers/guidance-queue.json`; static mode falls back to a
  localStorage draft plus JSON download. The floating Feedback FAB pre-fills
  the current page path.
- **Inference merge** — `drain_stub_queue.py --apply` folds the guidance
  queue into `stub-audit-inference.json` as `guidance.research`
  (wanted / direction / question tasks) and `guidance.feedback` (page-level
  notes), so the same pass that enriches stubs can seed wanted pages and
  honour corrections.
- **Backward compatibility** — `#stubs` still routes to the Guide tab;
  `/api/v2/stubs*` endpoints remain; `stub-audit.html` redirects to
  `index.html#stubs`; `cosmos stubs` remains an alias of `cosmos guidance`.
- **CLI & dashboard** — `cosmos guidance open|status|build`; the unified
  dashboard MyKB tab is relabelled **MyKB → Guidance** and embeds
  `index.html#guidance`.

## Related
- [[wiki/syntheses/guidance-execution-loop-2026-08-06|Guidance Execution Loop]] — turns the queue into scaffolds + a research manifest
- [[wiki/syntheses/stub-auditor-live-queue|Stub Auditor — Live Data & Inference Queue]]
- [[wiki/syntheses/wiki-self-improvement|Wiki Self-Improvement]] — the umbrella practice
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — curation loop norms
- [[wiki/syntheses/post-pass-consolidation|Post-Pass Consolidation]] — the ritual after each pass
- [[wiki/syntheses/graph-health-checks|Graph Health Checks]] — verification side
