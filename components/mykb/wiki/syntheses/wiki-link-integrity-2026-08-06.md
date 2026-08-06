---
type: "synthesis"
title: "Wiki Link Integrity Repair — De-links, Malformed Wikilinks, Honest Audit"
description: "Root-cause repair of the wiki's broken links: dead log entries de-linked, malformed wikilinks rewired, and a rewritten link checker that mirrors app resolution"
tags: ["mykb", "wiki-browser", "links", "link-check", "curation", "audit-tooling"]
timestamp: "2026-08-06T12:00:00Z"
status: "growing"
---

# Wiki Link Integrity Repair

## Summary
The red-link scan added by the guidance loop was only as honest as its link
graph. A rewritten `link_check.py` showed the wiki was actually much healthier
than the old checker reported — and found the *real* breakage: 4,594 dead
Markdown links in `wiki/log.md` (pointing at pages deleted in the junk-entity
archive) and ~1,858 malformed wikilinks across 214 generated entity pages
(unclosed `]]`, a stale `wiki/web-platforms/supercategories/` prefix, and
breadcrumb hops to the wrong index). All of it is repaired; the audit now
reports **0 unresolved links** across the 5,400 wiki files.

## Details
- **Old checker lied** — it stripped `./` with `lstrip('./')`, which also
  swallowed `../` prefixes, and it scanned frontmatter and fenced/inline code
  examples, so its "30,787 unresolved" count was noise. The rewritten
  `link_check.py` resolves `../` against the source file's directory, strips
  frontmatter + code fences + inline code spans, defaults to `wiki/` scope
  (`--all` for the bundle, where archives legitimately keep stale links),
  falls back to unique basenames for moved pages, and exits 1 on breakage so
  CI can gate on it.
- **Dead targets de-linked, not orphaned** — `wiki/log.md` referenced
  thousands of pages deleted as junk entities. The fix converts those to
  code-span labels (`` `Abi` ``) instead of links, so history stays readable
  and nothing dangles.
- **Malformed wikilinks rewired** — 214 generated entity pages had unclosed
  `]]`, a junk `wiki/web-platforms/supercategories/` prefix from an old
  generator, and dead related-entity links. They were normalized to canonical
  paths (with basename fallback for archived/moved targets; pages that no
  longer exist became plain labels).
- **Breadcrumb canonicalization** — 167 entity pages labeled their domain hop
  `Android Core` but pointed at `wiki/web-platforms/00-index` (the *Web
  Platforms Index*). Retargeted to `wiki/android-core/00-index`, which is the
  real Android Core index.

## Rules going forward
- Link audits must mirror the app's resolver semantics (`resolveWikiPath`:
  root-relative + `../` vs source dir, basename fallback) or they produce
  false alarms.
- When a target is deleted, de-link (code-span label) rather than leaving a
  broken link; when it moved, retarget; when it was archived as junk, prefer
  the archive path so the link still resolves.
- Breadcrumb hops should point at the domain's real index page, not a legacy
  bucket path.

## Cross-references
- [[wiki/syntheses/wiki-link-resolution-and-junk-audit]]
- [[wiki/syntheses/guidance-execution-loop-2026-08-06]]
