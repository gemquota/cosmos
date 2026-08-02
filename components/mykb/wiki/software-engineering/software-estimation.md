---
type: "concept"
title: "Software Estimation"
description: "Predicting effort and duration with uncertainty made explicit"
tags: ["estimation", "planning", "uncertainty", "process"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Estimation", "https://en.wikipedia.org/wiki/Planning_poker"]
---

# Software Estimation

## Summary
Software estimation produces ranges, not promises: effort and duration predictions with explicit uncertainty. The discipline is calibrating over time — comparing estimates to actuals — and using estimates for planning tradeoffs, not for accountability theater.

## Details
- Estimates are distributions: give ranges and confidence, and state the assumptions behind them.
- Relative estimation (story points) beats absolute for planning; absolute time estimates serve commitments.
- Calibration is the only way to improve: track estimate vs actual and learn your bias.
- Break work down: small pieces estimate better than big ones; unknown work should be an explicit risk, not a hidden padding.
- Estimation is negotiation: stakeholders need ranges, options, and the cost of certainty.
- Anti-pattern: estimates used as targets — that converts honest ranges into sandbagged numbers.
- For the mykb bundle, estimation covers curation batches: how many articles per week, with a buffer for verification.

Worked example — the wiki team estimates a curation feature at 5-8 story points with a 70% confidence range of 2-3 weeks; the retrospective compares actuals and nudges next month's estimate.

## Related
- [[wiki/software-engineering/planning-poker|Planning Poker]]
- [[wiki/software-engineering/story-points|Story Points]]
- [[wiki/software-engineering/velocity-metrics|Velocity Metrics]]
- [[wiki/software-engineering/sprint-planning|Sprint Planning]]
- [[wiki/software-engineering/backlog-grooming|Backlog Grooming]]
- [[wiki/communities/stakeholder-management|Stakeholder Management]]
- [[wiki/software-engineering/estimation-techniques|Estimation Techniques]]
- [[wiki/software-engineering/agile-ceremonies|Agile Ceremonies]]
- [[wiki/dev-tools/code-coverage-tools|Code Coverage Tools]]
- [[wiki/dev-tools/dashboards-practice|Dashboards Practice]]
