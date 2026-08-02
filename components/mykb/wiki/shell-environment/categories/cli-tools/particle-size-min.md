---
type: "entity"
title: "Particle Size Min"
description: "Particle System"
tags: ["entity", "ast", "bash", "bootstrap", "bun", "cli"]
timestamp: "2026-07-19T22:41:41Z"
status: "growing"
resource: ""
---

## Particle Size Min

Particle System — a visual effect technique using many small sprites to simulate fire, smoke, or other phenomena. Used in game development and data visualization.

**Related topics:** bash, bootstrap, bun, cli

**Domain:** OS & Shell › [[wiki/web-platforms/index|Shell Environment]] › [[wiki/web-platforms/index|Cli Tools]]

## Overview

Particle Size Min is the lower bound on the size of particles in a particle system. Particle systems render many small sprites — each with position, velocity, size, color, and lifetime — to simulate phenomena such as fire, smoke, rain, and debris. Clamping minimum size serves two purposes: it keeps particles visible at any zoom or scale, and it bounds per-particle rendering cost by preventing degenerate, sub-pixel sprites from consuming fill-rate and memory.

## Details

- Parameter role: min size works with max size to define the size range; the emitter often interpolates within it over a particle's lifetime.
- Rendering cost: tiny particles can still cost a full draw call each; a minimum size reduces overdraw and sprite-management overhead.
- Visual stability: without a floor, particles may flicker or vanish as they shrink, breaking the effect's continuity.
- Scaling: when the canvas or viewport scales, min size may need to scale too, so the parameter is often expressed in screen or world units.
- Tuning: setting min too high makes the effect look blocky; too low reintroduces flicker — sessions typically tune it alongside [[wiki/shell-environment/categories/cli-tools/density|Density]] and emitter rate.
- CLI integration: simulators expose the parameter via config or flags so runs are reproducible from the command line.

In the cli-tools family, Particle Size Min is one of several simulation parameters that scripts pass to headless or visual runs. Documenting units, defaults, and the interaction between min size and particle count makes the system tunable without reading source. When artifacts appear — sparkle, pop-in, or missing particles — min size is one of the first parameters to check.

## Related Entities

- [[wiki/shell-environment/categories/cli-tools/body-simulator|Body Simulator]]
- [[wiki/shell-environment/categories/cli-tools/density|Density]]
- [[wiki/shell-environment/categories/cli-tools/drip-rate|Drip Rate]]
- [[wiki/shell-environment/categories/cli-tools/fluid-simulator|Fluid Simulator]]
- [[wiki/shell-environment/categories/cli-tools/glow-intensity|Glow Intensity]]
- [[wiki/shell-environment/categories/cli-tools/gravity-sim|Gravity Sim]]
- [[wiki/shell-environment/categories/cli-tools/hybrid-gravity|Hybrid Gravity]]
- [[wiki/shell-environment/categories/cli-tools/interaction-radius|Interaction Radius]]
