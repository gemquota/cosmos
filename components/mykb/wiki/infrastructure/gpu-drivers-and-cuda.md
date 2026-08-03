---
type: "concept"
title: "GPU Drivers & CUDA"
description: "Kernel drivers and runtime toolchains that expose GPU compute"
tags: ["gpu", "cuda", "drivers", "compute"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# GPU Drivers & CUDA

## Summary
GPU drivers and CUDA are the software stack that exposes GPU compute to applications: the kernel driver manages the hardware and exposes device interfaces, the CUDA runtime and libraries give programs a high-level programming model (kernels, memory, streams), and the toolchain (nvcc, cuDNN, NCCL) turns CUDA code into executable work. The stack is the difference between "there is a GPU in this machine" and "programs can use the GPU".

## Details
- The layer cake: the kernel driver (a set of modules — nvidia.ko, nvidia-modeset.ko, nvidia-uvm.ko, nvidia-drm.ko — not a single file) owns the hardware: device initialization, memory management (VRAM allocation), DMA, and the ioctl interface that user-space uses. The user-space runtime (libcuda, the CUDA driver API) talks to the kernel driver and manages contexts, modules, and streams; the CUDA runtime library (libcudart) wraps that in the familiar API; and the domain libraries (cuBLAS, cuDNN, cuFFT, NCCL) provide the optimized kernels that most real workloads actually call — the average PyTorch user never writes CUDA, but PyTorch ships CUDA kernels for every operation. The container stack (nvidia-container-toolkit) makes all of this work inside containers by injecting the driver's user-space libraries and creating device nodes.
- The version-compatibility matrix is the operational heart: the kernel driver supports a range of CUDA versions (the driver is backward-compatible — newer drivers run older CUDA runtimes), and each CUDA version supports a range of GPU architectures (compute capabilities). The failure modes are the mismatches: a container built with a CUDA version newer than the host driver (fails with "CUDA driver version is insufficient"), or an application compiled for a GPU architecture the hardware does not support (fails with "no kernel image is available"). The fixes are version management — matching driver, CUDA toolkit, and container images — which is why the container images (nvidia/cuda) exist as a matrix and why "check the driver/CUDA compatibility" is the first troubleshooting step.
- The driver's operational properties: it is a kernel module with a huge attack and bug surface (the reason distributions hesitate to ship it by default), it must match the kernel version for DKMS builds, and its updates (or the container runtime's) are a common cause of GPU nodes going into "not ready" states. The discipline: pin driver versions per node pool, validate with nvidia-smi before scheduling workloads, and treat driver upgrades as planned maintenance with node drain.
- The runtime behavior that matters: CUDA streams and async execution define concurrency (multiple streams can overlap kernels and copies — the foundation of CUDA performance tuning), and memory management (pinned memory, unified memory) defines transfer speed.
- For mykb: the node anchors the GPU software stack — the sibling nodes cover the scheduling (GPU compute infrastructure) and the physical layer (accelerator observability).

## Related
- [[wiki/infrastructure/gpu-compute-infrastructure|GPU Compute Infrastructure]]
- [[wiki/os-shell/device-drivers-and-udev|Device Drivers & udev]]
- [[wiki/os-shell/device-drivers|Device Drivers]]
