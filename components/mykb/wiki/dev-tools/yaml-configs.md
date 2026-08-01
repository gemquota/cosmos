---
type: "concept"
title: "YAML Configs"
description: "Human-readable YAML files used to configure tools, pipelines, and applications"
tags: ["yaml", "config", "serialization", "tooling"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# YAML Configs

## Summary
YAML (YAML Ain't Markup Language) is a human-friendly data serialization format that has become the default for configuration: CI pipelines, Kubernetes manifests, and this wiki's frontmatter. Readability is its strength; type pitfalls are its weakness.

## Details
- Indentation is syntax; tabs break parsers. String-likes (yes/no, numbers) cause classic gotchas.
- Tools like yamllint and schema validation catch errors early.
- RSIS3 relevance: frontmatter and spec files in cosmos are YAML/JSON configs.

## Related
- [[wiki/data-storage/yaml-frontmatter|YAML Frontmatter]] — the wiki's metadata lives in YAML
- [[wiki/devops-infra/kubernetes|Kubernetes]] — manifests are YAML at scale
- [[wiki/devops-infra/docker-compose|Docker Compose]] — compose files configure dev stacks
- [[wiki/software-engineering/documentation-as-code|Documentation as Code]] — config-as-code shares the docs pipeline
