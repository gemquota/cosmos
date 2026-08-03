---
type: "concept"
title: "Honeypots & Deception"
description: "Decoy services that attract and expose attacker behavior"
tags: ["honeypot", "deception", "security", "detection"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Honeypots & Deception

## Summary
Honeypots are decoy systems designed to be attacked: fake services, fake credentials, fake data, and fake networks that attract attackers and expose their behavior. The core insight: in a honeypot, every connection is suspicious by definition — no legitimate user has a reason to touch it — so any interaction is an alert, and the interaction itself becomes intelligence about the attacker's tools, techniques, and objectives.

## Details
- The taxonomy: low-interaction honeypots emulate services (an SSH daemon that logs login attempts, a web server that serves trap pages) and are cheap, safe, and high-signal for the automated attack noise — they catch scanners and credential-stuffing bots with almost no risk. High-interaction honeypots run real systems the attacker can fully interact with, yielding deep intelligence (what commands an intruder runs, what they exfiltrate) at high risk and high maintenance cost. Honeytokens sit one level up: fake credentials, fake database records, fake API keys, and fake files embedded in real systems — a credential that should never be used, an API key that should never be called — so their use is an instant, high-confidence compromise signal.
- The deception-network pattern scales this: the whole environment contains planted lures — decoy ports, decoy subnets, decoy admin accounts, decoy documents — and the network's monitoring watches for lure interaction. The goal is not just detection but attacker misinformation: an attacker who believes they have found a real admin account or a real credential store wastes time and reveals their playbook in a controlled environment. Deception is defense-in-depth's misdirection layer: it does not stop an attacker, it exposes and slows them.
- The value is the intelligence: honeypots capture attacker behavior that IDS cannot — the actual tools, the exploit chain, the lateral movement patterns, the exfiltration targets. Every probe of a honeypot is a free red-team report from the real attacker population, and the collected artifacts (IPs, payloads, commands) feed detection elsewhere.
- The failure modes: the honeypot that is too attractive (it lures internal users or legitimate automation — false alarms that erode trust in the alerting), the honeypot that is discoverable (fingerprintable service banners teach attackers to avoid the whole network), and the danger case — a high-interaction honeypot that is poorly isolated becomes a beachhead the attacker uses to attack the real network.
- For mykb: honeypots sit in the detection cluster with IDS and fail2ban — the three form the detection spectrum: log-triggered prevention, signature/anomaly detection, and deliberate deception.

## Related
- [[wiki/devops-infra/network-observability|Network Observability]] — related coverage in the same cluster
- [[wiki/cloud-infra/network-address-translation-variants|NAT Variants]] — related coverage in the same cluster
- [[wiki/infrastructure/network-interface-bonding|Network Interface Bonding]] — related coverage in the same cluster
- [[wiki/infrastructure/network-policy|Network Policy]] — related coverage in the same cluster
- [[wiki/infrastructure/storage-systems|Storage Systems]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
