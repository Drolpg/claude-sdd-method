"""Compare a Mermaid classDiagram (the documented domain model) with type declarations in source code.

For every class in the diagram it reports whether a type with that name is declared in the code and which diagram
members are not mentioned in the declaring file. It also lists domain types in the code that the diagram omits.
Works by text search, so it is language-agnostic but approximate: read every reported gap before concluding.
Notes in the diagram ("note for X ...") are printed next to missing classes, because they usually document aliases.

Example:
  python -I model_vs_code.py docs/domain/domain-model.md src --ext .java .kt --domain-dir domain/model
"""
import argparse
import os
import re
import sys

DECLARATION = re.compile(
    r"\b(?:class|interface|record|enum|struct|trait|object)\s+([A-Z]\w*)"  # Java, Kotlin, C#, TS, Python, Rust, Scala
    r"|\btype\s+([A-Z]\w*)\b"                                               # Go, TypeScript aliases
)


def parse_diagram(text):
    classes, notes, current = {}, {}, None
    for raw in text.splitlines():
        line = raw.strip()
        note = re.match(r'note\s+for\s+(\w+)\s+"(.*)"', line)
        if note:
            notes[note.group(1)] = note.group(2)
            continue
        opened = re.match(r"class\s+(\w+)\s*(?:~[^~]*~)?\s*\{", line)
        if opened:
            current = opened.group(1)
            classes.setdefault(current, [])
            continue
        if line == "}":
            current = None
            continue
        if current and line and not line.startswith("<<"):
            member = re.sub(r"\(.*", "", line.lstrip("+-#~ ")).split()
            if member:
                classes[current].append(member[-1].strip("$*"))
    return classes, notes


def index_sources(root, extensions):
    declared = {}
    for folder, _, files in os.walk(root):
        for name in files:
            if os.path.splitext(name)[1] in extensions:
                path = os.path.join(folder, name)
                with open(path, encoding="utf-8", errors="replace") as fh:
                    body = fh.read()
                for match in DECLARATION.finditer(body):
                    declared.setdefault(match.group(1) or match.group(2), []).append((path, body))
    return declared


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("diagram", help="file containing the Mermaid classDiagram (.md or .mmd)")
    parser.add_argument("src_root", help="source root to scan")
    parser.add_argument("--ext", nargs="+", default=[".java", ".kt", ".cs", ".ts", ".py", ".go"],
                        help="source file extensions to scan")
    parser.add_argument("--domain-dir", default="domain/model",
                        help="path fragment that marks domain model code, for the 'not in diagram' list")
    args = parser.parse_args()

    with open(args.diagram, encoding="utf-8") as fh:
        classes, notes = parse_diagram(fh.read())
    declared = index_sources(args.src_root, set(args.ext))

    print(f"diagram classes: {len(classes)}; declared types in code: {len(declared)}")
    for name, members in sorted(classes.items()):
        hits = declared.get(name)
        if not hits:
            hint = f'  (note: "{notes[name]}")' if name in notes else ""
            print(f"[MISSING IN CODE] {name}{hint}")
            continue
        body = "\n".join(text for _, text in hits)
        absent = [m for m in members if not re.search(rf"\b{re.escape(m)}\b", body)]
        if absent:
            where = os.path.relpath(hits[0][0], args.src_root)
            print(f"[MEMBER GAP] {name} ({where}): {', '.join(absent)}")

    marker = os.sep + os.path.normpath(args.domain_dir.strip("/\\")) + os.sep
    domain_types = {name for name, hits in declared.items()
                    if any(marker in path for path, _ in hits)}
    omitted = sorted(t for t in domain_types if t not in classes and not t.endswith(("Test", "Exception")))
    print("[IN CODE, NOT IN DIAGRAM]", ", ".join(omitted) if omitted else "none")


if __name__ == "__main__":
    main()
