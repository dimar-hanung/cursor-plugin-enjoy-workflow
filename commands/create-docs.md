---
name: create-docs
description: Create technical product docs in Bahasa Indonesia with Mermaid in the docs/ folder. Includes feature file-map when mapping FE/BE files. Not for prose reports (canvas-markdown) or interactive Canvas (.canvas.tsx).
---

## When to use (vs other deliverables)

| Need | Use instead |
|------|-------------|
| Interactive / visual exploration beside chat | Cursor Canvas (`.canvas.tsx`) |
| Long prose analysis / audit as a markdown file | `canvas-markdown` → `.agents/canvas-markdown/` |
| Product docs, architecture notes, feature file maps | **This command** → `docs/` |

Do not duplicate the same content into `docs/` and `.agents/canvas-markdown/`.

## Rules

1. Write `docs/{{topic-kebab}}.md` (Bahasa Indonesia).
2. Include Mermaid where it clarifies flow, architecture, or schema (`mermaid-diagram-specialist`).
3. No line numbers in file maps — use component/method names.
4. Single-repo features: drop secondary-module / dual FE–BE scaffolding.
5. Prefer `project-locations` if present.

## Doc shell

```markdown
# Judul Dokumen
## Daftar Isi
## Overview
## Visualization
(diagrams + short captions)
## Isi
…
```

## Feature file-map (when mapping a feature)

```markdown
---
name: {{docs-name}}
description: {{one line}}
---

# {{Feature Display Name}} File Map

Use for "{{internal feature name}}".

## Files Mapping

### Frontend (`{{frontend-root}}`)
- [File](relative/path) — role

### Backend (`{{backend-root}}`)
- [File](relative/path) — role

### Integration Entry Points
- [File](relative/path) — role

## Database Mapping
- **{{table}}**: relation to feature (optional)

## Runtime path
- Frontend route / REST base / socket namespace (as relevant)
```

Delete unused sections. Find files with `rg` on feature name tokens before writing.

User Request:
