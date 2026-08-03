---
type: "concept"
title: "CPU Governors & Frequency Scaling"
description: "Dynamic voltage and frequency scaling policies on modern CPUs"
tags: ["governor", "cpufreq", "cpu", "power"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# CPU Governors & Frequency Scaling

## Summary
CPU frequency scaling (DVFS, dynamic voltage and frequency scaling) lets the kernel adjust a CPU's clock speed and voltage on the fly, trading performance for power. The governor is the policy that decides: `performance` pins the CPU at maximum, `powersave` at minimum, `ondemand`/`schedutil` ramp up under load, and `conservative` ramps more slowly. On modern Intel and AMD systems, `schedutil` and hardware-managed P-states (HWP) have largely replaced the older governors.

## Details
- Mechanism: the cpufreq subsystem exposes `scaling_governor` and `scaling_cur_freq` per CPU under `/sys/devices/system/cpu/cpu*/cpufreq/`. `ondemand` samples load periodically and jumps to high frequency on a threshold, then decays; `schedutil` reads the scheduler's per-entity load directly, reacting to task wakeups with no sampling delay — which is why it became the default. Intel's HWP (hardware P-states, `intel_pstate` driver) moves the decision into the CPU itself, with the kernel only setting energy-performance preference (EPP); AMD uses a similar CPPC mechanism.
- Concrete examples: a batch server sets `performance` to minimize latency variance for latency-critical work; a laptop on battery lets `schedutil`/HWP balance power and responsiveness; `cpupower frequency-set -g powersave` for thermal-limited CI boxes; `turbostat` and `cpupower frequency-info` verify actual frequencies; energy-aware scheduling (EAS) on big.LITTLE phones biases wakeups toward efficiency cores under light load.
- Failure modes: the classic failure is a misconfigured governor causing thermal throttling to fight the load: pinned `performance` on an inadequate cooler leads to sustained high temperatures, frequency collapse, and worse latency than a balanced governor. Frequency ramping lag (ondemand's sampling delay) causes the "first request is slow" pattern on bursty web servers; and virtualization adds confusion — guest OSes see scaled frequencies (kvmclock/ACPI) that do not reflect the host's real clock, so benchmarks inside VMs misread CPU speed.
- Operational tradeoffs: aggressive scaling saves real power and heat on idle-heavy workloads (servers can spend most of their time at minimum frequency), at the cost of frequency-switching latency and sometimes higher variance; pinning frequency removes variance but wastes energy and risks thermal issues. Modern guidance: leave the default (schedutil on most distros, HWP on Intel) unless a measured workload needs a change, tune EPP for latency vs. efficiency preferences, and verify with `turbostat` rather than trusting `scaling_cur_freq` on every platform.
- RSIS3/mykb relevance: RSIS3 loop workers doing periodic telemetry and graph rebuilds are bursty workloads where frequency ramping latency matters less than thermal headroom; the same principle — let a feedback controller choose operating points instead of pinning extremes — mirrors how loop parameters are tuned rather than hardcoded.

## Related
- [[wiki/os-shell/numa-and-cpu-topology|NUMA & CPU Topology]]
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]]
- [[wiki/os-shell/memory-management-paging|Memory Management & Paging]]
