#!/usr/bin/env python3
"""Repair Markdown formatting in the seven X-Evil Network documentation files.

Run from the repository root on the feature branch:
    python3 scripts/fix_markdown_docs.py

The script only edits the seven listed Markdown files. Review the resulting diff
before committing; it does not commit, push, or merge anything.
"""
from pathlib import Path
import re
import sys

FILES = [
    "docs/README.md",
    "docs/NETWORK-OVERVIEW.md",
    "docs/PROJECT-LIFECYCLE.md",
    "standards/SECURITY-STANDARD.md",
    "projects/README.md",
    "integrations/README.md",
    "releases/README.md",
]

INDEX_HEADINGS = {
    "Purpose", "Core Documentation", "Standards",
    "Project Management", "Governance", "Maintenance",
}

def split_cells(line):
    return [cell.strip().strip('"') for cell in line.split("|")]

def convert_tables(lines):
    out = []
    i = 0
    while i < len(lines):
        # Source tables are contiguous pipe-delimited rows without a separator.
        if "|" in lines[i] and not lines[i].lstrip().startswith("|"):
            j = i
            while j < len(lines) and "|" in lines[j] and not lines[j].lstrip().startswith("|"):
                j += 1
            if j - i >= 2:
                rows = [split_cells(line) for line in lines[i:j]]
                width = max(map(len, rows))
                rows = [row + [""] * (width - len(row)) for row in rows]
                out.append("| " + " | ".join(rows[0]) + " |")
                out.append("| " + " | ".join(["---"] * width) + " |")
                out.extend("| " + " | ".join(row) + " |" for row in rows[1:])
                i = j
                continue
        out.append(lines[i])
        i += 1
    return out

def fix_file(path):
    original = path.read_text(encoding="utf-8")
    text = original.replace("\r\n", "\n").strip()
    lines = text.split("\n")

    if lines and not lines[0].startswith("#"):
        lines[0] = "# " + lines[0].strip()

    if path.as_posix() == "docs/README.md":
        lines = [
            "## " + line.strip() if line.strip() in INDEX_HEADINGS else line
            for line in lines
        ]

    # Section titles are isolated by blank lines; consecutive numbered procedure
    # steps remain ordered lists.
    for i, line in enumerate(lines):
        if re.fullmatch(r"\d{1,2}\. [A-Z][^\n]*", line) and i + 1 < len(lines) and not lines[i + 1].strip():
            lines[i] = "## " + line

    lines = convert_tables(lines)
    text = "\n".join(lines)

    # Render metadata as labelled fields.
    text = re.sub(
        r"^((?:Document status|Network|Network authority|Document type|Applies to|"
        r"Document owner|Classification|Review cadence|Purpose):) (.+)$",
        r"**\1** \2",
        text,
        flags=re.MULTILINE,
    )

    # Use inline code for literal repository paths and technical identifiers.
    text = re.sub(
        r'"((?:\.\./|00-governance/|docs/|standards/|projects/|integrations/|releases/)[^"\n]+)"',
        r"`\1`",
        text,
    )
    text = re.sub(r'"(STRUCTURE-MANIFEST\.json|README\.md|main|GITHUB_TOKEN)"', r"`\1`", text)

    # Link references to documents where a relative path is unambiguous.
    link_map = {
        "../docs/PROJECT-LIFECYCLE.md": "Project Lifecycle Standard",
        "../standards/SECURITY-STANDARD.md": "Security Standard",
        "../projects/README.md": "Project Registry",
        "../integrations/README.md": "Integration Governance",
        "../releases/README.md": "Release Documentation",
        "NETWORK-OVERVIEW.md": "Network Overview",
        "PROJECT-LIFECYCLE.md": "Project Lifecycle",
        "SECURITY-STANDARD.md": "Security Standard",
    }
    for target, label in link_map.items():
        literal = f"`{target}`"
        link = f"[{label}]({target})"
        text = text.replace(literal, link)

    if path.as_posix() == "docs/README.md":
        text = re.sub(
            r'"Network Overview" \(NETWORK-OVERVIEW\.md\)',
            "[Network Overview](NETWORK-OVERVIEW.md)", text
        )
        text = re.sub(
            r'"Project Lifecycle" \(PROJECT-LIFECYCLE\.md\)',
            "[Project Lifecycle](PROJECT-LIFECYCLE.md)", text
        )
        # Normalize the index table and its two internal links.
        text = re.sub(
            r"\| Document \| Description \|\n\|[-| ]+\|\n.*?(?=\n## Standards)",
            "| Document | Description |\n|---|---|\n"
            "| [Network Overview](NETWORK-OVERVIEW.md) | Network purpose, architecture, governance, and operating principles. |\n"
            "| [Project Lifecycle](PROJECT-LIFECYCLE.md) | Proposed lifecycle stages and project management procedures. |\n",
            text,
            flags=re.DOTALL,
        )

    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False

def main():
    root = Path.cwd()
    missing = [name for name in FILES if not (root / name).is_file()]
    if missing:
        print("ERROR: Run this script from the repository root. Missing files:")
        print("\n".join(f"  - {name}" for name in missing))
        return 2

    changed = []
    for name in FILES:
        if fix_file(root / name):
            changed.append(name)

    print(f"Processed {len(FILES)} documentation files.")
    print(f"Changed {len(changed)} files:")
    for name in changed:
        print(f"  - {name}")
    print("\nNext: inspect `git diff --check` and `git diff`, then validate links and review the changes.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
      
