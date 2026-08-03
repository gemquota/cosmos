---
type: "concept"
title: "Intrusion Detection Systems"
description: "Signature and anomaly detection for host and network activity"
tags: ["ids", "security", "monitoring", "detection"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Intrusion Detection Systems

## Summary
Intrusion detection systems (IDS) monitor host and network activity to find signs of intrusion — matching known attack patterns (signature detection) or flagging behavior that deviates from the baseline (anomaly detection). An IDS is the detection layer of security: it does not stop attacks like a firewall, it sees them and reports them, so the response can happen.

## Details
- The two detection philosophies. Signature detection compares traffic and events against a database of known attack patterns — exploit signatures, malware indicators, suspicious command sequences. It is precise (low false positives on known attacks) but blind to anything new: a novel attack has no signature, and signature updates lag the attackers. Anomaly detection builds a baseline of normal behavior (traffic volumes, connection patterns, user behavior, process activity) and flags deviations. It can catch novel attacks (anything abnormal is suspicious) but suffers false positives — normal-but-unusual behavior (a new deployment, a legitimate data export, a sysadmin working late) looks like an intrusion. The two are complementary, and production IDS uses both: signatures for the known, anomalies for the unknown.
- The placement dimension: network-based (NIDS) sits on the network path or taps — monitoring traffic for attack patterns (Snort/Suricata) — while host-based (HIDS) lives on each machine, watching filesystem integrity, process behavior, logs, and system calls (Wazuh, Osquery, auditd). NIDS sees what crosses the wire (including lateral movement between segments) but is blind to encrypted traffic and to activity that never hits the network; HIDS sees what happens on the machine (including encrypted-communication endpoints and file changes) but only where it is installed. Modern practice deploys both, with the NIDS at chokepoints and the HIDS on every host.
- The modern evolution: detection engineering. Raw IDS alerting drowns analysts in false positives; the practice evolved into detection engineering — writing and curating high-signal detections, tuning baselines, and feeding alerts into a SIEM/SOAR pipeline with correlation and response. The metric of an IDS deployment is not "alerts generated" but detection coverage and time-to-detection — how much of the attack surface is monitored and how quickly intrusions are seen.
- Failure modes: the alert flood (analysts ignore alerts — the boy-who-cried-wolf failure that makes IDS worse than none), the detection blind spot (encrypted traffic, ephemeral cloud workloads, and fileless attacks evade both signature and host monitoring), and the IDS itself being attacked (an attacker who compromises the monitoring infrastructure blinds the defense).
- For mykb: IDS is the detection tier — fail2ban (prevention) and honeypots (deception) are its siblings in the detection spectrum.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/os-shell/systemd-and-init-systems|systemd & Init Systems]]
- [[wiki/infrastructure/fail2ban-and-intrusion-prevention|fail2ban & Intrusion Prevention]]
- [[wiki/devops-infra/feature-flag-systems-revisited|Feature Flag Systems]]
