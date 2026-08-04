---
type: "entity"
title: "Files Created"
resource: ""
---
description: "Tracking and managing the files a process or agent creates as side effects"
tags: ["entity", "api", "ast", "auth", "authentication", "cli", "file-management"]
timestamp: "2026-07-19T22:41:41Z"

# Files Created

## Summary
Files Created is the practice of tracking which files a process, script, or agent creates during a run. It matters because unmanaged side effects litter workspaces, leak sensitive data, and make runs unreproducible. Knowing exactly what was written is the first step toward cleanup, audit, and safe automation.

## Details
- **Definition** — a run manifest records each file created, with path, size, and the step that produced it.
- **Why track** — side-effect awareness supports cleanup, reproducibility, review, and security auditing of what a run touched.
- **Naming discipline** — deterministic, prefixed paths in a designated workspace make created files easy to identify and clean up.
- **Cleanup policy** — ephemeral files should be removed on success, retained on failure for debugging, and swept by a scheduled policy otherwise.
- **Security** — files may contain tokens or personal data; tracking includes making sure permissions are restrictive and secrets never persist by default.
- **Reproducibility** — when runs recreate their outputs from a manifest, a later run can verify nothing extra or missing was produced.
- **Common failure modes** — writes to surprising locations such as home directories, leftover temp files, and overwrites of files the process did not own.
- **Worked example** — a report generator writes outputs under a run-scoped directory and logs each path; a cleanup step removes the directory unless a flag keeps it for debugging.
- **Practical relevance** — explicit file creation discipline keeps agent and CLI runs tidy, reviewable, and safe to rerun.

## Related
- [[wiki/tooling/file-storage|File Storage]] — where created files live
- [[wiki/tooling/archive-policies|Archive Policies]] — retention of produced artifacts
- [[wiki/data-storage/backup-strategies|Backup Strategies]] — protecting important outputs
- [[wiki/software-engineering/logging-strategies|Logging Strategies]] — recording what happened
- [[wiki/testing/smoke-testing|Smoke Testing]] — verifying run artifacts
- [[wiki/tooling/backup-verification|Backup Verification]] — checking written data
