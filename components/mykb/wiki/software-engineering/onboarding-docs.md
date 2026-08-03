---
type: "concept"
title: "Onboarding Docs"
description: "Documentation that gets a new person productive: setup, architecture map, conventions, and first tasks"
tags: ["documentation", "onboarding", "dx", "team"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Onboarding Docs

## Summary

Onboarding docs are the written path from zero to productive: repo map, local setup, architecture overview, conventions, and first-task walkthroughs. They are the cheapest bus-factor insurance and the first casualty of drift — good ones are maintained like code.

## Details
- Mechanism: effective onboarding docs are layered (5-minute overview → full setup → deep dives), executable (scripts, not 40-step checklists), and verified (a fresh environment can follow them); they live with the code (README, docs/) and are updated when the setup changes; ownership keeps them honest.
- Concrete example: a repo's README gets a new hire to a running dev environment in 15 minutes via one setup script; an architecture doc points to the ADRs and module maps; a first-task guide walks through the exact files a typical ticket touches. The failure pattern: docs that say "see confluence" and setup steps that assume prior context.
- Failure modes: drift — setup steps that no longer work because nobody owns the doc; the 90-page manual nobody reads; onboarding docs that describe what the code should do, not how to navigate it; and tribal knowledge that never gets written because "it is easier to show them".
- Operational tradeoffs: documentation time competes with features, but every undocumented hour of setup is paid by every future new hire; the pattern is short, executable, owned docs, and a rule that setup changes update the docs in the same PR.
- RSIS3/mykb relevance: the wiki's components keep onboarding notes in-repo; the loop's knowledge-acquisition practice extends this to agents, which need the same written context to start productively.
- Verification: keep a "first day" checklist that a real newcomer runs; the doc that has never been followed end-to-end is assumed broken.
- Discoverability: link onboarding docs from README, PR templates, and the issue tracker so they are found at the moment of need, not in a wiki graveyard.

## Related
- [[wiki/software-engineering/developer-experience|Developer Experience]] — onboarding is DX's first impression
- [[wiki/software-engineering/documentation-as-code|Documentation as Code]] — onboarding docs live in the repo and stay current
- [[wiki/dev-tools/devcontainers|Devcontainers]] — containerized setup removes environment drift
- [[wiki/memory/knowledge-capture|Knowledge Capture]] — capturing what onboarding teaches
- [[wiki/memory/provenance|Provenance]] — onboarding records the why behind decisions
