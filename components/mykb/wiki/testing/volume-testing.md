---
type: "concept"
title: "Volume Testing"
description: "Testing with large data volumes to expose scaling issues"
tags: ["volume-testing", "testing", "data", "scaling"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.ibm.com/topics/volume-testing", "https://grafana.com/docs/k6/latest/testing-guides/"]
---

# Volume Testing

## Summary
Volume testing runs the system against large data volumes, records, files, and messages, to expose scaling issues in storage, queries, and processing. It checks behavior as data grows, not just as users grow.

## Details
- Scale dimensions: database rows, log volume, message backlog, and file sizes.
- Verify query plans degrade gracefully under indexing, partitioning, and pagination.
- Watch insert and update throughput, storage growth, and backup times.
- Volume issues are common in reporting, search, and event pipelines.
- Test with production-shaped data: distribution, skew, nulls, and duplicates matter.
- Review indexes alongside; plans that work on small tables can collapse at scale.
- Combine volume runs with load tests to model realistic total work.

## Related
- [[wiki/testing/database-testing|Database Testing]] — query behavior at scale
- [[wiki/testing/performance-testing|Performance Testing]] — the umbrella volume fits under
- [[wiki/devops-infra/database-indexing|Database Indexing]] — indexes degrade under volume
- [[wiki/devops-infra/sharding|Sharding]] — horizontal scaling for data growth
- [[wiki/testing/load-testing|Load Testing]] — concurrency combined with volume
- [[wiki/testing/test-data-management|Test Data Management]] — producing realistic large datasets
