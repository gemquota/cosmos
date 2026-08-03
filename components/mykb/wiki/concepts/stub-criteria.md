---
type: "concept"
title: "Stub Criteria"
description: "The minimum bar a new article must meet to exist as a stub"
tags: ["criteria", "stubs", "standards", "curation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Stub Criteria

## Summary
Stub criteria define the floor: a stub needs correct frontmatter, a one-sentence description, a short framing body, and a Related block of resolvable links. The bar is deliberately low — a stub is not a finished article, it is a placeholder with enough structure to be useful and enough direction to be promotable.

## Details
- The requirements in detail: frontmatter must be valid (type, title, description, tags, timestamp, status), because every downstream tool — linting, graph building, the health dashboard — parses it. The description must be a real one-sentence definition, not a vague gesture, because the description is what search and the graph surface. The body must frame the concept — summary plus a few concrete details — so the stub is informative even before promotion. The Related block must contain only resolvable links, so the stub joins the graph immediately rather than introducing dead links.
- The stub is a promise to promote, so it should name the questions a full article must answer — that makes the future promotion cheap. The best stubs are not just definitions but work orders: they record what is known and what remains open, so the promotion pass starts from a checklist rather than a blank page. This is the operational content of "stub" as a status: it is a state with an exit condition, not a permanent resting place.
- Articles that cannot meet even the stub bar are better as raw captures or seed candidates than as wiki pages. The bar filters out notes that are too thin, too ephemeral, or too speculative to warrant a page — those belong in the inbox or the seed list, where they cost nothing and can grow on their own schedule. Enforcing the bar at creation is what keeps the wiki's baseline quality from decaying page by page.
- The failure modes: stubs that are really just titles (body that says nothing), stubs with dead links (graph debt created at birth), and the cultural failure where the stub bar is treated as the quality bar — the wiki fills with permanent stubs and promotion stops.
- For mykb, stub criteria are enforced by linting at write time, and stub-ratio is the metric that tracks how many promises are outstanding. The promotion campaign (stub → growing) is the mechanism that pays down those promises, and the criteria are what keep the promises honest.

## Related
- [[wiki/concepts/seed-article-criteria|Seed Article Criteria]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/concepts/stub-ratio|Stub Ratio]]
- [[wiki/concepts/article-quality-checklist|Article Quality Checklist]]
- [[wiki/concepts/expansion-needed|Expansion Needed]]
- [[wiki/data-storage/open-knowledge-format|Open Knowledge Format]]
