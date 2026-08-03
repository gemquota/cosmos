---
type: "concept"
title: "Object Lock & WORM"
description: "Write-once-read-many protection on object storage"
tags: ["object-lock", "worm", "compliance", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Object Lock & WORM

## Summary

Object lock (S3), WORM (Azure immutability, GCP retention policies) make objects undeletable and unmodifiable for a set period — compliance-mode locks are absolute; governance mode allows permissioned exceptions. They are the enforcement layer for retention and anti-tamper requirements.

## Details
- Mechanism: S3 Object Lock applies legal holds (until removed) or retention periods (days/years) per object or bucket default; compliance mode cannot be removed by any user including root; governance mode can be lifted by privileged principals; Azure blob immutability (time-based and legal hold) and GCP retention policies (with lock option) are the equivalents. Versioning must be enabled for S3 object lock.
- Concrete example: a securities firm locks trade records for 7 years in compliance mode so even a compromised admin cannot purge them; an incident-response team stores evidence with legal hold; a backup bucket uses governance lock so automation can extend but not accidentally delete. Misuse: compliance locks that block legitimate deletion until the retention clock expires.
- Failure modes: forgetting versioning, making object lock impossible; retention periods misconfigured (years too long, blocking storage reclamation); legal holds without release procedures accumulating forever; and object lock applied to a bucket where lifecycle rules conflict, causing unexpected retains or denials.
- Operational tradeoffs: immutability guarantees integrity at the cost of operational flexibility — plan retention durations with legal/compliance input and test the governance release path; compliance locks are a strong deterrent to insider deletion and ransomware (delete-key attacks can still lock out access, so protect credentials separately).
- RSIS3/mykb relevance: the wiki's evidence and backup buckets use object lock; this note records the retention matrix and release runbook the loop consults before changing lifecycle policies.
- Cost modeling: immutability grows storage monotonically until retention expires; model the growth when setting periods so the compliance feature does not become a surprise bill. Review lock coverage quarterly — new buckets without versioning create enforcement gaps.

## Related
- [[wiki/cloud-infra/object-storage-protocols|Object Storage Protocols]]
- [[wiki/cloud-infra/object-storage|Object Storage]]
