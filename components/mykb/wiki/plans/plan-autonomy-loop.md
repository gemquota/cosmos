---
type: "plan"
title: "Plan: Build Full Autonomy Loop"
description: "Connect PulseScheduler to PulseEngine so the system runs autonomously on a cron-like schedule"
tags: ["plan", "autonomy", "pulse", "scheduler", "pending"]
timestamp: "2026-07-21T10:25:00Z"
status: "draft"
---

# Plan: Build Full Autonomy Loop

## Goal
Eliminate the need for --auto flag. PulseScheduler should be able to trigger PulseEngine.main() directly.

## Steps

### Step 1: Refactor PulseEngine.main() into callable API
Currently main() parses args and runs. Need an async entry point that accepts goal/goal_id directly.

### Step 2: Wire PulseScheduler cycle hook to PulseEngine
Set PulseScheduler.set_hook() to call the refactored entry point.

### Step 3: Add scheduler config toggle for auto-mode
Auto-mode config flag that enables autonomous cycle triggering.

### Step 4: Add temporal horizon enforcement
PulseScheduler already has 4h deadline handling. Ensure auto-triggered cycles honor it.

### Step 5: Telemetry for autonomous cycles
Ensure auto-triggered cycles write to TelemetryWriter with scheduler_cycle channel.

## Contingency
If refactoring PulseEngine.main() is too invasive, wrap it in a subprocess call from the hook.

## Expected Duration
2-3 pulse cycles
