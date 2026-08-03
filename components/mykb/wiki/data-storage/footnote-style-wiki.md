---
type: "concept"
title: "Footnote Style"
description: "The convention for footnote-based citations in the wiki"
tags: ["footnotes", "citations", "style", "references"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Footnote Style

## Summary
Footnote style moves source details to numbered footnotes, keeping the prose clean while preserving full references at the page's foot.

## Details
- The wiki's footnote convention must specify numbering, reuse (citing one source from several places), and how footnotes render in exports.
- Footnotes trade against inline links: footnotes keep prose readable, inline links keep evidence visible.
- For mykb, footnote-style and inline-citation-style are two allowed patterns, and linting would keep articles from mixing them.

- What the convention must specify: numbering, reuse (citing one source from several places), and how footnotes render in exports — each has a default that authors should not have to rediscover.
- Numbering rule: footnotes number in order of first citation within the page; reused sources keep their original number, so a reader never sees the same source under two numbers.
- Rendering rule: in exports, footnotes appear at the page foot with a reference list; inline citations are the alternative pattern, and mixing the two within one page is the failure the lint rules target.
- Tradeoffs: footnotes keep prose readable by moving evidence out of the line, while inline links keep evidence visible at the point of claim; the choice is per-article, but consistency within a page is mandatory.
- Enforcement: the standing rule is that a page uses one style; the lint rules check the convention, and the metadata score tracks whether pages follow it.
- Source quality: footnote style is about placement, not provenance — the cited source still needs the usual vetting, and the footnote should point at a stable URL or identifier so the reference survives link rot.
- Export behavior: exports should carry the reference list and keep footnote numbering stable across formats, so a printed or PDF version of a page is as useful as the live one.
- Edge cases: a source cited from several places, a footnote on a heading, and a footnote in a table cell are the cases the convention should settle explicitly rather than leave to author judgment.
## Related
- [[wiki/data-storage/inline-citation-style|Inline Citation Style]]
- [[wiki/data-storage/reference-lists|Reference Lists]]
- [[wiki/data-storage/citation-placement|Citation Placement]]
- [[wiki/data-storage/footnote-style-wiki|Footnote Style]]
- [[wiki/data-storage/citation-necessity|Citation Necessity]]
- [[wiki/data-storage/source-formatting|Source Formatting]]
