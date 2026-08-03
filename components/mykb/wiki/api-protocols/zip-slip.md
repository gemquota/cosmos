---
type: "concept"
title: "Zip Slip"
description: "Path traversal via archive entries that escape the extraction directory"
tags: ["security", "file-upload", "attacks", "paths"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Zip Slip

## Summary
Zip Slip is a path-traversal vulnerability in archive extraction: a malicious zip, tar, or other archive contains entry names like `../../etc/cron.d/evil` or absolute paths, and an extraction routine that trusts those names writes files outside the intended directory. A single crafted upload can overwrite application code, configuration, or system files, converting an innocent "extract this archive" feature into remote code execution.

## Details
- Mechanism: archives store entry names as arbitrary strings. A naive extractor joins the destination directory with the entry name and opens the result for writing; an entry named `../../app/config.py` resolves outside the destination, so the write lands in a location the developer never intended. The vulnerability appears in nearly every language because default extraction helpers historically did not validate paths: Python's `zipfile.extractall`, Java's `ZipInputStream`, and many Node.js tar libraries were affected or shipped vulnerable examples, and CVE-2018-1000001 (the original Zip Slip advisory) catalogued hundreds of affected products.
- Concrete examples: an upload endpoint that accepts a zip of report templates and extracts to a per-user directory — a crafted entry overwrites a shared template file that the server later renders; a dependency installer that extracts a package tarball where an entry named `../../.ssh/authorized_keys` plants an attacker key; a backup-restore feature where an archive entry lands in the web root as a PHP script, enabling direct code execution.
- Failure modes: the failure chain is: (1) no validation of entry names before writing, (2) validation that is not canonicalized (checking the raw string for `..` but missing `..%2f`, backslashes, or absolute paths, or being bypassed by symlink entries whose targets escape), and (3) missing symlink handling, where an archive that first writes a symlink and then writes through it redirects files outside the root even with name checks. Zip Slip is also a second-order problem: archives can be nested, so a zip inside a zip must be validated recursively.
- Operational tradeoffs: the defense is mechanical: before writing each entry, resolve `destination + entry_name` with the same canonicalization the filesystem will use, and require the result to stay within the destination root; reject or skip entries that escape, and reject absolute paths and drive-letter prefixes. Symlinks require special care — either extract them as plain files or verify their targets too. Extraction libraries now ship safe-by-default APIs, so prefer them and add a test that extracts a malicious fixture and asserts no file is written outside the sandbox.
- RSIS3/mykb relevance: MyKB's import and snapshot features are archive consumers; the standing rule is to extract only into a dedicated directory with canonical path checks and a symlink policy, mirroring RSIS3's hygiene of validating untrusted input before it touches persistent state.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/api-protocols/cache-poisoning|Cache Poisoning]]
- [[wiki/api-protocols/request-smuggling|Request Smuggling]]
- [[wiki/api-protocols/ssrf-practice|SSRF Attacks]]
- [[wiki/security-auth/ssrf-prevention|SSRF Prevention]]
- [[wiki/security-auth/deserialization-attacks|Deserialization Attacks]]
- [[wiki/security-auth/privilege-escalation|Privilege Escalation]]
