---
type: "concept"
title: "File Upload Security"
description: "Hardening endpoints that accept user files against malware, bombs, and traversal"
tags: ["security", "uploads", "http", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# File Upload Security

## Summary
File upload endpoints are a favorite target: they combine user-controlled bytes, content-type confusion, path traversal, decompression bombs, and stored-XSS risks. Hardening them means validating at every layer — size, type, storage, and serving.

## Details
A secure upload pipeline validates: request limits (max size, count, rate), content sniffing versus declared type (never trust the client's Content-Type or filename), actual file content (magic bytes), storage location (outside the web root, randomized names, no user-controlled paths), and serving policy (Content-Disposition attachment, nosniff, correct MIME). Each layer assumes the one before failed.

The mechanism: the server streams the upload to a quota-limited location, checks the magic bytes against an allowlist, re-encodes images or renames to server-generated names, stores with restrictive permissions, and serves from a path that cannot execute scripts. Archive uploads are extracted only under strict caps (entry count, total size, ratio) to defuse zip bombs. Antivirus or malware scanning adds a quarantine step where the threat model justifies it.

Concrete example: a wiki avatar upload accepts JPEG and PNG. The server rejects files larger than 2MB, verifies 0xFFD8 or PNG magic, strips EXIF, re-encodes to a fixed-size image, stores as avatar_<uuid>.png, and serves with Content-Type: image/png plus nosniff. An attacker uploading a PHP file named avatar.png gets a re-encoded image or a rejection — the payload never reaches the server's script interpreter.

Failure modes: trusting the client filename enables path traversal (../../etc/cron.d/x) and stored XSS (filename with script); trusting Content-Type enables polyglot files; storing in the web root enables direct script execution; missing size caps enable disk-filling and decompression-bomb DoS; and serving user files as inline HTML re-enables the stored-XSS chain that nosniff and attachment headers are meant to block.

Operational tradeoffs: strict type allowlists and re-encoding add CPU and can reject legitimate rare formats; randomizing names breaks user-facing URL conventions but kills traversal and guessing; per-tenant quotas bound abuse. The baseline is defense in depth: validate bytes, isolate storage, randomize names, serve safely, and log every upload for audit.

RSIS3/mykb relevance: any attachment feature in the wiki or dashboard inherits this checklist; encoding the pipeline contract lets RSIS3's security reviews verify each layer in order.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/api-protocols/zip-slip|Zip Slip]]
- [[wiki/api-protocols/cache-poisoning|Cache Poisoning]]
- [[wiki/api-protocols/request-smuggling|Request Smuggling]]
- [[wiki/security-auth/ssrf-prevention|SSRF Prevention]]
- [[wiki/security-auth/deserialization-attacks|Deserialization Attacks]]
- [[wiki/security-auth/privilege-escalation|Privilege Escalation]]
