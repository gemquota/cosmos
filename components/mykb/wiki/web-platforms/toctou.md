---
type: "concept"
title: "TOCTOU Vulnerabilities"
description: "Time-of-check to time-of-use gaps in authorization and files"
tags: ["concurrency", "security", "filesystem", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# TOCTOU Vulnerabilities

## Summary
Time-of-check to time-of-use gaps in authorization and files. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Check-then-use gaps let state change between check and use
- Atomic operations and re-validation after acquisition close gaps
- Open question — how do CAS-style operations map to filesystems?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/web-platforms/atomic-writes|Atomic Writes]] — related coverage in the same cluster
- [[wiki/web-platforms/file-locks|File Locking]] — related coverage in the same cluster
- [[wiki/web-platforms/race-conditions-web|Race Conditions on the Web]] — related coverage in the same cluster
- [[wiki/api-protocols/idempotency|Idempotency]] — related coverage in the same cluster
- [[wiki/api-protocols/optimistic-concurrency|Optimistic Concurrency]] — related coverage in the same cluster
- [[wiki/web-platforms/web-apis|Web APIs]] — related coverage in the same cluster
