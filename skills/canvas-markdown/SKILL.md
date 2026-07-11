---
name: canvas-markdown
description: >-
  Write standalone reports as markdown files in .agents/canvas-markdown/.
  Use for long analyses, investigations, research summaries, or data-heavy
  conclusions that should live outside the chat. Read this skill when creating,
  editing, or updating files in .agents/canvas-markdown/.
---

# Canvas Markdown

Write the deliverable as a markdown file at:

```
<workspace>/.agents/canvas-markdown/<topic>.md
```

## When to use

Use when the user wants a **standalone report** — analyses, audits, research summaries, or multi-section findings they may revisit or share.

Skip for code changes, short answers, drafts for other tools, or work inside an existing document.

## How to write

1. **Write the file** with the write/edit tool. Do not paste the full report in chat.
2. **Name** the file with descriptive kebab-case (e.g. `billing-audit-q2.md`).
3. **One topic, one file.** Update the same file when the conclusion changes — do not create duplicates.
4. **Make it self-contained.** Lead with the conclusion. Include all data inline; no placeholders or "see chat above".
5. **Gitignore** — on first write in a workspace, ensure `.agents/canvas-markdown/` is in `.gitignore`.

## Chat response

After writing or updating:

- Give a brief summary (a few sentences)
- Link to the file with its full absolute path
- Do not duplicate the full markdown body unless the user asks
