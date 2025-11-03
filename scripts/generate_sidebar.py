#!/usr/bin/env python3
from pathlib import Path

def build_sidebar(root: Path, lines: list):
    for p in sorted(root.iterdir()):
        if p.name.startswith("_") or p.name.startswith("."):
            continue
        if p.is_dir():
            lines.append(f"<details><summary><strong>{p.name}</strong></summary>")
            build_sidebar(p, lines)
            lines.append("</details>")
        elif p.suffix == ".md":
            name = p.stem
            link = str(p.with_suffix("")).replace("\\", "/")
            lines.append(f"- [[{link}|{name}]]")

def main():
    wiki = Path("wiki").resolve()
    out = wiki / "_Sidebar.md"
    lines = ["# Navigation", ""]
    build_sidebar(wiki, lines)
    lines.append("\n---\n[🏠 Home](Home)\n")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out}")

if __name__ == "__main__":
    main()
