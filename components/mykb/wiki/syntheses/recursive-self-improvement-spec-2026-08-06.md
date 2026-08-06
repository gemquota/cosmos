---
type: "synthesis"
title: "Recursive Self-Improvement Specification — SPACE v2 Export"
description: "The completed 326-probe SPACE session (67/67 questions, 67 artifacts) that pins down what recursive self-improvement is and how RSIS3 should be built and operated"
tags: ["recursive-self-improvement", "space", "specification", "rsis3", "architecture", "export"]
timestamp: "2026-08-06T13:56:00Z"
status: "growing"
---

# Recursive Self-Improvement Specification — SPACE v2 Export

## Summary
The `recursive-self-improvement` project completed a full SPACE v2.0.0
elicitation session (`sess_cdd506e4`, 67/67 questions, 259 multi-choice
options) and exported the resulting specification. The spec fixes the
identity of the domain — **SPACE itself is the subject**: a programmable
specification engine that transforms structured elicitation probes into
development specifications, sitting at the intersection of prompt
engineering, software specification, and developer tooling. It then
constrains the build: a small, expert-facing, cloud-native tool with a
10-entity core model, REST/JSON I/O, and a solo-or-pair BDFL operating
model. The full export lives at
`components/space/exports/recursive-self-improvement-specification.json`.

## Details
- **Domain identity** — SPACE (Superb Prompt Automatic Creation Engine)
  is a programmable specification engine: structured elicitation probes in,
  development specifications out. Audience is experts/researchers; scope is
  tightly bounded; no causal links; entities change independently.
- **Core entity model** — 10 entities in 2–3 categories: Framework
  (326-probe set), Session, Project (container), Artifact (extracted data,
  value + source question + confidence), Series (themed rounds), Round
  (2 questions + follow-ups), Question (open-ended probe), Export, User,
  Engine. One-to-many cardinality, stateful lifecycles with transition
  rules, state-gated relationships, 3–5 attributes per entity.
- **Session mechanics** — 7 series, each round has 2 questions plus
  follow-ups; artifacts derive from questions with confidence scores
  (`derived_from` chains, e.g. `association_types` ← `entity_list`).
- **Technical substrate** — REST/JSON only, single database, small data
  (<10GB), low traffic (<100 req/s), vertical scaling, static env config,
  Linux + macOS, x86-64 + ARM, minimal hardware (<1GB RAM).
- **Operations & process** — continuous flow (Kanban), automated CI/CD to
  dev/staging/prod, standard quality gates (mandatory reviews, unit +
  integration tests), basic security (password auth, TLS), best-effort
  availability, 3–9 month phased timeline.
- **Known deltas vs. the actual cosmos implementation** — the spec says
  "no causal links" and "entities change independently", while the cosmos
  MyKB knowledge graph in practice links artifacts, series dependencies,
  and pulse outcomes; treat the spec as the elicitation baseline, not a
  post-hoc description of the repo.

## Related
- [[wiki/agent-systems/recursive-self-improvement|Recursive Self-Improvement]] — the concept page this spec grounds
- [[wiki/syntheses/guidance-ui-2026-08-06|MyKB Guidance UI]] — the surface that turns such specs into research direction
- [[wiki/syntheses/wiki-self-improvement|Wiki Self-Improvement]] — the umbrella practice for acting on specs
- [[wiki/syntheses/cosmos-dashboard-mykb-integration|Cosmos Dashboard ↔ MyKB Integration]] — where SPACE and MyKB meet
