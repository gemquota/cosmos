---
type: "concept"
title: "HTTP Status Checks"
description: "Using HTTP response codes to verify source URLs"
tags: ["http", "status", "verification", "references"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# HTTP Status Checks

## Summary
HTTP status checks fetch a URL and read its response code: 200 means live, 3xx means moved, 4xx means gone, and 5xx means the server is failing.

## Details
- Checks must follow redirects and treat them deliberately — a 301 to a new canonical URL is a signal, not a failure.
- Rate and volume are governed: full-wiki checks are scheduled and throttled so monitoring does not look like an attack.
- For mykb, status checks are the raw input to dead-link detection, and only 200s count as verified sources at promotion time.

## Related
- [[wiki/api-services/dead-link-detection|Dead Link Detection]]
- [[wiki/api-services/link-rot-monitoring|Link-Rot Monitoring]]
- [[wiki/cloud-infra/source-vetting|Source Vetting]]
- [[wiki/api-protocols/http-status-checks|HTTP Status Checks]]
- [[wiki/api-protocols/url-formatting|URL Formatting]]
- [[wiki/concepts/verifiability-score|Verifiability Score]]
