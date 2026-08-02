---
type: "concept"
title: "Data Deployment Strategies"
description: "Shipping data changes with controlled risk"
tags: ["deployment", "rollout", "dataops", "strategies"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Data Deployment Strategies

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Expand-contract (parallel run, dual writes, cutover) is the safe schema-deploy pattern.
- Canary/blue-green apply to serving layers; backfill-then-catch-up applies to models.
- Shadow running compares old and new outputs before switch.
- Every strategy needs rollback: versioned outputs and reversible steps.

## Related

- [[wiki/data-storage/schema-migrations|Schema Migrations]] — migration patterns
- [[wiki/infrastructure/blue-green-deployments|Blue-Green Deployments]] — blue-green
- [[wiki/infrastructure/canary-deployments|Canary Deployments]] — canary
- [[wiki/data-storage/zero-downtime-migrations|Zero Downtime Migrations]] — zero downtime
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
