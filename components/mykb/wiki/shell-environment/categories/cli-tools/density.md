---
type: "entity"
title: "Density"
description: "Bash — shell scripting language, CLI — command-line tooling, CSS — web styling language"
tags: ["entity", "ast", "bash", "bug", "cli", "css"]
timestamp: "2026-07-19T22:41:41Z"
status: "growing"
resource: ""
---


## Density

Density appears in 1 session(s) categorized as Debugging, Frontend, Shell. Related topics: bash, cli, css.

**Domain:** OS & Shell › [[wiki/os-shell/supercategories/shell-environment/index|Shell Environment]] › [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/index|Cli Tools]]

## Overview

Density describes how much of something occupies a given space or volume — mass per unit volume in physics, information per unit area in displays, or particles per cell in a simulation. In the shell and CLI tooling context, density appears in simulation parameters (particle density, fluid density) and in display design (information density of a UI). It is a tunable parameter whose value changes both the behavior of a system and the cost of computing it.

## Details

- Simulations: particle and fluid simulators treat density as a core input; higher density means more interactions per cell and more computation, while lower density produces sparser, cheaper results.
- CLI usage: scripts read and set density from configuration or command-line flags, and report it in output for reproducibility.
- Frontend and CSS: information density governs spacing, font sizes, and grid tightness; it affects readability, scanability, and visual balance.
- Debugging: a density parameter set too high or too low is a common root cause of simulation artifacts — clumping, explosions, or empty regions — making it a frequent subject of debugging sessions.
- Ranges: simulations often clamp density to stable bounds; exceeding them degrades numerical stability rather than just changing visuals.

The entity belongs to a family of simulation parameters — see [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/particle-size-min|Particle Size Min]] and [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/tension|Tension]] — where each knob trades behavior against cost. Documenting the parameter's units, default, and effect lets scripts set it deliberately and lets debugging sessions reason about artifacts from the values used. When density appears in a session, the fix is usually to check the value against the documented range before touching the simulation logic.

## Related Entities

- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/body-simulator|Body Simulator]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/drip-rate|Drip Rate]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/fluid-simulator|Fluid Simulator]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/glow-intensity|Glow Intensity]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/gravity-sim|Gravity Sim]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/hybrid-gravity|Hybrid Gravity]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/interaction-radius|Interaction Radius]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/kh|Kh]]
