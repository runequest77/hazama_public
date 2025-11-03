#!/usr/bin/env python3
from pathlib import Path
import argparse

SKIP = {"_Sidebar.md", "_Footer.md", "Home.md", "home.md"}

def rel_no_ext(root: Path, p: Path) -> str:
    return p.relative_to(root).with_suffix("").as_posix()

def list_dirs(p: Path):
    return sorted(d for d in p.iterdir() if d.is_dir() and not d.name.startswith(('.', '_')))

def list_pages(p: Path):
    return sorted(f for f in p.iterdir() if f.is_file() and f.suffix == ".md" and f.name not in SKIP)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="Wiki repo root")
    ap.add_argument("--output", default="_Sidebar.md", help="Output file (relative to root)")
    args = ap.parse_args()

    root = Path(args.root)
    out_path = root / args.output
    lines = ["# Navigation", "", "[[Home|Home]]", ""]

    # トップレベル：フォルダ → その直下のフォルダ/ページ
    for d in list_dirs(root):
        # 1階層目：フォルダ自身（フォルダ名/フォルダ名.md へ）
        lines.append(f"- [[{rel_no_ext(root, d / (d.name + '.md'))}|{d.name}]]")

        # 2階層目：サブフォルダ（サブフォルダ名/サブフォルダ名.md へ）
        for sd in list_dirs(d):
            lines.append(f"  - [[{rel_no_ext(root, sd / (sd.name + '.md'))}|{sd.name}]]")

        # 2階層目：フォルダ直下のページ
        for f in list_pages(d):
            lines.append(f"  - [[{rel_no_ext(root, f)}|{f.stem}]]")

    # トップレベル直下のページ（最後に）
    top_pages = list_pages(root)
    if top_pages:
        lines.append("")
        for f in top_pages:
            lines.append(f"- [[{rel_no_ext(root, f)}|{f.stem}]]")

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {out_path}")

if __name__ == "__main__":
    main()
