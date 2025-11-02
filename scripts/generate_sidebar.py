#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, re, sys, argparse
from pathlib import Path

PAGE_EXTS = (".md", ".markdown", ".rst", ".asciidoc", ".mediawiki")
SPECIAL_FILES = {"_Sidebar.md", "_Footer.md"}
HOME_FILES = {"Home.md", "home.md"}

num_prefix_re = re.compile(r"^\s*\d+[-_]\s*")

def strip_num_prefix(name: str) -> str:
    return num_prefix_re.sub("", name)

def normalize_link_target(path_no_ext: str) -> str:
    # GitHub Wiki の [[link]] はファイル名の空白を '-' にする慣習が強い
    return path_no_ext.replace(" ", "-").replace("\\", "/")

def guess_title(file_path: Path) -> str:
    try:
        text = file_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        # 読めないときはファイル名ベース
        text = ""
    # 1) YAML front matter
    if text.startswith("---"):
        m = re.search(r"^title:\s*(.+?)\s*$", text, flags=re.MULTILINE)
        if m:
            return m.group(1).strip()
    # 2) 最初の H1
    m = re.search(r"^\s*#\s+(.+?)\s*$", text, flags=re.MULTILINE)
    if m:
        return m.group(1).strip()
    # 3) ファイル名から
    title = file_path.stem
    title = strip_num_prefix(title)
    title = title.replace("-", " ").replace("_", " ").strip()
    # 極端な小文字化はしない（NPCなど保持）
    return title or file_path.stem

def is_page(path: Path) -> bool:
    if not path.is_file():
        return False
    if path.name in SPECIAL_FILES or path.name in HOME_FILES:
        return False
    return path.suffix.lower() in PAGE_EXTS

def build_tree(root: Path) -> dict:
    """
    ツリーは { "files": [(PathRel,title)], "dirs": { name: subtree, ... } }
    """
    tree = {"files": [], "dirs": {}}
    for entry in sorted(root.iterdir(), key=lambda p: (p.is_file(), strip_num_prefix(p.name).lower())):
        if entry.name == ".git":
            continue
        if entry.is_file() and is_page(entry):
            rel = entry.relative_to(root)
            title = guess_title(entry)
            tree["files"].append((rel, title))
        elif entry.is_dir():
            subtree = build_tree(entry)
            # 空フォルダは無視（ページが無いなら出力しない）
            if subtree["files"] or subtree["dirs"]:
                tree["dirs"][entry.name] = subtree
    return tree

def print_tree(tree: dict, root: Path, out_lines: list, indent: int = 0, base: Path = None):
    """
    Markdown の箇条書きで階層出力
    """
    prefix = "  " * indent + "- "
    # 1) ファイル（同階層）
    for rel, title in tree["files"]:
        without_ext = str(rel.with_suffix(""))
        link = normalize_link_target(without_ext)
        out_lines.append(f"{prefix}[[{link}|{title}]]")
    # 2) ディレクトリ
    for dirname in sorted(tree["dirs"].keys(), key=lambda n: strip_num_prefix(n).lower()):
        subtree = tree["dirs"][dirname]
        # 見出し代わりにグループ行を作る（クリック不可の“擬似セクション”）
        group_title = strip_num_prefix(dirname).replace("-", " ").replace("_", " ").strip() or dirname
        out_lines.append(f"{prefix}**{group_title}**")
        print_tree(subtree, root, out_lines, indent + 1, base)

def main():
    ap = argparse.ArgumentParser(description="Generate _Sidebar.md for GitHub Wiki from folder tree and page titles.")
    ap.add_argument("--root", default=".", help="Wiki repo root (contains Home.md, etc). Default: current dir")
    ap.add_argument("--output", default="_Sidebar.md", help="Output file path. Default: _Sidebar.md")
    ap.add_argument("--title", default="Navigation", help="Top heading in sidebar. Default: Navigation")
    ap.add_argument("--include-home", action="store_true", help="Add a 'Back to Home' link at the end")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"not found: {root}", file=sys.stderr)
        sys.exit(1)

    tree = build_tree(root)

    lines = [f"# {args.title}", ""]
    # ルート直下ファイルを先に見せるため、print_tree で全体を一度に出す
    print_tree(tree, root, lines, indent=0)

    if args.include_home:
        lines += ["", "---", "[🏠 Back to Home](Home)"]

    out = Path(args.output)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {out}")

if __name__ == "__main__":
    main()
