---
type: "concept"
title: "Code Ownership"
description: "The policy deciding who is responsible for reviewing and maintaining a given piece of code"
tags: ["ownership", "team", "process", "maintenance"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Code Ownership

## Summary
Code ownership assigns responsibility for parts of the codebase: strict ownership restricts changes to designated owners, while shared or collective ownership lets anyone change anything with review. The policy shapes review load and bus factor.

## Details
- Strict ownership guarantees expertise but creates bottlenecks; shared ownership spreads load but needs standards.
- CODEOWNERS files in git hosts automate review assignment.
- RSIS3 relevance: the wiki uses area-level responsibility (per-worker scopes) during acquisition rounds.

## Related
- [[wiki/software-engineering/bus-factor|Bus Factor]] — ownership concentration directly affects the bus factor
- [[wiki/software-engineering/code-review|Code Review]] — owners are the required reviewers
- [[wiki/software-engineering/pair-programming|Pair Programming]] — collaboration dilutes single-owner risk
- [[wiki/concepts/identity-system|RSIS3 Identity System]] — who owns what is an identity question
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — knowledge areas need owners too
