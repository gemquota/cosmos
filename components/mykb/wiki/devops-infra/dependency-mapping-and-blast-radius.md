---
type: "concept"
title: "Dependency Mapping & Blast Radius"
description: "Knowing what breaks when a service fails to limit impact"
tags: ["blast-radius", "dependencies", "reliability", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Dependency Mapping & Blast Radius

## Summary
Dependency mapping records which components depend on which — services, libraries, databases, teams — so change impact can be predicted. Blast radius is the set of things that can break when one component changes. Together they turn "who might this affect?" from tribal knowledge into a computed, reviewable answer.

## Details
- Mechanism: build a graph from deployment manifests, API calls (traced), database schemas, package imports, and team ownership; annotate edges with direction, criticality, and change frequency; compute blast radius by walking the graph from a changed node; surfaces as dashboards, PR impact labels, and CI gates.
- Concrete example: a change to the shared auth library tags every service importing it; a schema change to the users table lists all consumers of the users API; a config change to the ingress marks every route behind it. Tools range from hand-maintained docs to automated scanners (Deptrac for PHP, import analysis, OpenTelemetry service graphs).
- Failure modes: stale maps — the graph drifts from reality and gives false confidence; missing edges — untraced calls (DNS, shared files, cron jobs) hide real blast radius; over-broad ownership that marks everything critical, making the signal useless; blast radius computed on topology alone without runtime data, missing failure propagation.
- Tradeoffs: accurate mapping costs instrumentation and maintenance; approximate mapping is cheap but must be labeled as such; the payoff is safer, faster changes and better incident response because responders know what to watch.
- Operational notes: regenerate the graph automatically on deploy, couple it to an ownership model, and use it in change review and rollback decisions.
- RSIS3 relevance: RSIS3's loop ecosystem is a dependency graph — mapping which loops consume which state makes a change to a shared registry's format assessable before it breaks downstream loops; the blast-radius list is what a change review must sign off on.

## Related
- [[wiki/cloud-infra/block-device-mapping-gcp|Block Device Mapping on GCP]]
- [[wiki/devops-infra/renovate-and-dependency-updates|Renovate & Dependency Updates]]
- [[wiki/shell-environment/categories/cli-tools/interaction-radius|Interaction Radius]]
