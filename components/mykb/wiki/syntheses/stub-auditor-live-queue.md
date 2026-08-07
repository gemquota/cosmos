---
type: "synthesis"
title: "Stub Auditor — Live Data & Inference Queue"
description: "A live, human-in-the-loop stub triage that queues decisions for a batched inference pass"
tags: ["stub-auditor", "curation", "inference-pass", "workflow", "mykb"]
timestamp: "2026-08-05T00:00:00Z"
status: "growing"
---

# Stub Auditor — Live Data & Inference Queue

## Summary
Stub triage is a two-phase pipeline: a human reviews the current stub set in
the Stub Auditor SPA, and the decisions are queued to a file that a later
inference pass consumes. Live scans come from the wiki daemon, not a baked
snapshot, so the review always starts from the current wiki state.

## Details
- **Live data** — `GET /api/v2/stubs` reuses `build_stub_audit.scan_stubs()`
  so the SPA and the static build share one source of truth. A HEAD-keyed
  cache of first-commit dates keeps the live scan fast (git log runs once per
  HEAD, not per request).
- **Queue file** — `Save queue` POSTs to `/api/v2/stubs/queue`, which writes
  `.wiki-daemon/buffers/stub-audit-queue.json` (atomically via temp+rename).
  Opened statically, the SPA falls back to downloading the same JSON.
- **Inference handoff** — `drain_stub_queue.py --apply` executes the
  mechanical decisions (categorize/archive/delete via `git mv`/`git rm` with
  filesystem fallback for untracked files) and emits
  `.wiki-daemon/buffers/stub-audit-inference.json` for `enrich` items: each
  task carries the path, metadata, and opening snippet so workers expand past
  the 320-word floor without re-scanning.
- **Rules** — decisions are keyed by wiki-relative path so progress survives
  data-source switches; `--plan` is the default and mutates nothing; missing
  files are reported, never silently skipped.

## Related
- [[wiki/syntheses/guidance-ui-2026-08-06|MyKB Guidance UI]] — the stub auditor's successor as the general guidance surface
- [[wiki/syntheses/wiki-self-improvement|Wiki Self-Improvement]] — the umbrella practice
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — curation loop norms
- [[wiki/syntheses/post-pass-consolidation|Post-Pass Consolidation]] — the ritual after each pass
- [[wiki/syntheses/graph-health-checks|Graph Health Checks]] — verification side
- [[wiki/syntheses/parallel-agent-acquisition|Parallel Agent Acquisition]] — the fan-out shape the inference pass uses
