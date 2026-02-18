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
| **Elara Protocol Whitepaper v0.3.0** | 51 | [**PDF**](ELARA-PROTOCOL-WHITEPAPER.v0.3.0.pdf) |
| *Complete protocol specification: DAM architecture, dimensional extensibility, Layer 1.5 performance runtime, Layer 2 testnet, post-quantum cryptography, zero-knowledge validation, interplanetary operations, token economics, 33 attack vector analysis, Phase 6 native hardware* |||
| **Elara Core Whitepaper v1.3.5** | 43 | [**PDF**](ELARA-CORE-WHITEPAPER.v1.3.5.pdf) |
| *Layer 3 reference implementation: persistent memory, 3D Cognition (models, predictions, principles, workflow patterns), prompt-level intention resolution, knowledge graph, Layer 1↔Layer 3 bridge, Layer 2 network stub + testnet, emotional modeling, continuous autonomous thinking, deployment modularity — 45 tools, 15 modules* |||
| **Elara Hardware Whitepaper v0.1.6** | 66 | [**PDF**](ELARA-HARDWARE-WHITEPAPER.v0.1.6.pdf) |
| *Native hardware architecture for the DAM: 9-op ISA, dimensional extensibility, dimensional memory model, photonic mesh interconnect, heterogeneous chiplet design, PQC acceleration, security analysis* |||

**Previous versions:** [Protocol v0.2.9 (PDF)](docs/ELARA-PROTOCOL-WHITEPAPER.v0.2.9.pdf), [v0.2.8 (PDF)](docs/ELARA-PROTOCOL-WHITEPAPER.v0.2.8.pdf), [v0.2.7 (PDF)](docs/ELARA-PROTOCOL-WHITEPAPER.v0.2.7.pdf), [v0.2.6 (PDF)](docs/ELARA-PROTOCOL-WHITEPAPER.v0.2.6.pdf), [v0.2.5 (PDF)](docs/ELARA-PROTOCOL-WHITEPAPER.v0.2.5.pdf). [Core v1.3.4 (PDF)](docs/ELARA-CORE-WHITEPAPER.v1.3.4.pdf), [v1.3.3 (PDF)](docs/ELARA-CORE-WHITEPAPER.v1.3.3.pdf), [v1.3.2 (PDF)](docs/ELARA-CORE-WHITEPAPER.v1.3.2.pdf), [v1.3.1 (PDF)](docs/ELARA-CORE-WHITEPAPER.v1.3.1.pdf), [v1.3.0 (PDF)](docs/ELARA-CORE-WHITEPAPER.v1.3.0.pdf). [Hardware v0.1.5 (PDF)](docs/ELARA-HARDWARE-WHITEPAPER.v0.1.5.pdf), [v0.1.4 (PDF)](docs/ELARA-HARDWARE-WHITEPAPER.v0.1.4.pdf), [v0.1.3 (PDF)](docs/ELARA-HARDWARE-WHITEPAPER.v0.1.3.pdf), [v0.1.2 (PDF)](docs/ELARA-HARDWARE-WHITEPAPER.v0.1.2.pdf), [v0.1.1 (PDF)](docs/ELARA-HARDWARE-WHITEPAPER.v0.1.1.pdf), [v0.1.0 (PDF)](docs/ELARA-HARDWARE-WHITEPAPER.v0.1.0.pdf). v0.3.0: Layer 2 testnet operational, L1↔L3 bridge shipped, Phase 1 roadmap items marked as shipped. v1.3.5: 45 tools across 15 modules, 15-phase overnight brain, v0.11.0 references, bridge hardening details. v0.1.6: 100 total tests (72 Rust + 28 cross-lang Python), updated cross-references. All three documents audited for cross-reference consistency, hash chains corrected, reference citations fixed. Second audit: energy μJ→Wh conversion corrected (was 3,600x inflated), ChromaDB 9→14 collections, personality mode values synced with code, directed phase names synced with code, four-layer architecture (was three), Dilithium3 Round 3 vs FIPS 204 clarified, line count updated to ~31,400. Third audit (formulas + terms): decay formula fixed (linear→exponential, was producing invalid values >20h), conviction voting reconciled (tau is time constant not half-life, 7→30 day ramp clarified), temporal headroom corrected (432x→4,320x, was 10x off), monolithic yield corrected (35%→64%, Poisson model), naive-to-cached speedup corrected (150x→73x), cross-zone trust formula now includes correlation discount, gossip rounds corrected (~20→~6-10), Phase 6 dates (2033→2026-2040), dual Layer 2 numbering fixed, SHA-2/SHA-3 dual-mode hash cores specified, NTT count updated, link budget specified with receiver sensitivity, resonance score variable maximum documented, qwen2.5:32b→7b, tool dispatch count 38→37, "quadrants"→"regions". Fourth audit: gossip traffic calculation corrected (was understated — clarified compact announcements, zone-partitioned propagation, O(n·log n) message count), "38 non-core tools"→37 (Core L1277), phase label "Synthesis"→"Self-Review" + added round-15.md (Core L967), "Buildable today"→"Component technologies available" (Hardware Gen 1), PRIVATE record misleading 100x removed (ZKP dominates both sides), Dilithium3 table footnoted for FIPS 204 final, serialization tax range clarified, Gen 2 energy 2.4→2.38μJ, "AI analysis layer"→"AI intelligence layer", PUBLIC signing 330→310μs, attack vector 11.26 double-count clarified, witness CPU-seconds 2→1.5, SPHINCS+ asymmetric speedup explained, "testnet"→"stub testnet". Fifth audit: Dilithium verification CPU-hours was 5x inflated (double-counting 5-witness factor: 208,333→41,667 CPU-hours, total 225,834→59,168), ToC Phase 6 date 2033→2026, Gen TDP ranges synced with Section 10.1 detailed breakdown (Gen 1 12-18W→12-15W, Gen 2 18-28W→17-23W, Gen 3 25-34W→20-34W), valence contribution ratio 5-6x→6-7x (actual 6.5), "a edge"→"an edge", hardware ops total 18→19μs.

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

The architecture is designed for dimensional expansion — additional structural dimensions and operational layers can be added when hardware substrates exist to support them. **Lineage Depth** (causal hop count) is the first candidate for a sixth dimension, mapping to 3D stacked memory.

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
| Protocol v0.3.0 | `591abec737f28d864bcd39c664eb00becbc8b9bd9567c1882ecee854af42fb2e` |
| Core v1.3.5 | `5bfabe1b198dcb3c8949d67ac31062f2bd5ef002cdfe1942c4c7b41c4780f699` |
| Hardware v0.1.6 | `f5e3f2fca7def44de2c8333b8b6761421f5f2293d195334334d818baa3793a24` |

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
