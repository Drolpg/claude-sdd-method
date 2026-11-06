"""Sentence-level diff between two documents (e.g. a Miro doc extracted by extract_miro_docs.py and a repo file).

Markup, table pipes and formatting are normalized away, so the output shows wording differences only.
Lines starting with '-' exist only in the first file; lines starting with '+' only in the second.

Example:
  python -I doc_diff.py out/3458764681513228441.md docs/adr/ADR-003-authentication-strategy.md --limit 60
"""
import argparse
import difflib
import html
import re
import sys


def sentences(path):
    with open(path, encoding="utf-8") as fh:
        text = html.unescape(fh.read())
    text = re.sub(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$", " ", text, flags=re.M)  # table separators
    text = re.sub(r"^\s*```\w*\s*$", " ", text, flags=re.M)  # code fences and their language tags
    text = re.sub(r"<[^>]+>", " ", text).replace("\\", "")
    text = re.sub(r"[*_`#>|]", " ", text)
    text = re.sub(r"(^|\s)-{3,}(\s|$)", " ", text).replace("&#32;", " ")
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"([(\[])\s+", r"\1", text)      # "( x" -> "(x": spaces left behind by removed code spans
    text = re.sub(r"\s+([)\],.;:])", r"\1", text)  # "x )" -> "x)"
    return [s.strip() for s in re.split(r"(?<=[.;:!?])\s+", text) if len(s.strip()) > 3]


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("first", help="first document (e.g. the board copy)")
    parser.add_argument("second", help="second document (e.g. the repository file)")
    parser.add_argument("--limit", type=int, default=60, help="maximum number of diff lines to print")
    args = parser.parse_args()

    a, b = sentences(args.first), sentences(args.second)
    ratio = difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()
    out = [line for line in difflib.unified_diff(a, b, "first", "second", n=0, lineterm="")
           if line[:1] in "+-" and not line.startswith(("+++", "---"))]
    print(f"similarity={ratio:.2f} first_sentences={len(a)} second_sentences={len(b)} diff_lines={len(out)}")
    for line in out[:args.limit]:
        print(line[:400])
    if len(out) > args.limit:
        print(f"... ({len(out) - args.limit} more lines)")


if __name__ == "__main__":
    main()
