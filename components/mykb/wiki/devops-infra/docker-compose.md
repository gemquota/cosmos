---
type: "concept"
title: "Docker Compose"
description: "Declarative local multi-container orchestration with a single YAML file"
tags: ["docker", "compose", "containers", "devops", "local-dev"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.docker.com/compose/", "https://docs.docker.com/compose/compose-file/"]
---

# Docker Compose

## Summary
Docker Compose defines and runs multi-container apps from `compose.yaml`: services, networks, volumes, and env in one file. It is the standard for local development environments.

## Details
- `docker compose up` builds and starts the stack; `down` tears it down; profiles and overrides vary environments.
- Great for standing up Postgres, Redis, and the mykb daemon together on a laptop.
- Compose is dev-focused; production-grade orchestration belongs to Kubernetes.
- Docker Compose defines multi-container applications in a YAML file, declaring services, networks, volumes, and dependencies for local development.
- One command (docker compose up) builds and runs the whole stack, and profiles extend it to selectable service groups.
- Compose is the standard for local development and CI of composed services, though production often migrates to orchestration like Kubernetes.
- The file is the contract: environment, ports, healthchecks, and dependencies live in version-controlled YAML.
- **Worked example / comparison** — Worked example — the wiki's dev stack is a compose file with a web service, a graph worker, and a database service on a shared network, started with one command.
- For mykb, docker-compose is documented as the local multi-service runtime, the on-ramp to the kubernetes article.

## Related
- [[wiki/devops-infra/kubernetes|Kubernetes]]
- [[wiki/security/container-hardening|Container Hardening]]
- [[wiki/devops-infra/postgresql|PostgreSQL]]
- [[wiki/api-protocols/rabbitmq|RabbitMQ]]
- [[wiki/devops-infra/terraform|Terraform]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/decision-guides|Decision Guides]]
