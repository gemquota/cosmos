---
type: "entity"
title: "CI/CD Patterns"
tags: ["devops", "ci", "cd", "github-actions", "automation"]
source: ["sessions/"]
---

# CI/CD Patterns

CI/CD patterns across the ecosystem.

## GitHub Actions
```yaml
name: Deploy
on: push
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: peaceiris/actions-gh-pages@v3
```

## Patterns
- Matrix testing across Python/node versions
- pip/npm caching for faster runs
- Conditional deploys (main branch only)
- Status badges in README

See also: [[wiki/devops-infra/index|DevOps & Infrastructure]], [[wiki/development/index|Development]]
