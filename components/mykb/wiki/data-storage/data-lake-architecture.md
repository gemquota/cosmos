---
type: "concept"
title: "Data Lake Architecture"
description: "Low-cost, schema-flexible storage for all of an organization's data"
tags: ["data-lake", "object-storage", "schema-on-read", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Data_lake", "https://en.wikipedia.org/wiki/Data_lakehouse"]
---

# Data Lake Architecture

## Summary

A data lake stores raw data at any scale and format, typically on object storage, at low cost.
Schema-on-read lets analysts interpret data when it is used rather than when it is stored.
Lakes enable open formats, machine learning over raw data, and flexible exploration.
Lakes succeed when governance arrives before scale; a lake without ownership quickly becomes a swamp.

## Details

- Zones (raw, curated, consumption) organize quality and ownership within the lake.
- Open table formats add ACID, versioning, and performance to lake files.
- Key risks: data swamps, ungoverned access, and small-file sprawl.
- Lakehouse architectures add warehouse-style management on top.
- Catalog everything on arrival: schema, owner, and quality metadata reduce later archaeology.
- Open formats keep lake data portable across engines and vendors.
- Treat the lake as an asset class with an owner and a lifecycle; unowned lakes become liabilities.

## Related

- [[wiki/data-storage/data-lake-zones-and-layouts|Data Lake Zones And Layouts]] — zoning
- [[wiki/data-storage/open-table-formats-and-interoperability|Open Table Formats And Interoperability]] — table formats
- [[wiki/data-storage/sql-on-lakehouse|Sql On Lakehouse]] — querying
- [[wiki/data-storage/data-lake|Data Lake]] — existing lake note
- [[wiki/data-storage/object-storage|Object Storage]] — storage substrate
- [[wiki/data-storage/small-file-problem-and-compaction|Small File Problem And Compaction]] — layout hygiene

