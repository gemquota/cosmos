---
type: "concept"
title: "HTTP Status Checks"
description: "Using status codes as machine-readable signals in link and API verification"
tags: ["http", "status-codes", "monitoring", "verification"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# HTTP Status Checks

## Summary
HTTP status checks treat response codes as machine-readable signals for link verification, uptime monitoring, and API health. The 2xx/3xx/4xx/5xx classification drives whether a check passes, retries, or fails.

## Details
A status check sends a request (HEAD or GET) and classifies the response: 2xx is healthy, 3xx requires following or evaluating the redirect, 4xx means the target is wrong (client or resource gone), and 5xx means the server is failing. Automated systems — dead-link detectors, uptime probes, contract tests — encode this classification as pass/fail/retry logic instead of leaving it to humans.

The mechanism: for link checking, a 404 means the URL is dead (or hidden), 410 means deliberately removed, and 301/308 mean the link should be updated to the new target — each with a different action. For API health, a 503 with Retry-After means "down for now, check later," while a 200 on the health endpoint means the service is serving. The nuance is that status alone is insufficient: the checker must also handle redirects, authentication (401 for private endpoints is healthy), and content-type expectations.

Concrete example: mykb's link-checker would scan wiki pages for wikilinks and URLs. A link that returns 404 would be flagged for review, a 301 would be auto-updated to the canonical location, and a 503 would schedule a recheck with backoff. A naive checker that treats every non-2xx as broken would churn on rate-limited (429) and temporarily unavailable (503) targets — which is why retry semantics belong in the checker.

Failure modes: treating 401/403 as broken links for authenticated resources produces false positives; following redirect chains without a hop limit hangs or loops; ignoring Retry-After and 429 hammers targets into blocking you; and HEAD checks that the server doesn't support can return 405 where GET would succeed — the checker should fall back to GET.

Operational tradeoffs: status checks are cheap and deterministic, but they measure reachability, not correctness — a page that returns 200 with an error body passes. Pair status checks with content checks (title, hash, schema) where correctness matters. Rate-limit your own checking, cap redirect hops, and classify 5xx as retryable so transient blips don't create alert noise.

RSIS3/mykb relevance: the wiki's link-checker and the dashboard's health views would both be status-check consumers; documenting the classification table here keeps the two implementations consistent.

## Related
- [[wiki/api-services/dead-link-detection|Dead Link Detection]]
- [[wiki/api-services/link-rot-monitoring|Link-Rot Monitoring]]
- [[wiki/cloud-infra/source-vetting|Source Vetting]]
- [[wiki/api-protocols/url-formatting|URL Formatting]]
- [[wiki/concepts/verifiability-score|Verifiability Score]]
