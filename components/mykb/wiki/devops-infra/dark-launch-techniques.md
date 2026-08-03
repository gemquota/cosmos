---
type: "concept"
title: "Dark Launch Techniques"
description: "Running new code paths invisibly behind flags before exposure"
tags: ["dark-launch", "feature-flags", "testing", "releases"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Dark Launch Techniques

## Summary
Dark launching ships code behind flags or routes so it runs in production without being visible to users: the new path executes, is logged and measured, but the user-visible result still comes from the old path. It de-risks rewrites by validating behavior under real production load before flipping the switch.

## Details
- Mechanism: the request enters the system and a flag decides which implementation to call; in dark mode the new implementation runs alongside and its result is compared or discarded; telemetry compares outcomes, latencies, and errors; rollout flips the flag once confidence is proven.
- Concrete example: a search rewrite — live traffic is sent to both the old and new rankers; the UI shows the old result while the new one is scored and logged; offline analysis measures agreement and quality; a canary-style flip then moves real users over gradually.
- Failure modes: dark code with side effects — a "read-only" comparison path that writes to the database or sends emails duplicates effects; unbounded resource cost when the dark path doubles CPU, memory, or API spend — size it like a real rollout; measurement bias when the dark path lacks the same inputs (e.g. no feedback loop), so it looks better or worse than it will be live; flag config drift where the dark path silently becomes the live path after a cleanup.
- Tradeoffs: dark launching gives real-traffic validation without user impact but doubles compute and adds code complexity that must be maintained until the flip; it complements — rather than replaces — canaries, which expose the new path to real users gradually.
- Operational notes: make dark paths observably tagged (span attributes, log fields), add budget and error alerts before enabling, and schedule removal of the old path after the flip.
- RSIS3 relevance: RSIS3's L2 improvement proposals can dark-launch — run the proposed strategy in shadow mode against live pulse data, compare outcomes, and promote only proven changes.

## Related
- [[wiki/infrastructure/snapshot-and-clone-techniques|Snapshot & Clone Techniques]]
- [[wiki/infrastructure/data-anonymization-techniques|Data Anonymization Techniques]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
