---
type: "concept"
title: "IPFS & Content Addressing"
description: "Distributed content-addressed storage and its tradeoffs"
tags: ["ipfs", "content-addressing", "p2p", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# IPFS & Content Addressing

## Summary
IPFS (InterPlanetary File System) is a distributed, peer-to-peer storage network built on content addressing: every file is identified by the hash of its contents rather than by a location. The idea — "what you want, not where it is" — inverts the web's model: instead of asking a specific server for a specific path, you ask the network for the content with a given hash, and any node that has it can answer.

## Details
- The mechanism: a file is split into blocks, each block is hashed (CID — content identifier, a multihash), and the file's CID is the root of a Merkle DAG linking the blocks. Because the identifier is derived from the content, identical content always has the identical CID — deduplication is automatic — and any change to any block changes the root CID, giving cryptographic integrity: if you have the CID, you can verify the content you receive is exactly what was requested. The network layer (libp2p) finds peers holding the content (DHT routing, provider records) and retrieves blocks from any of them, with caching at every hop — popular content gets faster and more distributed as more nodes fetch it.
- The strengths: integrity (content-verifiable — no tampered mirrors, no broken links in the classic sense), resilience (no single server to take down; any node with the content serves it), offline/censorship resistance (the network routes around failures and blocking), and deduplication. The flagship use is content-addressed publishing (immutable releases, verifiable datasets), which is why the pattern appears in package registries (IPFS-backed mirrors), NFT metadata, and archive projects: the CID is a permanent, self-verifying reference.
- The weaknesses are the other half of the tradeoff, and they are structural: content availability is not guaranteed — a CID only resolves if some peer is hosting the blocks, so unpinned content can vanish (the famous "permanent web" that needs pinning services to actually persist); mutable content needs a naming layer (IPNS/DNSLink — a pointer that updates — reintroducing the trust question content addressing eliminated); performance depends on peer proximity and DHT health; and the storage is a public good problem — most nodes store little, and the network relies on dedicated pinning services.
- The comparison that clarifies it: content addressing vs location addressing is the same shift as git (content-addressed commits) vs a shared filesystem — and the failure modes are the same: content-addressed systems guarantee integrity, not availability; persistence is an operational choice, not a property of the hash.
- For mykb: the node connects content hashing/ETags (the same integrity logic at web scale), CDNs (the centralized availability answer), and storage systems — the tradeoff spectrum for content distribution.

## Related
- [[wiki/devops-infra/content-hashing-and-etags|Content Hashing & ETags]]
- [[wiki/cloud-infra/content-delivery-networks|Content Delivery Networks]]
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
