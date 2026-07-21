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
| `/search-related-problem` | Find one related bug/problem from context |

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
