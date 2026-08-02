---
type: "concept"
title: "dbt Environments and Jobs"
description: "Managing dbt projects across dev, staging, and prod"
tags: ["dbt", "environments", "jobs", "analytics-engineering"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# dbt Environments and Jobs

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- dbt environments isolate credentials, schemas, and job configurations.
- Jobs run models, tests, and docs on schedules or git triggers.
- CI jobs run on PRs with deferral to prod for faster, accurate runs.
- Environment parity reduces 'works in dev' surprises.

## Related

- [[wiki/data-storage/data-pipeline-orchestration|Data Pipeline Orchestration]] — orchestration
- [[wiki/data-storage/dbt-and-analytics-engineering|Dbt And Analytics Engineering]] — dbt fundamentals
- [[wiki/infrastructure/data-environments-dev-staging-prod|Data Environments Dev Staging Prod]] — environment strategy
- [[wiki/infrastructure/ci-cd-for-data|Ci Cd For Data]] — CI/CD
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
