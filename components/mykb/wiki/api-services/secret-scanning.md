---
type: "concept"
title: "Secret Scanning"
description: "Automated detection of credentials committed to repositories and other surfaces"
tags: ["secret-scanning", "credentials", "repos", "detection"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning", "https://docs.gitlab.com/ee/user/application_security/secret_detection/"]
---

# Secret Scanning

## Summary


## Details
- Secret scanning detects credentials — API keys, tokens, passwords, and private keys — that were accidentally committed to a repository.
- It works both historically (scanning the whole git history) and at push time (blocking or warning on new commits).
- The response is a playbook: rotate the leaked secret immediately, scrub history, and confirm the secret was not used elsewhere.
- Prevention is complementary: secret linting, environment variables, and tooling that never writes secrets to disk.
- **Worked example / comparison** — Worked example — a developer commits a .env file; push-time scanning blocks it, the secret is rotated before it is ever used, and history scrubbing removes the copy.
- For mykb, secret scanning is the enforcement layer under the workspace-hygiene practices the wiki documents.

## Related
- [[wiki/api-services/api-key-management|API Key Management]]
- [[wiki/security/secrets-management|Secrets Management]]
- [[wiki/identity/key-rotation|Key Rotation]]
- [[wiki/devops-infra/github-actions|GitHub Actions]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/security/secrets-management|Secrets Management]]
