---
type: "concept"
title: "Thermal Throttling & Power"
description: "Heat limits that cut CPU frequency and the power budget tradeoffs"
tags: ["thermal", "throttling", "power", "cpu"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Thermal Throttling & Power

## Summary
Thermal throttling is the CPU protecting itself from heat damage by cutting frequency (and voltage) when temperatures approach the silicon's limit: a chip that boosts to 4.5 GHz for a few seconds drops to 3.0 GHz under sustained load if the cooler cannot dissipate the heat. Power and thermal management — TDP, power limits, and frequency scaling working together — is why "the CPU is fast on paper but slow in my chassis" is a real, measurable phenomenon.

## Details
- Mechanism: modern CPUs expose a temperature target (Tjmax, e.g., 100°C) and a package power budget (TDP, PL1/PL2 on Intel; PPT on AMD). The hardware and the OS cooperate: the CPU boosts while temperature and power are below limits (PL2, turbo), then pulls frequency down to sustain PL1; the kernel's `intel_pstate`/`AMD pstate` drivers and ACPI thermal zones (`/sys/class/thermal/`) enforce thermal policy, and `powercap` (`/sys/class/powercap/intel-rapl`) exposes energy budgets. Throttling is normal under bursty load — the problem is when sustained load hits the thermal ceiling and frequency collapses below the "expected" level, silently extending job runtime.
- Concrete examples: a laptop benchmark scores fine on a cold start but 20% lower on the second run — the cooler heat-soaked and PL1 kicked in; a 1U server with a high-TDP CPU in a dense rack throttles under a long build (check with `turbostat` — it shows actual frequency vs. max); `sensors` reads temperatures; `cpupower frequency-info` shows current frequency; a data center adds airflow or reduces ambient temperature to reclaim headroom; power capping (`powercap-set`) deliberately lowers PL1 to fit a power budget, trading throughput for density.
- Failure modes: the classic failures are treating throttle as a CPU bug (it is a thermal/cooling design issue — the fix is airflow, heatsink, ambient temperature, or a lower TDP chip), dust-clogged coolers causing gradual degradation with no code change, and misconfigured BIOS power limits (a "quiet" mode that permanently caps frequency). The subtle failure is inconsistent performance: throttled runs make benchmarks and capacity planning meaningless because the same job takes different times depending on heat soak — which is why latency-sensitive services need headroom, not just "the CPU can do it".
- Operational tradeoffs: the power/thermal envelope is a triangle: performance, power, and heat — pick two. Undervolting and power capping reduce heat and energy at some throughput cost; aggressive turbo buys peak performance at the cost of thermal headroom and energy. The practice rules: measure sustained frequency with `turbostat` under your real workload (not just peak), size cooling to sustained TDP rather than marketing turbo, monitor temperature trends (`sensors`/IPMI) and power-limit throttling counters (`rdmsr 0x1FC`-style or RAPL), and set power limits deliberately where density matters. RSIS3/mykb relevance: RSIS3's batch indexing loops are sustained-load jobs — exactly the workloads that heat-soak; scheduling heavy work with thermal headroom and monitoring frequency collapse keeps batch runtime predictable, mirroring the loop-hygiene rule that long jobs must account for environmental constraints.

## Related
- [[wiki/infrastructure/power-and-cooling-datacenter|Power & Cooling in the Datacenter]] — related coverage in the same cluster
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]] — related coverage in the same cluster
- [[wiki/os-shell/memory-management-paging|Memory Management & Paging]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
