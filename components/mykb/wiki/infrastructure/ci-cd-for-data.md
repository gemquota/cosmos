---
type: "concept"
title: "CI/CD for Data"
description: "Automated testing and deployment for data pipelines"
tags: ["ci-cd", "dataops", "pipelines", "deployment"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# CI/CD for Data

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- CI runs linting, tests, and validation on every change; CD deploys to environments.
- Data CI/CD adds data-quality gates and backfill planning to code deploys.
- Deployments are reversible: keep rollback scripts and versioned outputs.
- Tooling: dbt Cloud, GitHub Actions, Airflow, lakeFS, and DVC.

## Related

- [[wiki/data-storage/data-pipeline-orchestration|Data Pipeline Orchestration]] — orchestration
- [[wiki/data-storage/data-versioning|Data Versioning]] — versioning
- [[wiki/infrastructure/data-deployment-strategies|Data Deployment Strategies]] — deploy strategies
- [[wiki/infrastructure/dbt-environments-and-jobs|Dbt Environments And Jobs]] — dbt CI/CD
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
