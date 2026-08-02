---
type: "concept"
title: "Broadcast Joins and Bucketing"
description: "Avoiding shuffles by replicating small tables or pre-bucketing data"
tags: ["broadcast-join", "bucketing", "spark", "join"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Broadcast Joins and Bucketing

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Broadcast joins ship a small table to every executor, avoiding a full shuffle.
- Bucketing pre-partitions tables by key so joins can be shuffle-free.
- Bucketed joins work when both sides use compatible bucket counts and keys.
- Costs: broadcast memory on executors, bucketing maintenance on write.

## Related

- [[wiki/data-storage/join-algorithms|Join Algorithms]] — join algorithms
- [[wiki/data-storage/clustered-tables|Clustered Tables]] — physical clustering
- [[wiki/data-storage/spark-tuning-and-shuffle-optimization|Spark Tuning And Shuffle Optimization]] — shuffle reduction
- [[wiki/data-storage/bucketing-and-clustering-in-tables|Bucketing And Clustering In Tables]] — table bucketing
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
