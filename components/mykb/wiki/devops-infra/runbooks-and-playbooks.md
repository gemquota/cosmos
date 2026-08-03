---
type: "concept"
title: "Runbooks & Playbooks"
description: "Step-by-step operational procedures for known incidents"
tags: ["runbook", "playbook", "incident", "ops"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Runbooks & Playbooks

## Summary
Runbooks and playbooks are the operational documents that tell responders what to do: runbooks are the step-by-step procedures for specific alerts and incidents, while playbooks are the broader playbooks (in the incident-management sense) covering scenarios, decision trees, and escalation. Together they convert experience into repeatable action.

## Details
- Runbook mechanics: one per alert or known failure — symptoms, quick checks, commands, expected outputs, rollback steps, and when to escalate; written for a tired on-call engineer at 3am; linked from the alert itself.
- Playbook mechanics: scenario-level guidance — a decision tree for outage classes (dependency down, data corruption, security event), communication templates, stakeholder lists, and handoff procedures; they cover the judgment calls runbooks cannot.
- Concrete example: a runbook for high database latency (check slow queries, replication lag, connection count; commands to run; when to fail over); a playbook for a suspected security incident (contain, preserve evidence, notify, coordinate with security, communicate status).
- Failure modes: runbooks that rot — written once and never updated after systems change; procedures that assume a state the system no longer has; runbooks so long or so vague they are ignored; a playbook that exists but was never practiced; responders improvising because the document does not match reality.
- Tradeoffs: documentation costs time to write and maintain but is the cheapest way to scale on-call knowledge; the alternative — tribal knowledge — fails when the expert is unavailable; the mature pattern is runbooks in the repo, validated in game days, and updated in the incident retrospective.
- Operational notes: link alerts to runbooks, review runbooks in postmortems, and test the critical ones in drills.
- RSIS3 relevance: cosmos's operational knowledge (daemon recovery, dashboard regeneration, wiki restore) should live as runbooks in the repo — RSIS3's loops can even reference them as executable procedures.

## Related
- [[wiki/devops-infra/runbooks|Runbooks]] — related coverage in the same cluster
- [[wiki/infrastructure/data-eng-runbooks|Data Eng Runbooks]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-pillars|Observability Pillars]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
