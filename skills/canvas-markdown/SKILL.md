---
name: canvas-markdown
description: >-
  Write standalone prose reports as markdown in .agents/canvas-markdown/.
  Use for long text analyses the user may revisit as a file — not for Cursor
  Canvas (.canvas.tsx), not for product docs in docs/. Read this skill when
  creating, editing, or updating files in .agents/canvas-markdown/.
---

# Canvas Markdown

Write the deliverable as a markdown file at:

```
<workspace>/.agents/canvas-markdown/<topic>.md
```

## Deliverable router (pick one)

| Need | Use | Path / form |
|------|-----|-------------|
| Interactive / visual layout beside chat (tables, charts, explorations) | Cursor **Canvas** skill | `.canvas.tsx` |
| Long **prose** report to reopen or share as a file | **This skill** | `.agents/canvas-markdown/<topic>.md` |
| Product / feature **technical docs** (ID, Mermaid, file maps) | `/create-docs` | `docs/<topic>.md` |
| Word / `.docx` | `docx` skill | `.docx` file |

**Do not** write the same report in more than one of these. If the user says only "report" / "analisis" without format: prefer **this skill** for prose conclusions; prefer **Canvas** when they ask for a canvas, dashboard-like layout, or interactive exploration; prefer **`/create-docs`** when they ask for docs, dokumentasi, or a file map under `docs/`.

## When to use

Use when the user wants a **standalone prose report** — analyses, audits, research summaries, or multi-section findings they may revisit or share as markdown.

Skip for:

- Code changes, short answers, drafts for other tools, or work inside an existing document
- Cursor Canvas / `.canvas.tsx` requests → Canvas skill
- Technical product documentation → `/create-docs`
- Word documents → `docx`

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
