---
type: "concept"
title: "Atomic Writes"
description: "Replacing files via temp file and rename to avoid partial states"
tags: ["filesystem", "reliability", "data", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Atomic Writes

## Summary
Replacing files via temp file and rename to avoid partial states. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Write-temp-then-rename prevents readers seeing partial files
- fsync ordering decides durability, not just rename
- Open question — how do journals and WALs extend atomicity?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/web-platforms/file-locks|File Locking]] — related coverage in the same cluster
- [[wiki/web-platforms/race-conditions-web|Race Conditions on the Web]] — related coverage in the same cluster
- [[wiki/web-platforms/toctou|TOCTOU Vulnerabilities]] — related coverage in the same cluster
- [[wiki/api-protocols/idempotency|Idempotency]] — related coverage in the same cluster
- [[wiki/api-protocols/optimistic-concurrency|Optimistic Concurrency]] — related coverage in the same cluster
- [[wiki/web-platforms/web-apis|Web APIs]] — related coverage in the same cluster
