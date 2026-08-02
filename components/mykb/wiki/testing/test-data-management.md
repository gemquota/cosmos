---
type: "concept"
title: "Test Data Management"
description: "Provisioning, anonymizing, and refreshing test data"
tags: ["test-data", "testing", "anonymization", "fixtures"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.ibm.com/topics/test-data-management", "https://www.prisma.io/docs/orm/prisma-migrate/workflows/seeding"]
---

# Test Data Management

## Summary
Test data management provisions, anonymizes, and refreshes data for test environments, balancing realism, isolation, and compliance. Bad test data makes tests flaky, or worse, falsely green.

## Details
- Sources: synthesized fixtures, anonymized production copies, and snapshot datasets.
- Anonymization: mask personal data to comply with privacy rules before reuse.
- Refresh cadence: scheduled clones keep environments realistic.
- Isolation: per-test data and shared reference data must be clearly separated.
- Version data alongside the code that expects it; seed migrations together.
- Performance tests need production-shaped volume and skew.
- Track data lineage so a test's assumptions stay discoverable.

## Related
- [[wiki/testing/database-seeding|Database Seeding]] — populating test databases
- [[wiki/testing/factories-and-fixtures|Factories and Fixtures]] — building test objects
- [[wiki/testing/fake-data-generators|Fake Data Generators]] — realistic synthetic values
- [[wiki/testing/test-environments|Test Environments]] — where managed data lives
- [[wiki/security-auth/privacy-by-design|Privacy by Design]] — anonymization requirements
- [[wiki/testing/database-testing|Database Testing]] — queries against managed data
