---
name: plan-rules
description: >-
  Formats implementation plans as Cursor `.plan.md` files with YAML frontmatter
  (Plan UI). Agent-first domains ordered bottom-up by codebase deps (default
  backend → frontend). Must do + Inventory per domain, written at outcome level
  (where + what must be true), never literal code edits. Plans are straightforward
  directives with no questions, options, or opinions — ask decisions via
  AskQuestion outside the plan. Study cases capture user behaviour before and
  after. Plans may be large — do not truncate. Use when creating, drafting, or
  presenting any plan — or when switching to Plan mode.
---

# Plan Rules

## Plan tone (non-negotiable)

The plan is for an AI agent to **execute**, not to discuss. Write **one** decided path.

- **Do** state facts and required work: Goal, User Behaviour (study cases), What Current/Changes, Must do, Inventory, Out of Scope.
- **Do** write at outcome level — where the change lands and what must be true after. The agent chooses the code.
- **Do not** put questions, A/B options, "or", "optionally", "consider", trade-offs, or recommendations in the plan.
- **When a decision matters** → **AskQuestion outside the plan** (≤4/round). Bake the answer in as fact, then continue.

## Before writing

1. Explore real paths and deps.
2. Blocking A vs B → AskQuestion outside the plan. Never options inside `.plan.md`.
3. Bake answers into Must do / Out of Scope. Write YAML frontmatter first. Domains, not task lists. Do not truncate.

## Domain order

A **domain** = one dependency-bounded area. Order by codebase deps — foundations before dependents, not by feature story.

- **Stack (default):** shared → **backend** (one domain per area) → **frontend** → wiring
- **Inside BE:** schema → repos → services → handlers
- **Inside FE:** utils/types → components → pages

Wrong: one blob "Frontend"/"Backend", or frontend before the APIs it needs.

## Frontmatter

```yaml
---
name: Short plan title
overview: One-line summary (or "")
todos:
  - id: domain-user-service
    content: "user-service: after shared-schema; done when Must do passes"
    status: pending
isProject: false
---
```

One `todo` per domain, same order as Domain order. Status: `pending` | `in-progress` | `completed` | `error`.

## Body

This order only. No extra top-level sections. No Domain Index / Risks / Review Surface.

```markdown
# Overview

## Goal
[What and why.]

## User Behaviour (Study Cases)
[Skip when no user-facing surface — write `No user-facing change.`]

Each case: title + three prose paragraphs — `The situation`, `Before changes`, `After changes`. No bullets or options inside a case. Usually 2–5 cases (happy path + edges that drive Must do).

### [Title]
The situation …
Before changes …
After changes …

## What Current (Technical)
[Existing modules / APIs that matter.]

## What Changes (Technical)
[High-level changes; detail under domains.]

## Visualization (Technical)
[Title + 1–2 sentence description + mermaid. Skip section if none needed.]

# Implementation by Domain

**Done when:** all Must do checked, Inventory paths exist, no out-of-scope work.

## Domain order
1. `[shared / schema]` depends on none
2. `[backend]` depends on 1
3. `[frontend]` depends on 2

## Domain: [name]
**Goal**: … 1–2 paragraphs
**Depends on**: …

### Must do
- [ ] In `[where]`, [outcome] so [why].

### Inventory
- **New files** — `path` — purpose
- **Modified files** — `path` — what changes
- **Data schema changes** — … (or None)
- **API endpoints** — `METHOD /path` — purpose (or None)

# Out of Scope
[Non-goals. Or: None.]

# Summary
- **Important notes** — env, config, breaking changes spanning domains
```

## User Behaviour (Study Cases)

Observable behaviour — not feature bullets. Three paragraphs per case: **The situation** (who, context, trigger), **Before changes** (today), **After changes** (once Must do passes). Separate paragraphs; don't blend Before/After into one.

Good:

> The situation A shopper with two Blue Widgets taps Pay when only one is in stock.
> Before changes Spinner, success toast, order page — stock goes negative silently.
> After changes Inline error naming the SKU; cart unchanged; Pay succeeds only when stock holds.

Bad: vague ("better UX"), undecided ("guest checkout — TBD"), bullets/labels (**Actor:** …), implementation detail (`GET /orders` returns 200).

## Must do

Outcome-level checkboxes: **where**, **what must be true**, **why** (`so …`). No lines, diffs, or step-by-step edits.

Default: `In <where>, <outcome> so <reason>.`

Good:

- In `createOrder`, atomic stock decrement so concurrent orders cannot oversell.
- In `POST /orders`, reject insufficient stock with `409` `{ code: "INSUFFICIENT_STOCK" }` so clients show a stock-specific message.
- On `GET /orders/:id`, only owner or `admin` passes authorization so users cannot read another's PII.
- In `CheckoutForm`, Submit disabled while in flight so users cannot double-submit.

Bad — too low-level: change line 42, rename `qty`, add `try/catch` steps.

Bad — vague/undecided: improve the API, optionally CSV, Redis vs in-memory, "consider edge cases".
