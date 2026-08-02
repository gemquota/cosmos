---
type: "concept"
title: "Data Pipeline Testing"
description: "Testing data code before it breaks production"
tags: ["pipeline-testing", "ci-cd", "data-quality", "testing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.greatexpectations.io/", "https://docs.getdbt.com/docs/build/tests"]
---

# Data Pipeline Testing

## Summary

Pipeline testing validates code, data, and behavior before deployment.
It spans unit tests, integration tests, and data-quality gates.
Testing turns pipeline changes from risky into routine.
Testing is what makes pipeline refactors safe and releases boring.

## Details

- Unit test transforms with fixture data.
- Integration test connectors and schema compatibility.
- Data-quality checks run on outputs at promotion time.
- Test against representative, not just happy-path, data.
- CI/CD runs tests per change; monitoring runs them live.
- Test against prod-like data to catch cardinality surprises.
- Separate environment tests from live data-quality monitoring.
- Tested pipelines fail loudly in CI instead of silently in production.

## Related

- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — frameworks
- [[wiki/infrastructure/ci-cd-for-data|Ci Cd For Data]] — pipeline
- [[wiki/data-storage/test-data-generation|Test Data Generation]] — test data
- [[wiki/data-storage/data-quality-checks|Data Quality Checks]] — quality
- [[wiki/data-storage/data-validation-before-promotion|Data Validation Before Promotion]] — gates
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability

