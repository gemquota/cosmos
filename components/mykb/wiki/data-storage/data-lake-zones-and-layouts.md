---
type: "concept"
title: "Data Lake Zones and Layouts"
description: "Structuring a lake into bronze, silver, and gold areas"
tags: ["data-lake", "zones", "bronze-silver-gold", "layout"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Data Lake Zones and Layouts

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Zones separate raw ingestion from curated and serving data.
- Bronze: raw as-received; Silver: cleaned, conformed; Gold: business-ready marts.
- Zone boundaries map to ownership and access control.
- Physical layout should mirror zones plus partition strategy.

## Related

- [[wiki/data-storage/data-lake|Data Lake]] — lake
- [[wiki/data-storage/bronze-silver-gold|Bronze Silver Gold]] — medallion layers
- [[wiki/data-storage/raw-landing-and-curated-zones|Raw Landing And Curated Zones]] — zone details
- [[wiki/data-storage/data-lake-file-layouts|Data Lake File Layouts]] — file layout
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
