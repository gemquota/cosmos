---
type: "entity"
title: "Physics Update"
description: "Physics Engine"
tags: ["entity", "ast", "bash", "css", "dom", "feature"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
status: "growing"
---

## Physics Update

Physics Engine — software simulating physical systems (gravity, collision, forces). Used in game development and interactive simulations.

**Related topics:** bash, css, dom, feature

**Domain:** OS & Shell › [[wiki/web-platforms/00-index|Shell Environment]] › [[wiki/web-platforms/00-index|Web Dev]] › Physics Update

## Overview

Physics Update refers to the step in a simulation loop where physical state advances: forces are computed, velocities and positions are integrated, and collisions are resolved. The page was recorded in a session tagged with css, dom, and feature, alongside a physics-engine description, pointing to a browser-rendered simulation with an update loop.

## The Update Loop

Simulations advance time in fixed steps. A fixed-timestep loop accumulates real elapsed time and steps the physics a whole number of times, which keeps behavior stable and deterministic regardless of frame rate; an accumulator pattern avoids both tunneling at high speeds and drift at low frame rates. Rendering happens once per frame, interpolating between physics states when the step rate differs from the frame rate.

## Integration and Collision

Velocity Verlet and semi-implicit Euler are common integrators: each step updates velocity from forces, then position from velocity. Collision handling detects overlaps and applies impulses or positional correction, ideally with a few solver iterations for stacking stability. Broad-phase checks (bounding boxes, grids) discard distant pairs before narrow-phase tests.

## Context

The DOM and CSS tags suggest the simulation is drawn in the browser and styled like the other web-dev demos in this branch, such as the chemical playground and diffusion simulator. The feature tag indicates a capability being added or exercised. Keeping the general mechanics here makes the page accurate for any such engine.

Determinism is worth protecting: iteration order, floating-point accumulation, and random seeds all affect whether two runs match, so simulations that must be reproducible document these choices. Testing physics code with hand-computed cases and invariants such as energy and momentum catches integration bugs early. The related demos in this branch exercise exactly these concerns in the browser.

## Related Entities

- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/analysis-2|Analysis 2]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/budget|Budget]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/canvas|Canvas]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/chemical-playground|Chemical Playground]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/context-2|Context 2]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/defi|Defi]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/diffusion-simulator|Diffusion Simulator]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/engine-telemetry-core|Engine Telemetry Core]]
