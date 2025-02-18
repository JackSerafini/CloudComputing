# Cloud Computing Performance Testing

This repository provides a collection of benchmarks comparing the performance of virtual machines (VMs) and containers (CTs) across various workloads, including computational tasks, disk I/O, and network throughput.

## Overview

- **Virtual Machines (VMs):** Set up using VirtualBox with Ubuntu live-server images.
- **Containers (CTs):** Deployed via Docker with a custom docker-compose configuration.
- **Benchmarks Used:**
  - **HPL (High Performance Linpack):** Evaluates floating-point computational performance.
  - **Sysbench:** Tests CPU and memory performance.
  - **Iozone:** Measures disk I/O performance (both local and over NFS).
  - **Iperf3:** Assesses network throughput and latency.

## Key Findings

- **Overall Performance:** Containers generally outperform VMs in HPL, Iozone, and Iperf3 tests due to lower overhead and more efficient resource utilization.
- **Sysbench Anomaly:** In CPU and memory tests with sysbench, VMs showed a slight advantage. This is likely because sysbench does not offer tuning options like HPL, making the inherent overhead of containerization more apparent.

## Repository Contents

- **Benchmark Configurations & Scripts:** Configuration files and scripts to run each benchmark.
- **Performance Data:** Logs and analyzed results for all tests.
- **Documentation:** Detailed explanations of the testing methodology and tuning process (full report available in the repository).
