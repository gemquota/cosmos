---
type: "synthesis"
title: "Wiki Link Resolution & Junk-Entity Audit"
description: "Canonical link resolution for the wiki browser plus junk-entity triage in the stub auditor"
tags: ["mykb", "wiki-browser", "links", "stub-auditor", "curation", "performance"]
timestamp: "2026-08-05T00:00:00Z"
status: "growing"
---

# Wiki Link Resolution & Junk-Entity Audit

## Summary
Two long-standing MyKB pain points got root-cause fixes: wiki links broke for
several independent reasons, and pre-archived junk entities were invisible to
the stub auditor. Link handling now resolves through one canonical resolver,
and the auditor surfaces `raw/archive/junk-entities-*` for deletion without
slowing down.

## Details
- **One resolver, one source of truth** — `resolveWikiPath()` in
  `components/mykb/index.html` turns any link/hash target into a canonical
  `files.json` path. It handles `../` links (resolved against the *current
  file's directory*, not a regex strip), `wiki/` prefixes, `.md` suffixes,
  `wiki/wiki/` double prefixes, case-insensitive lookups, and a unique-
  basename fallback that lands archived/moved pages (e.g. `wiki/topics/ast-10`
  → `raw/archive/session-artifacts-2026-07/topics/ast-10.md`). Deep links in
  the URL hash survive reloads through the same resolver.
- **Click dedupe** — the content click handler calls `stopPropagation()` so
  the document-level `.md` interceptor no longer re-navigates with the raw
  unresolved href (a race that rendered the *second* navigation as an error
  page). Wikilink clicks pass the raw target instead of force-appending
  `.md`.
- **Dead-link UX** — the error page now offers “Search for &lsquo;basename&rsquo;”
  so an unresolvable link becomes a search, not a dead end.
- **Junk entities in the audit** — `build_stub_audit.py` scans
  `raw/archive/junk-entities-*` and tags items `junk` (`j: 1`) with their full
  bundle-relative path. The SPA adds a “junk archive” filter bucket
  (unchecking the wiki buckets isolates junk for bulk deletion), renders
  Keep/Delete only for junk cards, and emits `git rm raw/archive/...` lines;
  `drain_stub_queue.py` accepts `raw/` paths so the queue applies them.
- **Pagination performance** — the categorizer `<select>` (one per card, all
  45 areas) was the dominant render cost; it is now built lazily in
  `openPicker()` on first open, and cards render into a
  `DocumentFragment`. Measured ~100× faster page renders on the 4,267-item
  audit (old render did not finish in 100 s under jsdom; new is ~280 ms).
- **Dashboard menu** — nav-tab tooltips are a floating overlay
  (`components/rsis3/dashboard/style.css`) so hovering never inflates the tab
  bar; touch devices skip tab tooltips entirely.

## Rules
- Links in wiki content may be `wiki/`-prefixed, bare, `../`-relative, or
  point at archived files — the browser must resolve, not assume one shape.
- Junk-entity archive trees are a deletion queue: surface them in the auditor,
  never hide them from curation.
- Anything rendered per-card on every keystroke (pickers, selects, option
  lists) belongs in a lazy builder, not the card template.

## Related
- [[wiki/syntheses/stub-auditor-live-queue|Stub Auditor — Live Data & Inference Queue]] — the queue pipeline junk items feed into
- [[wiki/syntheses/orphan-detection|Orphan Detection]] — the other side of link health
- [[wiki/syntheses/graph-health-checks|Graph Health Checks]] — verification of link integrity
- [[wiki/syntheses/wiki-self-improvement|Wiki Self-Improvement]] — the umbrella practice
- [[wiki/syntheses/post-pass-consolidation|Post-Pass Consolidation]] — this note's ritual
- [[wiki/concepts/knowledge-graph-memory|Knowledge-Graph Memory]] — the substrate links build
