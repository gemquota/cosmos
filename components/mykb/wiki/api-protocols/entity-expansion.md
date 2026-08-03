---
type: "concept"
title: "Entity Expansion"
description: "Parser features that let small documents expand into large structures"
tags: ["security", "xml", "parsing", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Entity Expansion

## Summary
Entity expansion is the parser feature behind billion-laughs and related amplification attacks: a small document references entities that resolve into much larger structures, exhausting memory or CPU. The mitigation is limiting, disabling, or sandboxing entity processing.

## Details
Entities are XML's macro feature: <!ENTITY name "value"> defines a replacement, and &name; expands it wherever it appears. Legitimate uses are small and bounded; attacks make the expansion recursive or multiplicative. In billion-laughs, entities reference other entities that reference others, so the expansion is exponential. In quadratic blowup, a document with N entity references of size N resolves to N^2 output bytes — a 1-megabyte file can become gigabytes.

The mechanism: parsers that process DTDs resolve entities as they build the tree, either eagerly (all entities expanded regardless of use) or lazily (expanded on reference). The cost is paid in memory (expanded text retained) and CPU (resolution work). Because the document itself is tiny, conventional request-size limits do not apply; the limits must be on expansion behavior: entity count, nesting depth, total expanded size, and external entity references.

Concrete example: an API accepts XML configs and parses with a DOM parser and DTD processing enabled. A 200-byte payload with ten nested ten-fold entities forces the parser to materialize 10^10 copies — an instant OOM. The same parser also resolves external entities, enabling file reads (XXE) when the DTD references file:// — entity expansion and XXE are the same knob.

Failure modes: libraries that disable DTD by default can be re-enabled through configuration (DOCTYPE in the payload); limits that only check output size still allow CPU exhaustion from expansion attempts; and parsers that resolve external entities add SSRF and local file disclosure on top of the memory cost. JSON and YAML have analogous issues (deep nesting, alias expansion) that need their own depth and count caps.

Operational tradeoffs: disabling DTD processing entirely is the correct default for virtually all API input; where DTDs are genuinely required, enforce entity count, depth, and total-size caps and prohibit external entities. The same hardening applies to any parser in the ingestion path, including third-party dependencies that auto-parse. Load tests with adversarial documents prove the caps hold.

RSIS3/mykb relevance: the wiki's ingestion and parsing tooling must treat entity expansion limits as a standing configuration check; encoding the caps here lets RSIS3 verify parser settings across runs.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/api-protocols/timing-attacks|Timing Attacks]]
- [[wiki/api-protocols/padding-oracle|Padding Oracle]]
- [[wiki/api-protocols/hash-collision-dos|Hash Collision DoS]]
- [[wiki/security-auth/cve-disclosures|CVE Disclosures]]
- [[wiki/api-protocols/rate-limiting|Rate Limiting]]
- [[wiki/api-protocols/backpressure|Backpressure]]
