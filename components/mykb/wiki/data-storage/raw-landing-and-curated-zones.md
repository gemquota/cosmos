---
type: "concept"
title: "Raw Landing and Curated Zones"
description: "The first two stages of lake ingestion"
tags: ["landing-zone", "curated", "data-lake", "zones"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Raw Landing and Curated Zones

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Raw/landing: append-only, source-of-truth copies, minimal transformation.
- Curated: cleansed, typed, deduplicated data ready for analysis.
- Keep raw immutable for re-processing; never let downstream corrupt it.
- Curated outputs should be reproducible from raw.

## Related

- [[wiki/data-storage/data-lake|Data Lake]] — lake
- [[wiki/data-storage/data-lake-zones-and-layouts|Data Lake Zones And Layouts]] — zones
- [[wiki/data-storage/bronze-silver-gold|Bronze Silver Gold]] — medallion mapping
- [[wiki/data-storage/data-versioning-models|Data Versioning Models]] — reproducibility
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
