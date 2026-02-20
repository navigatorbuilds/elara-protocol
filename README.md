# Elara Protocol

**A Post-Quantum Universal Validation Layer for Digital Work**

---

## What is this?

The Elara Protocol is a layered architecture for cryptographically validating all forms of digital work — from a poem written on a $30 phone in Kenya to telemetry data from a Mars colony operations center.

- **Layer 1: Local Validation** — Hash, sign, prove. Works offline, on any device, in under 2ms. Post-quantum from genesis.
- **Layer 1.5: Performance Runtime** — Optional Rust DAM VM with 9 ISA operations, parallel batch verify, and PyO3 bindings. Same wire format as Layer 1.
- **Layer 2: Network Consensus** — Adaptive Witness Consensus (AWC) across partitioned networks, including interplanetary delays.
- **Layer 3: AI Intelligence** — Persistent cognitive architecture for pattern recognition, anomaly detection, and collective learning across the network.

The minimum viable network is **one device**. No blockchain required. No cloud dependency. No subscription.

## Whitepapers

| Document | Pages | Download |
|----------|-------|----------|
| **Elara Protocol Whitepaper v0.4.1** | 67 | [**PDF**](ELARA-PROTOCOL-WHITEPAPER.v0.4.1.pdf) |
| *Complete protocol specification: DAM architecture, dimensional extensibility, Layer 1.5 performance runtime, Layer 2 testnet, post-quantum cryptography, zero-knowledge validation, interplanetary operations, token economics (summary), 33 attack vector analysis, Phase 6 native hardware. Unified trust model (node-level + record-level), combined governance formula, AWC implementation status.* |||
| **Elara Core Whitepaper v1.4.0** | 51 | [**PDF**](ELARA-CORE-WHITEPAPER.v1.4.0.pdf) |
| *Layer 3 reference implementation: persistent memory, 3D Cognition (models, predictions, principles, workflow patterns), Cortical Execution Model (5-layer concurrent architecture: reflex cache, reactive event bus, deliberative worker pools, contemplative brain, social network), long-range temporal memory with landmarks, reflexive memory hippocampus, knowledge graph, Layer 1↔Layer 3 bridge, Layer 2 network stub, emotional modeling, continuous autonomous thinking — 45 tools, 15 modules, 222 tests* |||
| **Elara Hardware Whitepaper v0.1.7** | 51 | *Available on request* |
| *Native hardware architecture for the DAM: 9-op ISA, dimensional extensibility, dimensional memory model, photonic mesh interconnect, heterogeneous chiplet design, PQC acceleration, security analysis, storage economics cross-reference* |||
| **Elara Tokenomics Paper v0.2.0** | 15 | *Available on request* |
| *Token economic model: conservation supply, storage delegation market, witness incentive mechanics, anti-centralization mechanisms, governance economics (with combined formula), two-level trust model, launch strategy* |||

All documents have undergone 8 audit passes for cross-reference consistency, formula verification, numerical accuracy, and cross-document coherence. Previous versions and source files are maintained privately.

## Architecture

```
Device Spectrum                      What They Run
─────────────────────────────────────────────────────
Microcontroller (factory sensor)     Layer 1 only
$30 Phone (Kenya)                    Layer 1 only
Laptop (developer)                   Layer 1 + 1.5 (Rust) + 2
GPU Server (network node)            Layer 1 + 1.5 + 2 + 3 (Elara Core)
```

**No layer depends on the layers above it.** Layer 1 is universal. Layer 2 is accessible. Layer 3 is powerful.

## Key Innovation: The Directed Acyclic Mesh (DAM)

The protocol introduces a novel data structure — the **Directed Acyclic Mesh** — extending DAG architectures with five dimensions:

1. **Time** — Causal ordering without universal clock
2. **Concurrency** — Parallel validation streams
3. **Zone topology** — Partition-tolerant across planetary distances
4. **Classification projection** — Context-dependent views of the same data
5. **AI analysis** — Cognitive layer for pattern discovery

The architecture is designed for dimensional expansion — additional structural dimensions and operational layers can be added when hardware substrates exist to support them. **Lineage Depth** (causal hop count) is the first candidate for a sixth dimension, mapping to 3D stacked memory.

This is not a blockchain. It is a mesh that works when nodes are offline, when light-speed delays span 4-22 minutes, and when the network is partitioned across planets.

## Implementations

### Layer 1: Elara Layer 1 (Local Validation)

Reference implementation of Layer 1 — post-quantum local validation with Dilithium3 + SPHINCS+, SQLite-backed DAG, and a CLI for validating files from the terminal.

- **Repository:** Private (patent pending)
- **Crypto:** CRYSTALS-Dilithium3 (FIPS 204) + SPHINCS+-SHA2-192f (FIPS 205)
- **Performance:** Identity generation in 2ms, file validation in 1-2ms

### Layer 1.5: Elara Runtime (Rust DAM Virtual Machine)

Rust implementation of DAM concepts with PyO3 bindings — crypto, wire format, dimensional storage, and all 9 DAM operations. Byte-identical wire format with Layer 1. Callable from Python as an optional fast path.

- **Repository:** Private (patent pending)
- **Crypto:** Same liboqs algorithms via `oqs` Rust crate (vendored), cross-language sign/verify verified
- **Features:** 5-tuple addressing, tiled storage, in-memory DAG index, parallel batch verify via rayon

### Layer 3: Elara Core (AI Intelligence)

Reference implementation of Layer 3 — a cognitive architecture that gives AI assistants persistent memory, emotional modeling, autonomous reasoning, and self-awareness.

- **Repository:** [github.com/navigatorbuilds/elara-core](https://github.com/navigatorbuilds/elara-core)
- **PyPI:** `pip install elara-core`
- **Documentation:** [elara.navigatorbuilds.com](https://elara.navigatorbuilds.com)

## Provenance

All documents are timestamped using [OpenTimestamps](https://opentimestamps.org/) — cryptographic proofs anchored in the Bitcoin blockchain.

| Document | Hash (SHA-256) |
|----------|---------------|
| Protocol v0.4.1 | `4f0ea34aa76800ed3d8fafffc87a34d1318f0493d55389da15f6bbabad189e46` |
| Core v1.4.0 | `3119757080b79ac2d0ae10dd098c6dca092e58455ff4a8eb40a9fe2b6f42e80d` |
| Hardware v0.1.7 | `1a2fbc5101ea221ca2ca4d58a5cfa5588bbf65bf294c6b747feab53c14785dee` |
| Tokenomics v0.2.0 | `9e50ddc10aa2df36e242dbe6294d83b7e20be09564ea7f1117e18e6ff109d613` |

## Intellectual Property

- **US Provisional Patent:** Application No. 63/983,064 (filed February 14, 2026)
- **Priority date:** February 14, 2026
- **Non-provisional deadline:** February 14, 2027

## License

[Business Source License 1.1](LICENSE) — free to read, fork, modify, and use for personal, educational, academic, and internal purposes. Commercial use of the protocol specification to build competing products requires a separate license. Converts to Apache 2.0 on February 18, 2030.

## Author

**Nenad Vasic** — Solo developer, Montenegro
- Email: nenadvasic@protonmail.com
- GitHub: [@navigatorbuilds](https://github.com/navigatorbuilds)
- Site: [navigatorbuilds.com](https://navigatorbuilds.com)

---

*The same math for the teenager in Kenya and the colonist on Mars.*
