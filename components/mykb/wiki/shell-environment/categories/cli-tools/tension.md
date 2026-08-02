---
type: "entity"
title: "Tension"
description: "Bash — shell scripting language, CLI — command-line tooling, CSS — web styling language"
tags: ["entity", "ast", "bash", "bug", "cli", "css"]
timestamp: "2026-07-19T22:41:41Z"
status: "growing"
resource: ""
---


## Tension

Tension appears in 1 session(s) categorized as Debugging, Frontend, Shell. Related topics: bash, cli, css.

**Domain:** OS & Shell › [[wiki/os-shell/supercategories/shell-environment/index|Shell Environment]] › [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/index|Cli Tools]]

## Overview

Tension is a force or constraint parameter used in physical simulations — surface tension in fluid systems, spring tension in particle networks, and boundary tension in membranes. It controls how strongly a system resists deformation or pulls toward a stable shape. In the cli-tools family, tension is a tunable knob alongside density and particle size: higher tension makes structures stiffer and more cohesive, while lower tension allows fluid, loose behavior.

## Details

- Fluid simulation: surface tension shapes droplets and coalescence; too high creates artificial clumping, too low makes liquids smear into foam.
- Particle networks: spring tension determines how particles hold relative positions, influencing elasticity, vibration, and stability.
- Numerical effects: extreme tension values can make integration unstable — oscillations grow until the simulation explodes — a classic debugging target.
- Units and ranges: tension is usually normalized; scripts pass it as a flag or config value, and sessions record the value alongside the observed artifact.
- Interaction: tension interacts with [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/density|Density]] and [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/particle-size-min|Particle Size Min]]; changing one often requires retuning the others.

From a frontend and CSS view, tension is also a design word — spacing, line-height, and contrast create visual tension that guides attention. In either reading, the lesson is the same: tension is a dial, not a constant. Debugging sessions isolate which parameter caused the artifact by varying one knob at a time, and they record the stable range so future runs start from known-good values instead of rediscovering them.

## Related Entities
## Recording Values

Because simulation artifacts are often reproducible only at specific parameter values, sessions should record the tension setting alongside the bug report: the value, the expected behavior, and the observed artifact. That trio turns a vague "it looks wrong" report into a testable case, and lets the next session reproduce and fix without re-exploring the parameter space.


- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/body-simulator|Body Simulator]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/density|Density]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/drip-rate|Drip Rate]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/fluid-simulator|Fluid Simulator]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/glow-intensity|Glow Intensity]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/gravity-sim|Gravity Sim]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/hybrid-gravity|Hybrid Gravity]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/interaction-radius|Interaction Radius]]
