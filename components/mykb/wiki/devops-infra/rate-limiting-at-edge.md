---
type: "concept"
title: "Rate Limiting at the Edge"
description: "Token-bucket limits enforced in CDN, gateway, or reverse proxy layers"
tags: ["rate-limiting", "edge", "gateway", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Rate Limiting at the Edge

## Summary
Rate limiting at the edge protects services before requests consume backend resources: CDN and gateway layers (Cloudflare, Fastly, nginx, Envoy) enforce request budgets per client, path, or token, rejecting or shaping excess traffic. Edge enforcement is the first line of defense against abuse, scraping, and traffic spikes.

## Details
- Mechanism: the edge tracks request rates per key (IP, user, API token, path) in a distributed counter or token bucket; limits are configured with burst allowances and rejection behavior (429, retry-after, queueing); policies differentiate classes of traffic — logged-in users get higher budgets than anonymous ones.
- Concrete example: a CDN rule allowing 100 requests/minute per IP for the public API and 10/minute for unauthenticated search; a gateway token bucket of 5,000 requests/hour per API key with a 429 and Retry-After on excess; bot protection rules that rate-limit known scraping patterns at the edge.
- Failure modes: IP-based limits behind NAT or shared egress punishing legitimate users; per-IP limits trivially bypassed by distributed attackers; rate limiting that kicks in during legitimate spikes (launch day), blocking real users — set limits from capacity, not habit; backend still overwhelmed because the edge limit is too generous or keyed incorrectly; 429 handling that is not client-visible, causing silent retry storms.
- Tradeoffs: edge rate limiting is cheap to operate and scales with the CDN, but it lacks backend context (per-user quotas, business rules); the common stack is edge limits for abuse and coarse protection plus service-level limits for fine-grained, business-aware quotas; the tradeoff is where enforcement lives versus what it can know.
- Operational notes: monitor 429 rates and limit hits, size limits from real capacity, and make rejection responses actionable.
- RSIS3 relevance: the dashboard and wiki API behind an edge benefit from limits that keep scrapers and misbehaving clients from starving the daemon — a config change, not a code change.

## Related
- [[wiki/cloud-infra/cdns-and-edge-networking|CDNs & Edge Networking]] — related coverage in the same cluster
- [[wiki/cloud-infra/edge-locations|Edge Locations]] — related coverage in the same cluster
- [[wiki/cloud-infra/edge-computing|Edge Computing]] — related coverage in the same cluster
- [[wiki/infrastructure/data-encryption-at-rest|Data Encryption At Rest]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
