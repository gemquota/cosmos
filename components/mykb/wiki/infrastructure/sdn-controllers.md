---
type: "concept"
title: "SDN Controllers"
description: "Centralized brains that program distributed forwarding"
tags: ["sdn", "controller", "networking", "automation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# SDN Controllers

## Summary
SDN controllers centralize the network's control plane: a software brain computes forwarding decisions and programs distributed switches through southbound APIs such as OpenFlow. This separation of "what the network should do" from "how individual switches do it" enables policy-driven automation, global optimization, and programmatic network services.

## Details
- Mechanism: the controller maintains a topology graph and policy model, computes paths or flow rules, and installs them into switches via the southbound API. Applications talk to the controller through a northbound API to request connectivity, security, or QoS services without touching switch CLI.
- Deployments: single controllers are simple but fragile; clustered controllers (for example ONOS or OpenDaylight with Raft-based state replication) tolerate controller failure; hierarchical designs place domain controllers under a parent for large fabrics, where the top-level controller acts as a policy store rather than a hot path.
- Failure modes: controller loss can leave switches fail-open (forwarding with stale rules) or fail-closed (dropping new flows) depending on configuration; clustered controllers can split-brain; flow-table overflow pushes rules out of TCAM; stale topology after a link flap causes black holes until recomputation.
- Tradeoffs: centralized visibility and programmable policy versus a new single point of failure, higher operational complexity, and harder debugging when the data plane and control plane disagree. The controller must also handle switch-request storms when many devices reconnect at once.
- Operational practice: run controllers in odd-numbered clusters, pre-provision fallback flows for critical paths, monitor southbound session counts, and version the northbound API carefully because applications depend on it. Test controller restart with switches in varied states, since recovery paths differ by configuration.
- Consistency: controllers must reconcile their model against switch reality — periodic resync and switch-side rule verification catch flows deleted or altered out-of-band.
- RSIS3/mykb relevance: the control-plane/data-plane split is a useful analogy for RSIS3's own separation of reflection loops from execution, and this node keeps that parallel retrievable during architecture discussions.

## Related
- [[wiki/devops-infra/ingress-controllers|Ingress Controllers]]
- [[wiki/devops-infra/admission-controllers-and-webhooks|Admission Controllers & Webhooks]]
- [[wiki/infrastructure/storage-systems|Storage Systems]]
