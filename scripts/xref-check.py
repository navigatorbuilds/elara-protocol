#!/usr/bin/env python3
"""Cross-reference checker for Elara whitepapers.

Scans all 4 current whitepapers and finds every version reference
to other Elara documents. Reports mismatches, stale references,
builds a full dependency map, checks OTS timestamps, and verifies
GitHub/deployment readiness.

Usage:
    python scripts/xref-check.py              # scan and report
    python scripts/xref-check.py --fix        # show what needs fixing
    python scripts/xref-check.py --deps       # show dependency graph only
"""

import re
import subprocess
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
        r"Hardware\s+[Ww]hitepaper.*?v(\d+\.\d+\.\d+)",
        r"Hardware\s+[Ww]hitepaper.*?[Vv]ersion\s+(\d+\.\d+\.\d+)",
        r"Hardware\s+WP.*?v(\d+\.\d+\.\d+)",
        r"Hardware\s+[Ww]hitepaper.*?v(\d+\.\d+\.\d+).*?Vasic",
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


# Which papers are PUBLIC (pushed to GitHub) vs PRIVATE (local only)
PUBLIC_PAPERS = {"protocol", "core"}
PRIVATE_PAPERS = {"hardware", "tokenomics"}

# Expected root-level PDFs on GitHub (public papers only)
ROOT_PDFS = {
    "protocol": f"ELARA-PROTOCOL-WHITEPAPER.v{CURRENT_VERSIONS['protocol']}.pdf",
    "core": f"ELARA-CORE-WHITEPAPER.v{CURRENT_VERSIONS['core']}.pdf",
}


def check_ots_timestamps() -> int:
    """Check that all current whitepapers have OTS timestamps."""
    print("\n OTS TIMESTAMP CHECK")
    print("=" * 60)

    issues = 0
    for name, filename in PAPERS.items():
        md_path = DOCS_DIR / filename
        pdf_path = DOCS_DIR / filename.replace(".md", ".pdf")

        for path, label in [(md_path, "md"), (pdf_path, "pdf")]:
            ots_path = Path(str(path) + ".ots")
            if not path.exists():
                print(f"  !! {name} {label}: FILE MISSING — {path.name}")
                issues += 1
            elif not ots_path.exists():
                print(f"  !! {name} {label}: NO OTS — run: ots stamp {path.name}")
                issues += 1
            else:
                # Check OTS is newer than source (not stale)
                if ots_path.stat().st_mtime < path.stat().st_mtime:
                    print(f"  !! {name} {label}: STALE OTS — source modified after stamping")
                    issues += 1
                else:
                    print(f"     {name} {label}: OK")

    print()
    if issues > 0:
        print(f"  !! {issues} OTS issue(s) found")
    else:
        print("  All timestamps present and current.")

    return issues


def check_file_placement() -> int:
    """Check that files are in the right places (root PDFs, docs/ folder)."""
    print("\n FILE PLACEMENT CHECK")
    print("=" * 60)

    repo_root = DOCS_DIR.parent
    issues = 0

    # Check root-level PDFs for public papers
    for name, pdf_name in ROOT_PDFS.items():
        root_pdf = repo_root / pdf_name
        docs_pdf = DOCS_DIR / pdf_name
        if not root_pdf.exists():
            print(f"  !! {name}: ROOT PDF MISSING — {pdf_name}")
            issues += 1
        elif not docs_pdf.exists():
            print(f"  !! {name}: DOCS PDF MISSING — docs/{pdf_name}")
            issues += 1
        else:
            print(f"     {name}: root + docs/ PDF present")

    # Check docs/ has md + pdf for ALL papers
    for name, filename in PAPERS.items():
        md_path = DOCS_DIR / filename
        pdf_path = DOCS_DIR / filename.replace(".md", ".pdf")
        if not md_path.exists():
            print(f"  !! {name}: docs/ MD MISSING — {filename}")
            issues += 1
        if not pdf_path.exists():
            print(f"  !! {name}: docs/ PDF MISSING — {filename.replace('.md', '.pdf')}")
            issues += 1

    # Check for stale root PDFs (old versions still in root)
    for pdf_file in sorted(repo_root.glob("ELARA-*.pdf")):
        if pdf_file.name == "LICENSE.pdf":
            continue
        if pdf_file.name not in ROOT_PDFS.values():
            print(f"  ?? STALE ROOT PDF: {pdf_file.name} — consider removing")
            issues += 1

    print()
    if issues > 0:
        print(f"  !! {issues} placement issue(s) found")
    else:
        print("  All files in correct locations.")

    return issues


def check_github_status() -> int:
    """Check git status — uncommitted changes, unpushed commits, tracked files."""
    print("\n GITHUB STATUS CHECK")
    print("=" * 60)

    repo_root = DOCS_DIR.parent
    issues = 0

    # Check for uncommitted changes in tracked files
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True, text=True, cwd=repo_root
        )
        changes = [
            line for line in result.stdout.strip().split("\n")
            if line.strip()
        ]
        if changes:
            print(f"  !! {len(changes)} uncommitted change(s):")
            for c in changes[:10]:
                print(f"     {c}")
            issues += len(changes)
        else:
            print("     Working tree clean")
    except FileNotFoundError:
        print("  ?? git not found")
        issues += 1

    # Check for unpushed commits
    try:
        result = subprocess.run(
            ["git", "log", "--oneline", "@{u}..HEAD"],
            capture_output=True, text=True, cwd=repo_root
        )
        unpushed = [
            line for line in result.stdout.strip().split("\n")
            if line.strip()
        ]
        if unpushed:
            print(f"  !! {len(unpushed)} unpushed commit(s):")
            for c in unpushed[:5]:
                print(f"     {c}")
            issues += 1
        else:
            print("     All commits pushed")
    except FileNotFoundError:
        pass

    # Check that public papers are tracked in git
    try:
        result = subprocess.run(
            ["git", "ls-files"],
            capture_output=True, text=True, cwd=repo_root
        )
        tracked = set(result.stdout.strip().split("\n"))

        for name in PUBLIC_PAPERS:
            md_file = f"docs/{PAPERS[name]}"
            pdf_root = ROOT_PDFS.get(name, "")
            pdf_docs = f"docs/{PAPERS[name].replace('.md', '.pdf')}"
            ots_md = f"docs/{PAPERS[name]}.ots"
            ots_pdf = f"docs/{PAPERS[name].replace('.md', '.pdf')}.ots"

            for f, label in [
                (md_file, "docs/ md"),
                (pdf_root, "root pdf"),
                (pdf_docs, "docs/ pdf"),
                (ots_md, "md.ots"),
                (ots_pdf, "pdf.ots"),
            ]:
                if f and f not in tracked:
                    print(f"  !! {name}: NOT TRACKED — {f}")
                    issues += 1

        # Verify private papers are NOT tracked
        for name in PRIVATE_PAPERS:
            md_file = f"docs/{PAPERS[name]}"
            if md_file in tracked:
                print(f"  !! {name}: TRACKED BUT SHOULD BE PRIVATE — {md_file}")
                issues += 1

    except FileNotFoundError:
        pass

    print()
    if issues > 0:
        print(f"  !! {issues} GitHub issue(s) found")
    else:
        print("  GitHub is clean and up to date.")

    return issues


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

    # Post-reference checks: OTS, file placement, GitHub
    ots_issues = check_ots_timestamps()
    placement_issues = check_file_placement()
    github_issues = check_github_status()

    total_issues = stale_count + ots_issues + placement_issues + github_issues

    print()
    print("=" * 60)
    if total_issues == 0:
        print(" ALL CHECKS PASSED — ready to ship")
    else:
        print(f" {total_issues} TOTAL ISSUE(S) — fix before shipping")
        if stale_count:
            print(f"   {stale_count} stale cross-reference(s)")
        if ots_issues:
            print(f"   {ots_issues} OTS timestamp issue(s)")
        if placement_issues:
            print(f"   {placement_issues} file placement issue(s)")
        if github_issues:
            print(f"   {github_issues} GitHub issue(s)")
    print("=" * 60)

    return 1 if total_issues > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
