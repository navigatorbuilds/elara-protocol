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
| **Elara Protocol Whitepaper v0.2.8** | 51 | [**PDF**](ELARA-PROTOCOL-WHITEPAPER.v0.2.8.pdf) |
| *Complete protocol specification: DAM architecture, Layer 1.5 performance runtime, post-quantum cryptography, zero-knowledge validation, interplanetary operations, token economics, 33 attack vector analysis, Phase 6 native hardware* |||
| **Elara Core Whitepaper v1.3.3** | 27 | [**PDF**](ELARA-CORE-WHITEPAPER.v1.3.3.pdf) |
| *Layer 3 reference implementation: persistent memory, 3D Cognition, knowledge graph, emotional modeling, continuous autonomous thinking, deployment modularity* |||
| **Elara Hardware Whitepaper v0.1.4** | 66 | [**PDF**](ELARA-HARDWARE-WHITEPAPER.v0.1.4.pdf) |
| *Native hardware architecture for the DAM: 9-op ISA, dimensional memory model, photonic mesh interconnect, heterogeneous chiplet design, PQC acceleration, security analysis* |||

**Previous versions:** [Protocol v0.2.7 (PDF)](docs/ELARA-PROTOCOL-WHITEPAPER.v0.2.7.pdf), [v0.2.6 (PDF)](docs/ELARA-PROTOCOL-WHITEPAPER.v0.2.6.pdf), [v0.2.5 (PDF)](docs/ELARA-PROTOCOL-WHITEPAPER.v0.2.5.pdf). [Core v1.3.2 (PDF)](docs/ELARA-CORE-WHITEPAPER.v1.3.2.pdf), [v1.3.1 (PDF)](docs/ELARA-CORE-WHITEPAPER.v1.3.1.pdf), [v1.3.0 (PDF)](docs/ELARA-CORE-WHITEPAPER.v1.3.0.pdf). [Hardware v0.1.3 (PDF)](docs/ELARA-HARDWARE-WHITEPAPER.v0.1.3.pdf), [v0.1.2 (PDF)](docs/ELARA-HARDWARE-WHITEPAPER.v0.1.2.pdf), [v0.1.1 (PDF)](docs/ELARA-HARDWARE-WHITEPAPER.v0.1.1.pdf), [v0.1.0 (PDF)](docs/ELARA-HARDWARE-WHITEPAPER.v0.1.0.pdf). v1.3.3: Knowledge graph module (43 tools, 13 modules). v0.2.8/v1.3.2/v0.1.4: Layer 1.5 (Rust DAM VM) added to protocol architecture.

Markdown source files, OTS proofs, and all versions are in the [`docs/`](docs/) folder.

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

This is not a blockchain. It is a mesh that works when nodes are offline, when light-speed delays span 4-22 minutes, and when the network is partitioned across planets.

## Implementations

### Layer 1: Elara Layer 1 (Local Validation)

Reference implementation of Layer 1 — post-quantum local validation with Dilithium3 + SPHINCS+, SQLite-backed DAG, and a CLI for validating files from the terminal.

- **Repository:** [github.com/navigatorbuilds/elara-layer1](https://github.com/navigatorbuilds/elara-layer1)
- **Crypto:** CRYSTALS-Dilithium3 (FIPS 204) + SPHINCS+-SHA2-192f (FIPS 205)
- **Performance:** Identity generation in 2ms, file validation in 1-2ms

### Layer 1.5: Elara Runtime (Rust DAM Virtual Machine)

Rust implementation of DAM concepts with PyO3 bindings — crypto, wire format, dimensional storage, and all 9 DAM operations. Byte-identical wire format with Layer 1. Callable from Python as an optional fast path.

- **Repository:** [github.com/navigatorbuilds/elara-runtime](https://github.com/navigatorbuilds/elara-runtime)
- **Crypto:** Same liboqs algorithms via `oqs` Rust crate (vendored), cross-language sign/verify verified
- **Features:** 5-tuple addressing, tiled storage, in-memory DAG index, parallel batch verify via rayon

### Layer 3: Elara Core (AI Intelligence)

Reference implementation of Layer 3 — a cognitive architecture that gives AI assistants persistent memory, emotional modeling, autonomous reasoning, and self-awareness.

- **Repository:** [github.com/navigatorbuilds/elara-core](https://github.com/navigatorbuilds/elara-core)
- **PyPI:** `pip install elara-core`
- **Documentation:** [elara.navigatorbuilds.com](https://elara.navigatorbuilds.com)

## Provenance

All documents are timestamped using [OpenTimestamps](https://opentimestamps.org/) — cryptographic proofs anchored in the Bitcoin blockchain. OTS proof files (`.ots`) are included in [`docs/`](docs/).

| Document | Hash (SHA-256) |
|----------|---------------|
| Protocol v0.2.8 | `371a933a20f9de7a457200f8fe108a9a9113dd0c64b73d2b4e54ec845237a762` |
| Core v1.3.3 | `28803e4c80069163c7d5469c4e2fb7e97b29ff3826737bd01051b5126f9bd079` |
| Hardware v0.1.4 | `1c36e4af613d714a931d01f2f2b8de55081e4b8bda944c14e08a17d053e359c9` |

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
