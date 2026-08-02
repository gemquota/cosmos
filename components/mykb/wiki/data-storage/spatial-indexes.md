---
type: "concept"
title: "Spatial Indexes"
description: "R-trees and grid structures for geospatial queries"
tags: ["spatial-index", "geospatial", "r-tree", "gis"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://postgis.net/workshops/postgis-intro/indexing.html", "https://www.postgresql.org/docs/current/gist.html"]
---

# Spatial Indexes

## Summary
Spatial indexes organize geometries so that bounding-box, proximity, and containment queries avoid scanning every record. The dominant structure is the R-tree, which groups nearby geometries into nested bounding rectangles; PostGIS exposes it through PostgreSQL's GiST access method.

## Details
- **R-tree idea** — each index entry stores a minimum bounding rectangle (MBR); children cluster into parent MBRs, so a point-in-polygon or range query prunes whole subtrees whose rectangles cannot intersect the search region.
- **GiST in Postgres** — PostGIS indexes geometry and geography columns with `USING GIST`; the planner uses the index for `&&` (overlaps), `ST_DWithin`, `ST_Intersects`, and `ORDER BY <->` nearest-neighbor scans.
- **Grid and geohash variants** — grid indexes and geohash prefixes map space to cells, trading precision for simplicity; they suit point lookups but handle skewed distributions less gracefully than R-trees.
- **Hilbert and Z-order curves** — space-filling curves order points linearly so range queries map to contiguous index ranges; often used in columnar and key-value stores for multidimensional data.
- **Trade-offs** — spatial indexes are expensive to maintain and best on read-heavy workloads; complex geometries need good bounding boxes or the index degenerates to a full scan.

## Related
- [[wiki/data-storage/b-tree-indexing|B-Tree Indexing]] — the ordered default spatial indexes extend
- [[wiki/data-storage/composite-indexes|Composite Indexes]] — multi-dimensional alternatives via columns
- [[wiki/data-storage/query-tuning|Query Tuning]] — reading planner output for spatial scans
- [[wiki/devops-infra/postgresql|PostgreSQL]] — host of the GiST access method
- [[wiki/devops-infra/query-planning|Query Planning]] — how index use is decided
