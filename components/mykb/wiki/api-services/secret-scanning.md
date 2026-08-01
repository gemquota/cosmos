---
type: "concept"
title: "Secret Scanning"
description: "Automated detection of credentials committed to repositories and other surfaces"
tags: ["secret-scanning", "credentials", "repos", "detection"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning"]
---

# Secret Scanning

- Secret scanning detects API keys, tokens, and passwords that leak into source control, issues, or chat.
- Platforms (GitHub, GitLab) scan history and notify owners; the leaked secret must be rotated, not just deleted.
- Prevention pairs scanning with secret managers, pre-commit hooks, and short-lived credentials.
- For mykb: scanning every repo plus rotating anything found is the minimum bar for API key hygiene.

## Related

- [[wiki/api-services/api-key-management|API Key Management]] — the keys scanning protects
- [[wiki/security/secrets-management|Secrets Management]] — where secrets should live instead
- [[wiki/identity/key-rotation|Key Rotation]] — rotating leaked credentials
- [[wiki/devops-infra/github-actions|GitHub Actions]] — scanning in CI
