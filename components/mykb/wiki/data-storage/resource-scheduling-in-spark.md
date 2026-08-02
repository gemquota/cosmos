---
type: "concept"
title: "Resource Scheduling in Spark"
description: "How Spark acquires and shares cluster resources"
tags: ["spark", "scheduling", "yarn", "kubernetes"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Resource Scheduling in Spark

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Spark runs on standalone, YARN, Kubernetes, or Mesos, each with different scheduling.
- Dynamic allocation grows/shrinks executors based on pending tasks.
- Fair vs FIFO schedulers share cluster capacity across jobs.
- Scheduling delays and locality preferences affect shuffle-heavy jobs.

## Related

- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — engine landscape
- [[wiki/infrastructure/container-scheduling|Container Scheduling]] — K8s scheduling
- [[wiki/data-storage/spark-executors-and-memory-planning|Spark Executors And Memory Planning]] — executor sizing
- [[wiki/infrastructure/workload-management-and-queues|Workload Management And Queues]] — queue governance
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
