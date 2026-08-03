---
type: "concept"
title: "Billion Laughs"
description: "XML entity-expansion attack that grows output exponentially"
tags: ["security", "xml", "dos", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Billion Laughs

## Summary
The billion laughs attack is an XML entity-expansion bomb: nested entity definitions expand exponentially, exhausting memory or CPU. It is the archetype of amplification attacks and motivates entity limits in every parser.

## Details
Billion laughs (also the XML bomb) works by defining entities that reference other entities: <!ENTITY a "123"><!ENTITY b "&a;&a;...">. Each entity references the previous one multiple times, so a tiny document — a few hundred bytes — expands to gigabytes during parsing. The canonical payload defines a0..a9 where each level references the prior level ten times, producing 10^10 copies of the literal.

The mechanism: the XML parser resolves entities as it builds the document tree. When entities are nested by reference, resolution is recursive and multiplicative; parsers that expand all entities eagerly (SAX or DOM with DTD processing on) compute the full expansion even if the app only reads one element. The same amplification pattern appears in other recursive-expansion contexts: zip bombs, JSON nesting bombs, YAML alias bombs, and gzip bombs.

Concrete example: an API accepts XML invoices; an attacker POSTs a one-kilobyte document with nested entities. The parser expands it into three gigabytes of strings, exhausting the container's memory and causing an OOM restart — a cheap denial of service. The same endpoint also risks entity-based file reads (XXE) if the DTD can reference file:// or network URLs, which is why the mitigations overlap.

Failure modes: even with expansion limits, CPU can be exhausted before the byte limit trips; entity resolution that allows external DTDs adds SSRF and file-read; and libraries that only cap output size but not nesting depth or entity counts still die on deeply nested or wide structures. Parser misconfiguration — defaulting DTD processing on — is the root cause in most real incidents.

Operational tradeoffs: disabling DTD and entity processing entirely is the safe default for APIs that never need custom DTDs; where entities are required, cap entity count, nesting depth, expansion ratio, and total output bytes, and reject anything over the caps. The same limits should apply to JSON depth and YAML alias counts. Load tests should include adversarial documents so the caps are proven, not assumed.

RSIS3/mykb relevance: this is a canonical failure mode for the wiki's ingestion tooling — any parser that touches untrusted documents needs entity limits; encoding the limits here lets check-practices verify parser configuration.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/api-protocols/entity-expansion|Entity Expansion]]
- [[wiki/api-protocols/timing-attacks|Timing Attacks]]
- [[wiki/api-protocols/padding-oracle|Padding Oracle]]
- [[wiki/security-auth/cve-disclosures|CVE Disclosures]]
- [[wiki/api-protocols/rate-limiting|Rate Limiting]]
- [[wiki/api-protocols/backpressure|Backpressure]]
