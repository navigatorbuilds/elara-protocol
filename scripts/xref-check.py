#!/usr/bin/env python3
"""Cross-reference checker for Elara whitepapers.

Scans all 4 current whitepapers and finds every version reference
to other Elara documents. Reports mismatches, stale references,
and builds a full dependency map.

Usage:
    python scripts/xref-check.py              # scan and report
    python scripts/xref-check.py --fix        # show what needs fixing
    python scripts/xref-check.py --deps       # show dependency graph only
"""

import re
import sys
from pathlib import Path

DOCS_DIR = Path(__file__).parent.parent / "docs"

# Current versions — UPDATE THESE when bumping any paper
CURRENT_VERSIONS = {
    "protocol": "0.5.2",
    "core": "1.5.1",
    "hardware": "0.1.8",
    "tokenomics": "0.3.2",
}

# Map paper names to their current filenames
PAPERS = {
    "protocol": f"ELARA-PROTOCOL-WHITEPAPER.v{CURRENT_VERSIONS['protocol']}.md",
    "core": f"ELARA-CORE-WHITEPAPER.v{CURRENT_VERSIONS['core']}.md",
    "hardware": f"ELARA-HARDWARE-WHITEPAPER.v{CURRENT_VERSIONS['hardware']}.md",
    "tokenomics": f"ELARA-TOKENOMICS.v{CURRENT_VERSIONS['tokenomics']}.md",
}

# Patterns that match version references to each paper
VERSION_PATTERNS = {
    "protocol": [
        r"Protocol.*?[Ww]hitepaper.*?v(\d+\.\d+\.\d+)",
        r"Protocol.*?[Vv]ersion\s+(\d+\.\d+\.\d+)",
        r"protocol\s+whitepaper\s*\(v(\d+\.\d+\.\d+)\)",
        r"Protocol.*?v(\d+\.\d+\.\d+).*?Vasic",
        r"Elara Protocol.*?Version\s+(\d+\.\d+\.\d+)",
    ],
    "core": [
        r"Core.*?[Ww]hitepaper.*?v(\d+\.\d+\.\d+)",
        r"Core.*?v(\d+\.\d+\.\d+).*?Vasic",
        r"Core.*?[Vv]ersion\s+(\d+\.\d+\.\d+)",
    ],
    "hardware": [
        r"Hardware.*?[Ww]hitepaper.*?v(\d+\.\d+\.\d+)",
        r"Hardware.*?[Vv]ersion\s+(\d+\.\d+\.\d+)",
        r"Hardware\s+WP.*?v(\d+\.\d+\.\d+)",
        r"Hardware.*?v(\d+\.\d+\.\d+).*?Vasic",
    ],
    "tokenomics": [
        r"Tokenomics.*?[Ww]hitepaper.*?v(\d+\.\d+\.\d+)",
        r"Tokenomics.*?[Vv]ersion\s+(\d+\.\d+\.\d+)",
        r"Tokenomics.*?v(\d+\.\d+\.\d+).*?Vasic",
    ],
}

# Software version patterns — these reference the CODEBASE version (v0.x.x)
# not the WHITEPAPER version (v1.x.x). Tracked separately as informational.
SOFTWARE_VERSION = "0.13.0"  # Current Elara Core software version

SOFTWARE_PATTERNS = [
    r"Elara\s+Core\s+v(\d+\.\d+\.\d+)",
    r"\*\*shipped\*\*\s*\(v(\d+\.\d+\.\d+)",
]


def scan_paper(paper_name: str) -> list[dict]:
    """Scan a paper for all version references to other papers."""
    filepath = DOCS_DIR / PAPERS[paper_name]
    if not filepath.exists():
        print(f"  WARNING: {filepath.name} not found")
        return []

    lines = filepath.read_text().splitlines()
    refs = []

    for target_paper, patterns in VERSION_PATTERNS.items():
        if target_paper == paper_name:
            # Skip self-references (paper referencing its own version)
            continue
        for pattern in patterns:
            for i, line in enumerate(lines, 1):
                for match in re.finditer(pattern, line, re.IGNORECASE):
                    version = match.group(1)
                    refs.append({
                        "source": paper_name,
                        "target": target_paper,
                        "version_found": version,
                        "version_expected": CURRENT_VERSIONS[target_paper],
                        "line": i,
                        "stale": version != CURRENT_VERSIONS[target_paper],
                        "context": line.strip()[:120],
                    })

    # Check software version references (informational, not errors)
    for pattern in SOFTWARE_PATTERNS:
        for i, line in enumerate(lines, 1):
            for match in re.finditer(pattern, line, re.IGNORECASE):
                version = match.group(1)
                already_found = any(r["line"] == i for r in refs)
                if not already_found:
                    refs.append({
                        "source": paper_name,
                        "target": "core-software",
                        "version_found": version,
                        "version_expected": SOFTWARE_VERSION,
                        "line": i,
                        "stale": False,  # Software versions in roadmap are historical
                        "context": line.strip()[:120],
                        "info_only": True,
                    })

    return refs


def print_dependency_graph(all_refs: list[dict]):
    """Print which papers reference which."""
    print("\n DEPENDENCY GRAPH")
    print("=" * 60)

    deps: dict[str, set] = {p: set() for p in PAPERS}
    for ref in all_refs:
        if not ref.get("info_only"):
            deps[ref["source"]].add(ref["target"])

    for paper, targets in sorted(deps.items()):
        current_v = CURRENT_VERSIONS[paper]
        if targets:
            target_str = ", ".join(
                f"{t} v{CURRENT_VERSIONS[t]}" for t in sorted(targets)
            )
            print(f"  {paper} v{current_v} --> {target_str}")
        else:
            print(f"  {paper} v{current_v} --> (no cross-references)")

    print()


def print_full_report(all_refs: list[dict]):
    """Print all references with stale highlighting."""
    print("\n CROSS-REFERENCE REPORT")
    print("=" * 60)
    print(f"  Current versions: "
          f"Protocol v{CURRENT_VERSIONS['protocol']} | "
          f"Core v{CURRENT_VERSIONS['core']} | "
          f"Hardware v{CURRENT_VERSIONS['hardware']} | "
          f"Tokenomics v{CURRENT_VERSIONS['tokenomics']}")
    print()

    stale_count = 0
    ok_count = 0

    for paper_name in PAPERS:
        paper_refs = [r for r in all_refs if r["source"] == paper_name]
        if not paper_refs:
            print(f"  [{paper_name.upper()}] No cross-references found")
            continue

        print(f"  [{paper_name.upper()} v{CURRENT_VERSIONS[paper_name]}]")
        for ref in sorted(paper_refs, key=lambda r: r["line"]):
            is_info = ref.get("info_only", False)
            if is_info:
                print(
                    f"  .. L{ref['line']:>4d} | "
                    f"software v{ref['version_found']} | INFO"
                )
                continue
            status = "STALE" if ref["stale"] else "OK"
            marker = "!!" if ref["stale"] else "  "
            print(
                f"  {marker} L{ref['line']:>4d} | "
                f"{ref['target']} v{ref['version_found']}"
                f"{' -> v' + ref['version_expected'] if ref['stale'] else ''}"
                f" | {status}"
            )
            if ref["stale"]:
                print(f"         {ref['context']}")
                stale_count += 1
            else:
                ok_count += 1
        print()

    print("-" * 60)
    print(f"  Total: {ok_count + stale_count} cross-references "
          f"({ok_count} OK, {stale_count} STALE)")

    if stale_count > 0:
        print(f"\n  !! {stale_count} STALE REFERENCE(S) NEED FIXING !!")
    else:
        print("\n  All cross-references are consistent.")

    return stale_count


def main():
    args = set(sys.argv[1:])
    deps_only = "--deps" in args
    show_fix = "--fix" in args

    # Check all papers exist
    missing = []
    for name, filename in PAPERS.items():
        if not (DOCS_DIR / filename).exists():
            missing.append(f"{name}: {filename}")
    if missing:
        print("Missing papers:")
        for m in missing:
            print(f"  {m}")
        print()

    # Scan all papers
    all_refs = []
    for paper_name in PAPERS:
        all_refs.extend(scan_paper(paper_name))

    # Print dependency graph
    print_dependency_graph(all_refs)

    if deps_only:
        return 0

    # Print full report
    stale_count = print_full_report(all_refs)

    if show_fix and stale_count > 0:
        print("\n FIX LIST")
        print("=" * 60)
        stale_refs = [r for r in all_refs if r["stale"]]
        for ref in stale_refs:
            src_file = PAPERS[ref["source"]]
            print(
                f"  {src_file}:{ref['line']}\n"
                f"    {ref['target']} v{ref['version_found']} "
                f"-> v{ref['version_expected']}\n"
                f"    {ref['context']}\n"
            )

    return 1 if stale_count > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
