---
type: "concept"
title: "Decompression Bombs"
description: "Small compressed payloads that expand into huge data during decompression"
tags: ["security", "dos", "compression", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Decompression Bombs

## Summary
A decompression bomb is a small compressed payload — zip, gzip, or similar — that expands to an enormous size during decompression, exhausting memory, disk, or CPU. Like entity expansion, it is amplification delivered through a legitimate format.

## Details
The canonical zip bomb is a small archive whose entries are highly compressible (zeros or repeated patterns). A 42-kilobyte zip can expand to terabytes because each entry itself contains a nested archive. gzip bombs work the same way: a few megabytes of compressed zeros can decompress to gigabytes. The amplification ratio is the attack; the format is otherwise legitimate.

The mechanism: decompression is streamed, so the damage happens incrementally as bytes are produced. An API that reads the whole response into memory, or a server that extracts an upload to disk without limits, is vulnerable. The worst cases are nested archives (a zip inside a zip) and formats with high compression ratios, where a small byte budget defeats size-only checks on the compressed input.

Concrete example: an API accepts .zip uploads and extracts them to a temp directory. An attacker uploads a 10-megabyte zip that expands to 100 gigabytes of zeros across thousands of entries. The extraction loop writes until the disk fills or the process is OOM-killed — a denial of service that costs the attacker nothing. The fix: cap total uncompressed size, entry count, compression ratio, and nesting depth before and during extraction.

Failure modes: checking only the compressed file size is useless against high-ratio bombs; streaming limits that are not enforced during extraction (only after) still let the process exhaust memory; and decompression of attacker data in middleware — request body decompression, log parsing — happens before application-level limits can run. Libraries that auto-decompress (axios, requests, tar) inherit the risk silently.

Operational tradeoffs: enforcing limits requires streaming decompression with a running byte count and abort on exceed, which adds code but no user-visible cost; rejecting high-ratio inputs outright can break legitimate large-but-true payloads, so limits must be documented and tunable. Defense in depth: run extraction in sandboxed storage with quota, cap per-request body size, and rate-limit upload endpoints.

RSIS3/mykb relevance: the wiki's ingestion pipeline should treat any compressed artifact as untrusted; documenting the byte-cap and ratio-cap contract here gives RSIS3's check-practices a concrete limit to verify.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/billion-laughs|Billion Laughs]] — related coverage in the same cluster
- [[wiki/api-protocols/entity-expansion|Entity Expansion]] — related coverage in the same cluster
- [[wiki/api-protocols/timing-attacks|Timing Attacks]] — related coverage in the same cluster
- [[wiki/security-auth/cve-disclosures|CVE Disclosures]] — related coverage in the same cluster
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — related coverage in the same cluster
- [[wiki/api-protocols/backpressure|Backpressure]] — related coverage in the same cluster
