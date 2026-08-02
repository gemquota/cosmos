---
type: "concept"
title: "Data Testing Frameworks"
description: "Automated checks for data and data pipelines"
tags: ["testing", "data-quality", "great-expectations", "dbt"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.greatexpectations.io/", "https://docs.getdbt.com/docs/build/tests"]
---

# Data Testing Frameworks

## Summary

Data testing frameworks turn quality expectations into automated, repeatable checks.
They run in CI and on schedules, blocking bad promotions.
Tooling ranges from SQL assertions to full expectation suites.
Data tests are assertions about reality, so they fail when reality changes; review and adapt them.

## Details

- dbt tests: unique, not_null, relationships, and custom SQL.
- Great Expectations: declarative expectation suites with docs.
- Soda and elementary add monitoring and anomaly detection.
- Tests should run at promotion time and on live data.
- Own tests per team; shared frameworks keep the bar consistent.
- Run tests at multiple stages: CI, promotion, and scheduled monitoring.
- Keep a small, high-signal suite rather than hundreds of noise checks.
- Frameworks standardize quality work so it survives team changes and scales across domains.

## Related

- [[wiki/data-storage/soda-and-dbt-tests|Soda And Dbt Tests]] — SQL-native checks
- [[wiki/data-storage/data-pipeline-testing|Data Pipeline Testing]] — pipeline testing
- [[wiki/data-storage/data-validation-before-promotion|Data Validation Before Promotion]] — promotion gates
- [[wiki/data-storage/data-quality-checks|Data Quality Checks]] — existing note
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — contracts
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

