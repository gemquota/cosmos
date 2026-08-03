---
type: "concept"
title: "Dogfooding"
description: "Using your own product to find and fix its flaws"
tags: ["dogfooding", "self-testing", "practice", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Dogfooding", "https://en.wikipedia.org/wiki/Eating_your_own_dog_food"]
---

# Dogfooding

## Summary
Dogfooding is the practice of using one's own product in real work so its flaws surface naturally. For AI systems it means the improvement loop runs on itself — the wiki would be curated with the wiki's own tools, the agent uses its own agent stack — turning incidents into fixes.

## Details
- **Why it works** — real usage exposes problems no synthetic test can: friction, broken links, missing features.
- **Eat-your-own-dog-food lineage** — self-hosting culture in compilers generalized to products.
- **Agent/AI form** — dogfooding doubles as self-evaluation: the system is its own first production user.
- **Risk** — dogfooding biases the product toward the maker's use; external users still matter.
- **RSIS3 example** — the cosmos bundle would be dogfooded: workers use the wiki's own practices, and pass reports update the practices.

- Why it works: real usage exposes problems no synthetic test can — friction, broken links, missing features — because the product meets its own deployment conditions.
- Boundary: dogfooding is a complement, not a substitute, for external testing; makers' blind spots are exactly where dogfooding is weakest, so outside users still matter.
- Operationalizing it: the standing rule is that the wiki's tooling is used to curate the wiki, so tooling defects surface as curation incidents that get fixed in the same cycle.
- Feedback path: incidents found while dogfooding should flow into the same fix-and-verify pipeline as external reports, so the practice closes the loop rather than just adding anecdotes.
- Cost awareness: dogfooding slows the maker's own work, so the practice should target the highest-value flows — the ones that run every pass — rather than every possible feature.
## Related
- [[wiki/decisions/self-hosting|Self-Hosting]] — the technical sibling
- [[wiki/concepts/incident-driven-improvement|Incident-Driven Improvement]] — what dogfooding feeds
- [[wiki/syntheses/feedback-integration-loops|Feedback Integration Loops]] — closing the loop
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — the evaluative benefit
- [[wiki/syntheses/wiki-self-improvement|Wiki Self-Improvement]] — the wiki dogfooding itself
- [[wiki/syntheses/parallel-agent-acquisition|Parallel Agent Acquisition (5×100) & Writer Reliability]] — dogfooded pass
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — recovery mechanism for self-built tooling
- [[wiki/decisions/checkpoint-selection|Checkpoint Selection]] — choosing states
- [[wiki/decisions/model-selection-practice|Model Selection in Practice]] — choosing configs
