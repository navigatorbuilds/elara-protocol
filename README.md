# Elara Protocol

**A Post-Quantum Universal Validation Layer for Digital Work**

---

## What is this?

The Elara Protocol is a three-layer architecture for cryptographically validating all forms of digital work — from a poem written on a $30 phone in Kenya to telemetry data from a Mars colony operations center.

- **Layer 1: Local Validation** — Hash, sign, prove. Works offline, on any device, in under 2ms. Post-quantum from genesis.
- **Layer 2: Network Consensus** — Adaptive Witness Consensus (AWC) across partitioned networks, including interplanetary delays.
- **Layer 3: AI Intelligence** — Persistent cognitive architecture for pattern recognition, anomaly detection, and collective learning across the network.

The minimum viable network is **one device**. No blockchain required. No cloud dependency. No subscription.

## Whitepapers

| Document | Pages | Download |
|----------|-------|----------|
| **Elara Protocol Whitepaper v0.2.6** | 49 | [**PDF**](docs/ELARA-PROTOCOL-WHITEPAPER.v0.2.6.pdf) |
| *Complete protocol specification: DAM architecture, post-quantum cryptography, zero-knowledge validation, interplanetary operations, token economics, 33 attack vector analysis, Phase 6 native hardware* |||
| **Elara Core Whitepaper v1.3.0** | 26 | [**PDF**](docs/ELARA-CORE-WHITEPAPER.v1.3.0.pdf) |
| *Layer 3 reference implementation: persistent memory, 3D Cognition, emotional modeling, continuous autonomous thinking, deployment modularity* |||
| **Elara Hardware Whitepaper v0.1.0** | 35 | [**PDF**](docs/ELARA-HARDWARE-WHITEPAPER.v0.1.0.pdf) |
| *Native hardware architecture for the DAM: 9-op ISA, dimensional memory model, photonic mesh interconnect, heterogeneous chiplet design, PQC acceleration, security analysis* |||

**Previous versions:** [Protocol v0.2.5 (PDF)](docs/ELARA-PROTOCOL-WHITEPAPER.v0.2.5.pdf) — v0.2.6 adds Phase 6: Native Hardware Architecture (2033–2040).

Markdown source files, OTS proofs, and all versions are in the [`docs/`](docs/) folder.

## Architecture

```
Device Spectrum                      What They Run
─────────────────────────────────────────────────────
Microcontroller (factory sensor)     Layer 1 only
$30 Phone (Kenya)                    Layer 1 only
Laptop (developer)                   Layer 1 + 2
GPU Server (network node)            Layer 1 + 2 + 3 (Elara Core)
```

**No layer depends on the layers above it.** Layer 1 is universal. Layer 2 is accessible. Layer 3 is powerful.

## Key Innovation: The Directed Acyclic Mesh (DAM)

The protocol introduces a novel data structure — the **Directed Acyclic Mesh** — extending DAG architectures with five dimensions:

1. **Time** — Causal ordering without universal clock
2. **Concurrency** — Parallel validation streams
3. **Zone topology** — Partition-tolerant across planetary distances
4. **Classification projection** — Context-dependent views of the same data
5. **AI analysis** — Cognitive layer for pattern discovery

This is not a blockchain. It is a mesh that works when nodes are offline, when light-speed delays span 4-22 minutes, and when the network is partitioned across planets.

## Implementations

### Layer 1: Elara Layer 1 (Local Validation)

Reference implementation of Layer 1 — post-quantum local validation with Dilithium3 + SPHINCS+, SQLite-backed DAG, and a CLI for validating files from the terminal.

- **Repository:** [github.com/navigatorbuilds/elara-layer1](https://github.com/navigatorbuilds/elara-layer1)
- **Crypto:** CRYSTALS-Dilithium3 (FIPS 204) + SPHINCS+-SHA2-192f (FIPS 205)
- **Performance:** Identity generation in 2ms, file validation in 1-2ms

### Layer 3: Elara Core (AI Intelligence)

Reference implementation of Layer 3 — a cognitive architecture that gives AI assistants persistent memory, emotional modeling, autonomous reasoning, and self-awareness.

- **Repository:** [github.com/navigatorbuilds/elara-core](https://github.com/navigatorbuilds/elara-core)
- **PyPI:** `pip install elara-core`
- **Documentation:** [elara.navigatorbuilds.com](https://elara.navigatorbuilds.com)

## Provenance

All documents are timestamped using [OpenTimestamps](https://opentimestamps.org/) — cryptographic proofs anchored in the Bitcoin blockchain. OTS proof files (`.ots`) are included in [`docs/`](docs/).

| Document | Hash (SHA-256) |
|----------|---------------|
| Protocol v0.2.6 | See document footer |
| Core v1.3.0 | `6b7da9f2b92e08344572f20f0098f3e686cf3ccc9bd0bd7af8b76e90bdc0a0e7` |
| Hardware v0.1.0 | `e0f27ed98f7ccd6ef2db04b6c911712b60cbc1bbe4256d1141a93b97924c6225` |

## Intellectual Property

- **US Provisional Patent:** Application No. 63/983,064 (filed February 14, 2026)
- **Priority date:** February 14, 2026
- **Non-provisional deadline:** February 14, 2027

## License

Whitepapers are published for review, collaboration, and academic citation. The protocol specification and reference implementation are open for non-commercial use. See individual documents for details.

## Author

**Nenad Vasic** — Solo developer, Montenegro
- Email: nenadvasic@protonmail.com
- GitHub: [@navigatorbuilds](https://github.com/navigatorbuilds)
- Site: [navigatorbuilds.com](https://navigatorbuilds.com)

---

*The same math for the teenager in Kenya and the colonist on Mars.*
