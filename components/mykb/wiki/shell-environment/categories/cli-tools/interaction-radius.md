---
type: "entity"
title: "Interaction Radius"
description: "Bash — shell scripting language, CLI — command-line tooling"
tags: ["entity", "ast", "bash", "bootstrap", "bun", "cli"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
status: "growing"
---


## Interaction Radius

Interaction Radius appears in 1 session(s) categorized as Shell. Related topics: bash, bootstrap, bun, cli.

**Domain:** OS & Shell › [[wiki/web-platforms/00-index|Shell Environment]] › [[wiki/web-platforms/00-index|Cli Tools]]

## The Concept

Interaction radius is the effective range within which a user or agent can affect a system — the space, scope, or surface that responds to an input. It generalizes across contexts:

- **UI and pointer input** — the hit area around a target that registers clicks or touches; touch targets need generous radii to be reliable, and pointer-capture APIs widen or narrow the effective area.
- **Keyboard and focus** — the focused element defines the interaction radius for typed input; tab order and focus traps move it.
- **CLI scope** — a shell command's radius is the working directory, environment, and permission context it can reach; PATH limits which commands resolve, and sandboxes shrink the radius to a directory or container.
- **Agents and permissions** — an automation tool's radius is bounded by its granted scopes, tokens, and network access.

Designing with radius in mind means keeping affordances inside reach: buttons large enough to hit, autocomplete that covers the whole command space users type in, and least-privilege scopes so an accidental action cannot exceed its intended surface. Debugging "nothing responds" is usually a radius problem — the event landed outside the target, the focus was elsewhere, or the shell was running in a different directory than assumed.

## Measuring and Tuning

Hit-testing tells you where events land, but measuring the radius means testing at the edges: pointer coordinates near the boundary, keyboard focus after tabbing, or a command run from an unexpected directory. Automated tests that probe the extremes catch radius bugs before users do.

## Related Notes

- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/touchinput-2|TouchInput]] — pointer and touch hit areas
- [[wiki/os-shell/system-monitoring-tools|System Monitoring Tools]] — observing what a shell session can reach

## Related Entities

- [[wiki/shell-environment/categories/cli-tools/body-simulator|Body Simulator]]
- [[wiki/shell-environment/categories/cli-tools/density|Density]]
- [[wiki/shell-environment/categories/cli-tools/drip-rate|Drip Rate]]
- [[wiki/shell-environment/categories/cli-tools/fluid-simulator|Fluid Simulator]]
- [[wiki/shell-environment/categories/cli-tools/glow-intensity|Glow Intensity]]
- [[wiki/shell-environment/categories/cli-tools/gravity-sim|Gravity Sim]]
- [[wiki/shell-environment/categories/cli-tools/hybrid-gravity|Hybrid Gravity]]
- [[wiki/shell-environment/categories/cli-tools/kh|Kh]]

