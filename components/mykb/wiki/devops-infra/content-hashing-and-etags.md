---
type: "concept"
title: "Content Hashing & ETags"
description: "Validator-based caching with hashes, ETags, and immutable assets"
tags: ["etag", "hashing", "caching", "http"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Content Hashing & ETags

## Summary
Content hashing and ETags let caches validate freshness without transferring the body: a server computes a fingerprint of the representation, sends it as an ETag, and clients send If-None-Match to receive a 304 Not Modified when content is unchanged. Hash-named static assets go further — the hash lives in the URL, making staleness impossible.

## Details
- Mechanism: strong ETags (byte-exact, for example a SHA-256 of the content) allow safe revalidation; weak ETags (W/) indicate only semantic equivalence. The client sends `If-None-Match: "<etag>"` and the server replies 304 with an empty body, saving bandwidth; without ETags the fallback is Last-Modified/If-Modified-Since, which has second-granularity and can miss changes.
- Concrete example: a JSON API computes the ETag as a hash of the response body; repeated client polls cost a 304 instead of a full payload; a static site builder emits hashed filenames (app.8f3a2b.js) with `Cache-Control: immutable`, so browsers never revalidate and a deploy changes the URL.
- Failure modes: ETags based on timestamps that are non-deterministic across replicas, causing false 200s or constant revalidation; hashing an uncompressed body while serving gzip — the representation differs, so include Content-Encoding in the hash; ETags not updated when underlying data changes, silently serving stale JSON (for example a hash computed from an unflushed cache).
- Tradeoffs: hash-in-URL gives perfect cache correctness but requires unique URLs per version and garbage collection of old assets; ETag revalidation keeps one URL but costs a small round trip per check. Choose by volatility — stable assets use immutable hash URLs, dynamic data uses ETag revalidation.
- Operational notes: set Cache-Control correctly alongside ETags (private for user-specific data), make ETags deterministic across instances, and monitor the 304 ratio to verify caching works.
- RSIS3 relevance: the dashboard's generated snapshot JSON should use hash names or ETags so refreshes see new telemetry immediately while browsers cache aggressively.

## Related
- [[wiki/infrastructure/ipfs-and-content-addressing|IPFS & Content Addressing]]
- [[wiki/cloud-infra/content-delivery-networks|Content Delivery Networks]]
- [[wiki/os-shell/checksums-and-hashing-tools|Checksums & Hashing]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
