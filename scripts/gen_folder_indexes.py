#!/usr/bin/env python3
from pathlib import Path
import argparse

SKIP = {"_Sidebar.md", "_Footer.md", "Home.md", "home.md"}

def rel_no_ext(root: Path, p: Path) -> str:
    return p.relative_to(root).with_suffix("").as_posix()

def index_one(root: Path, folder: Path):
    idx = folder / f"{folder.name}.md"
    parent = folder.parent if folder != root else None
    subdirs = sorted(d for d in folder.iterdir() if d.is_dir() and not d.name.startswith(('.', '_')))
    pages = sorted(f for f in folder.iterdir()
                   if f.is_file() and f.suffix == ".md" and f.name not in SKIP and f.name != idx.name)

    lines = [f"# {folder.name}", ""]
    if parent:
        parent_idx = (parent / f"{parent.name}.md") if parent != root else Path("Home")
        lines += [f"- **Parent:** [[{rel_no_ext(root, parent_idx)}|{parent.name if parent != root else 'Home'}]]", ""]
    if subdirs:
        lines.append("## Subfolders")
        for d in subdirs:
            lines.append(f"- [[{rel_no_ext(root, d / (d.name + '.md'))}|{d.name}]]")
        lines.append("")
    if pages:
        lines.append("## Pages")
        for f in pages:
            lines.append(f"- [[{rel_no_ext(root, f)}|{f.stem}]]")
        lines.append("")

    idx.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {idx}")

def walk_and_make(root: Path, cur: Path):
    for d in sorted(p for p in cur.iterdir() if p.is_dir() and not p.name.startswith(('.', '_'))):
        index_one(root, d)
        walk_and_make(root, d)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="Wiki repo root")
    args = ap.parseArgs() if hasattr(argparse.ArgumentParser, "parseArgs") else ap.parse_args()

    root = Path(args.root)
    walk_and_make(root, root)

if __name__ == "__main__":
    main()
