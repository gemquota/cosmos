---
type: "readme"
title: "projects directory"
description: "Directory placeholder"
tags: [readme]
status: "growing"
---


## Readme

# Projects

Store active projects, learning plans, experiments, and long-term goals here.

Each project page should have:
- YAML frontmatter with `type: project`
- Project goals, timeline, and status
- Links to related concepts, sources, and decisions
- Checkpoint notes and next actions

**Domain:** Projects

## Project Lifecycle

Projects in this directory move through a small set of states: proposal, active, paused, and archived. A proposal records the problem, the goal, and the success criteria before work begins; an active project carries a timeline and checkpoint notes; a paused project documents why it stalled and what would resume it; an archived project captures the outcome and lessons. Keeping the status field accurate lets the directory serve as both a planner and a record.

## Anatomy of a Project Page

Each project page should have YAML frontmatter with type: project, plus a title, status, and timestamp. The body states the goal, scope, and acceptance criteria, then tracks progress with dated checkpoints. Links to related concepts, sources, and decisions tie the project into the wider wiki, and next actions are recorded so the project can be resumed without re-deriving context.

## Keeping the Index Current

The readme is intentionally short because the real content lives in the pages it points to. As projects are added, moved between states, or completed, the related links at the bottom should be updated so the directory always resolves. Experiments and learning plans belong here too, with the same structure, so that the knowledge captured during them is not lost.

The directory itself is meant to be scanned, not read top to bottom: a newcomer looks for the status field and the checkpoint notes, then follows the related links. Because the wiki is the shared memory of the projects, keeping this page accurate is a standing practice rather than a one-time chore. New project pages should follow the same frontmatter conventions so the directory stays uniform.

## Related

- [[wiki/projects/triad-integration|Triad Integration]]

## Concepts

- [Triad Integration — RSIS3 + mykb + myrsikb](triad-integration.md) — Triad Integration — RSIS3 + mykb + myrsikb
