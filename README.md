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

## Use with Codex (CLI + GUI)

Works for **both** Codex CLI and the ChatGPT / Codex desktop app (and IDE extension). Same skill folders; neither loads Cursor’s `.cursor-plugin/` format.

Docs: https://developers.openai.com/codex/skills

### Skills

Copy into the user skills dir (picked up by CLI and GUI):

```bash
mkdir -p ~/.agents/skills
cp -R ~/.cursor/plugins/local/enjoy-workflow/skills/. ~/.agents/skills/
```

Or keep them project-scoped by copying into a repo’s `.agents/skills/` instead.

Re-run the `cp` after `git pull` if you use the copy approach.

### Commands

Codex does not use Cursor `commands/*.md` as slash commands. Treat them as skills (wrap each prompt in `skills/<name>/SKILL.md`) or paste the prompt manually.

### Rules

Codex reads `AGENTS.md`, not Cursor `.mdc` rules. Copy useful rule text into `AGENTS.md` (project) if you need it.

Restart Codex / reopen the desktop app after copying so skills refresh.

## Use with VS Code GitHub Copilot

Works in **VS Code Copilot Chat / Agent**, and the same Agent Skills paths are used by Copilot CLI and cloud agent. Does **not** load Cursor’s `.cursor-plugin/`.

Docs: https://code.visualstudio.com/docs/agent-customization/agent-skills

### Skills

Point VS Code at the plugin skills folder with `chat.agentSkillsLocations` (User or Workspace settings):

```json
{
  "chat.agentSkillsLocations": {
    "~/.cursor/plugins/local/enjoy-workflow/skills": true
  }
}
```

Or copy them:

```bash
mkdir -p ~/.copilot/skills
cp -R ~/.cursor/plugins/local/enjoy-workflow/skills/. ~/.copilot/skills/
```

`~/.agents/skills/` also works (same folder Codex uses). Project-scoped alternative: copy into the repo’s `.github/skills/` or `.agents/skills/`.

Re-run the `cp` after `git pull` if you use the copy approach.

### Commands

Copilot does not read Cursor `commands/*.md`. Use [prompt files](https://code.visualstudio.com/docs/copilot/customization/prompt-files) (e.g. `.github/prompts/<name>.prompt.md`) or invoke skills with `/` in chat.

### Rules

Copilot uses `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`, and/or `AGENTS.md` — not Cursor `.mdc` rules. Copy useful rule text into one of those if you need it.

Reload the VS Code window (or reopen Copilot Chat) after setup so skills refresh.

## Inventory

### Skills (12)

| Skill | Source |
|-------|--------|
| `anti-slop-writing` | new (from `/refine-ux-writing`) |
| `brainstorm` | `~/.cursor/skills` |
| `canvas-markdown` | `~/.agents/skills` |
| `client-business-understanding` | `~/.cursor/skills` |
| `create-skill` | `~/.agents/skills` |
| `debug-top-down` | `~/.agents/skills` |
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

### Commands (13)

| Command | Description |
|---------|-------------|
| `/behaviour-research` | Verify exact versions of tech the current work touches + report version-specific pitfalls (chat; not plan-specific) |
| `/create-docs` | Technical docs in Bahasa Indonesia + Mermaid (+ feature file-map) |
| `/create-project-location` | Generate `.agents/skills/project-locations` for the workspace |
| `/create-quiz-plan` | Interactive quiz from the current plan |
| `/fundamental-think` | First-principles thinking before execution |
| `/fundamental-think-indo` | Same, in Bahasa Indonesia |
| `/plan-behaviour-research` | Same research as `/behaviour-research`, scoped to the plan + insert a Behaviour section |
| `/refine-ux-writing` | Triggers `anti-slop-writing` (EN → ID UX microcopy) |
| `/remove-unrelated` | Hide unnecessary technical detail |
| `/search-data-smell` | Find one bad data contract / shape smell; flag Breaking on that fix |
| `/search-overengineering` | Find one overengineering / simplification opportunity; flag Breaking on that fix |
| `/search-performance-can-improve` | Find one likely performance win via hot-path skim; flag Breaking on that fix |
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
