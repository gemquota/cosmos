---
type: "entity"
title: "Functionality Audit"
description: "Functionality Audit: inventorying features and verifying them against requirements"
tags: ["entity", "api", "ast", "aws", "bash", "bootstrap", "audit"]
timestamp: "2026-07-19T22:41:40Z"
resource: ""
---

# Functionality Audit

## Summary

Functionality Audit is the bootstrap-cluster entity for systematically reviewing what a system can do: inventorying features, checking them against requirements, and finding gaps. Audits convert vague impressions of completeness into evidence. They matter because unverified features are the ones that fail first. Audits are how a team proves its system does what it claims, to itself and to its users.

## Details

- **Definition** — A functionality audit catalogs implemented features, maps them to requirements, and records verification status.
- **Feature inventory** — A structured list of capabilities with owners and entry points makes scope visible.
- **Gap analysis** — Requirements without implementations, and implementations without requirements, both surface in mapping.
- **Verification** — Each feature should be exercised or tested; unverifiable claims are risks, not features.
- **Coverage metrics** — Counts of audited versus verified features quantify progress and focus remaining work.
- **Worked example** — An audit lists twenty features, verifies eighteen, and flags two that regressed after a refactor.
- **Failure modes** — Audits that inventory code without checking behavior, or that rot after the release, waste effort.
- **Practical relevance** — Regular audits keep documentation honest and prevent silent feature decay.
- **Evidence links** — Each audited feature points at its tests or verification run, so claims are checkable.
- **Recurring cadence** — Scheduled audits catch decay before users do, rather than in response to incidents.
- **Owner assignment** — Every gap found needs an owner and a disposition: fix, document, or consciously accept.
- **Tooling** — Scripts that crawl routes, commands, and entry points generate a first-pass inventory that humans then verify.

## Related

- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/project-overview|Project Overview]] — claims the audit checks
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/best-for|Best For]] — evidence-based feature choices
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/decisiontype|DecisionType]] — audit outcome types
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/execution-modes|Execution Modes]] — auditing every mode
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/00-index|Bootstrap Index]] — cluster index page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/dead-imports|Dead Imports]] — finding unused features
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/depth-levels|Depth Levels]] — auditing nested behavior
