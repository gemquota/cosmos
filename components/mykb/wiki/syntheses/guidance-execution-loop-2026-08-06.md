---
type: "synthesis"
title: "Guidance Execution Loop — Wanted Links, Scaffolds, Research Manifest"
description: "Closing the guidance loop: red-link wanted pages feed the queue, drain_guidance scaffolds them as stubs, and a research manifest hands direction to the next session"
tags: ["guidance", "wanted-pages", "red-links", "scaffolding", "research-manifest", "mykb"]
timestamp: "2026-08-06T00:00:00Z"
status: "growing"
---

# Guidance Execution Loop — Wanted Links, Scaffolds, Research Manifest

## Summary
The Guide tab stopped at *capturing* direction; this pass makes guidance
*executable*. Red links (wikilinks that resolve to no page) are surfaced as
standing research signals, added to the research queue in one click, and
`drain_guidance.py --apply` scaffolds them into `status: stub` pages that
flow straight into the normal enrichment pipeline. A research manifest
carries the remaining directions and page feedback to the next session.

## Details
- **Red-link scan** — `build_stub_audit.py` resolves every `` `Target`]] ``
  against a full-disk wiki inventory (root-relative paths + unique-basename
  fallback, mirroring the app's `resolveWikiPath`), strips code spans/fences
  first so syntax examples don't count, and ranks survivors by inbound count
  with linking areas and a suggested path (`guidance.json → wanted_links`).
  A clean link graph yields few/no candidates; each is a page the wiki itself
  says is missing.
- **Scaffolding** — `drain_guidance.py --apply` creates `wanted` items as
  `wiki/<area>/<slug>.md` and `question` items as `wiki/questions/<slug>.md`,
  with frontmatter `type`, `status: stub`, `created`, and
  `source: ["guidance-queue"]`. Paths come from the item's path field or are
  derived (questions → `questions/`, else the item area or `concepts`);
  titles derive from the path basename when no title is given. Existing files
  are never overwritten (idempotent re-apply).
- **Research manifest** — apply also writes
  `.wiki-daemon/buffers/guidance-inference.json` with `created`, `skipped`,
  `research` (directions), and `feedback` (suggestion/correction/priority/
  note), so future acquisition sessions consume one file instead of scraping
  the queue.
- **Naming pattern** — a wanted item that is really a *concept* (red link or
  explicit) scaffolds as a concept stub; a *question* scaffolds under
  `wiki/questions/` with `type: question`. The loop then re-enters the stub
  auditor: scaffold → triage → enrich → promote.

## Related
- [[wiki/syntheses/guidance-ui-2026-08-06|MyKB Guidance UI]] — the surface this loop executes
- [[wiki/syntheses/stub-auditor-live-queue|Stub Auditor — Live Data & Inference Queue]] — the triage half of the loop
- [[wiki/syntheses/wiki-self-improvement|Wiki Self-Improvement]] — the umbrella practice
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — how scaffolds grow into articles
- [[wiki/meta-learning/wikilinks|Wikilinks]] — first page scaffolded from a red link
