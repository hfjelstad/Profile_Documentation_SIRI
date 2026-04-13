#!/usr/bin/env python3
"""
validate-xml.py — Local SIRI XML validation (Windows/Linux/macOS)

Usage:
    python scripts/validate-xml.py                   # validate all XML
    python scripts/validate-xml.py --changed          # validate only git-changed XML
    python scripts/validate-xml.py file1.xml ...      # validate specific files
"""

import sys
import os
import subprocess
from pathlib import Path

try:
    from lxml import etree
except ImportError:
    print("ERROR: lxml not installed. Run: pip install lxml")
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = REPO_ROOT / "siri-xsd" / "xsd"
SCHEMA_FILE = SCHEMA_DIR / "siri.xsd"
SIRI_XSD_VERSION = "v2.2"


def clone_schema():
    """Clone the official SIRI XSD if not present."""
    if SCHEMA_FILE.exists():
        return
    print(f"Schema not found. Cloning SIRI XSD ({SIRI_XSD_VERSION})...")
    subprocess.run(
        [
            "git", "clone", "--depth=1", "--branch", SIRI_XSD_VERSION,
            "https://github.com/SIRI-CEN/SIRI.git",
            str(REPO_ROOT / "siri-xsd"),
        ],
        check=True,
    )
    if not SCHEMA_FILE.exists():
        print(f"ERROR: Could not obtain schema at: {SCHEMA_FILE}")
        sys.exit(2)
    print(f"Schema cloned from https://github.com/SIRI-CEN/SIRI ({SIRI_XSD_VERSION})\n")


def load_schema():
    """Parse and return the SIRI XSD schema."""
    clone_schema()
    try:
        schema_doc = etree.parse(str(SCHEMA_FILE))
        return etree.XMLSchema(schema_doc)
    except etree.XMLSchemaParseError as e:
        print(f"ERROR: Failed to parse schema: {e}")
        sys.exit(2)


def find_all_xml():
    """Find all XML files under Services/ and Objects/."""
    files = []
    for folder in ["Services", "Objects"]:
        search_dir = REPO_ROOT / folder
        if search_dir.exists():
            files.extend(search_dir.rglob("*.xml"))
    return sorted(files)


def find_changed_xml(base="main"):
    """Find git-changed XML files relative to a base branch."""
    try:
        subprocess.run(
            ["git", "fetch", "origin", base, "--depth=1"],
            capture_output=True, cwd=str(REPO_ROOT),
        )
        result = subprocess.run(
            ["git", "merge-base", "HEAD", f"origin/{base}"],
            capture_output=True, text=True, cwd=str(REPO_ROOT),
        )
        merge_base = result.stdout.strip()
        if not merge_base:
            print(f"Could not determine merge-base with {base}. Validating all XML.")
            return find_all_xml()

        result = subprocess.run(
            ["git", "diff", "--name-only", merge_base, "HEAD"],
            capture_output=True, text=True, cwd=str(REPO_ROOT),
        )
        files = []
        for line in result.stdout.strip().splitlines():
            if line.lower().endswith(".xml") and not line.startswith("siri-xsd/"):
                full = REPO_ROOT / line
                if full.exists():
                    files.append(full)
        return sorted(files)
    except Exception:
        print("Git diff failed. Validating all XML instead.")
        return find_all_xml()


def validate_files(schema, files):
    """Validate a list of XML files against the schema."""
    passed = 0
    failed = 0
    failed_files = []

    for filepath in files:
        rel = filepath.relative_to(REPO_ROOT)
        try:
            doc = etree.parse(str(filepath))
            if schema.validate(doc):
                print(f"  ✅ {rel}")
                passed += 1
            else:
                print(f"  ❌ {rel}")
                for err in schema.error_log[:5]:
                    print(f"     {err}")
                failed += 1
                failed_files.append(rel)
        except etree.XMLSyntaxError as e:
            print(f"  ❌ {rel}")
            print(f"     XML parse error: {e}")
            failed += 1
            failed_files.append(rel)

    return passed, failed, failed_files


def main():
    args = sys.argv[1:]

    # Collect files
    if not args:
        files = find_all_xml()
    elif args[0] == "--changed":
        base = args[1] if len(args) > 1 else "main"
        files = find_changed_xml(base)
    else:
        files = []
        for arg in args:
            p = Path(arg)
            if not p.is_absolute():
                p = REPO_ROOT / p
            if p.exists():
                files.append(p)
            else:
                print(f"WARNING: File not found: {arg}")

    if not files:
        print("No XML files to validate.")
        sys.exit(0)

    print(f"Validating {len(files)} XML file(s) against SIRI schema...\n")

    schema = load_schema()
    passed, failed, failed_files = validate_files(schema, files)

    print()
    print("────────────────────────────────")
    print(f"  Results: {passed} passed, {failed} failed")
    print("────────────────────────────────")

    if failed > 0:
        print("\nFailed files:")
        for f in failed_files:
            print(f"  - {f}")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
