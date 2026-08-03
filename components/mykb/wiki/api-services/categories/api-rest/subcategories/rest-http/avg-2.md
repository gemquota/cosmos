---
type: "entity"
status: "growing"
title: "AVG"
description: "Acronym referenced in session 019f2369"
tags: ["acronym", "android", "api", "ast", "auth", "backend", "entity"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
---


## Avg 2

Average — a statistical measure. Could be SQL AVG() or a general metric in benchmarks.

Acronym referenced in session 019f2369

**Domain:** Mobile Platform › [[wiki/web-platforms/00-index|Android Core]] › [[wiki/web-platforms/supercategories/api-services/categories/api-rest/00-index|Api Clients › Avg 2

## Overview

An average is a single summary value computed from a set of measurements, used to characterize the typical case in a distribution. The choice of average matters: the arithmetic mean is sensitive to outliers, the median is robust to them, and the mode reflects the most frequent value. In technical work, "AVG" most often refers to the SQL aggregate function `AVG()`, which computes the arithmetic mean of a numeric column, or to a benchmark metric that summarizes latency, throughput, or resource usage across runs.

## SQL AVG()

`SELECT AVG(column) FROM table` returns the mean of the non-null values in the column, ignoring NULLs by default. It is commonly combined with `GROUP BY` to compute per-category averages, with `HAVING` to filter groups after aggregation, and with `WHERE` to restrict the input rows. Windowed usage such as `AVG(value) OVER (ORDER BY ts ROWS BETWEEN ...)` produces moving averages useful for trend analysis. Because the aggregate discards the distribution, pairing it with `MIN`, `MAX`, `COUNT`, and percentile queries gives a much fuller picture of the data.

## Averages in Benchmarks

Benchmarks often report mean latency, but means hide tail behavior. A few slow requests can dominate the arithmetic mean, so teams pair it with percentiles such as p50, p95, and p99, and with standard deviation, when summarizing response times. Outliers such as connection-timeout spikes should be identified and understood before the mean is trusted, and the measurement window and workload should be recorded with every result so different runs can be compared.

## Summary

Whichever sense of "average" applies — the SQL aggregate or a benchmark metric — the useful practice is the same: know exactly what is being averaged, handle outliers explicitly, and report the shape of the distribution alongside the single number.

## Related Entities

- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aap-2|Aap 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aar|Aar
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aarrr|Aarrr
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/abi|Abi
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/accr-2|Accr 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/ace-core|Ace Core
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acid|Acid
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acli|Acli
