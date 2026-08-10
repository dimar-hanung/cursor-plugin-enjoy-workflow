---
name: plan-rules
description: >-
  Formats implementation plans as Cursor `.plan.md` files with YAML frontmatter
  (Plan UI). Agent-first dependency stages ordered bottom-up by codebase deps
  (default backend → frontend). Must do + Inventory per stage; Data schema changes
  and API contract (REST, GraphQL, RPC, etc.) as separate stage sections when applicable, written at outcome level with imperative verbs
  (where + what must be true), never literal code edits.
  Plans are straightforward directives with no questions, options, or opinions
  — ask decisions via AskQuestion outside the plan. Study cases capture user
  behaviour before and after. Plans may be large — do not truncate. Use when
  creating, drafting, or presenting any plan — or when switching to Plan mode.
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
3. Map deps both ways: what the change needs · who calls what you will touch.
4. Split **reuse** vs **new** (types, helpers, endpoints already there vs missing pieces).
5. Stop exploring when you can name each stage, its dependency order, and the files it touches.

Every Inventory path and every Must do `where` must be something you opened.

### 3. Resolve blockers

1. If A vs B blocks the plan → AskQuestion outside the plan.
2. Bake answers into Must do / Out of Scope as facts.
3. Never leave options inside `.plan.md`.

### 4. Order dependency stages

A **dependency stage** = one bounded unit whose outputs must exist before dependents start. Order by codebase deps, not by feature story.

**Default stack**

1. shared / schema
2. backend (one stage per bounded area; inside BE: schema → repos → services → handlers)
3. frontend (utils/types → clients/hooks → components → pages; **Wire** UI to backend contracts here)

**Wrong:** one blob "Frontend"/"Backend" · frontend before the APIs it needs · FE Must do that only builds UI shells without wiring.

**Separate integration stage** only when glue spans multiple apps/services (shared SDK, env rollout, mobile + web). Not the default.

### 5. Write YAML frontmatter first

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

1. One `todo` per dependency stage, same order as Dependency order.
2. `content` format: `"[stage-name]: after [deps]"`.
3. Status: `pending` | `in-progress` | `completed` | `error`.

### 6. Write the body (this order only)

Fill sections in this sequence. Skip rules are inline.

1. **Goal** — what and why.
2. **User Behaviour (Study Cases)** — see format below. If no user-facing surface, write `No user-facing change.`
3. **What Current (Technical)** — existing modules / APIs that matter.
4. **What Changes (Technical)** — high-level; detail lives under stages.
5. **Visualization (Technical)** — only if cross-stage flow / state machine / schema relationship is non-obvious from Must do. Title + 1–2 sentences + mermaid via skill `mermaid-diagram-specialist`. Else omit.
6. **Bottom-Up Implementation**
   - **Dependency order** — numbered list matching frontmatter todos.
   - **For each stage** — Goal · Depends on · Must do · Data schema changes (if any) · API contract (if any) · Inventory.
7. **Validation** — skip if none / fully covered by stage Verify.
8. **Out of Scope** — non-goals, or `None`.
9. **Summary** — env, config, breaking changes spanning stages.

### 7. Self-check before presenting

- [ ] English throughout; domain labels quoted, not translated
- [ ] No questions / options / "optionally" / trade-offs in the plan
- [ ] Frontmatter todos match Dependency order 1:1
- [ ] Every study-case **After changes** has ≥1 Must do
- [ ] Every Must do uses `[Verb] … so …`
- [ ] Schema / API sections omitted when unused; present when the stage changes them
- [ ] Inventory paths and Must do `where` were opened during explore
- [ ] No `####` headings; no extra top-level sections (no Stage Index / Risks / Review Surface)

---

## Format: study cases

Usually 1–5 cases (happy path + edges that drive Must do).

For each case:

1. `### [Short case title]`
2. Three separate English prose paragraphs — do not blend Before/After; no bullets inside a case:
   - **The situation** — who, context, trigger
   - **Before changes** — today
   - **After changes** — once Must do passes

**Good**

> The situation A shopper on `"Belanja"` with two Blue Widgets taps Pay when only one is in stock.
> Before changes Spinner, success toast, order page — stock goes negative silently.
> After changes Inline error naming the SKU; cart unchanged; Pay succeeds only when stock holds.

**Bad:** vague ("better UX") · undecided ("guest checkout — TBD") · bullets/labels (**Actor:** …) · implementation detail (`GET /orders` returns 200) · translating `"Belanja"` → `Shopping`.

---

## Format: Must do

**Formula:** `[Verb] <where> to <outcome> so <reason>.`

- Imperative, verb first — not "In `[where]`…".
- Every item needs a `so` reason. If you cannot state one, the item is vague, unnecessary, or too low-level.
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
| Wire | Connect UI to backend (clients, hooks) — frontend stages |
| Persist | Data that must survive |
| Clear | Reset state after success |
| Disable / Show | UI guards and feedback |
| Ensure | Catch-all invariant (sparingly) |

By layer: API → Create, Reject, Return, Enforce, Expose · Service → Add, Enforce, Change · FE → Wire, Change, Disable, Show · Schema → Add, Persist, Change.

**Good**

- Enforce stock cannot go negative in `createOrder` so concurrent orders cannot oversell.
- Reject insufficient stock on `POST /orders` so clients show a stock-specific message.
- Wire `CheckoutForm` to `POST /orders` so Pay submits the cart and navigates on success.

**Bad**

- Below function level: Create `src/orders/createOrder.ts`, change line 42, rename `qty` · Reject with `409` `{ code: "…" }` in Must do (put status/body in API contract).
- Vague: improve the API, optionally CSV, "consider edge cases".
- Passive: In `createOrder`, atomic stock decrement… · Submit disabled while in flight.

---

## Format: Data schema changes

Own `### Data schema changes` under the stage — **not** inside Inventory. Omit the section when the stage has no schema change. Use project migration/ORM names and types.

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

Own `### API contract` under the stage — **not** inside Inventory. Omit when the stage has no new/changed consumer-facing API. Match the project's style (REST, GraphQL, gRPC/tRPC, WebSocket, etc.). Use existing field names and error shapes.

**Steps per operation**

1. Bold label with project identifier + `— new` or `— changed` (e.g. ``**`POST /orders` — new** (REST)``).
2. **Auth:** … when applicable.
3. Input / success / errors — pick labels for the style:
   - REST → **Request**, **Success `NNN`** (real status code, e.g. `201`), **Errors**
   - GraphQL → **Variables**, **Response**, **Errors**
   - RPC / similar → **Input**, **Output**, **Errors**
4. Payload shapes in multiline `json` fences (not one-line `{ … }`).
5. **New** → full contract, no field markers.
6. **Changed** → resulting contract; mark field deltas as **`//` comments on that field line** (no separate **Diffs** block):
   - `// [new]`
   - `// [edited] before: … · after: …`
   - `// [removed]` — keep the removed field in the fence only so the marker is visible

Copy the shape from the body template below.

---

## Format: Inventory (per stage)

Ordered parent list only:

1. **New files** — `path` — purpose
2. **Modified files** — `path` — what changes
3. **Verify** — command or scenario (or `None`)

---

## Body template

Copy this structure. Replace placeholders. Keep Data schema / API examples only when that stage needs them — otherwise delete those sections.

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
[High-level changes; detail under stages.]

## Visualization (Technical)
[Title + 1–2 sentence description + mermaid. Omit unless non-obvious. Use skill "mermaid-diagram-specialist".]

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
    "status": "OrderStatus!", // [edited] before: PENDING | DONE · after: PENDING | SHIPPED | DONE
    "shippedAt": "DateTime", // [new]
    "weight": "number" // [removed]
  }
}
```

### Inventory
1. **New files**
  - `path` — purpose
2. **Modified files**
  - `path` — what changes
3. **Verify**
  - command or scenario (or None)

# Validation
[Skip if none — trivial or fully covered by stage Verify lines.]

- Run `…` — expect …
- Prove study case "[Title]" by …

# Out of Scope
[Non-goals. Or: None.]

# Summary
- **Important notes** — env, config, breaking changes spanning stages
````
