from __future__ import annotations

import argparse
import json
import shutil
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class PackItem:
    source: Path
    dest: Path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def iter_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if path.is_file() and "__pycache__" not in path.parts:
            yield path


def validate() -> int:
    required = [
        ROOT / "core" / "north_star.md",
        ROOT / "skills" / "objective-first" / "SKILL.md",
        ROOT / "agents" / "claudecode" / "CLAUDE.md",
        ROOT / "agents" / "codex" / "AGENTS.md",
        ROOT / "agents" / "openclaude" / "AGENTS.md",
    ]
    missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
    if missing:
        print("Missing files:")
        for item in missing:
            print(f" - {item}")
        return 1
    print("OK: required files found.")
    return 0


def make_zip(out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in iter_files(ROOT):
            if file == out:
                continue
            zf.write(file, file.relative_to(ROOT))
    print(f"Created: {out}")


def copy_pack(agent: str, target: Path) -> None:
    src = ROOT / "agents" / agent
    if not src.exists():
        raise SystemExit(f"Unknown agent pack: {agent}")
    target.mkdir(parents=True, exist_ok=True)
    for file in iter_files(src):
        rel = file.relative_to(src)
        dest = target / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file, dest)
    print(f"Copied {agent} pack to {target}")


def main() -> int:
    parser = argparse.ArgumentParser(prog="MetaContextOS")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("validate", help="Check that key files exist")

    z = sub.add_parser("zip", help="Create a zip bundle")
    z.add_argument("--out", default=str(ROOT / "MetaContextOS.zip"))

    c = sub.add_parser("copy-pack", help="Copy a specific agent pack into a destination")
    c.add_argument("agent", choices=["claudecode", "codex", "openclaude", "cursor", "windsurf", "continue", "aider"])
    c.add_argument("--target", required=True)

    args = parser.parse_args()

    if args.cmd == "validate":
        return validate()
    if args.cmd == "zip":
        make_zip(Path(args.out))
        return 0
    if args.cmd == "copy-pack":
        copy_pack(args.agent, Path(args.target))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
