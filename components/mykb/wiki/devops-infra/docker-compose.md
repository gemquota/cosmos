---
type: "concept"
title: "Docker Compose"
description: "Declarative local multi-container orchestration with a single YAML file"
tags: ["docker", "compose", "containers", "devops", "local-dev"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Docker Compose

## Summary
Docker Compose defines and runs multi-container apps from `compose.yaml`: services, networks, volumes, and env in one file. It is the standard for local development environments.

## Details
- `docker compose up` builds and starts the stack; `down` tears it down; profiles and overrides vary environments.
- Great for standing up Postgres, Redis, and the mykb daemon together on a laptop.
- Compose is dev-focused; production-grade orchestration belongs to Kubernetes.

## Related
- [[wiki/devops-infra/kubernetes|Kubernetes]] — production orchestration counterpart
- [[wiki/security/container-hardening|Container Hardening]] — apply to local images too
- [[wiki/devops-infra/postgresql|PostgreSQL]] — typical compose service
- [[wiki/api-protocols/rabbitmq|RabbitMQ]] — local broker stacks
- [[wiki/devops-infra/terraform|Terraform]] — cloud provisioning beyond local
