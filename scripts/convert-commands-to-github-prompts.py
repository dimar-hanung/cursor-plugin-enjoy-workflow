#!/usr/bin/env python3
"""Convert Cursor plugin commands and skills for VS Code / GitHub Copilot.

Commands: commands/<name>.md  ->  <VS Code User>/prompts/<name>.prompt.md
Skills:   skills/<name>/      ->  ~/.copilot/skills/<name>/  (full tree copy)

Official discovery paths (VS Code Copilot Agent Skills docs):
  Prompts (global):  %APPDATA%\\Code\\User\\prompts  (Windows)
  Skills (personal): ~/.copilot/skills  (also ~/.agents/skills, ~/.claude/skills)
  Skills (project):  <repo>/.github/skills  (with --workspace)

Usage (from repo root):
  python scripts/convert-commands-to-github-prompts.py
  python scripts/convert-commands-to-github-prompts.py --commands-only
  python scripts/convert-commands-to-github-prompts.py --skills-only
  python scripts/convert-commands-to-github-prompts.py --workspace   # write to <repo>/.github instead
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
USER_INPUT_MARKERS = (
    ("USER REQUEST:", "${input:request:Describe your request}"),
    ("PERMINTAAN USER:", "${input:request:Jelaskan permintaanmu}"),
)


def default_vscode_prompts_root() -> Path:
    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA")
        if appdata:
            return Path(appdata) / "Code" / "User" / "prompts"
        return Path.home() / "AppData" / "Roaming" / "Code" / "User" / "prompts"
    if sys.platform == "darwin":
        return (
            Path.home()
            / "Library"
            / "Application Support"
            / "Code"
            / "User"
            / "prompts"
        )
    return Path.home() / ".config" / "Code" / "User" / "prompts"


def default_copilot_skills_root() -> Path:
    return Path.home() / ".copilot" / "skills"


def legacy_prompts_skills_root() -> Path:
    return default_vscode_prompts_root() / "skills"


def resolve_output_dirs(workspace: bool, repo_root: Path) -> tuple[Path, Path]:
    if workspace:
        prompts_root = repo_root / ".github" / "prompts"
        skills_root = repo_root / ".github" / "skills"
        return prompts_root, skills_root

    return default_vscode_prompts_root(), default_copilot_skills_root()


def cleanup_legacy_skills_dir() -> bool:
    legacy_dir = legacy_prompts_skills_root()
    if not legacy_dir.is_dir():
        return False
    shutil.rmtree(legacy_dir)
    return True


def find_repo_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in (current, *current.parents):
        if (candidate / "commands").is_dir() or (candidate / "skills").is_dir():
            return candidate
    return start.resolve()


def parse_simple_frontmatter(raw: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        fields[key.strip()] = value.strip().strip("\"'")
    return fields


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text

    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text

    return parse_simple_frontmatter(match.group(1)), text[match.end() :]


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def derive_description(body: str, fallback_name: str) -> str:
    for line in body.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            if len(stripped) > 160:
                return stripped[:157] + "..."
            return stripped
    return f"Run the {fallback_name} workflow."


def convert_user_input_markers(body: str) -> str:
    updated = body.rstrip()
    for marker, replacement in USER_INPUT_MARKERS:
        if updated.endswith(marker):
            prefix = updated[: -len(marker)].rstrip()
            return f"{prefix}\n\n{replacement}\n"
        if updated.endswith(marker.rstrip(":")):
            prefix = updated[: -len(marker.rstrip(":"))].rstrip()
            return f"{prefix}\n\n{replacement}\n"
    return f"{updated}\n"


def build_prompt_file(name: str, description: str, body: str) -> str:
    body = convert_user_input_markers(body)
    return (
        "---\n"
        f"name: {yaml_quote(name)}\n"
        f"description: {yaml_quote(description)}\n"
        "---\n\n"
        f"{body}"
    )


def skill_output_name(skill_dir: Path) -> str:
    skill_md = skill_dir / "SKILL.md"
    if skill_md.is_file():
        meta, _ = split_frontmatter(skill_md.read_text(encoding="utf-8"))
        if meta.get("name"):
            return meta["name"]
    return skill_dir.name


def convert_command(command_path: Path, output_dir: Path) -> Path:
    text = command_path.read_text(encoding="utf-8")
    meta, body = split_frontmatter(text)

    stem = command_path.stem
    name = meta.get("name", stem)
    description = meta.get("description") or derive_description(body, name)

    output_path = output_dir / f"{name}.prompt.md"
    output_path.write_text(
        build_prompt_file(name, description, body),
        encoding="utf-8",
        newline="\n",
    )
    return output_path


def convert_commands(source_dir: Path, output_dir: Path, label: str) -> list[Path]:
    if not source_dir.is_dir():
        print(f"error: commands source not found: {source_dir}", file=sys.stderr)
        return []

    command_files = sorted(source_dir.glob("*.md"))
    if not command_files:
        print(f"error: no .md files in {source_dir}", file=sys.stderr)
        return []

    output_dir.mkdir(parents=True, exist_ok=True)

    written: list[Path] = []
    print(f"Commands -> {label}")
    for command_path in command_files:
        output_path = convert_command(command_path, output_dir)
        written.append(output_path)
        print(f"  {command_path.name} -> {output_path}")
    return written


def convert_skill(skill_dir: Path, output_root: Path) -> Path:
    name = skill_output_name(skill_dir)
    output_dir = output_root / name

    if output_dir.exists():
        shutil.rmtree(output_dir)

    shutil.copytree(
        skill_dir,
        output_dir,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"),
    )
    return output_dir


def convert_skills(source_dir: Path, output_dir: Path, label: str) -> list[Path]:
    if not source_dir.is_dir():
        print(f"error: skills source not found: {source_dir}", file=sys.stderr)
        return []

    skill_dirs = sorted(
        path
        for path in source_dir.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    )
    if not skill_dirs:
        print(f"error: no skill folders with SKILL.md in {source_dir}", file=sys.stderr)
        return []

    output_dir.mkdir(parents=True, exist_ok=True)

    written: list[Path] = []
    print(f"Skills -> {label}")
    for skill_dir in skill_dirs:
        output_path = convert_skill(skill_dir, output_dir)
        written.append(output_path)
        print(f"  {skill_dir.name}/ -> {output_path}/")
    return written


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert commands/*.md and skills/*/SKILL.md for VS Code / GitHub Copilot."
    )
    parser.add_argument(
        "--commands-only",
        action="store_true",
        help="Convert commands only (skip skills)",
    )
    parser.add_argument(
        "--skills-only",
        action="store_true",
        help="Convert skills only (skip commands)",
    )
    parser.add_argument(
        "--workspace",
        action="store_true",
        help="Write prompts and skills to <repo>/.github/prompts and <repo>/.github/skills",
    )
    parser.add_argument(
        "--cleanup-legacy",
        action="store_true",
        help="Remove old User/prompts/skills/ after a successful skills conversion (non-workspace mode)",
    )
    parser.add_argument(
        "--commands-source",
        type=Path,
        default=None,
        help="Source folder with Cursor command .md files (default: <repo>/commands)",
    )
    parser.add_argument(
        "--commands-output",
        type=Path,
        default=None,
        help="Output folder for .prompt.md files (default: VS Code User/prompts)",
    )
    parser.add_argument(
        "--skills-source",
        type=Path,
        default=None,
        help="Source folder with skill directories (default: <repo>/skills)",
    )
    parser.add_argument(
        "--skills-output",
        type=Path,
        default=None,
        help="Output folder for skill trees (default: ~/.copilot/skills, or <repo>/.github/skills with --workspace)",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=None,
        help="Repository root (default: auto-detect from script location)",
    )
    args = parser.parse_args()

    if args.commands_only and args.skills_only:
        print("error: use only one of --commands-only or --skills-only", file=sys.stderr)
        return 1

    repo_root = args.repo_root or find_repo_root(Path(__file__).parent)
    default_prompts_dir, default_skills_dir = resolve_output_dirs(args.workspace, repo_root)
    run_commands = not args.skills_only
    run_skills = not args.commands_only

    commands_written: list[Path] = []
    skills_written: list[Path] = []

    prompts_output = args.commands_output or default_prompts_dir
    skills_output = args.skills_output or default_skills_dir

    if run_commands:
        commands_written = convert_commands(
            args.commands_source or (repo_root / "commands"),
            prompts_output,
            str(prompts_output),
        )
        if not commands_written and not args.skills_only:
            return 1
        if commands_written:
            print()

    if run_skills:
        skills_written = convert_skills(
            args.skills_source or (repo_root / "skills"),
            skills_output,
            str(skills_output),
        )
        if not skills_written and not args.commands_only:
            return 1
        if skills_written and args.cleanup_legacy and not args.workspace:
            if cleanup_legacy_skills_dir():
                print(f"\nRemoved legacy skills folder: {legacy_prompts_skills_root()}")
            else:
                print("\nNo legacy User/prompts/skills folder to remove.")

    total = len(commands_written) + len(skills_written)
    if total == 0:
        return 1

    parts: list[str] = []
    if commands_written:
        parts.append(f"{len(commands_written)} prompt(s)")
    if skills_written:
        parts.append(f"{len(skills_written)} skill(s)")
    if args.workspace:
        destination = "<repo>/.github/prompts + <repo>/.github/skills"
    else:
        destination = "VS Code User/prompts + ~/.copilot/skills"
    print(f"\nConverted {' and '.join(parts)} to {destination}.")
    print(f"  prompts: {prompts_output}")
    print(f"  skills:  {skills_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
