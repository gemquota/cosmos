---
type: "index"
title: "Wiki Index — Where to Look"
description: "Nested navigation map for the mykb knowledge base: pick a family, then a folder; every folder has an index page."
tags: ["index", "navigation", "mykb"]
timestamp: "2026-08-02T00:00:00Z"
---

# Wiki Index — Where to Look

This page is the map of the knowledge base. Pick a **family** below, then open
the folder's `index.md` for its full listing. The sidebar (Docs tab) mirrors
the folder structure; Search and the Graph tab work across everything.

## 1. Foundations & Concepts
- [[wiki/concepts/index|concepts/]] — cross-cutting ideas and research reports
  (mykb system reports, nine-loop hierarchy, open questions)

## 2. Frontend & UI
- [[wiki/frontend/index|frontend/]] — HTML/CSS/JS, frameworks
  (angular, ajax-spa, bootstrap), styling, UI patterns
- [[wiki/frontend-frameworks/index|frontend-frameworks/]] — framework entity notes
- [[wiki/js-ts-ecosystem/index|js-ts-ecosystem/]] — JavaScript/TypeScript tooling
- [[wiki/web-platforms/index|web-platforms/]] — browser & web platform concepts

## 3. Backend & APIs
- [[wiki/api-services/index|api-services/]] — REST/HTTP services, API clients, JSON
- [[wiki/api-protocols/index|api-protocols/]] — HTTP methods, status codes, protocol design
- [[wiki/cloud-infra/index|cloud-infra/]] — cloud hosting & infrastructure services

## 4. Security & Identity
- [[wiki/security-auth/index|security-auth/]] — authentication, authorization, web security
- [[wiki/security/index|security/]] — general security concepts
- [[wiki/identity/index|identity/]] — identity, sessions, MFA, password policy

## 5. Data & Storage
- [[wiki/data-storage/index|data-storage/]] — databases, storage engines, caching, streaming

## 6. Infrastructure & DevOps
- [[wiki/infrastructure/index|infrastructure/]] — containers, networking, service mesh
- [[wiki/devops-infra/index|devops-infra/]] — CI/CD, deployment, SRE
- [[wiki/development/index|development/]] — dev workflows, CLI tools, ORMs
- [[wiki/dev-tools/index|dev-tools/]] — developer tooling entities
- [[wiki/tooling/index|tooling/]] — shell/CLI tooling entities

## 7. Shell & OS
- [[wiki/os-shell/index|os-shell/]] — shell scripting, POSIX, text processing
- [[wiki/shell-environment/index|shell-environment/]] — shell environment entities

## 8. AI / ML / Agents
- [[wiki/ai-ml/index|ai-ml/]] — machine learning concepts and models
- [[wiki/ml-frameworks/index|ml-frameworks/]] — ML frameworks
- [[wiki/meta-learning/index|meta-learning/]] — meta-learning and self-improvement
- [[wiki/llm-agents/index|llm-agents/]] — LLM agent patterns
- [[wiki/agent-systems/index|agent-systems/]] — agent architecture (loops, delegation, memory)
- [[wiki/prompt-engineering/index|prompt-engineering/]] — prompt patterns and techniques

## 9. Platforms
- [[wiki/android-core/index|android-core/]] — Android platform
- [[wiki/mobile-platform/index|mobile-platform/]] — mobile concepts

## 10. Engineering & Testing
- [[wiki/testing/index|testing/]] — testing strategies and tools
- [[wiki/software-engineering/index|software-engineering/]] — architecture, refactoring, ADRs

## 11. Memory & Synthesis
- [[wiki/memory/index|memory/]] — personal knowledge management, note systems, provenance
- [[wiki/syntheses/index|syntheses/]] — distilled cross-session conclusions
- [[wiki/compositions/index|compositions/]] — instruction-set bundles (setup, dev workflow, API, data, security, devops, languages)
- [[wiki/decisions/index|decisions/]] — recorded architecture decisions

## 12. Project Records & OKF Types
- [[wiki/episodes/index|episodes/]] · [[wiki/experiments/index|experiments/]] ·
  [[wiki/pulses/index|pulses/]] · [[wiki/questions/index|questions/]] ·
  [[wiki/reflections/index|reflections/]] · [[wiki/projects/index|projects/]] ·
  [[wiki/sources/index|sources/]] · [[wiki/plans/index|plans/]] · [[wiki/ops/index|ops/]]
- [[wiki/entities/index|entities/]] — RSIS3 system entities (memory client, pulse engine, …)
- [daily/](daily/README.md) — daily notes

## 13. Archives (kept for history)
- [raw/archive/](../raw/README.md) — session artifacts, archived junk
  entities, old audits. Not part of the active knowledge map.

---

### Quick "where does X live?" lookup

| You want… | Look in |
|-----------|---------|
| Auth / login / OAuth | `security-auth/` |
| REST, HTTP, API clients | `api-services/` + `api-protocols/` |
| Shell scripting / bash | `os-shell/` |
| React, Angular, CSS | `frontend/` |
| Databases, caching, SQL | `data-storage/` |
| Docker, CI/CD, deployment | `infrastructure/` + `devops-infra/` |
| ML models, prompting, agents | `ai-ml/` + `llm-agents/` + `agent-systems/` |
| PKM / note-taking / zettelkasten | `memory/` |
| Distilled conclusions | `syntheses/` |
| Setup / workflow instruction sets | `compositions/` |

*See also: [Home](../Home.md) · [Iteration Log](log.md) · [Wiki Schema](../ops/wiki-schema.md)*
