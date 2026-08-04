---
type: "entity"
title: "Sim Speed"
resource: ""
---
description: "Controlling the rate at which a simulation advances relative to real time"
tags: ["entity", "angular", "api", "ast", "auth", "authentication", "simulation", "time-control"]
timestamp: "2026-07-19T22:41:42Z"

# Sim Speed

## Summary
Sim speed controls how quickly a simulation's virtual clock advances relative to real time. It matters because simulations must run slower than real time for observability, faster for training and search, and at a fixed rate for determinism. Speed control is what makes a simulation a usable laboratory instead of a black box.

## Details
- **Definition** — sim speed is the ratio of simulated time elapsed to wall-clock time; a factor of two runs the world twice as fast as real time.
- **Fixed timesteps** — advancing the simulation in fixed-size steps decouples physics and logic from frame rate, keeping results stable across machines.
- **Real-time mode** — a factor of one with catch-up and slow-down logic keeps a live simulation aligned with the clock while absorbing jitter.
- **Fast-forward** — running many steps per second accelerates training runs, search over future states, and long-horizon experiments.
- **Slow motion** — running below one makes emergent behavior visible and gives operators time to intervene during debugging.
- **Determinism** — at a fixed speed and seed, the same input produces the same sequence of states, which enables replay and reproducible research.
- **Common failure modes** — variable timesteps that cause unstable physics, speed changes that desynchronize clients, and catch-up spikes that overload systems.
- **Worked example** — a load test simulates an hour of user traffic in two minutes by fast-forwarding; when a bug appears, operators replay the same run in slow motion to inspect it.
- **Practical relevance** — explicit speed control is the foundation of testable, debuggable, and repeatable simulation work.

## Related
- [[wiki/agent-systems/simulation-environments-agents|Simulation Environments for Agents]] — worlds with virtual clocks
- [[wiki/llm-agents/deterministic-replay|Deterministic Replay]] — reproducible runs
- [[wiki/agent-systems/agent-timeouts|Agent Timeouts]] — bounding simulation steps
- [[wiki/testing/performance-testing|Performance Testing]] — accelerated workload runs
- [[wiki/software-engineering/metrics-and-monitoring|Metrics and Monitoring]] — observing run behavior
- [[wiki/testing/chaos-engineering|Chaos Engineering]] — time-shifted failure testing
