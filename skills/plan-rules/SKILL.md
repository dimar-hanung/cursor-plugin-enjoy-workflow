---
name: plan-rules
description: >-
  Formats `.plan.md` plans with YAML frontmatter and bottom-up dependency
  stages. Must do + Inventory per stage; Data schema / API contract
  (REST, GraphQL, RPC, etc.) as separate stage sections when applicable.
  Outcome-level directives in English. AskQuestion outside the plan. Do not
  truncate. Use when creating, drafting, or presenting a plan, or when
  switching to Plan mode.
---

# Plan Rules

## Plan tone (non-negotiable)

Plans are for an AI agent to **execute**, not discuss. Write **one** decided path.

- **English only** — Goal, study cases, Must do, Data schema, API contract, Inventory, Out of Scope.
- **Quote non-English domain labels** — e.g. `"Belanja"`. Do not translate.
- **Outcome level** — where the change lands and what must be true after. The agent picks the code.
- **No** questions, options, "or", "optionally", "consider", trade-offs, recommendations.
- **Blocking decisions** → AskQuestion outside the plan (≤4/round). Bake the answer in as fact.

## Before writing

1. **Explore first — verify, never infer.** Guessed paths send the agent to files that do not exist.
   - Trace one real path top down: entry (route/page/job) → handler → service → repo → schema. Open each file.
   - Copy the nearest similar feature's patterns (error shape, auth, validation, naming, tests).
   - Map deps both ways: what the change needs (stage order) and who calls what you touch (breakage).
   - Cite only what you opened. Stop once you can name each stage, its deps, and its files.
2. Blocking A vs B → AskQuestion outside the plan. Never options inside `.plan.md`.
3. Write frontmatter first. Dependency stages, not flat lists. Do not truncate.
4. **Skip a formal plan** for trivial one-file work. State the change and execute.
5. **Not for ui-craft motion audits** — those use `plans/motion-plan-template.md`.

## Dependency stage order

A **dependency stage** = a bounded unit whose outputs must exist before dependents begin. Order by codebase deps — foundations before dependents, not by feature story.

- **Stack (default):** shared → **backend** (one stage per bounded area) → **frontend**
- **Inside BE:** schema → repos → services → handlers
- **Inside FE:** utils/types → API clients/hooks → components → pages (wire to backend as you build)

**Wire** UI to APIs in frontend Must do — no separate wiring stage for normal full-stack work. **Separate integration stage** only when glue spans multiple frontends/services (shared SDK, env rollout, mobile + web). Wrong: one "Frontend"/"Backend" blob, frontend before its APIs, or FE Must do that only builds UI shells.

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

One `todo` per stage, same order as Dependency order. Status: `pending` | `in-progress` | `completed` | `error`. **Todo content:** `"[stage-name]: after [deps]"`.

## Body

Order below only. No Stage Index / Risks / Review Surface. **Max heading `###`** — use bold labels for tables, API operations, and sub-blocks.

**User Behaviour (Study Cases)** — Observable behaviour, not feature bullets. 1–5 cases. Each case: title + three English prose paragraphs — **The situation** (who, context, trigger), **Before changes** (today), **After changes** (once Must do passes). Separate paragraphs; don't blend. No bullets in a case. Every **After changes** must be covered by a Must do item. Quote non-English domain labels.

Good:

> The situation A shopper on `"Belanja"` with two Blue Widgets taps Pay when only one is in stock.
> Before changes Spinner, success toast, order page — stock goes negative silently.
> After changes Inline error naming the SKU; cart unchanged; Pay succeeds only when stock holds.

Bad: vague ("better UX"), undecided ("guest checkout — TBD"), bullets/labels, implementation detail (`GET /orders` returns 200), translated domain labels.

**Must do** — Outcome-level: **where**, **what must be true**, **why**. Imperative, verb first. **Every item needs a `so` reason** — if none fits, the item is vague or too low-level. **Formula:** `[Verb] <where> to <outcome> so <reason>.`

Verbs by intent (use **Ensure** only when nothing sharper fits): **Create** new capability · **Add** behavior · **Change** replace · **Update** adjust · **Remove** stop · **Enforce** rule · **Reject** error path · **Return** response · **Expose** field · **Wire** UI↔BE (FE Must do) · **Persist** data · **Clear** state · **Disable** / **Show** UI · **Ensure** catch-all. By layer: API → Create/Reject/Return/Enforce/Expose · Service → Add/Enforce/Change · FE → Wire/Change/Disable/Show · Schema → Add/Persist/Change.

Good:
- Enforce atomic stock decrement in `createOrder` so concurrent orders cannot oversell.
- Reject insufficient stock on `POST /orders` with `409 { code: "INSUFFICIENT_STOCK" }` so clients show a stock-specific message.
- Wire `CheckoutForm` to `POST /orders` so Pay submits the cart and navigates on success.

Bad — too low-level (`change line 42`), vague (`improve the API`), passive (`Submit disabled while in flight`).

**Data schema changes** — Own `### Data schema changes` section, **not** inside Inventory. One bold label per table. Omit the section when the stage has none.

**New table** — flat column list under the label. **Changed table** — flat **Columns** (resulting shape) + flat **Diffs**: `**[new]**` · `**[edited]**` (`before: … · after: …` one line) · `**[removed]**` (before only). Unchanged columns get no Diff line.

Use names/types from the project's migration/ORM layer (Prisma, Drizzle, raw SQL).

```markdown
### Data schema changes

**`orders` — changed**

**Columns**
- `status` — text NOT NULL
- `shipped_at` — timestamptz NULL

**Diffs**
- `status` **[edited]** — before: `CHECK IN ('pending','done')` · after: `CHECK IN ('pending','shipped','done')`
- `shipped_at` **[new]**
- `price` **[removed]** — before: numeric(10,2) NOT NULL
```

**API contract** — Own `### API contract` section, **not** inside Inventory. **Not REST-only** — REST, GraphQL, gRPC/tRPC, WebSocket/events, etc. One bold operation label per contract (project's identifier: `POST /orders`, `Mutation createOrder`, `orders.create`, `OrderService.CreateOrder`). Omit when the stage has none.

- **Sections** — Auth (when applicable), then style-matched blocks: REST → **Request** / **Success `NNN`** / **Errors** · GraphQL → **Variables** / **Response** / **Errors** · RPC → **Input** / **Output** / **Errors**.
- **New** = full contract; **Changed** = resulting contract + flat **Diffs** lines.
- **Payload shapes** — multiline `json` fences for nested/multi-field objects; short flat objects may stay inline. Diffs use one line per field unless the value is large.

Use names/types the project already uses (OpenAPI, GraphQL schema, Zod, protobuf, DTOs). Match existing error shape.

````markdown
### API contract

**`POST /orders` — new** (REST) · Auth: session cookie

**Request**
```json
{ "items": [{ "sku": "string", "qty": "number" }] }
```

**Success `201`**
```json
{ "id": "string", "status": "pending" }
```

**Errors**
- `409`: `{ "code": "INSUFFICIENT_STOCK", "sku": "string" }`
- `401` — unauthenticated

**`Query order(id: ID!)` — changed** (GraphQL)

**Response**
```json
{ "order": { "id": "ID!", "status": "OrderStatus!", "shippedAt": "DateTime" } }
```

**Diffs**
- `order.status` **[edited]** — before: `PENDING | DONE` · after: `PENDING | SHIPPED | DONE`
- `order.shippedAt` **[new]**
````

## Body template

````markdown
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
## What Changes (Technical)
## Visualization (Technical)
[Skip unless a cross-stage flow / state machine / schema is non-obvious.]

# Bottom-Up Implementation

## Dependency order
1. `[shared / schema]` — none
2. `[backend]` — after 1
3. `[frontend]` — after 2, wires UI to backend

## Stage: [name]
**Goal**: … · **Depends on**: …

### Must do
- [Verb] `[where]` to [outcome] so [why].

### Data schema changes
[Omit when none.]

### API contract
[Omit when none. REST, GraphQL, RPC, etc.]

### Inventory
1. **New files** — `path` — purpose
2. **Modified files** — `path` — what changes
3. **Verify** — command or scenario (or None)

# Validation
[Skip if covered by Verify.] Run `…` — expect … · Prove study case "[Title]" by …

# Out of Scope
[Non-goals. Or: None.]

# Summary
- **Important notes** — env, config, breaking changes spanning stages
````
