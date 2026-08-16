---
name: plan-rules-simple
description: >-
  Formats a high-level `.plan.md` as a one-page RFC for developer review:
  Problem, Proposal, Impact, Decision Requested. No executor detail (Tasks,
  schema, API payloads, Inventory). Use when the user wants a simple or
  high-level plan, a plan that's easy to review, or /plan-rules-simple. For an
  executor-ready plan, use /plan-rules.
---

# Plan Rules (Simple)

One-page RFC-style `.plan.md` so a developer can review the direction and the ask without file-level or payload-level executor detail. Format follows the lightweight RFC / one-pager pattern: Problem → Proposal → Impact → Decision Requested.

## Vs `/plan-rules`

| Need | Use |
| --- | --- |
| High-level plan a developer can review quickly | **This command** |
| Full executor-ready plan (parallel domains, Tasks, schema, API contract, Inventory) | `/plan-rules` |

If they later want `/run-plan`, rewrite with `/plan-rules` first so each domain has Tasks and Inventory.

## Hard rules

- Write the **entire** plan in **English**. Keep non-English business-process labels in **double quotes** — do not translate them (e.g. At `"Belanja"`, …).
- One decided path only. No questions, A/B options, "or", "optionally", "consider", trade-offs, or recommendations inside `.plan.md`. Decisions → **AskQuestion outside the plan** (≤4/round). Bake the answer into Proposal / Out of Scope.
- Max heading level `##`. Allowed H1s: `# Overview` · `# Decision` · `# Out of Scope`. No `###`.
- Keep it to one page. If a section needs more than ~5 lines, the plan is too detailed for this format — use `/plan-rules`.

## Procedure

### 1. Explore (verify, never infer)

Open the real path end to end (entry → handler → service → repo → schema) and the closest existing feature. You need the map even though no Inventory is written. Stop when you can state the problem, the proposed direction, and the impact without guessing.

### 2. Write YAML frontmatter first

```yaml
---
name: Short plan title
overview: One-line summary (or "")
isProject: false
---
```

No `todos`. This format is for review, not execution.

### 3. Write the body (this order only)

1. **Problem** — what is broken, missing, or insufficient, and the cost of the status quo. Be specific: name the user-facing symptom or the operational pain. 2–4 sentences.
2. **Proposal** — the high-level direction: key components and how they connect. Name modules / APIs, not files or payloads. One short paragraph, or a paragraph plus a mermaid diagram via `mermaid-diagram-specialist` when the flow is non-obvious.
3. **Impact** — what changes for users and for the system: scope (roughly which capabilities), success signal, main risk with its mitigation. Bullets, one line each.
4. **Decision Requested** — what the reviewer must confirm before implementation. One sentence, no rhetorical questions.

Fill each section using the body template. Do not add sections.

### 4. Self-check before presenting

- [ ] Hard rules held (English, quotes, one path, no `###`, no extra H1s)
- [ ] Problem names a concrete symptom or cost — not "improve X"
- [ ] Proposal is direction-level — no file paths, field diffs, or payloads
- [ ] Impact covers user change, success signal, and top risk
- [ ] Decision Requested is one confirmable sentence
- [ ] Fits on one page; no Tasks / schema / API contract / Inventory / Validation / study cases

## Do not write

- `todos` in YAML
- Study cases / User Behaviour
- Parallel Domains / Provides / Consumes / Outcome
- Tasks / Data schema / API contract / Inventory
- Validation / Alternatives Considered / Open Questions

This format is a review gate, not a design doc. Alternatives and open questions are resolved before the plan is written (AskQuestion outside the plan), and execution detail belongs in `/plan-rules`.

---

## Body template

Copy this structure. Replace placeholders.

````markdown
# Overview

## Problem
[What is broken or missing, and the cost of the status quo. 2–4 sentences.]

## Proposal
[High-level direction: key components and how they connect. One short paragraph, or paragraph + mermaid.]

## Impact
- [User-facing change]
- [Success signal — observable]
- [Top risk — mitigation]

# Decision

## Decision Requested
[One sentence: what the reviewer must confirm before implementation.]

# Out of Scope
[Non-goals, or `None`.]
````
