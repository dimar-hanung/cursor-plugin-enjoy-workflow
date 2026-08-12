---
name: plan-rules
description: >-
  Formats implementation plans as Cursor `.plan.md` files with YAML frontmatter
  (Plan UI). Agent-first domain stages that all start in parallel — never a
  pipeline that waits on a previous stage. Each domain publishes a request-shaped
  Contract plus an Outcome so other domains bind to the contract, not to finished
  work. Tasks + Inventory per domain; Data schema changes and API contract
  (REST, GraphQL, RPC, etc.) as separate domain sections when applicable, written
  at outcome level with imperative verbs (where + what must be true), never
  literal code edits. Plans are straightforward directives with no questions,
  options, or opinions — ask decisions via AskQuestion outside the plan. Study
  cases capture user behaviour before and after. Plans may be large — do not
  truncate. Use when creating, drafting, or presenting any plan — or when
  switching to Plan mode.
---

# Plan Rules

Write a `.plan.md` the executor agent can run without guessing. Follow the steps in order. Copy the body template at the end and fill it — do not invent extra top-level sections.

## When to use / skip

| Case | Action |
| --- | --- |
| Creating, drafting, or presenting a plan · switching to Plan mode | Use this skill |
| Trivial work (typo, one obvious file, repeated one-line fix) | Skip the plan — state the change and execute |

## Hard rules

- Write the **entire** plan in **English**.
- Keep non-English business-process labels in **double quotes** — do not translate them (e.g. At `"Belanja"`, …).
- One decided path only. No questions, A/B options, "or", "optionally", "consider", trade-offs, or recommendations inside `.plan.md`.
- Decisions → **AskQuestion outside the plan** (≤4/round). Bake the answer in, then continue.
- Outcome level only: where + what must be true. The executor chooses the code.
- Max heading level `###`. Table names and API operations are **bold labels**, not `####`.
- Do not truncate. Plans may be large.
- Cite only files and symbols you opened.

## Procedure

### 1. Gate

1. If the work is trivial or a motion audit → follow **When to use / skip** and stop this skill.
2. Otherwise continue.

### 2. Explore (verify, never infer)

Do this before writing YAML or body text.

1. Trace **one** real path end to end, top down: entry (route / page / job) → handler → service → repo → schema. Open each file.
2. Find the closest existing feature that does something similar. Copy its patterns (error shape, auth, validation, naming, tests).
3. Map who calls what you touch (so each Contract is complete) and which files each domain owns (so parallel agents do not collide).
4. Split **reuse** vs **new** (types, helpers, endpoints already there vs missing pieces).
5. Stop exploring when you can name each domain, its Contract (request / success / errors), its Outcome, and the files it owns.

Every Inventory path and every Task `where` must be something you opened.

### 3. Resolve blockers

1. If A vs B blocks the plan → AskQuestion outside the plan.
2. Bake answers into Tasks / Out of Scope as facts.
3. Never leave options inside `.plan.md`.

### 4. Split domain stages (parallel)

A **domain** = one bounded capability an agent can finish without waiting for another stage. Split by domain, not by stack layer or codebase dependency order.

All domains **start together**. Coordination is the published **Contract**, not stage order. An agent implements or consumes the request shape in the plan — it does not wait for another domain's code to land.

- **Do** split by capability (`orders`, `stock`, `notifications`). One domain owns a coherent Contract and a non-overlapping file set.
- **Do** put API and UI of the same capability in **separate parallel domains** when they share a Contract and would not edit the same files (`orders-api` exposes `POST /orders`, `orders-ui` consumes it). Both start now; UI **Wire**s to the Contract, not to a finished backend stage.
- **Do not** pipeline layers: shared → schema → repos → services → handlers → frontend. That forces waiting.
- **Do not** write `Depends on`, `after [stage]`, or any gate that says another domain must finish first.
- **Do not** put the same path in two domains' Inventory. If they would collide, merge them or give the file to one owner; others consume the Contract.

**Wrong:** one blob "Frontend"/"Backend" · a backend stage that must finish before UI starts · UI Tasks that only build shells without wiring to the Contract.

**Separate integration domain** only when glue spans multiple apps/services (shared SDK, env rollout, mobile + web) — and it still starts in parallel against those Contracts, not after them.

Execute with `/run-plan` — one Composer 2.5 subagent per domain, all started together.

### 5. Write YAML frontmatter first

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

1. One `todo` per domain. List in any order — none is a gate for another.
2. `content` format: `"[domain]: [request] → [outcome]"`.
3. Status: `pending` | `in-progress` | `completed` | `error`.

### 6. Write the body (this order only)

Fill sections in this sequence. Skip rules are inline.

1. **Goal** — what and why.
2. **User Behaviour (Study Cases)** — see format below. If no user-facing surface, write `No user-facing change.`
3. **What Current (Technical)** — existing modules / APIs that matter.
4. **What Changes (Technical)** — high-level; detail lives under domains.
5. **Visualization (Technical)** — only if cross-domain contracts / state machine / schema relationship is non-obvious from Tasks. Title + 1–2 sentences + mermaid via skill `mermaid-diagram-specialist`. Else omit.
6. **Parallel Domains**
   - **Domains** — bullets (not a sequence). Each: name · Request · Outcome.
   - **For each domain** — Contract · Outcome · Tasks · Data schema changes (if any) · API contract (if any) · Inventory.
7. **Validation** — skip if none / fully covered by domain Verify.
8. **Out of Scope** — non-goals, or `None`.
9. **Summary** — env, config, breaking changes spanning domains.

### 7. Self-check before presenting

- [ ] English throughout; domain labels quoted, not translated
- [ ] No questions / options / "optionally" / trade-offs in the plan
- [ ] Frontmatter todos match the Domains list 1:1; none is a gate
- [ ] Every study-case **After changes** has ≥1 Task
- [ ] Every Task uses `[Verb] … so …`
- [ ] Every domain has Contract (Request / Success / Errors) and Outcome
- [ ] Schema / API sections omitted when unused; present when the domain changes them
- [ ] Inventory paths and Task `where` were opened during explore; no path in two domains
- [ ] No `####` headings; no extra top-level sections (no Stage Index / Risks / Review Surface)

---

## Format: study cases

Usually 1–5 cases (happy path + edges that drive Tasks).

For each case:

1. `### [Short case title]`
2. Three separate English prose paragraphs — do not blend Before/After; no bullets inside a case:
   - **The situation** — who, context, trigger
   - **Before changes** — today
   - **After changes** — once Tasks pass

**Good**

> The situation A shopper on `"Belanja"` with two Blue Widgets taps Pay when only one is in stock.
> Before changes Spinner, success toast, order page — stock goes negative silently.
> After changes Inline error naming the SKU; cart unchanged; Pay succeeds only when stock holds.

**Bad:** vague ("better UX") · undecided ("guest checkout — TBD") · bullets/labels (**Actor:** …) · implementation detail (`GET /orders` returns 200) · translating `"Belanja"` → `Shopping`.

---

## Format: Contract and Outcome

Every domain stage must show both. The Contract is the request other domains bind to. The Outcome is the done-check for this domain.

**Contract** is request-shaped — not a prose goal, not a file list. Detailed payloads live in **API contract** when the domain has a consumer-facing API.

| Field | What to write |
| --- | --- |
| **Request** | The call: `METHOD /path` `{ fields }`, or `fn(args)`, or event payload |
| **Success** | Status + body (or return value) when the request is accepted |
| **Errors** | Status + `{ code, … }` (or thrown code) the consumer must handle |
| **Consumes** | Other domains' Request this domain binds to. Omit when none |

The exposing domain implements Request/Success/Errors. The consuming domain **Wire**s to that same Request — it does not wait for the exposing domain to finish.

**Good**

```text
**Contract**:
- Request: `POST /orders` `{ items: [{ sku, qty }], paymentMethod }`
- Success: `201` `{ orderId, status }`
- Errors: `409` `{ code: "INSUFFICIENT_STOCK", sku }`
- Consumes: `stock` `decrementStock(sku, qty)`

**Outcome**: A shopper can pay; concurrent checkouts cannot drive stock negative; clients receive a stock-specific error.
```

**Bad:** "depends on stock stage" · "after orders-api" · Request with no Success/Errors · Outcome that restates Task file edits.

---

## Format: Tasks

Section heading: `### Tasks`. Each bullet is one **Task**.

**Formula:** `[Verb] <where> to <outcome> so <reason>.`

- Imperative, verb first — not "In `[where]`…".
- Every Task needs a `so` reason. If you cannot state one, the item is vague, unnecessary, or too low-level.
- **`where` max = function / symbol / route / component** — not file paths with line edits, field renames, status codes, or payload shapes (those belong in Inventory / Data schema / API contract).
- Use **Ensure** only when no sharper verb fits.

| Verb | Use for |
| --- | --- |
| Create | New capability, endpoint, flow |
| Add | New behavior on existing surface |
| Change | Replace existing behavior |
| Update | Adjust contract/UI without full rewrite |
| Remove | Stop bad behavior |
| Enforce | Rule or invariant |
| Reject | Error paths |
| Return | API response contract |
| Expose | New API/field consumers need |
| Wire | Connect UI to a Contract (clients, hooks) — UI domain; bind to Request/Success/Errors |
| Persist | Data that must survive |
| Clear | Reset state after success |
| Disable / Show | UI guards and feedback |
| Ensure | Catch-all invariant (sparingly) |

By kind of work (not stage order): API → Create, Reject, Return, Enforce, Expose · Service → Add, Enforce, Change · UI → Wire (to Contract), Change, Disable, Show · Schema → Add, Persist, Change.

**Good**

- Enforce stock cannot go negative in `createOrder` so concurrent orders cannot oversell.
- Reject insufficient stock on `POST /orders` so clients show a stock-specific message.
- Wire `CheckoutForm` to `POST /orders` so Pay submits the cart and navigates on success.

**Bad**

- Below function level: Create `src/orders/createOrder.ts`, change line 42, rename `qty` · Reject with `409` `{ code: "…" }` in Tasks (put status/body in API contract).
- Vague: improve the API, optionally CSV, "consider edge cases".
- Passive: In `createOrder`, atomic stock decrement… · Submit disabled while in flight.

---

## Format: Data schema changes

Own `### Data schema changes` under the domain — **not** inside Inventory. Omit the section when the domain has no schema change. Use project migration/ORM names and types.

**Steps per table**

1. Bold label: ``**`table` — new**`` or ``**`table` — changed**`` (not a heading).
2. **New table** → flat column list under the label (no Diffs).
3. **Changed table** → **Columns** (resulting shape) then **Diffs** only for deltas:
   - `col` **[new]**
   - `col` **[edited]** — before: … · after: … (one line)
   - `col` **[removed]** — before: …
4. Unchanged columns need no Diffs line.

Copy the shape from the body template below.

---

## Format: API contract

Own `### API contract` under the domain — **not** inside Inventory. Omit when the domain has no new/changed consumer-facing API. Match the project's style (REST, GraphQL, gRPC/tRPC, WebSocket, etc.). Use existing field names and error shapes. This is the detailed payload for the domain **Contract**.

**Steps per operation**

1. Bold label with project identifier + `— new` or `— changed` (e.g. ``**`POST /orders` — new** (REST)``).
2. **Auth:** … when applicable.
3. Input / success / errors — pick labels for the style:
   - REST → **Request**, **Success `NNN`** (real status code, e.g. `201`), **Errors**
   - GraphQL → **Variables**, **Response**, **Errors**
   - RPC / similar → **Input**, **Output**, **Errors**
4. Show payload shapes in multiline fenced blocks using the contract notation and language tag already used by the current codebase (for example `json`, `graphql`, `proto`, or `ts`) — not one-line `{ … }`.
5. **New** → full contract, no field markers.
6. **Changed** → resulting contract; express field deltas in a form valid for that contract:
   - If its notation supports comments, annotate the field with that notation's comment syntax (for example `//` or `#`): `[new]`, `[edited] before: … · after: …`, or `[removed]`.
   - If its notation does not support comments, keep the fenced contract valid and add a flat **Changes** list immediately below it using the same markers.
   - Removed fields must not remain active in the resulting contract; show them as commented-out fields or **Changes** entries.

Copy the shape from the body template below.

---

## Format: Inventory (per domain)

Ordered parent list only:

1. **New files** — `path` — purpose
2. **Modified files** — `path` — what changes
3. **Verify** — command or scenario (or `None`)

---

## Body template

Copy this structure. Replace placeholders. Keep Data schema / API examples only when that domain needs them — otherwise delete those sections.

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
[Existing modules / APIs that matter.]

## What Changes (Technical)
[High-level changes; detail under domains.]

## Visualization (Technical)
[Title + 1–2 sentence description + mermaid. Omit unless non-obvious. Use skill "mermaid-diagram-specialist".]

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

### Tasks
- [Verb] `[where]` to [outcome] so [why].

### Data schema changes

**`orders` — new**

- `id` — uuid PK
- `status` — text NOT NULL DEFAULT 'pending'
- `created_at` — timestamptz NOT NULL

**`orders` — changed**

**Columns**
- `id` — uuid PK
- `status` — text NOT NULL
- `shipped_at` — timestamptz NULL
- `created_at` — timestamptz NOT NULL

**Diffs**
- `status` **[edited]** — before: text NOT NULL CHECK (status IN ('pending','done')) · after: text NOT NULL CHECK (status IN ('pending','shipped','done'))
- `shipped_at` **[new]**

### API contract

**`POST /orders` — new** (REST)

Auth: session cookie

**Request**
```json
{
  "items": [
    { "sku": "string", "qty": "number" }
  ]
}
```

**Success `201`**
```json
{
  "id": "string",
  "status": "pending"
}
```

**Errors**
- `409`:
```json
{
  "code": "INSUFFICIENT_STOCK",
  "sku": "string"
}
```
- `401` — unauthenticated

**`Query order(id: ID!)` — changed** (GraphQL)

Auth: session cookie

**Variables**
```json
{
  "id": "ID!"
}
```

**Response**
```json
{
  "order": {
    "id": "ID!",
    "status": "OrderStatus!",
    "shippedAt": "DateTime"
  }
}
```

**Changes**
- `order.status` **[edited]** — before: PENDING | DONE · after: PENDING | SHIPPED | DONE
- `order.shippedAt` **[new]**
- `order.weight` **[removed]** — before: number

### Inventory
1. **New files**
  - `path` — purpose
2. **Modified files**
  - `path` — what changes
3. **Verify**
  - command or scenario (or None)

# Validation
[Skip if none — trivial or fully covered by domain Verify lines.]

- Run `…` — expect …
- Prove study case "[Title]" by …

# Out of Scope
[Non-goals. Or: None.]

# Summary
- **Important notes** — env, config, breaking changes spanning domains
````
