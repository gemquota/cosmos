---
type: "concept"
title: "BigQuery Architecture"
description: "Serverless columnar warehouse with disaggregated storage and a petabit-scale query fabric"
tags: ["bigquery", "gcp", "serverless", "warehouse"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# BigQuery Architecture

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- BigQuery separates storage (Colossus) from compute (Dremel/Borg) and charges per query or flat-rate slots.
- Columnar Capacitor format and tree-shaped shuffle give high scan throughput on petabyte tables.
- Partitioning, clustering, and materialized views control cost; slots bound concurrency in flat-rate mode.
- BI Engine and BigLake extend it toward interactive and lakehouse workloads.

## Related

- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse fundamentals
- [[wiki/data-storage/massively-parallel-processing|Massively Parallel Processing]] — MPP roots of Dremel
- [[wiki/infrastructure/serverless-data-platforms|Serverless Data Platforms]] — serverless cost model
- [[wiki/data-storage/partition-pruning-and-zone-maps|Partition Pruning And Zone Maps]] — cost control via pruning
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
