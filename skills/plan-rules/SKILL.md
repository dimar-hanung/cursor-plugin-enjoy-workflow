---
name: plan-rules
description: >-
  Formats implementation plans as Cursor `.plan.md` files with YAML frontmatter
  (Plan UI). Agent-first domain stages that all start in parallel — never a
  pipeline that waits on a previous stage. Each domain publishes a request-shaped
  Contract plus an Outcome so other domains bind to the contract, not to finished
  work. Must do + Inventory per domain, written at outcome level with imperative
  verbs (where + what must be true), never literal code edits. Plans are
  straightforward directives with no questions, options, or opinions — ask
  decisions via AskQuestion outside the plan. Study cases capture user behaviour
  before and after. Plans may be large — do not truncate. Use when creating,
  drafting, or presenting any plan — or when switching to Plan mode.
---

# Plan Rules

## Plan tone (non-negotiable)

The plan is for an AI agent to **execute**, not to discuss. Write **one** decided path.

- **Do** state facts and required work: Goal, User Behaviour (study cases), What Current/Changes, Domains, Contract, Outcome, Must do, Inventory, Out of Scope.
- **Do** write at outcome level — where the change lands and what must be true after. The agent chooses the code.
- **Do not** put questions, A/B options, "or", "optionally", "consider", trade-offs, or recommendations in the plan.
- **When a decision matters** → **AskQuestion outside the plan** (≤4/round). Bake the answer in as fact, then continue.

## Before writing

1. **Explore first — verify, never infer.** A plan built on guessed paths sends the agent to files that do not exist.
   - Trace one real path end to end, top down: entry point (route / page / job) → handler → service → repo → schema. Open each file. Names and folder conventions lie.
   - Find the closest feature that already does something similar and copy its patterns — error shape, auth guard, validation, naming, test style.
   - Map who calls what you touch (so each Contract is complete) and which files each domain owns (so parallel agents do not collide).
   - Split reuse from new: existing types, helpers, endpoints to reuse vs pieces genuinely missing.
   - Cite only what you opened. Every path in Inventory and every `where` in Must do must be a file or symbol you saw.
   - **Stop exploring when** you can name each domain, its Contract (request / success / errors), its Outcome, and the files it owns. Reading past that is thrashing.
2. Blocking A vs B → AskQuestion outside the plan. Never options inside `.plan.md`.
3. Bake answers into Must do / Out of Scope. Write YAML frontmatter first. Parallel domain stages, not a dependency pipeline, not a flat task list. Do not truncate.
4. **Skip a formal plan** for trivial work (single obvious edit, typo, one-file fix you have done many times). State the change and execute.
5. **Not for ui-craft motion audits** — those write self-contained files under `plans/` via `motion-plan-template.md`. Keep feature/product work in `.plan.md` (this skill).

## Domain stages (parallel)

A **domain** = one bounded capability an agent can finish without waiting for another stage. Split by domain, not by stack layer or codebase dependency order.

All domains **start together**. Coordination is the published **Contract**, not stage order. An agent implements or consumes the request shape in the plan — it does not wait for another domain's code to land.

- **Do** split by capability (`orders`, `stock`, `notifications`). One domain owns a coherent Contract and a non-overlapping file set.
- **Do** put API and UI of the same capability in **separate parallel domains** when they share a Contract and would not edit the same files (`orders-api` exposes `POST /orders`, `orders-ui` consumes it). Both start now; UI **Wire**s to the Contract, not to a finished backend stage.
- **Do not** pipeline layers: shared → schema → repos → services → handlers → frontend. That forces waiting.
- **Do not** write `Depends on`, `after [stage]`, or any gate that says another domain must finish first.
- **Do not** put the same path in two domains' Inventory. If they would collide, merge them or give the file to one owner; others consume the Contract.

Wrong: one blob "Frontend"/"Backend", a backend stage that must finish before UI starts, or UI Must do that only builds shells without wiring to the Contract.

**Separate integration domain** only when glue spans multiple frontends or services (shared SDK, env rollout, mobile + web client) — and it still starts in parallel against those Contracts, not after them.

Execute with `/run-plan` — one Composer 2.5 subagent per domain, all started together.

## Frontmatter

```yaml
---
name: Short plan title
overview: One-line summary (or "")
todos:
  - id: domain-orders-api
    content: "orders-api: POST /orders → pay without oversell"
    status: pending
  - id: domain-orders-ui
    content: "orders-ui: POST /orders → Pay wired, stock error shown"
    status: pending
isProject: false
---
```

One `todo` per domain. List in any order — none is a gate for another. Status: `pending` | `in-progress` | `completed` | `error`.

**Todo `content` format:** `"[domain]: [request] → [outcome]"`

## Body

This order only. No extra top-level sections beyond those listed below. No Stage Index / Risks / Review Surface.

```markdown
# Overview

## Goal
[What and why.]

## User Behaviour (Study Cases)
[Skip when no user-facing surface — write `No user-facing change.`]

Each case: title + three prose paragraphs — `The situation`, `Before changes`, `After changes`. No bullets or options inside a case. Usually 1–5 cases (happy path + edges that drive Must do). Every case's **After changes** must be covered by at least one Must do item.

### [Title]
The situation …
Before changes …
After changes …

## What Current (Technical)
[Existing modules / APIs that matter.]

## What Changes (Technical)
[High-level changes; detail under domains.]

## Visualization (Technical)
[Title + 1–2 sentence description + mermaid. Skip unless cross-domain contracts, state machine, or schema relationship is non-obvious from Must do alone.]

# Parallel Domains

## Domains
All start together. Bind to Contracts, not to finished stages. Bullets, not a sequence.

- `[orders-api]` — Request `POST /orders` `{ items, paymentMethod }` — Outcome: pay without oversell
- `[stock]` — Request `decrementStock(sku, qty)` — Outcome: stock never negative
- `[orders-ui]` — Request consumes `POST /orders` — Outcome: Pay wired; stock error shown

## Stage: [domain]
**Contract**:
- Request: `METHOD /path` `{ fields }` (or `fn(args)` / event)
- Success: `status` `{ fields }`
- Errors: `status` `{ code, … }`
- Consumes: `[other-domain]` `Request` (bind to that Contract; do not wait). Omit this line when the domain consumes nothing.

**Outcome**: [What must be true when this domain is done — observable, 1–2 sentences.]

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
[Skip if none — trivial or fully covered by domain Verify lines.]

- Run `…` — expect …
- Prove study case "[Title]" by …

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

## Contract and Outcome

Every domain stage must show both. The Contract is the request other domains and agents bind to. The Outcome is the done-check for this domain.

**Contract** is request-shaped — not a prose goal, not a file list.

| Field | What to write |
| --- | --- |
| **Request** | The call: `METHOD /path` `{ fields }`, or `fn(args)`, or event payload |
| **Success** | Status + body (or return value) when the request is accepted |
| **Errors** | Status + `{ code, … }` (or thrown code) the consumer must handle |
| **Consumes** | Other domains' Request this domain binds to. Omit when none |

The exposing domain implements Request/Success/Errors. The consuming domain **Wire**s to that same Request — it does not wait for the exposing domain to finish.

Good:

```text
**Contract**:
- Request: `POST /orders` `{ items: [{ sku, qty }], paymentMethod }`
- Success: `201` `{ orderId, status }`
- Errors: `409` `{ code: "INSUFFICIENT_STOCK", sku }`
- Consumes: `stock` `decrementStock(sku, qty)`

**Outcome**: A shopper can pay; concurrent checkouts cannot drive stock negative; clients receive a stock-specific error.
```

Bad: "depends on stock stage", "after orders-api", "implement the orders module", Request with no Success/Errors, Outcome that restates Must do file edits.

## Must do

Outcome-level checkboxes: **where**, **what must be true**, **why**. Write **imperative active** sentences — verb first, not "In `[where]`…".

**Every Must do item must include a reason clause introduced by `so`.** Never omit the reason. If a meaningful `so <reason>` cannot be stated, the item is probably vague, unnecessary, or too low-level.

**Default formula:** `[Verb] <where> to <outcome> so <reason>.`

Pick the verb by intent. Use **Ensure** only when no sharper verb fits.

| Verb | Use when |
| --- | --- |
| **Create** | New capability, endpoint, flow |
| **Add** | New behavior on existing surface |
| **Change** | Replace existing behavior |
| **Update** | Adjust contract/UI without full rewrite |
| **Remove** | Stop bad behavior |
| **Enforce** | Rule or invariant |
| **Reject** | Error paths |
| **Return** | API response contract |
| **Expose** | New API/field consumers need |
| **Wire** | Connect UI to a Contract (clients, hooks) — belongs in the UI domain; bind to Request/Success/Errors, do not wait for the API domain |
| **Persist** | Data that must survive |
| **Clear** | Reset state after success |
| **Disable** / **Show** | UI guards and feedback |
| **Ensure** | Catch-all invariant (sparingly) |

By kind of work (not stage order): API → Create, Reject, Return, Enforce, Expose · Service → Add, Enforce, Change · UI → Wire (to Contract), Change, Disable, Show · Schema → Add, Persist, Change.

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
