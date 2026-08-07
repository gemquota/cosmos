---
type: "synthesis"
title: "Stub Audit Pass 2026-08-06 — 141 Reviewed, 3 Archived, 126 Enriched"
description: "Full 141-item stub-audit pass: 3 pages archived with retarget policy, all 126 queued stubs enriched past the 320-word floor, and the auditor UI fixed"
tags: ["stub-auditor", "archive", "retarget", "inference-pass", "mykb"]
timestamp: "2026-08-06T00:00:00Z"
status: "stable"
source: []
---

# Stub Audit Pass 2026-08-06 — 141 Reviewed, 3 Archived, 126 Enriched

## Summary
The Stub Auditor reviewed 141 of 4267 wiki files. Twelve were kept as-is,
three agent-systems pages were archived to `raw/archive/stub-audit-2026-08-06/`,
and all 126 queued stubs (108 agent-systems, 16 ai-ml, 2 testing) were
enriched past the 320-word floor and promoted from `stub` to `growing`.
This pass settled the archive mechanics, the inbound-link policy for
archived pages, and the end-to-end queue → drain → manifest → enrichment →
reindex pipeline, and fixed the auditor's inference UI.

## Details
- **Archive convention** — move with `git mv wiki/<area>/<file>.md
  raw/archive/stub-audit-YYYY-MM-DD/<area>/<file>.md`; the destination
  directory must be created first (`git mv` will not create parents). Archived
  pages keep their frontmatter and are excluded from the stub scan because the
  scan walks `wiki/` only.
- **Inbound-link policy (archives)** — retarget every wikilink to the nearest
  living canonical page instead of linking into `raw/`:
  - `planning-systems` → `agent-planning-systems`
  - `honest-signaling` → `signaling-ai` (or `honest-ai` when the source page
    is `signaling-ai` itself, to avoid self-links)
  - `instruction-following` → `instruction-hierarchy`, except in
    `instruction-hierarchy`/`instruction-robustness` (self-link risk) where it
    goes to `instruction-following-benchmarks`
  - Drop the archived page's entries from the area `00-index.md` (both the
    curated wikilink section and the generated markdown listing); strip junk
    auto-added `— note` links rather than retargeting them.
- **Pipeline** — decisions are written to
  `.wiki-daemon/buffers/stub-audit-queue.json` (SPA schema: `path` prefixed
  `wiki/`, `decision` in k/e/c/a/d), then `drain_stub_queue.py --plan` /
  `--apply` writes `.wiki-daemon/buffers/stub-audit-inference.json` for the
  enrichment pass.
- **Tooling note** — `drain_stub_queue.py` archives to
  `raw/archive/stub-audit-<date>/wiki/<...>` (keeps the `wiki/` prefix), which
  differs from the report convention. Execute archive moves from the report
  manually and keep archive items out of the queue before `--apply`, or the
  double-move falls back to a filesystem rename and crashes.
- **Enrichment completed (126/126)** — all 126 queued stubs expanded past
  the 320-word floor (range 320-370 body words), status bumped stub→growing,
  following the Summary/Details/Related structure with 2-8 resolvable related
  wikilinks per page. No links point at the three archived pages; self-links
  were removed (notably the `queue-management`, `instruction-hierarchy`, and
  `agent-planning-systems` self-links).
- **Auditor UI fixed (not removed)** — `stub_audit_template.html` static-mode
  fallbacks now print copyable terminal commands (`cosmos stubs open|build|
  plan|apply|status`) instead of dead buttons, and the header/status text
  explains when the live API is unavailable. `server.py` exposes
  `POST /api/v2/stubs/queue/plan|apply` and `/api/v2/stubs/build`;
  `cli/cosmos` exposes the matching `stubs` subcommands. Verified live with
  curl against a test server.
- **Verification (final)** — manifest check clean for all 126 tasks:
  no sub-320 bodies, no broken wikilinks, no `stub` statuses remaining.
  Bundle-wide link check over all 169 changed wiki files shows only
  illustrative template links in `log.md` (e.g. ``{page}`area}/{page}]]`).
  Graph rebuilt 5,397 nodes / 35,540 edges; `files.json` 6,856 entries
  (`--check` OK); stub index 3,348 → 3,220; auditor lists 4,264 → 4,138 stubs.

## Related
- [[wiki/syntheses/stub-auditor-live-queue|Stub Auditor — Live Data & Inference Queue]] — the pipeline this pass ran
- [[wiki/syntheses/stub-expansion-pass-500-2026-08|500-Stub Expansion Pass]] — prior bulk enrichment
- [[wiki/syntheses/wiki-link-resolution-and-junk-audit|Wiki Link Resolution & Junk-Entity Audit]] — link hygiene
- [[wiki/syntheses/post-pass-consolidation|Post-Pass Consolidation]] — the ritual
- [[wiki/agent-systems/agent-planning-systems|Agent Planning Systems]] — retarget home for planning systems
- [[wiki/agent-systems/signaling-ai|Signaling in AI]] — retarget home for honest signaling
- [[wiki/agent-systems/instruction-hierarchy|Instruction Hierarchy]] — retarget home for instruction following
