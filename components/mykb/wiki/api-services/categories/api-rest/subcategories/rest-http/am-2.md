---
status: "growing"
type: "entity"
title: "AM"
description: "YAML (YAML Ain't Markup Language)"
tags: ["acronym", "android", "angular", "api", "ast", "auth", "aws", "bash", "bug", "entity"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
---

## Am 2

YAML (YAML Ain't Markup Language) — a human-readable data serialization language. Used for configuration files in Docker, CI/CD, and Kubernetes.

**Related topics:** android, angular, api, auth, aws, bash, bug

**Domain:** Mobile Platform › [[wiki/web-platforms/index|Android Core]] › [[wiki/web-platforms/index|Api Clients › Am 2

## Overview

YAML is an indentation-sensitive data format designed for configuration rather than programmatic data exchange. It is a superset of JSON, so every JSON document is valid YAML, but it adds features that make hand-written configuration pleasant: comments, multi-line strings, anchors, and merge keys. These properties make it the default format for Docker Compose files, CI/CD pipeline definitions, Kubernetes manifests, and the frontmatter of wiki notes.

## Common Uses

- **Docker and containers**: Compose services, build arguments, and volume definitions.
- **CI/CD**: GitHub Actions workflows, GitLab CI, and Ansible playbooks.
- **Kubernetes**: manifests for Deployments, Services, and ConfigMaps.
- **Documentation**: YAML frontmatter stores metadata such as title, tags, and timestamps.

## Syntax Notes

- Indentation defines structure; two spaces is the convention, and tabs are invalid.
- Scalars can be quoted or unquoted; quoting avoids ambiguity for strings that look like numbers or booleans.
- Anchors (`&name`) and aliases (`*name`) reuse blocks; merge keys (`<<`) combine mappings.
- Long strings use literal (`|`) or folded (`>`) block scalars for readability.

## Comparison to JSON

YAML is a superset of JSON, but the two formats differ in practice. JSON documents parse cleanly as YAML, while YAML adds comments, anchors, and block scalars that JSON lacks. YAML 1.1 treated unquoted `yes`, `no`, `on`, and `off` as booleans, a common source of bugs; YAML 1.2 aligns scalar typing more closely with JSON, but quoting values that look like booleans or numbers remains the safest habit.

## Validation and Tooling

Configuration files benefit from automated checks before they reach a runtime. Tools such as `yamllint` enforce style rules, `yq` reads and transforms documents in scripts, and JSON Schema validators catch structural mistakes in the YAML-compatible subset. Kubernetes applies strict schema validation to manifests, and CI pipelines typically lint configuration alongside code so a typo fails fast instead of surfacing at deploy time.

## Related Concepts

- [[wiki/dev-tools/yaml-configs|YAML Configs]] — configuration conventions in tooling
- [[wiki/data-storage/yaml-frontmatter|YAML Frontmatter]] — metadata headers in wiki notes
- [[wiki/devops-infra/kubernetes|Kubernetes]] — the largest YAML manifest ecosystem
- [[wiki/api-protocols/json-schema|JSON Schema]] — validation for YAML-compatible data

## Related Entities

- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aap-2|Aap 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aar|Aar
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aarrr|Aarrr
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/abi|Abi
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/accr-2|Accr 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/ace-core|Ace Core
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acid|Acid
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acli|Acli
