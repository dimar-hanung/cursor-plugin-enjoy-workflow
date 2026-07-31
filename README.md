# Enjoy Workflow

Personal Cursor plugin that bundles skills and slash commands so you can reuse the same workflows on any machine or Remote SSH session — without copying files into every server’s `~/.agents` or `~/.cursor`.

## Install (Git)

Repo: https://github.com/dimar-hanung/cursor-plugin-enjoy-workflow

### Install on each Cursor machine

```bash
git clone https://github.com/dimar-hanung/cursor-plugin-enjoy-workflow.git ~/.cursor/plugins/local/enjoy-workflow
```

On Windows (Git Bash):

```bash
git clone https://github.com/dimar-hanung/cursor-plugin-enjoy-workflow.git "$HOME/.cursor/plugins/local/enjoy-workflow"
```

Or use Cursor’s **Install from GitHub** for plugins if available, pointing at this repo.

### Reload

Restart Cursor or run **Developer: Reload Window**. Then open **Customize** and confirm the skills and `/commands` from Enjoy Workflow are listed.

### Remote SSH

Install the plugin **once on the Cursor client machine** (your laptop), not on each remote server home directory. Skills and commands come from the local plugin path and apply while you work over SSH.

### Update later

```bash
cd ~/.cursor/plugins/local/enjoy-workflow
git pull
```

Then reload the Cursor window.

## Use with OpenCode

OpenCode does **not** load Cursor plugins (`.cursor-plugin/`). Point config at this repo, or copy files into OpenCode’s dirs.

Assume the plugin is already cloned at `~/.cursor/plugins/local/enjoy-workflow` (or `"$HOME/.cursor/plugins/local/enjoy-workflow"` on Windows Git Bash).

### Skills

Point OpenCode at the plugin skills folder in `~/.config/opencode/opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "skills": ["~/.cursor/plugins/local/enjoy-workflow/skills"]
}
```

Or copy them:

```bash
mkdir -p ~/.config/opencode/skills
cp -R ~/.cursor/plugins/local/enjoy-workflow/skills/. ~/.config/opencode/skills/
```

Re-run the `cp` after `git pull` if you use the copy approach.

### Commands

```bash
mkdir -p ~/.config/opencode/commands
cp ~/.cursor/plugins/local/enjoy-workflow/commands/*.md ~/.config/opencode/commands/
```

### Rules (optional)

OpenCode does not read Cursor `.mdc` rules from the plugin. Either:

- Add them via `instructions` in `opencode.json` (copy or point at converted `.md` files), or
- Use a community bridge such as [`opencode-cursor-rules`](https://github.com/fidelix/opencode-cursor-rules)

Restart OpenCode after setup so skills and commands are picked up.

## Inventory

### Skills (11)

| Skill | Source |
|-------|--------|
| `brainstorm` | `~/.cursor/skills` |
| `canvas-markdown` | `~/.agents/skills` |
| `client-business-understanding` | `~/.cursor/skills` |
| `create-skill` | `~/.agents/skills` |
| `deep-agent` | `~/.agents/skills` |
| `docx` | `~/.agents/skills` |
| `mermaid-diagram-specialist` | `~/.agents/skills` |
| `plan-rules` | `~/.agents/skills` |
| `push-git-workflow` | `~/.agents/skills` |
| `tidy-env` | new |
| `ui-craft` | merged (anti-slop + Emil + Apple + animation skills) |

`tugas-kuliah` stays personal in `~/.cursor/skills` (not in this plugin).

### Rules (3)

| Rule | Description |
|------|-------------|
| `agents-skills` | Always require `.agents/skills` for major modules |
| `principles` | Intent-first + readable/low-abstraction code |
| `table-structure-diagrams` | Column-level Mermaid ERDs for schema questions |

### Commands (8)

| Command | Description |
|---------|-------------|
| `/create-docs` | Technical docs in Bahasa Indonesia + Mermaid (+ feature file-map) |
| `/create-project-location` | Generate `.agents/skills/project-locations` for the workspace |
| `/create-quiz-plan` | Interactive quiz from the current plan |
| `/fundamental-think` | First-principles thinking before execution |
| `/fundamental-think-indo` | Same, in Bahasa Indonesia |
| `/refine-ux-writing` | UX writing EN → ID localization |
| `/remove-unrelated` | Hide unnecessary technical detail |
| `/search-related-problem` | Find one likely bug via path skim (not edge-case hunting) |

## Layout

```text
enjoy-workflow/
├── .cursor-plugin/
│   └── plugin.json
├── skills/
│   └── <skill-name>/SKILL.md
├── commands/
│   └── <command>.md
├── rules/
│   └── <rule>.mdc
├── LICENSE
└── README.md
```

## License

MIT
