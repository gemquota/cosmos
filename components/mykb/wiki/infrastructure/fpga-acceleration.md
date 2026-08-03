---
type: "concept"
title: "FPGA Acceleration"
description: "Reconfigurable hardware for specialized workloads"
tags: ["fpga", "acceleration", "hardware", "compute"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# FPGA Acceleration

## Summary
FPGAs (field-programmable gate arrays) are reconfigurable hardware: arrays of logic blocks and routing that can be programmed to implement arbitrary digital circuits. As accelerators, they occupy the middle ground between CPUs (general but slow per operation) and ASICs (fast but fixed at design time) — you can build a custom circuit for a workload, and rebuild it when the workload changes.

## Details
- The reconfigurability is the defining property: an FPGA can be reprogrammed in milliseconds to seconds (full or partial reconfiguration) to implement a different circuit — a packet parser, a compression engine, an inference kernel, a financial-order preprocessor. The cost of the flexibility: FPGAs are less efficient per operation than an ASIC (the programmable fabric pays overhead) and far harder to program than a CPU (the toolchain is hardware design — Verilog/VHDL, synthesis, place-and-route, timing closure), so the bar for FPGA adoption is a workload that needs ASIC-like speed but is not stable enough (or not high-volume enough) to justify an ASIC.
- Where FPGAs win: workloads with extreme, deterministic low latency and high throughput that do not fit GPUs. Classic deployments: network acceleration (packet processing, DDoS filtering, SmartNIC functions — Microsoft, Amazon, and cloud providers use FPGAs in the network data path), trading (sub-microsecond market-data parsing and order processing — the reason "FPGA" is synonymous with HFT), signal processing and RF (Software Defined Radio), and inference acceleration for specific models where the operator can compile the network into a circuit. The common thread: regular, parallelizable computation with tight latency budgets, where the CPU's overhead or the GPU's latency/jitter is unacceptable.
- The modern access model removed the old barrier: cloud FPGAs (AWS F1, Azure, Alibaba) let teams rent FPGAs with an instance model, and the high-level synthesis (HLS) toolchain (C/C++ → hardware) has lowered the programming bar — though "lowered" is relative: the skill set and the design-debug cycle remain far heavier than software.
- Failure modes: overcommitting to FPGAs for workloads that are really CPU/GPU problems (the flexibility tax with no benefit), timing closure failures (the design cannot meet the clock — the FPGA programmer's version of "does not compile"), and long iteration cycles (a place-and-route run takes hours, so development is slow).
- For mykb: FPGA acceleration sits in the acceleration cluster — its siblings are GPU compute, ASIC design, and kernel bypass, and the comparison to each clarifies the others.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]]
