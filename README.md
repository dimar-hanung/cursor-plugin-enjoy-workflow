# Enjoy Workflow

Personal Cursor plugin that bundles skills and slash commands so you can reuse the same workflows on any machine or Remote SSH session — without copying files into every server’s `~/.agents` or `~/.cursor`.

## Install (Git)

### 1. Host the repo

Push this repository to GitHub (private is fine).

### 2. Install on each Cursor machine

```bash
git clone <repo-url> ~/.cursor/plugins/local/enjoy-workflow
```

On Windows (Git Bash):

```bash
git clone <repo-url> "$HOME/.cursor/plugins/local/enjoy-workflow"
```

Or use Cursor’s **Install from GitHub** for plugins if available, pointing at this repo.

### 3. Reload

Restart Cursor or run **Developer: Reload Window**. Then open **Customize** and confirm the skills and `/commands` from Enjoy Workflow are listed.

### 4. Remote SSH

Install the plugin **once on the Cursor client machine** (your laptop), not on each remote server home directory. Skills and commands come from the local plugin path and apply while you work over SSH.

### Update later

```bash
cd ~/.cursor/plugins/local/enjoy-workflow
git pull
```

Then reload the Cursor window.

## Inventory

### Skills (10)

| Skill | Source |
|-------|--------|
| `brainstorm` | `~/.cursor/skills` |
| `canvas-markdown` | `~/.agents/skills` |
| `client-business-understanding` | `~/.cursor/skills` |
| `create-docs-feature-mapping` | `~/.agents/skills` |
| `create-project-location-skill` | `~/.agents/skills` |
| `create-skill` | `~/.agents/skills` |
| `deep-agent` | `~/.agents/skills` |
| `docx` | `~/.agents/skills` |
| `mermaid-diagram-specialist` | `~/.agents/skills` |
| `plan-rules` | `~/.agents/skills` |

`tugas-kuliah` stays personal in `~/.cursor/skills` (not in this plugin).

### Commands (8)

| Command | Description |
|---------|-------------|
| `/create-agents-rule` | Add AGENTS.md rule for `.agents/skills` |
| `/create-docs` | Technical docs in Bahasa Indonesia + Mermaid |
| `/create-quiz-plan` | Interactive quiz from the current plan |
| `/debat-brainstorm` | Multi-perspective debate brainstorm |
| `/fundamental-think` | First-principles thinking before execution |
| `/fundamental-think-indo` | Same, in Bahasa Indonesia |
| `/refine-ux-writing` | UX writing EN → ID localization |
| `/remove-unrelated` | Hide unnecessary technical detail |

## Layout

```text
enjoy-workflow/
├── .cursor-plugin/
│   └── plugin.json
├── skills/
│   └── <skill-name>/SKILL.md
├── commands/
│   └── <command>.md
├── LICENSE
└── README.md
```

## License

MIT
