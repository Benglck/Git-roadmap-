#!/usr/bin/env python3
"""Update one letter in a Markdown file once per day, then commit and push."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import string
import subprocess
from pathlib import Path

MARKER_PATTERN = re.compile(r"<!-- daily-letter: ([a-z]) -->")


def run_git(args: list[str], cwd: Path) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=cwd,
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip()


def get_repo_root() -> Path:
    root = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()
    return Path(root)


def daily_letter(today: dt.date | None = None) -> str:
    date_value = today or dt.date.today()
    return string.ascii_lowercase[date_value.toordinal() % 26]


def update_file(md_path: Path, letter: str, dry_run: bool = False) -> bool:
    content = md_path.read_text(encoding="utf-8")
    marker = f"<!-- daily-letter: {letter} -->"
    match = MARKER_PATTERN.search(content)

    if match:
        if match.group(1) == letter:
            return False
        new_content = MARKER_PATTERN.sub(marker, content, count=1)
    else:
        suffix = "\n" if content.endswith("\n") else "\n\n"
        new_content = f"{content}{suffix}{marker}\n"

    if not dry_run:
        md_path.write_text(new_content, encoding="utf-8")

    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--file",
        default="README.md",
        help="Relative path to the .md file to update (default: README.md)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Show actions without writing or pushing")
    args = parser.parse_args()

    repo_root = get_repo_root()
    md_path = (repo_root / args.file).resolve()

    if not md_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {md_path}")
    if md_path.suffix.lower() != ".md":
        raise ValueError(f"File must end with .md: {md_path}")
    if repo_root not in md_path.parents and md_path != repo_root:
        raise ValueError("Target file must be inside this repository")

    letter = daily_letter()
    changed = update_file(md_path, letter, dry_run=args.dry_run)

    if not changed:
        print(f"No change needed for today. Letter is already '{letter}'.")
        return 0

    print(f"Updated {md_path.relative_to(repo_root)} to daily letter '{letter}'.")
    if args.dry_run:
        print("Dry run: skipping git add/commit/push.")
        return 0

    relative_file = str(md_path.relative_to(repo_root))
    run_git(["add", relative_file], cwd=repo_root)
    run_git(["commit", "-m", f"chore: daily markdown letter update {dt.date.today().isoformat()}"], cwd=repo_root)
    run_git(["push", "origin", "HEAD"], cwd=repo_root)
    print("Changes committed and pushed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
