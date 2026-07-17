---

## name: plan-rules
description: >-
  Formats implementation plans as Cursor `.plan.md` files with YAML frontmatter
  (Plan UI), plus overview (goal, current state, changes, visualization), phased
  tasks, out of scope boundaries, and factual summary for tech lead review. Use
  when creating, drafting, or presenting any plan — or when switching to Plan mode.

# Plan Rules

Use when proposing an implementation plan or switching to Plan mode. Skip for trivial one-file fixes.

- Explore enough to ground the plan in real paths; ask at most 2 clarifying questions.
- Write a `.plan.md` with **YAML frontmatter first** (required for Cursor Plan UI).



## Frontmatter (Plan UI)

```yaml
---
name: Short plan title
overview: One-line summary (or "")
todos:
  - id: phase-1-slug
    content: Phase 1 outcome
    status: pending
isProject: false
---
```

- `todos`: one per phase (`pending` | `in-progress` | `completed` | `error`). Detail stays in the body.
- `isProject`: `true` only for multi-repo / long-running work.



## Body structure

Keep this order. No extra top-level sections.

```markdown
# Overview

## Goal
[2–3 sentences: what and why]

## What Current
[Existing files, behavior, APIs — factual]

## What Changes
[What will change — factual bullets]

## Visualization
[At least one Mermaid diagram; use real module/file names]
### [Title Visualization 1]

### [Title Visualization 2]


# Implementation Phases

## Phase 1: [Outcome title]
**Goal**: …
**Tasks:**
### Task 1.1: …
[File paths + main logic/structure — no full code]

# Out of Scope
[What this plan does not cover, or: None — full scope as stated in Goal.]

# Summary
[New/modified files, schema, APIs, constraints — factual only]
```



## Must-knows

- Tasks name **file paths** and essential behavior; not complete code or “consider also…”.
- Diagrams use project names, not generic “Frontend” / “Database”.
- Body and summary stay **factual** — no recommendations or trade-off essays.

