---
type: "concept"
title: "CORS Policy"
description: "Cross-origin resource sharing rules controlling which origins may read responses"
tags: ["cors", "browsers", "http", "apis"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS"]
---

# CORS Policy

- CORS relaxes the same-origin policy selectively: servers declare which origins may read responses via Access-Control-Allow-Origin.
- Misconfiguration — reflecting arbitrary origins, allowing credentials broadly, permissive methods — turns APIs into data-leak surfaces.
- Preflight (OPTIONS) requests gate non-simple requests; the policy must match actual API needs.
- For mykb: the API gateway should own a single CORS allowlist rather than per-service defaults.

## Related

- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — the baseline CORS relaxes
- [[wiki/api-services/api-key-management|API Key Management]] — browser-exposed keys interact with CORS
- [[wiki/api-protocols/rest-apis|REST APIs]] — the endpoints CORS protects
- [[wiki/security-auth/security-headers|Security Headers]] — header policy layer
