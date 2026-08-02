---
type: "concept"
title: "Redshift Architecture"
description: "AWS's petabyte-scale MPP warehouse with leader and compute nodes"
tags: ["redshift", "aws", "mpp", "warehouse"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Redshift Architecture

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Redshift clusters split tables across slices on compute nodes; the leader node plans and coordinates queries.
- Columnar compression, zone maps, and sort/dist keys drive performance; spectrum extends queries to S3.
- RA3 nodes offload managed storage, decoupling compute and storage for elastic resize.
- Classic choices: distribution style (even/key/all), sort keys, and encoding per column.

## Related

- [[wiki/data-storage/massively-parallel-processing|Massively Parallel Processing]] — MPP architecture basics
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse fundamentals
- [[wiki/data-storage/partition-pruning-and-zone-maps|Partition Pruning And Zone Maps]] — zone maps as Redshift's skip layer
- [[wiki/data-storage/warehouse-optimization|Warehouse Optimization]] — tuning sort and dist keys
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
