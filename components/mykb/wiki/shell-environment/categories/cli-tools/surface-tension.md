---
type: "entity"
title: "Surface Tension"
description: "Bash — shell scripting language, CLI — command-line tooling, CSS — web styling language"
tags: ["entity", "ast", "bash", "bug", "cli", "css"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
status: "growing"
---


## Surface Tension

Surface Tension appears in 1 session(s) categorized as Debugging, Frontend, Shell. Related topics: bash, cli, css.

**Domain:** OS & Shell › [[wiki/os-shell/supercategories/shell-environment/index|Shell Environment]] › [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/index|Cli Tools]]

## Overview

Surface tension is the physical property that makes a fluid's surface behave like a stretched elastic film. In particle-based fluid simulation, it is modeled as an attractive force among particles near the fluid boundary: interior particles feel balanced forces, while surface particles are pulled inward, producing rounded droplets and cohesive blobs. The term appears in the CLI-tools simulation cluster, where it is one of several parameters — density, gravity, interaction radius — that the simulator exposes for tuning.

## Physics in Simulation

Simulators implement surface tension with pairwise forces that only activate within a short range and only near the surface, often computed by comparing local density against a rest density: regions with higher density push particles apart, and low-density regions at the boundary pull them together. Getting the coefficient wrong produces either droplets that scatter like mist or blobs that clump into a single mass, so tuning is iterative. The parameter interacts with [[wiki/shell-environment/categories/cli-tools/density|density]] and [[wiki/shell-environment/categories/cli-tools/interaction-radius|interaction radius]]: a longer interaction radius strengthens cohesion, while lower density weakens the boundary effect. [[wiki/shell-environment/categories/cli-tools/fluid-simulator|fluid simulator]] is the tool these parameters drive, and [[wiki/shell-environment/categories/cli-tools/drip-rate|drip rate]] captures the visible outcome — how fast liquid separates into drops.

## Debugging and Frontend

A bug in surface tension looks like implausible behavior: liquids that crawl up walls, explode into fragments, or merge instantly. Debugging compares the parameter values against expected ranges and inspects a single timestep for force anomalies. The frontend tag reflects the browser rendering where these effects are visualized, and the CSS tag the page styling around it. The [[wiki/shell-environment/categories/cli-tools/tension|tension]] page is the sibling entry in this cluster, and the CLI-tools index groups the full parameter family.

## Session Context

One session recorded the term under Debugging, Frontend, and Shell, so the page anchors the surface-tension parameter within the simulation toolchain.

## Related Entities

- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/body-simulator|Body Simulator]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/density|Density]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/drip-rate|Drip Rate]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/fluid-simulator|Fluid Simulator]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/glow-intensity|Glow Intensity]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/gravity-sim|Gravity Sim]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/hybrid-gravity|Hybrid Gravity]]
- [[wiki/os-shell/supercategories/shell-environment/categories/cli-tools/interaction-radius|Interaction Radius]]
