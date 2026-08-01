---
type: "concept"
title: "Site Reliability Engineering"
description: "Applying software engineering to operations: SLOs, error budgets, automation, and toil reduction"
tags: ["sre", "reliability", "slo", "operations", "error-budgets"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://sre.google/sre-book/table-of-contents/"]
---

# Site Reliability Engineering

## Summary
Site reliability engineering (SRE) applies software engineering practices to operations problems, treating reliability as a feature that can be designed, measured, and budgeted. Its core tools are service-level objectives, error budgets, and the systematic elimination of toil. SRE emerged at Google and is documented in the freely published SRE book.

## Details
- SLIs, SLOs, SLAs: an SLI is a measured indicator (latency, error rate); an SLO is the target (p99 < 200 ms, 99.9% of requests); an SLA is the contractual commitment derived from the SLO.
- Error budgets: the SLO defines an acceptable failure allowance (0.1% of requests); the budget is spent by releases and incidents, and when it is exhausted, launches pause and reliability work starts.
- Toil is manual, repetitive, automatable work (restarts, ticket triage, config edits); SRE's mandate is to measure it and drive it toward zero through automation.
- Operations load is shared: developers carry pagers for their services, funded by error-budget policy, which aligns incentives between feature velocity and reliability.
- Monitoring and alerting follow the golden signals, with alerts tied to SLO burn rather than every anomaly.
- SRE and DevOps are complementary: DevOps is a cultural movement; SRE is a concrete set of practices and roles for reliability.
- For mykb, SRE thinking applies at small scale too: define an SLO for the wiki's uptime, keep an error budget, and automate the toil of index rebuilds.

## Related
- [[wiki/devops-infra/error-budgets|Error Budgets]] — the release-governance mechanism
- [[wiki/compositions/devops-deployment|DevOps & Deployment Pattern]] — the cultural counterpart to SRE practice
- [[wiki/devops-infra/on-call-rotations|On-Call Rotations]] — shared operational load with developers
- [[wiki/devops-infra/runbooks|Runbooks]] — documented operational knowledge
- [[wiki/devops-infra/incident-response|Incident Response]] — what happens when budgets are spent
- [[wiki/devops-infra/golden-signals|Golden Signals]] — the SLIs that feed SLOs
- [[wiki/devops-infra/observability|Observability]] — the measurement layer SRE depends on
