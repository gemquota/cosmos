---
type: "concept"
title: "PARA Method"
description: "Organization system that files notes into Projects, Areas, Resources, and Archives"
tags: ["para", "organization", "pkm", "workflow"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# PARA Method

## Summary
PARA files everything into four top-level buckets — Projects, Areas, Resources, and Archives — based on the actionability of each item. It is designed to keep knowledge near the work that uses it, so the organization follows what the knowledge is for, not what the knowledge is about.

## Details
- **Buckets** — Projects (active, time-bound), Areas (ongoing responsibilities), Resources (topical references), Archives (inactive everything). A project has a goal and a deadline; an area is a standing responsibility (health, a service you maintain); resources are interests and references; archives hold everything no longer active.
- **Principle** — organize by actionability, not topic; a note lives where it is most likely to be needed. The same topic can appear in several buckets — a Kubernetes note exists in a project (migrating the cluster), an area (platform ownership), and a resource (general reference) without contradiction, because the buckets answer different questions.
- **Concrete example** — an engineer starting a migration creates a project folder with the migration plan and checklist; platform-runbook knowledge lives in the area folder; a general article on migration patterns is a resource; last year's finished migration moves to archives. When the next migration starts, the archive's plan is promoted back to a project.
- **Failure modes** — bucket drift, where items sit in the wrong bucket because the distinction between project and area is fuzzy; archive neglect, where archived items are never re-promoted so old knowledge rots; and the four-bucket habit applied to a wiki, where a note's meaning changes depending on which bucket the file lives in.
- **Tradeoffs** — PARA is excellent for action-oriented knowledge and keeps clutter down, but topic-based search and linking still require a graph layer on top; the buckets organize storage, not meaning, so PARA and a linked wiki complement each other.
- **Agent relevance** — an agent's memory could use the same triage: active goal context in Projects, standing knowledge in Resources, old pulses in Archives. The mykb equivalent is a status or namespace scheme that separates active work from durable reference.
- **RSIS3/mykb relevance** — PARA's actionability test is a useful filter for what belongs in a synthesis versus a concept page: actionable, time-bound conclusions are project material; durable patterns are resources. This node keeps that triage rule retrievable for curation passes.

## Related
- [[wiki/memory/personal-knowledge-management|Personal Knowledge Management]] — PARA is a PKM organization strategy
- [[wiki/memory/note-taking-methods|Note-Taking Methods]] — capture methods feed PARA buckets
- [[wiki/memory/information-architecture|Information Architecture]] — the discipline of structuring information spaces
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — triage into buckets is a curation act
- [[wiki/concepts/mykb-analysis|Mykb Analysis]] — how mykb organizes its own knowledge
