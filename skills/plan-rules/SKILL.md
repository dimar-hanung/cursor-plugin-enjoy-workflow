---
name: plan-rules
description: >-
  Formats implementation plans as Cursor `.plan.md` files with YAML frontmatter
  (Plan UI). Agent-first dependency stages ordered bottom-up by codebase deps
  (default backend → frontend). Must do + Inventory per stage, written at outcome level
  with imperative verbs (where + what must be true), never literal code edits.
  Plans are straightforward directives with no questions, options, or opinions
  — ask decisions via AskQuestion outside the plan. Study cases capture user
  behaviour before and after. Plans may be large — do not truncate. Use when
  creating, drafting, or presenting any plan — or when switching to Plan mode.
---

# Plan Rules

## Plan tone (non-negotiable)

The plan is for an AI agent to **execute**, not to discuss. Write **one** decided path.

- **Do** write the entire plan in **English** — Goal, study cases, Must do, Inventory, Out of Scope, everything.
- **Do** keep Indonesian (or other non-English) business-process labels in **double quotes** when they appear as domain names — do not translate those labels. Example: At `"Belanja"`, enforce stock check before Pay so checkout cannot oversell.
- **Do** state facts and required work: Goal, User Behaviour (study cases), What Current/Changes, Must do, Inventory, Out of Scope.
- **Do** write at outcome level — where the change lands and what must be true after. The agent chooses the code.
- **Do not** put questions, A/B options, "or", "optionally", "consider", trade-offs, or recommendations in the plan.
- **When a decision matters** → **AskQuestion outside the plan** (≤4/round). Bake the answer in as fact, then continue.

## Before writing

1. **Explore first — verify, never infer.** A plan built on guessed paths sends the agent to files that do not exist.
   - Trace one real path end to end, top down: entry point (route / page / job) → handler → service → repo → schema. Open each file. Names and folder conventions lie.
   - Find the closest feature that already does something similar and copy its patterns — error shape, auth guard, validation, naming, test style.
   - Map deps both ways: what the change needs (so stage order is real) and who calls what you touch (so breakage is known).
   - Split reuse from new: existing types, helpers, endpoints to reuse vs pieces genuinely missing.
   - Cite only what you opened. Every path in Inventory and every `where` in Must do must be a file or symbol you saw.
   - **Stop exploring when** you can name each stage, its dependency order, and the files it touches. Reading past that is thrashing.
2. Blocking A vs B → AskQuestion outside the plan. Never options inside `.plan.md`.
3. Bake answers into Must do / Out of Scope. Write YAML frontmatter first. Dependency stages, not flat task lists. Do not truncate.
4. **Skip a formal plan** for trivial work (single obvious edit, typo, one-file fix you have done many times). State the change and execute.
5. **Not for ui-craft motion audits** — those write self-contained files under `plans/` via `motion-plan-template.md`. Keep feature/product work in `.plan.md` (this skill).

## Dependency stage order

A **dependency stage** = one bounded unit whose outputs must exist before dependent stages begin. Order stages by codebase deps — foundations before dependents, not by feature story.

- **Stack (default):** shared → **backend** (one stage per bounded area) → **frontend**
- **Inside BE:** schema → repos → services → handlers
- **Inside FE:** utils/types → API clients/hooks → components → pages (wire to backend contracts as you build)

Bottom-up means backend contracts exist before frontend starts. **Wire** in frontend Must do — connect UI to those APIs; do not add a separate wiring stage for normal full-stack work.

Wrong: one blob "Frontend"/"Backend", frontend before the APIs it needs, or frontend Must do that only builds UI shells without wiring to backend.

**Separate integration stage** only when glue spans multiple frontends or services (shared SDK, env rollout, mobile + web client) — not the default.

## Frontmatter

```yaml
---
name: Short plan title
overview: One-line summary (or "")
todos:
  - id: stage-user-service
    content: "user-service: after shared-schema"
    status: pending
isProject: false
---
```

One `todo` per dependency stage, same order as Dependency order. Status: `pending` | `in-progress` | `completed` | `error`.

**Todo `content` format:** `"[stage-name]: after [deps]"`

## Body

This order only. No extra top-level sections beyond those listed below. No Stage Index / Risks / Review Surface.

**User Behaviour (Study Cases)** — Observable behaviour, not feature bullets. Usually 1–5 cases (happy path + edges that drive Must do). Each case: title + three **English** prose paragraphs — **The situation** (who, context, trigger), **Before changes** (today), **After changes** (once Must do passes). Separate paragraphs; don't blend Before/After. No bullets or options inside a case. Every **After changes** must be covered by at least one Must do item. Quote non-English domain labels — e.g. `"Belanja"` — do not translate them.

Good:

> The situation A shopper on `"Belanja"` with two Blue Widgets taps Pay when only one is in stock.
> Before changes Spinner, success toast, order page — stock goes negative silently.
> After changes Inline error naming the SKU; cart unchanged; Pay succeeds only when stock holds.

Bad: vague ("better UX"), undecided ("guest checkout — TBD"), bullets/labels (**Actor:** …), implementation detail (`GET /orders` returns 200), translating domain labels (`Shopping` instead of `"Belanja"`).

**Must do** — Outcome-level: **where**, **what must be true**, **why**. Imperative active sentences — verb first, not "In `[where]`…". **Every item needs a `so` reason.** If a meaningful `so <reason>` cannot be stated, the item is probably vague, unnecessary, or too low-level.

**Default formula:** `[Verb] <where> to <outcome> so <reason>.`

Pick the verb by intent. Use **Ensure** only when no sharper verb fits.

- **Create** — New capability, endpoint, flow
- **Add** — New behavior on existing surface
- **Change** — Replace existing behavior
- **Update** — Adjust contract/UI without full rewrite
- **Remove** — Stop bad behavior
- **Enforce** — Rule or invariant
- **Reject** — Error paths
- **Return** — API response contract
- **Expose** — New API/field consumers need
- **Wire** — Connect UI to backend (clients, hooks) — belongs in frontend Must do
- **Persist** — Data that must survive
- **Clear** — Reset state after success
- **Disable** / **Show** — UI guards and feedback
- **Ensure** — Catch-all invariant (sparingly)

By layer: API → Create, Reject, Return, Enforce, Expose · Service → Add, Enforce, Change · FE → Wire (to existing BE), Change, Disable, Show · Schema → Add, Persist, Change.

Good:

- Enforce atomic stock decrement in `createOrder` so concurrent orders cannot oversell.
- Reject insufficient stock on `POST /orders` with `409` `{ code: "INSUFFICIENT_STOCK" }` so clients show a stock-specific message.
- Enforce owner-or-admin access on `GET /orders/:id` so users cannot read another's PII.
- Disable Submit in `CheckoutForm` while payment is in flight so users cannot double-submit.
- Wire `CheckoutForm` to `POST /orders` so Pay submits the cart and navigates on success.
- Show an inline SKU error in `CheckoutForm` when stock is insufficient so checkout fails before payment.

Bad — too low-level: Create `src/orders/createOrder.ts`, change line 42, rename `qty`, add `try/catch` steps.

Bad — vague/undecided: improve the API, optionally CSV, Redis vs in-memory, "consider edge cases".

Bad — passive/weak: In `createOrder`, atomic stock decrement… · Submit disabled while in flight.

```markdown
# Overview

## Goal
[What and why.]

## User Behaviour (Study Cases)
[Skip when no user-facing surface — write `No user-facing change.`]

### [Short case title]
The situation …
Before changes …
After changes …

## What Current (Technical)
[Existing modules / APIs that matter.]

## What Changes (Technical)
[High-level changes; detail under stages.]

## Visualization (Technical)
[Title + 1–2 sentence description + mermaid. Skip unless cross-stage flow, state machine, or schema relationship is non-obvious from Must do alone.]

# Bottom-Up Implementation

## Dependency order
1. `[shared / schema]` depends on none
2. `[backend]` depends on 1
3. `[frontend]` depends on 2 — includes wiring UI to backend contracts

## Stage: [name]
**Goal**: … 1–2 paragraphs
**Depends on**: …

### Must do
- [Verb] `[where]` to [outcome] so [why].


### Inventory
1. **New files**
  - `path` — purpose
2. **Modified files**
  - `path` — what changes
3. **Data schema changes**
  - … (or None)
4. **API endpoints**
  - `METHOD /path` — purpose (or None)
5. **Verify**
  - command or scenario (or None)

# Validation
[Skip if none — trivial or fully covered by stage Verify lines.]

- Run `…` — expect …
- Prove study case "[Title]" by …

# Out of Scope
[Non-goals. Or: None.]

# Summary
- **Important notes** — env, config, breaking changes spanning stages
```
