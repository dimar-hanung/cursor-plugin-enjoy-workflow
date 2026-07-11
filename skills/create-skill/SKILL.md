---
name: create-skill
description: Guide for creating Agent Skills files for GitHub Copilot. Use this skill when asked to create a new skill, add a skill, or teach Copilot specialized behaviors for a project.
---

# 🧠 Agent Instructions: Creating Skills Files for GitHub Copilot

Here's a comprehensive guide to creating **Agent Skills** files for GitHub Copilot—your way of teaching Copilot specialized, reusable behaviors for your projects!

---

## 📁 1. Choose Where to Store Your Skill

| Scope                              | Path                           |
| ---------------------------------- | ------------------------------ |
| **Per-repository (project-level)** | `.agents/skills/<skill-name>/` |

---

## 🗂️ 2. Create the Directory Structure

Each skill lives in its own subdirectory. The key file is `SKILL.md`:

```
.agents/skills/my-skill/
    └── SKILL.md
```

---

## 📝 3. Write the `SKILL.md` File

This file uses **YAML frontmatter** for metadata, followed by Markdown for detailed instructions. Here's a skeleton:

```markdown name=SKILL.md
---
name: my-skill
description: Describe what this skill does and when Copilot should use it.
---

# Instructions for Copilot

Step-by-step directions, examples, workflow notes, and guidelines go here.

## Examples

- Show expected code style or output
- Provide specific commands (e.g., `npm test`, `pytest`)
- List project boundaries (e.g., "Never commit secrets")

## Rules

- **MUST**: Always use TypeScript strict mode.
- **NEVER**: Hardcode API keys or secrets.
```

---

## ✨ 4. Best Practices for High-Quality Skills

- **Be specific**: Define clear commands, tools, and expected outputs.
- **Use real code examples**: Don't just describe—demonstrate!
- **Set explicit rules**: Use "must" and "never" statements for boundaries.
- **Specify your stack**: Mention frameworks, versions, and conventions (e.g., "React 18 with TypeScript").
- **Keep it maintainable**: Update skills as your project evolves.

---

## 🛠️ 5. (Optional) Add Helper Scripts/Resources

You can include scripts, templates, or other resources in your skill folder. Copilot can use these when fulfilling requests.

```
.agents/skills/my-skill/
    ├── SKILL.md
    ├── templates/
    │   └── component-template.tsx
    └── scripts/
        └── validate.sh
```

---

## 📋 Skill Template (Copy & Paste)

Use this template when creating a new skill:

```markdown name=SKILL.md
---
name: <skill-name>
description: <One-line description of what this skill does and when to use it.>
---

# Skill: <skill-name>

## Overview

<Brief explanation of the skill's purpose and functionality.>

## When to Use

<List scenarios where this skill should be invoked.>

## Instructions

<Step-by-step directions for completing tasks with this skill.>

### Step 1: <First Step>
<Detailed instructions>

### Step 2: <Second Step>
<Detailed instructions>

## Examples

### Example 1: <Scenario>
```<code example>```

### Example 2: <Scenario>
```<code example>```

## Rules

- **MUST**: <Important rule>
- **MUST**: <Important rule>
- **NEVER**: <Prohibited action>
- **NEVER**: <Prohibited action>

## Resources

<Base directory for this skill: file:///path/to/.agents/skills/<skill-name>>
<Relative paths in this skill are relative to this base directory.>
```

---

## 🚀 Quick Reference

| Element | Purpose |
|---------|---------|
| `name` | Unique identifier for the skill |
| `description` | When Copilot should use this skill |
| Frontmatter | YAML metadata (between `---` markers) |
| Markdown body | Detailed instructions and examples |
| Rules | Explicit MUST/NEVER constraints |
| Examples | Concrete code/output samples |

---

## References

- [GitHub Blog: How to write a great agents.md](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)
- [Visual Studio Magazine: Hands-on with new GitHub Copilot Agent Skills](https://visualstudiomagazine.com/articles/2026/01/11/hand-on-with-new-github-copilot-agent-skills-in-vs-code.aspx)
