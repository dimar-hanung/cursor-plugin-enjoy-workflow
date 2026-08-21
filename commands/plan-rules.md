---
name: plan-rules
description: >-
  Write a `.plan.md` that's easy to review — include only what helps a reviewer
  decide; no fixed template. Use /plan-rules-simple for a one-page RFC only.
---

# Plan Rules

**Skip** trivial one-file fixes. **Use `/plan-rules-simple`** for a quick RFC without implementation detail.

- English. Business labels stay in **"quotes"**.
- One decided path — no options in the plan; decide outside first.
- Uncertain? Use `grill-me` (`skills/grill-me/SKILL.md`) — don't guess or leave TBD.
- Explore the real code path before writing; only cite files you opened.
- Present for review before deep implementation detail.

**Write for review.** Include only what helps a reviewer decide quickly. Reference list below — not a template. Every item is optional; add, remove, or reorder freely.

- **Goal** — what and why
- **Schema** — column-level diagram when data changes (`erDiagram`; see `table-structure-diagrams`); optional diff bullets
- **Study cases** — situation, before, after (max ~5)
- **Out of scope** — what you are not doing
- **Outcome** — done when… (prose is fine)
- **Tasks** — what to build, at symbol/route/component level
- **Files** — paths to touch and why
- **Flow diagram** — if the user journey is hard to picture
- **Validation** — how to prove it works

**Check before done:** if present — schema matches models/migrations; every "after" case has tasks; file list matches opened paths.
