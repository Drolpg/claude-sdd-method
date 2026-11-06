"""Extract doc and diagram widgets from a Miro canvas_read_as_svg dump, optionally matching them to repo files.

The Miro MCP tool canvas_read_as_svg returns JSON with an "svg" field; large results are saved by the harness to a
file. This script reads that file (or a raw SVG), writes one Markdown file per doc widget and one Mermaid file per
diagram widget, and prints an index. With --compare it also finds the most similar repository file for each doc.

Examples:
  python -I extract_miro_docs.py dump.txt out/
  python -I extract_miro_docs.py dump.txt out/ --compare . "docs/adr/*.md" "docs/tech-debt/*.md"
"""
import argparse
import difflib
import glob
import html
import json
import os
import re
import sys

FIELD_KEYS = ("Status", "Date", "Last Updated", "Data", "Atualizado em")


def load_svg(path):
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    try:
        return json.loads(raw)["svg"]
    except (json.JSONDecodeError, KeyError, TypeError):
        return raw


def table_to_text(table_html):
    """Flatten a Miro table (cells may hold Quill delta JSON) into 'a | b' lines."""
    rows = []
    for row in re.findall(r"<tr[^>]*>(.*?)</tr>", table_html, re.S):
        cells = []
        for cell in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", row, re.S):
            cell = html.unescape(cell).strip()
            if cell.startswith("{") and '"ops"' in cell:
                try:
                    ops = json.loads(cell)["ops"]
                    cell = "".join(op["insert"] if isinstance(op.get("insert"), str)
                                   else op.get("insert", {}).get("mention", {}).get("name", "")
                                   for op in ops)
                except (json.JSONDecodeError, KeyError, TypeError, AttributeError):
                    pass
            cells.append(" ".join(cell.split()))
        rows.append(" | ".join(cells))
    return "\n".join(rows)


def normalize(text):
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", " ", text).replace("\\", "")
    text = re.sub(r"[*_`#>|]", " ", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def header_fields(text):
    fields = {}
    plain = html.unescape(text)
    for key in FIELD_KEYS:
        hit = re.search(rf"\**{re.escape(key)}\**\s*[:|]\s*\**\s*([^\n*|]+)", plain)
        if hit:
            fields[key] = hit.group(1).strip()
    return fields


def top_level_widgets(svg, widget_type):
    """Yield (id, title, body) for foreignObject widgets of a type, handling nested foreignObjects."""
    pattern = rf'<foreignObject[^>]*data-miro-id="(\d+)"[^>]*data-type="{widget_type}"[^>]*>'
    for match in re.finditer(pattern, svg):
        title_hit = re.search(r'data-title="([^"]*)"', match.group(0))
        start = depth_pos = match.end()
        depth = 1
        while depth:
            next_open = svg.find("<foreignObject", depth_pos)
            next_close = svg.find("</foreignObject>", depth_pos)
            if next_close == -1:
                break
            if next_open != -1 and next_open < next_close:
                depth += 1
                depth_pos = next_open + 1
            else:
                depth -= 1
                depth_pos = next_close + 1
        body = svg[start:depth_pos - 1]
        yield match.group(1), (title_hit.group(1) if title_hit else ""), body


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("dump", help="canvas_read_as_svg JSON dump or raw SVG file")
    parser.add_argument("out_dir", help="directory for the extracted .md and .mmd files")
    parser.add_argument("--compare", nargs="+", metavar=("REPO_ROOT", "GLOB"),
                        help="repo root followed by one or more glob patterns to match docs against")
    args = parser.parse_args()

    svg = load_svg(args.dump)
    os.makedirs(args.out_dir, exist_ok=True)

    repo = {}
    if args.compare:
        root, *patterns = args.compare
        for pattern in patterns:
            for path in glob.glob(os.path.join(root, pattern), recursive=True):
                with open(path, encoding="utf-8") as fh:
                    text = fh.read()
                repo[os.path.relpath(path, root)] = (normalize(text), header_fields(text))

    for wid, _, body in top_level_widgets(svg, "doc"):
        body = re.sub(r'<foreignObject[^>]*data-type="table"[^>]*>(.*?)</foreignObject>',
                      lambda m: "\n" + table_to_text(m.group(1)) + "\n", body, flags=re.S)
        body = html.unescape(body)
        title = next((ln.strip("# ").strip() for ln in body.splitlines() if ln.startswith("#")), "(sem título)")
        with open(os.path.join(args.out_dir, f"{wid}.md"), "w", encoding="utf-8") as fh:
            fh.write(body)
        norm = normalize(body)
        print(f"DOC {wid}: {title[:110]}")
        print(f"    chars={len(norm)} fields={header_fields(body)}")
        if repo:
            ratio, path = max((difflib.SequenceMatcher(None, norm[:6000], txt[:6000], autojunk=False).ratio(), p)
                              for p, (txt, _) in repo.items())
            print(f"    best match={path} ratio={ratio:.2f} repo chars={len(repo[path][0])} "
                  f"fields={repo[path][1]}")

    for wid, title, body in top_level_widgets(svg, "diagram"):
        path = os.path.join(args.out_dir, f"diagram_{wid}.mmd")
        text = html.unescape(body)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"DIAGRAM {wid}: '{title}' chars={len(text)} -> {path}")

    for comment in re.findall(r"<comment[^>]*data-author=\"([^\"]*)\"[^>]*>(.*?)</comment>", svg, re.S):
        print(f"COMMENT ({comment[0]}): {html.unescape(comment[1])[:200]}")


if __name__ == "__main__":
    main()
