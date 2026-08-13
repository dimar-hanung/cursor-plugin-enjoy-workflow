---
name: plan-rules
description: >-
  Formats Cursor `.plan.md` plans with YAML todos and parallel domain stages
  (`### Provides`, `### Consumes`, `### Outcome`). Never a pipeline that waits
  on a previous stage. Use when creating, drafting, or presenting any plan —
  or when switching to Plan mode.
---

# Plan Rules

Follow the steps in order. Fill the body template at the end — do not invent extra top-level sections.

## When to use / skip

| Case | Action |
| --- | --- |
| Creating, drafting, or presenting a plan · switching to Plan mode | Use this skill |
| Trivial work (typo, one obvious file, repeated one-line fix) | Skip the plan — state the change and execute |
| UI motion audit (no product behaviour change) | Skip — use `skills/ui-craft/references/motion-plan-template.md`, not `.plan.md` |

If the table says skip, stop this skill.

## Hard rules

- Write the **entire** plan in **English**.
- Keep non-English business-process labels in **double quotes** — do not translate them (e.g. At `"Belanja"`, …).
- One decided path only. No questions, A/B options, "or", "optionally", "consider", trade-offs, or recommendations inside `.plan.md`.
- Decisions → **AskQuestion outside the plan** (≤4/round). Bake the answer into Tasks / Out of Scope.
- Tasks and study cases: outcome level (where + what must be true). Provides / Consumes / API contract: request-shaped. The executor chooses the code.
- Max heading level `###`. Table names and API operations are **bold labels**, not `####`.
- Do not truncate. Plans may be large.
- Cite only files and symbols you opened.

## Procedure

### 1. Explore (verify, never infer)

Do this before writing YAML or body text.

1. Trace **one** real path end to end, top down: entry (route / page / job) → handler → service → repo → schema. Open each file.
2. Find the closest existing feature that does something similar. Copy its patterns (error shape, auth, validation, naming, tests).
3. Map who calls what you touch (so each Provides is complete) and which files each domain owns (so parallel agents do not collide).
4. Split **reuse** vs **new** (types, helpers, endpoints already there vs missing pieces).
5. Stop exploring when you can name each domain, its Provides, its Consumes, its Outcome, and the files it owns.

Every Inventory path and every Task `where` must be something you opened.

### 2. Split domain stages (parallel)

A **domain** = one bounded capability an agent can finish without waiting for another stage. Split by domain, not by stack layer. All domains start together.

- **Do** split by capability (`orders`, `stock`, `notifications`). One domain owns each call and may Provide or Consume several. Split only when capability or Inventory files diverge — not because a domain has more than one call.
- **Do** put API and UI of the same capability in **separate parallel domains** when they would not edit the same files (`orders-api` Provides `POST /orders`, `orders-ui` Consumes it). Both start now; UI **Wire**s to that Provides, not to a finished backend stage.
- **Do** use a separate integration domain only when glue spans multiple apps/services (shared SDK, env rollout, mobile + web) — it still starts in parallel against those Provides.
- **Do not** pipeline layers: shared → schema → repos → services → handlers → frontend.
- **Do not** write `Depends on`, `after [stage]`, or any gate that says another domain must finish first.
- **Do not** put the same path in two domains' Inventory. If they would collide, merge them or give the file to one owner; others bind via Consumes.

### 3. Write YAML frontmatter first

```yaml
---
name: Short plan title
overview: One-line summary (or "")
todos:
  - id: domain-orders-api
    content: "orders-api → pay without oversell"
    status: pending
  - id: domain-stock
    content: "stock → stock never negative"
    status: pending
  - id: domain-payments
    content: "payments → charge recorded"
    status: pending
  - id: domain-orders-ui
    content: "orders-ui → Pay wired, stock error shown"
    status: pending
isProject: false
---
```

1. One `todo` per domain. List in any order — none is a gate for another.
2. `content` format: `"[domain] → [outcome]"`. Call lists live under `## Domains`, not in the todo.
3. Status: `pending` | `in-progress` | `completed` | `error`.

### 4. Write the body (this order only)

Allowed H1s: `# Overview` · `# Parallel Domains` · `# Validation` · `# Out of Scope` · `# Summary`. Duplicate `## Stage:` once per Domains item.

1. **Goal** — what and why.
2. **User Behaviour (Study Cases)** — format below. If no user-facing surface, write `No user-facing change.`
3. **What Current (Technical)** — existing modules / APIs that matter.
4. **Behaviour** — omit unless `/plan-behaviour-research` was run (then it sits here).
5. **What Changes (Technical)** — high-level; detail under domains.
6. **Visualization (Technical)** — only if cross-domain contracts / state machine / schema is non-obvious. Title + 1–2 sentences + mermaid via skill `mermaid-diagram-specialist`. Else omit.
7. **Parallel Domains** — `## Domains` numbered index (one numbered call per line under Provides / Consumes), then one `## Stage:` per domain.
8. **Validation** — skip if none / fully covered by domain Verify.
9. **Out of Scope** — non-goals, or `None`.
10. **Summary** — env, config, breaking changes spanning domains.

Delete `### Data schema changes` / `### API contract` when that domain has none.

### 5. Self-check before presenting

- [ ] English throughout; domain labels quoted, not translated
- [ ] No questions / options / "optionally" / trade-offs in the plan
- [ ] Frontmatter todos match the Domains list 1:1; none is a gate
- [ ] Every study-case **After changes** has ≥1 Task
- [ ] Every Task uses `[Verb] … so …`
- [ ] Every domain has `### Provides`, `### Consumes`, and `### Outcome`; Consumes copies each bound call (or `none`)
- [ ] Schema / API sections omitted when unused; present when the domain changes them
- [ ] Inventory paths and Task `where` were opened during explore; no path in two domains
- [ ] No `####` headings; no extra H1s (no Stage Index / Risks / Review Surface)

---

## Format: study cases
max 5 main cases.

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

## Format: Provides, Consumes, Outcome

Always write both headings (`none` when empty). Stack several calls under the same heading. Request / Success / Errors are bold labels, not headings. HTTP/GraphQL/RPC detail → **API contract** on the providing domain. Function calls stay fully specified here.

| Heading | What to write |
| --- | --- |
| `### Provides` | Each published call: bold label + Request + Success + Errors. `none` when this domain publishes no call. Exactly one domain owns each call. |
| `### Consumes` | Each bound call from another domain: **`[domain]` `[call]`** + that call's Request / Success / Errors (must match). Copy only the calls this stage binds to — not the rest of that domain's Provides. `none` when this domain binds to nothing. Copying is the interface — not a wait. |

**Good**

```markdown
### Provides
**`POST /orders`**
**Request:** `{ items: [{ sku, qty }], paymentMethod }`
**Success:** `201` `{ id, status }`
**Errors:** `409` `{ code: "INSUFFICIENT_STOCK", sku }`

**`GET /orders/:id`**
**Request:** `{ id }`
**Success:** `200` `{ id, status, items }`
**Errors:** `404` `{ code: "NOT_FOUND" }`

### Consumes
**`[stock]` `decrementStock`**
**Request:** `{ sku, qty }`
**Success:** `{ remaining }`
**Errors:** `{ code: "INSUFFICIENT_STOCK", sku }`

**`[payments]` `charge`**
**Request:** `{ orderId, method }`
**Success:** `{ chargeId, status }`
**Errors:** `{ code: "PAYMENT_FAILED" }`

### Outcome
A shopper can pay; concurrent checkouts cannot drive stock negative; clients receive a stock-specific error.
```

**Bad:** "depends on stock stage" · one blended Request covering two calls · Consumes a domain name with no call · copying a sibling's unused Provides · wrapping Provides/Consumes in a `**Contract**` bullet list.

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
| Wire | Connect UI to the providing domain's Provides (clients, hooks) |
| Persist | Data that must survive |
| Clear | Reset state after success |
| Disable / Show | UI guards and feedback |
| Ensure | Catch-all invariant (sparingly) |

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

Own `### Data schema changes` under the domain — **not** inside Inventory. Omit when unused. Use project migration/ORM names and types. Copy the shape from the body template.

---

## Format: API contract

Own `### API contract` under the domain — **not** inside Inventory. Omit when unused. This is the detailed payload for this domain's **Provides** — one operation block per Provides call. Match the project's style — one style per domain, not both: REST → **Request** / **Success `201`** (real HTTP status) / **Errors**; GraphQL → **Variables** / **Response** / **Errors**; RPC → **Input** / **Output** / **Errors**. Multiline fenced payloads in the codebase's notation. Changed operations: comment deltas in-contract, or a **Changes** list if comments are invalid. Copy the REST shape in the body template; rename labels for the project's style.

---

## Format: Inventory (per domain)

Ordered parent list only. Copy the shape from the body template.

---

## Body template

Copy this structure. Replace placeholders.

````markdown
# Overview

## Goal
[What and why.]

## User Behaviour (Study Cases)
### [Short case title]
**The situation** …
**Before changes** …
**After changes** …

## What Current (Technical)
[Existing modules / APIs that matter.]

## What Changes (Technical)
[High-level changes; detail under domains.]

## Visualization (Technical)
[Title + 1–2 sentences + mermaid.]

# Parallel Domains

## Domains
1. `[orders-api]`
   - Provides:
     1. `POST /orders`
     2. `GET /orders/:id`
   - Consumes:
     1. `[stock]` `decrementStock`
     2. `[payments]` `charge`
   - Outcome: pay without oversell
2. `[stock]`
   - Provides:
     1. `decrementStock`
   - Consumes: none
   - Outcome: stock never negative
3. `[payments]`
   - Provides:
     1. `charge`
   - Consumes: none
   - Outcome: charge recorded
4. `[orders-ui]`
   - Provides: none
   - Consumes:
     1. `[orders-api]` `POST /orders`
     2. `[orders-api]` `GET /orders/:id`
   - Outcome: Pay wired; stock error shown

## Stage: [domain]
### Provides
**`[call]`**
**Request:** `METHOD /path` `{ fields }`
**Success:** `status` `{ fields }`
**Errors:** `status` `{ code, … }`

### Consumes
**`[other-domain]` `[call]`**
**Request:** `{ fields }`
**Success:** `{ fields }`
**Errors:** `{ code, … }`

### Outcome
[What must be true when this domain is done — observable, 1–2 sentences.]

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
  ],
  "paymentMethod": "string"
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

### Inventory
1. **New files**
  - `path` — purpose
2. **Modified files**
  - `path` — what changes
3. **Verify**
  - command or scenario (or None)

# Validation
- Run `…` — expect …
- Prove study case "[Title]" by …

# Out of Scope
[Non-goals.]

# Summary
- **Important notes** — env, config, breaking changes spanning domains
````
