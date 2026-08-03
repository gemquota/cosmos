---
type: "concept"
title: "Bus Factor"
description: "The number of people whose departure would bring a project to a halt"
tags: ["risk", "team", "knowledge", "continuity"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Bus Factor

## Summary

Bus factor is the minimum number of people whose departure would stall a project — the team's hidden risk number. High bus-factor (low risk) comes from shared ownership, documentation, and review; low bus factor hides in unreviewed code and undocumented operations knowledge.

## Details
- Mechanism: bus factor is computed per critical component: how many people can explain, fix, and extend it? The risk concentrates in knowledge, not code lines — a 10k-line module one person owns is riskier than a 100k-line module three people review. Signals: unmerged PRs awaiting one reviewer, undocumented runbooks, TODOs only one person understands.
- Concrete example: a payment module's only author leaves; the team spends weeks rediscovering its invariants, while a documented-and-reviewed module with two owners absorbs the departure in days. The fix is structural: pair/review rotation, ADRs for key modules, runbooks for ops knowledge, and ownership that names at least two people.
- Failure modes: measuring bus factor by headcount rather than knowledge coverage; documentation that exists but is stale; and process theater (pairing on paper) that does not actually transfer understanding. The metric to watch is knowledge distribution: can a second person review and run the critical paths?
- Operational tradeoffs: reducing bus factor costs time (reviews, docs, rotation) that competes with feature work; the trade is resilience vs velocity, and the calibration is highest for irreplaceable, hard-to-hire knowledge. Rotate ownership periodically so the bus factor stays genuinely low.
- RSIS3/mykb relevance: the wiki's OKF notes are the team's bus-factor mitigation — knowledge persisted in searchable notes rather than in one engineer's head.
- Signals to watch: PRs awaiting a single reviewer, undocumented runbooks, and emergency fixes only one person can make are the practical indicators; track them, not just headcount.
- Remediation tempo: rotate knowledge deliberately — pair on critical modules, document post-incident, and require two-owner review for the top-risk components first.

## Related
- [[wiki/software-engineering/code-ownership|Code Ownership]] — narrow ownership lowers the bus factor
- [[wiki/software-engineering/onboarding-docs|Onboarding Docs]] — documentation is the bus-factor antidote
- [[wiki/memory/personal-knowledge-management|Personal Knowledge Management]] — externalized knowledge survives people
- [[wiki/devops-infra/backups|Backups]] — the data-side of continuity
- [[wiki/software-engineering/documentation-as-code|Documentation as Code]] — docs externalize knowledge and raise the bus factor
