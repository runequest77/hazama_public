#!/usr/bin/env python3
from pathlib import Path
import argparse

SKIP_FILES = {"_Sidebar.md", "_Footer.md", "Home.md", "home.md"}

def emit(root: Path, cur: Path, lines: list):
    # ディレクトリ（折りたたみ）
    for d in sorted(p for p in cur.iterdir() if p.is_dir() and not p.name.startswith(('.', '_'))):
        lines.append(f"<details><summary><strong>{d.name}</strong></summary>")
        emit(root, d, lines)
        lines.append("</details>")
    # ファイル（相対パスリンク、表示名は拡張子なしのファイル名そのまま）
    for f in sorted(p for p in cur.iterdir() if p.is_file() and p.suffix == ".md" and p.name not in SKIP_FILES):
        rel = f.relative_to(root).with_suffix("")         # 相対パス
        lines.append(f"- [[{rel.as_posix()}|{f.stem}]]")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="Wiki repo root (Home.md がある場所)")
    ap.add_argument("--output", default="_Sidebar.md")
    args = ap.parse_args()

    root = Path(args.root)
    lines = ["# Navigation", ""]
    emit(root, root, lines)
    lines += ["", "---", "[🏠 Home](Home)"]

    Path(args.output).write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {args.output}")

if __name__ == "__main__":
    main()
