---
type: "concept"
title: "Compression & Brotli"
description: "Content-encoding negotiation and when Brotli beats gzip"
tags: ["compression", "brotli", "gzip", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Compression & Brotli

## Summary
Compression reduces transfer size for text payloads. Brotli is Google's modern alternative to gzip, typically achieving 10-20% smaller output on HTML, JS, and CSS at similar or higher CPU cost; zstd is a third option with very fast decompression. Negotiation happens through Accept-Encoding, selection by content type, and application at the proxy or origin.

## Details
- gzip versus Brotli: Brotli (levels 1-11) usually beats gzip on web text because its dictionary is trained on web content; decompression speed matters most since browsers decompress once per download. zstd offers tunable speed-to-ratio tradeoffs and extremely fast decode.
- Mechanism: the server inspects `Accept-Encoding` (brotli, gzip), picks the best supported, and sets `Content-Encoding`; precompressed static assets avoid per-request CPU cost; dynamic responses trade CPU for bytes on every request, so cache compressed output and set `Vary: Accept-Encoding`.
- Concrete example: nginx with `brotli_static` serving precompressed `.br` files; a CDN edge compressing responses with Brotli level 5 and caching per encoding; an API that compresses JSON only above about 1 KB to avoid overhead on tiny responses.
- Failure modes: compressing already-compressed content (images, video) wastes CPU and can enlarge payloads — disable it for binary MIME types; a missing `Vary: Accept-Encoding` poisons caches, serving a Brotli copy to a gzip-only client; very low edge compression levels negate the benefit; high-level dynamic Brotli exhausts origin CPU under load.
- Tradeoffs: Brotli's best ratios cost encode time — level 11 is unsuitable for dynamic content, so precompress; gzip remains the baseline for dynamic content; zstd sits between on speed.
- Operational notes: test with `curl --compressed` and inspect `Content-Encoding`, measure byte savings per content class, and monitor origin CPU when enabling dynamic Brotli.
- RSIS3 relevance: the dashboard and wiki pages are static text — precompressing generated HTML and JSON with Brotli cuts egress and load time without touching the content pipeline.

## Related
- [[wiki/infrastructure/compression-in-storage|Compression in Storage]]
- [[wiki/os-shell/compression-tools|Compression Tools]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
